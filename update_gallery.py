import os

# Konfiguration
image_folder = 'assets/frisuren'
html_file = 'index.html'
valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')

# Marker in der HTML Datei
start_marker = ''
end_marker = ''

def generate_gallery_html():
    if not os.path.exists(image_folder):
        print(f"Fehler: Ordner '{image_folder}' existiert nicht.")
        return None

    # Bilder suchen
    images = [f for f in os.listdir(image_folder) if f.lower().endswith(valid_extensions)]
    images.sort() # Sortieren damit Reihenfolge konstant bleibt

    if not images:
        print("Keine Bilder gefunden.")
        return ""

    html_content = "\n"
    for img in images:
        # Pfad für HTML (Slash statt Backslash)
        web_path = f"{image_folder}/{img}"
        # HTML Block für jedes Bild
        html_content += f'        <img src="{web_path}" alt="Frisur {img}" loading="lazy">\n'
    
    return html_content

def update_index_file():
    new_gallery_content = generate_gallery_html()
    
    if new_gallery_content is None:
        return

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Prüfen ob Marker existieren
    if start_marker not in content or end_marker not in content:
        print("Fehler: Marker oder nicht in index.html gefunden.")
        return

    # Inhalt zwischen den Markern austauschen
    pre_part = content.split(start_marker)[0]
    post_part = content.split(end_marker)[1]

    new_full_content = pre_part + start_marker + new_gallery_content + "        " + end_marker + post_part

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_full_content)
    
    print(f"Erfolg: {len(new_gallery_content.strip().splitlines())} Bilder zur Galerie hinzugefügt.")

if __name__ == "__main__":
    update_index_file()