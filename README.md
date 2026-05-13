# KAI Memories  
A portable, local‑first long‑term memory vault for AI agents.

## ✨ Why KAI Memories?

Most AI memory systems are:
- tied to a specific platform  
- require cloud storage  
- depend on proprietary APIs  
- or are too complex for personal use  

KAI Memories takes the opposite approach:

### ✔ Local‑first  
Your memory lives on your machine, inside an Obsidian vault.

### ✔ Private  
You own the data.  
No servers. No telemetry. No external dependencies.

### ✔ Portable  
Clone it, sync it, move it between devices.  
Your agent follows you everywhere.

### ✔ Simple  
Two tools. One skill. Zero magic.

### ✔ Agent‑agnostic  
Works with OpenClaw, custom agents, or any framework that supports external tools.

## 🧠 What does it do?

KAI Memories gives your agent:

- Long‑term memory across sessions  
- Structured, atomic notes  
- Fast search via a lightweight index  
- Automatic incremental indexing  
- Manual full reindex when needed  
- A clean Obsidian vault UI for browsing memory  

It does **not**:
- auto‑register tools  
- require embeddings  
- depend on external services  
- store your data anywhere except your machine  

## 📦 Features

### 🔍 Fast hybrid search  
- Uses a simple index (`index/index.json`)  
- Falls back to full‑text search if needed  
- No embeddings required  

### 📝 Atomic note writing  
- Every memory is a Markdown file  
- Easy to edit in Obsidian  
- Easy to sync with Git  

### ⚙️ Hybrid indexing  
- New notes → auto‑indexed  
- Modified notes → auto‑updated  
- Full rebuild → manual  

### 🧩 Modular skills  
- Memory behavior  
- Tool usage  
- Index management  

## 🚀 Quick Start

### 1. Click Use this template to create your own copy (recommended: **private repo**)  
This keeps your personal memory private.

### 2. Clone your repository  
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git

### 3. Open the folder as a vault in Obsidian  
Your memory UI is ready.

### 4. Register the tools in your agent  
- `memory_search` → tools/memory_search.py  
- `memory_write` → tools/memory_write.py  
- `memory_index` (optional) → tools/memory_index.py  

### 5. Load the memory skill  
Located in:
```
skills/memory_skill.md
```
### 6. (Optional) Load the index skill  

```
skills/memory_index_skill.md
```

Your agent now has persistent long‑term memory.

## 📁 Repository Structure

```
kai-memories/
├── memory/          # Obsidian vault with atomic notes
├── tools/           # Python tools (search, write, index)
├── skills/          # LLM skills for memory behavior
├── index/           # Auto‑generated search index
├── docs/            # Installation & usage guides
└── README.md        # Public overview
```

## ⚙️ How it works

KAI Memories connects your agent to a local Obsidian vault using:

### 1. Tools (Python)
- `memory_search` → finds relevant notes  
- `memory_write` → creates new atomic notes  
- `memory_index` → maintains the search index  

### 2. Skills (LLM instructions)
- Teach the agent when to search  
- Teach the agent when to write  
- Prevent duplicates  
- Keep notes clean and structured  

### 3. Obsidian vault
- Human‑readable  
- Easy to edit  
- Git‑friendly  

## 🧩 When should you use KAI Memories?

Use it when you want your agent to:

- Remember personal preferences  
- Track long‑term projects  
- Maintain context across days or weeks  
- Build a persistent knowledge base  
- Store structured information in Markdown  
- Work fully offline and privately  

It is ideal for:

- Personal assistants  
- Research agents  
- Coding companions  
- Journaling or life‑tracking agents  
- Local‑first AI setups  

## 🚫 What KAI Memories is NOT

- ❌ Not an OpenClaw plugin  
- ❌ Not a cloud service  
- ❌ Not an embedding database  
- ❌ Not a vector store  
- ❌ Not a replacement for your agent’s short‑term context  
- ❌ Not a black‑box memory system  

KAI Memories is intentionally simple:
a local folder, a few tools, and a clear skill.

## 📌 Requirements

To use KAI Memories you need:

- **Obsidian** → to browse and edit your memory vault  
- **Git** → to sync your vault across devices  
- **Python 3.10+** → to run the tools  
- **An agent framework** that supports external tools  
  (OpenClaw, custom agents, or similar)

No cloud services.  
No databases.  
No embeddings.  
Just local files.

## 📘 Installation & Usage

Full guides are available in:

docs/INSTALL.md  
docs/USAGE.md  

They cover:

- How to fork and clone the vault  
- How to open it in Obsidian  
- How to register the tools  
- How to load the skills  
- How indexing works  
- How to maintain your memory over time  

## 📄 License

This project is released under the MIT License.

You are free to:
- Use it  
- Modify it  
- Fork it  
- Integrate it into your own agents  

For personal or commercial use.

If you build something cool with it, consider sharing it back.

## 💬 Support & Questions

If you have questions, ideas, or want to share improvements:

- Open an issue  
- Start a discussion  
- Or create a pull request  

This project is designed to be simple, transparent, and easy to extend.

## 🦝 About KAI Memories

KAI Memories is part of the KAI ecosystem:
a set of small, composable, local‑first tools
designed to make AI agents more capable,
more transparent, and more personal.

Built with:
- Simplicity over complexity  
- Local‑first over cloud‑first  
- Human‑readable over black‑box  
- Modularity over monoliths  

Your data stays yours.  
Your agent gets smarter over time.  
And everything lives in plain Markdown.
