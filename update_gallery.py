import os

VORHER_DIR = "assets/vorher"
NACHER_DIR = "assets/nacher"
HTML_FILE = "index.html"

def generate_blocks():
    blocks = []
    files = sorted(os.listdir(VORHER_DIR))

    for file in files:
        vorher_path = f"{VORHER_DIR}/{file}"
        nacher_path = f"{NACHER_DIR}/{file}"

        if not os.path.exists(nacher_path):
            print(f"⚠️ Kein Nachher-Bild für {file}")
            continue

        block = f"""
<div class="before-after">
  <div class="before-after-grid">
    <div>
      <img src="{vorher_path}" alt="Vorher Frisur">
      <div class="before-after-label label-before">Vorher</div>
    </div>
    <div>
      <img src="{nacher_path}" alt="Nachher Frisur">
      <div class="before-after-label label-after">Nachher</div>
    </div>
  </div>
</div>
"""
        blocks.append(block)

    return "\n".join(blocks)


def insert_into_html(blocks):
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    start = "<div class=\"gallery-grid\" id=\"before-after-gallery\">"
    end = "</div>"

    before, rest = html.split(start)
    _, after = rest.split(end, 1)

    new_html = before + start + blocks + "\n    " + end + after

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(new_html)


if __name__ == "__main__":
    blocks = generate_blocks()
    insert_into_html(blocks)
    print("✅ Galerie erfolgreich aktualisiert")
