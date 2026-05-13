# Kai Memories — Usage Guide

This document explains how to use Kai Memories once installed.

---

## 1. Ensure tools are registered

Your agent must expose:

- `memory_search`
- `memory_write`
- `memory_index` (optional but recommended)

Without these tools, the memory system will not work.

---

## 2. Load the memory skill

Load:

```
skills/memory_skill.md
```

This teaches the agent:
- When to search memory  
- When to write memory  
- How to store long‑term useful information  
- How to avoid duplicates  
- How to create atomic notes  

---

## 3. Optional: Load the index skill

Load:

```
skills/memory_index_skill.md
```

This allows the agent to:
- Refresh the index
- Rebuild the index
- Handle large manual edits

---

## 4. How memory works

### Reading memory
The agent:
- Calls `memory_search`
- Uses the index if available
- Reads only relevant notes
- Avoids scanning the entire vault

### Writing memory
The agent:
- Calls `memory_write`
- Creates atomic notes
- Appends instead of overwriting
- Automatically updates the index (if enabled)

### Indexing

- Automatic for new/changed notes  
- Manual for full rebuilds  
- Stored in `memory/index.json`  

---


## 5. Safe Writing Rules (important)

Kai Memories enforces a strict and predictable writing model to keep your vault clean and safe.

### 📌 All notes are written inside `memory/`
If the agent writes:
```
projects/ai/plan.md
```

The actual file becomes:

```
memory/projects/ai/plan.md
```


### 📌 Directory traversal is blocked
The following are rejected:

- `../`
- Absolute paths
- Hidden folders
- Anything escaping `memory/`

### 📌 Missing paths are normalized
If no path is provided:

```
memory/inbox/YYYY-MM-DD.md
```

### 📌 Subfolders are created automatically
No manual setup required.

### 📌 Notes are appended, not overwritten
Prevents accidental data loss.

### 📌 The agent cannot modify non‑memory files
Your personal notes remain untouched.

---

## 6. Recommended workflow

- Create your own private repo from the template  
- Use Obsidian to browse and edit notes  
- Use Git to sync across devices  
- Let the agent maintain long‑term memory  
- Rebuild the index occasionally if you reorganize notes manually  

---

Kai Memories is designed to be **simple, safe, and local‑first**.
