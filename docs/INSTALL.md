# Kai Memories — Installation Guide

Kai Memories is a portable long‑term memory vault designed to work with OpenClaw (or similar agent frameworks) and Obsidian.

It is NOT an official ClawHub plugin.  
Instead, it is a private, Git‑syncable memory module that you can clone and use across machines.

---

## 1. Prerequisites

Before installing Kai Memories, make sure you have:

- **Obsidian** (to open and browse the vault)
- **Git** (to clone and sync your memory across devices)
- **OpenClaw** or another agent framework that supports external tools
- Ability to **edit your agent configuration** to register tools

Kai Memories does NOT auto‑register tools.  
You must declare them manually in your agent.

---

## 2. Create your own repository from this template

Click:

**Use this template → Create a new repository**

Recommended:

- Make it **private** (your memory will live here)
- Name it something like `my-kai-memories`

This gives you:

- Full privacy  
- GitHub sync across devices  
- Version control for your memory  
- A clean starting point  

---

## 3. Clone your new repository

Clone your personal memory vault:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

## 4. Open the vault in Obsidian

1. Open Obsidian.
2. Choose “Open folder as vault”.
3. Select the folder you just cloned.

You can now browse, edit, and organize your memory using Obsidian.

---

## 5. Register the tools in your agent

Your agent MUST expose the following tools:

- `memory_search`
- `memory_write`
- `memory_index` (optional but recommended)

These tools correspond to the Python scripts inside:

```
kai-memories/tools/memory_search.py
kai-memories/tools/memory_write.py
kai-memories/tools/memory_index.py
```

The exact configuration depends on your OpenClaw setup, but conceptually you are telling the agent:

- “This is the tool called `memory_search` and it runs this script.”
- “This is the tool called `memory_write` and it runs this script.”
- “This is the tool called `memory_index` and it runs this script.”

Without registering these tools, the memory system will NOT work.

---

## 6. Load the memory skill

Once the tools are registered, load the memory behavior by using:

```
kai-memories/skills/memory_skill.md
```

You can:

- Paste its content into your agent’s system prompt, OR
- Use your framework’s skill loader to load it from file

This skill teaches the agent:

- When to call `memory_search`
- When to call `memory_write`
- How to avoid duplicates
- How to write atomic notes
- What information should or should not be stored

---

## 7. (Optional) Use the activation prompt

For convenience, you can use:

```
kai-memories/skills/activation_prompt.md
```

This is a short helper prompt that tells the agent:

- “Load the memory skill from this file”
- “Assume the tools are already registered”

---

## 8. Start using the agent

Once everything is connected:

- The agent can **read memory** before answering  
- The agent can **write memory** after important interactions  
- Your memory is **persistent**, **portable**, and **Git‑syncable**  
- Obsidian becomes your UI for browsing and editing memory  

You now have a fully functional long‑term memory system for your agent.

---

## 9. (Optional) Register the index tool

For best performance, register:

- `memory_index`

This tool allows:
- Full index rebuilds
- Incremental updates
- Manual refresh after Obsidian edits

The memory system works without it,  
but indexing will be slower and less accurate.

### Note about the index folder

The folder:

```
kai-memories/index/
```

contains the auto‑generated search index (index.json).
You do NOT need to edit it manually.
If deleted, it will be regenerated automatically.