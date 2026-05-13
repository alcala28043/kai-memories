# Memory Tools Instructions

You have access to two tools for interacting with the memory vault.  
These tools must already be registered in your agent configuration.

## 1. memory_search

Use this tool when:

- You need to recall past information.
- You want to check if something has already been stored.
- You need context from previous conversations, decisions, preferences, or projects.

**Input:**

- `query`: A short description of what you are looking for.

**Behavior:**

- The tool returns a list of notes from the memory vault.
- You must read the content and decide which notes are relevant.
- You should extract only the information that helps you answer the current request.

## 2. memory_write

Use this tool when:

- You want to store new information.
- You want to save a summary of an important conversation.
- You want to record a decision, preference, idea, or project update.
- You want to update long‑term memory.

**Input:**

- `content`: The full text of the note you want to store.

**Guidelines:**

- Notes must be atomic, concise, and meaningful.
- Avoid duplicates. If similar information already exists, update or reference it instead of creating a new note.
- Store only long‑term useful information, not temporary or trivial details.
- Write notes in clear English.
