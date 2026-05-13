# Tools

This directory contains the executable tools used by agents to interact with the Kai Memories vault.

These tools are NOT automatically registered.  
Your agent configuration must explicitly declare them.

---

## Available tools

### `memory_search.py`
Searches the memory vault.

Behavior:
- Uses the index (`index/index.json`) if available
- Falls back to full-text search if the index is missing
- Returns the content of matching notes

### `memory_write.py`
Creates new atomic notes inside:

```
memory/logs/
```

Behavior:
- Writes a new Markdown file
- Automatically triggers incremental indexing

### `memory_index.py`
Maintains the search index.

Behavior:
- Full index if no index exists
- Incremental index if index exists
- Only reindexes changed or new files
- Can be triggered manually via skill or tool call

---

## Indexing strategy (hybrid)

- New notes → automatically indexed  
- Modified notes → automatically updated  
- Manual reindex → available via skill  
- First run → full index  

---

## Notes

- Tools operate on the local filesystem  
- The vault is portable and Git-syncable  
- No embeddings or external models are required  
