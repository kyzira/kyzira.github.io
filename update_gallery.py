import os

IMAGE_DIR = "assets/frisuren"
HTML_FILE = "index.html"

allowed_ext = (".jpg", ".jpeg", ".png", ".webp")

# Bilder sammeln
images = sorted([
    f for f in os.listdir(IMAGE_DIR)
    if f.lower().endswith(allowed_ext)
])

# HTML für Galerie erzeugen
gallery_html = "\n".join([
    f'        <img src="{IMAGE_DIR}/{img}" alt="Frisur {i+1}" loading="lazy">'
    for i, img in enumerate(images)
])

# HTML-Datei laden
with open(HTML_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# Platzhalter ersetzen
html = html.replace(
    "<!-- GALLERY_IMAGES -->",
    gallery_html
)

# Datei zurückschreiben
with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"{len(images)} Bilder in die Galerie eingefügt.")
