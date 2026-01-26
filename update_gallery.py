import os

VORHER_DIR = "assets/vorher"
NACHHER_DIR = "assets/nachher"
HTML_FILE = "index.html"

def generate_blocks():
    blocks = []
    files = sorted(os.listdir(VORHER_DIR))

    for file in files:
        vorher_path = f"{VORHER_DIR}/{file}"
        nachher_path = f"{NACHHER_DIR}/{file}"

        if not os.path.exists(nachher_path):
            print(f"⚠️ Kein Nachher-Bild für {file}")
            continue

        block = f"""          <div class="before-after">
            <div class="before-after-grid">
              <div class="before-after-item">
                <img src="{vorher_path}" alt="Vorher-Bild Frisur" class="lightbox-trigger">
                <div class="before-after-label label-before">Vorher</div>
              </div>
              <div class="before-after-item">
                <img src="{nachher_path}" alt="Nachher-Bild Frisur" class="lightbox-trigger">
                <div class="before-after-label label-after">Nachher</div>
              </div>
            </div>
          </div>"""
        blocks.append(block)

    return "\n".join(blocks)


def insert_into_html(blocks):
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    start_marker = '<div class="gallery-grid" data-gallery="vorher-nachher">'
    end_marker = '</div>\n        <button class="scroll-indicator scroll-indicator-right"'

    start_idx = html.find(start_marker)
    if start_idx == -1:
        print("❌ Start-Marker nicht gefunden")
        return

    end_idx = html.find(end_marker, start_idx)
    if end_idx == -1:
        print("❌ End-Marker nicht gefunden")
        return

    new_html = html[:start_idx + len(start_marker)] + "\n" + blocks + "\n        " + html[end_idx:]

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(new_html)


if __name__ == "__main__":
    blocks = generate_blocks()
    insert_into_html(blocks)
    print("✅ Galerie erfolgreich aktualisiert")
