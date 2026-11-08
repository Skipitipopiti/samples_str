import os
import json

BASE_URL = "https://raw.githubusercontent.com/Skipitipopiti/samples_str/main/"
OUTPUT_FILE = "strudel.json"
AUDIO_EXTENSIONS = {".wav", ".mp3", ".flac", ".ogg"}

result = {"_base": BASE_URL}

for root, _, files in os.walk("."):
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in AUDIO_EXTENSIONS:
            key = os.path.splitext(file)[0]
            # Percorso relativo normalizzato con slash /
            rel_path = os.path.relpath(os.path.join(root, file), ".").replace("\\", "/")
            result[key] = rel_path

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)

print(f"Generato {OUTPUT_FILE} con {len(result) - 1} campioni.")