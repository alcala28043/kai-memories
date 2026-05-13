import os
import json
from datetime import datetime

BASE_DIR = "memory"

def is_safe_path(base, path):
    base = os.path.abspath(base)
    target = os.path.abspath(path)
    return os.path.commonpath([base]) == os.path.commonpath([base, target])

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def write_memory(request):
    """
    request = {
        "relative_path": "projects/ai/notes.md",
        "content": "Some text"
    }
    """

    relative_path = request.get("relative_path", "").strip()
    content = request.get("content", "").strip()

    if not content:
        return {"error": "Content is empty"}

    # Default folder if no path is provided
    if not relative_path:
        today = datetime.now().strftime("%Y-%m-%d")
        relative_path = f"inbox/{today}.md"

    # Normalize path
    relative_path = relative_path.replace("\\", "/")

    # Prevent directory traversal
    if ".." in relative_path or relative_path.startswith("/"):
        return {"error": "Unsafe path detected"}

    # Build final path inside memory/
    full_path = os.path.join(BASE_DIR, relative_path)

    # Validate final path is inside memory/
    if not is_safe_path(BASE_DIR, full_path):
        return {"error": "Path escapes memory directory"}

    # Ensure directory exists
    directory = os.path.dirname(full_path)
    ensure_directory(directory)

    # Write file
    with open(full_path, "a", encoding="utf-8") as f:
        f.write(content + "\n")

    return {"status": "ok", "path": full_path}

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Uso: python3 memory_write.py <relative_path> <content>")
        exit(1)

    relative_path = sys.argv[1]
    content = sys.argv[2]

    result = write_memory({
        "relative_path": relative_path,
        "content": content
    })

    print(result)
