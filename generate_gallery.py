import os

IMAGE_DIR = "images"
OUTPUT_FILE = "index.html"

with open(OUTPUT_FILE, "w") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ASTR 19 – Carina Nebula Gallery</title>
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
  <h1>ASTR 19 – Carina Nebula Student Gallery</h1>
  <div class="gallery">
""")

    for filename in sorted(os.listdir(IMAGE_DIR)):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            name = filename.split("_")[0]  # assumes FirstnameLastname_Carina.png
            f.write(f"""
    <div class="gallery-item">
      <img src="{IMAGE_DIR}/{filename}" alt="{name}'s Carina Nebula">
      <div class="caption">{name}</div>
    </div>
""")

    f.write("""
  </div>
</body>
</html>""")
