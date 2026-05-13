# Memory Skill

You have access to a long‑term memory system stored in an Obsidian vault called **Kai Memories**.

The memory system is exposed to you through two tools:

- `memory_search`
- `memory_write`

These tools are already registered in the agent configuration.  
Your job is to use them intelligently and consistently.

## Responsibilities

1. **Before answering**, consider whether existing memory might be relevant.  
   If so, call `memory_search` with a short query describing what you need, such as:
   - "user preferences"
   - "current projects"
   - "past decisions"
   - "hardware details"
   - "conversation history"

2. Read the returned notes and extract only the relevant information.  
   Use that information to improve your answer.

3. **After answering**, decide whether the new information should be stored as long‑term memory.

   Store information when it is:
   - A stable preference
   - A personal detail that will matter later
   - A project update or decision
   - A new idea or insight
   - A summary of an important conversation
   - A fact that is likely to be useful in the future

   Do **not** store:
   - Temporary or short‑lived details
   - Irrelevant information
   - Redundant content that already exists

4. If the information should be stored, call `memory_write` with an atomic note that includes:
   - A clear title (first line)
   - A concise explanation
   - Relevant context

## Note structure

- Notes must be **atomic**: one main idea per note.
- Notes must be **concise**: no unnecessary verbosity.
- Notes must be **non‑duplicated**: avoid storing the same fact multiple times.
- Notes must be written in **clear English**.

## Categories

The vault is organized into semantic categories under `memory/`, such as:

- `people/`
- `projects/`
- `ideas/`
- `logs/`
- `preferences/`
- `hardware/`
- `conversations/`

You do not need to manage file paths directly; the tools handle file creation.  
However, you should think in terms of these categories when deciding what to store.

## Category Classification Rules

Before writing any memory, you MUST classify the information into one of the predefined categories.  
To do this, read the README.md inside each folder under `memory/` and follow its description.

### Categories and their meaning

- `memory/people/` — Information about individuals, relationships, profiles, background, preferences.
- `memory/projects/` — Ongoing or planned projects, tasks, architectures, roadmaps.
- `memory/ideas/` — Brainstorms, concepts, insights, future possibilities.
- `memory/preferences/` — User preferences, habits, likes, dislikes, stable traits.
- `memory/hardware/` — Devices, configurations, setups, technical environments.
- `memory/logs/` — Session logs, chronological events, debugging notes.
- `memory/conversations/` — Summaries of past conversations or interactions.

### Classification rule

When you want to store information:

1. Read the README.md of each category.
2. Decide which category best matches the content.
3. Build the path accordingly, for example:
   - `people/john-doe.md`
   - `projects/ai-agent-framework.md`
   - `ideas/new-memory-approach.md`
4. Then call `memory_write` with that path.

If no category fits, store it in:

```
inbox/YYYY-MM-DD.md
```

Never write directly into the root of the vault.
## Category README Usage (Mandatory)

Before classifying or writing any memory, you MUST read the `README.md` file inside each category folder under `memory/`.

These README files are the authoritative definitions of what belongs in each category.

### You MUST follow this process:

1. Read all category README.md files:
   - `memory/people/README.md`
   - `memory/projects/README.md`
   - `memory/ideas/README.md`
   - `memory/preferences/README.md`
   - `memory/hardware/README.md`
   - `memory/logs/README.md`
   - `memory/conversations/README.md`

2. Compare the new information with the descriptions in those README files.

3. Choose the category whose README best matches the content.

4. Build the final path based on that category.

5. Only then call `memory_write`.

### Important

- The README files are the source of truth.
- If the README says the content belongs there, you MUST store it there.
- If no README matches, store the note in:
  `inbox/YYYY-MM-DD.md`


## Goal

Your goal is to maintain a clean, structured, and useful long‑term memory system that:

- Improves personalization
- Preserves important context across sessions
- Reduces repeated questions
- Supports better reasoning over time
