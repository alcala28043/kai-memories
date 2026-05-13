import os
import json

BASE_DIR = "memory"
INDEX_FILE = os.path.join(BASE_DIR, "index.json")

def build_index():
    index = {}

    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if not file.endswith(".md"):
                continue

            path = os.path.join(root, file)

            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
            except:
                continue

            index[path] = {
                "size": len(text),
                "preview": text[:200]
            }

    return index

def index_memory(request=None):
    index = build_index()

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    return {"status": "ok", "indexed_files": len(index)}
