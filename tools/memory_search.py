import os
import json

BASE_DIR = "memory"

def search_memory(request):
    """
    request = {
        "query": "keyword",
        "max_results": 5
    }
    """

    query = request.get("query", "").lower().strip()
    max_results = request.get("max_results", 5)

    if not query:
        return {"error": "Query is empty"}

    results = []

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

            if query in text.lower():
                results.append({
                    "path": path,
                    "preview": text[:200]
                })

            if len(results) >= max_results:
                break

    return {"results": results}

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Uso: python3 memory_search.py <query> [max_results]")
        exit(1)

    query = sys.argv[1]
    max_results = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    result = search_memory({
        "query": query,
        "max_results": max_results
    })

    print(json.dumps(result, indent=2, ensure_ascii=False))
