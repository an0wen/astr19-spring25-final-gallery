import csv

OUTPUT_FILE = "index.html"
METADATA_FILE = "metadata.csv"

with open(METADATA_FILE, newline='') as f:
    reader = csv.DictReader(f)
    entries = list(reader)

with open(OUTPUT_FILE, "w") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ASTR 19 - Carina Nebula Gallery</title>
  <style>
    body { font-family: sans-serif; background-color: #111; color: #eee; text-align: center; }
    h1 { margin-top: 20px; }
    .gallery { display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; padding: 20px; }
    .gallery-item { width: 300px; border: 1px solid #444; padding: 8px; background: #222; }
    .gallery-item img { width: 100%; height: auto; border-radius: 4px; }
    .caption { margin-top: 8px; font-size: 0.9em; color: #aaa; }
  </style>
</head>
<body>
  <h1>ASTR 19 - Spring 2025: Carina Nebula Gallery (Final Project)</h1>
  <div class="gallery">
""")

    for row in entries:
        token = row["token"].strip()
        name = row["name"].strip()
        description = row["description"].strip()

        thumb_url = f"https://lh3.googleusercontent.com/d/{token}"
        full_url = f"https://drive.google.com/uc?export=view&id={token}"

        f.write(f"""
    <div class="gallery-item">
      <a href="{full_url}" target="_blank" rel="noopener noreferrer">
        <img src="{thumb_url}">
      </a>
      <div class="caption"><strong>{name}</strong><br>{description}</div>
    </div>
""")

    f.write("""
  </div>
</body>
</html>
""")
