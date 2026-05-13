# Contributing to Kai Memories

Thank you for your interest in contributing to Kai Memories.  
This project is designed to be simple, modular, and safe — both for humans and AI agents.

This document explains how to contribute code, documentation, or improvements.

---

## 📌 1. Repository Model

Kai Memories uses a **template repository** model.

Users create their own private memory vault by clicking:

**Use this template → Create a new repository**

This means:

- No forks  
- No PRs from user vaults  
- No shared memory across users  

Contributions to the **template itself** happen here, in this upstream repo.

---

## 📌 2. Branching Strategy

The project uses a clean and predictable branching model:

- **main** → stable, production-ready template  
- **dev** → integration branch  
- **release/*** → pre-release staging  
- **feature/*** → individual work branches  

### Rules

- Never push directly to `main`  
- All work must start from a `feature/*` branch  
- All PRs must target `dev`  
- Releases are merged from `release/*` into `main`  

---

## 📌 3. Conventional Commits

All commits must follow the **Conventional Commits** format:

Examples:

```
feat: add safe path validation to memory_write
fix: correct index rebuild logic
docs: update installation guide
refactor: simplify search traversal
```

Prefixes allowed:

- `feat:`  
- `fix:`  
- `docs:`  
- `refactor:`  
- `test:`  
- `chore:`  

---

## 📌 4. Contribution Workflow (Humans)

1. Create a branch:

```
git checkout -b feature/my-improvement
```

2. Make your changes  
3. Commit using Conventional Commits  
4. Push your branch  
5. Open a Pull Request targeting `dev`  
6. Wait for review  
7. Once approved, it will be merged into `dev`  

Releases are handled by maintainers.

---

## 📌 5. Contribution Workflow (AI Agents)

AI agents (Claw, Cursor, Windsurf, Cline, OpenCode, etc.) **must follow stricter rules**.

### AI Rules

- Must work **only** in `feature/*` branches  
- Must never push to `dev`, `release`, or `main`  
- Must always open a Pull Request  
- Must include a SPEC or reasoning summary in the PR description  
- Must not modify files outside allowed directories  

### Allowed directories for AI agents

- `tools/`  
- `skills/`  
- `docs/`  
- `memory/` (example data only — not real user memory)  

### Forbidden directories

- `.github/`  
- `.obsidian/`  
- Anything outside the repo root  

---

## 📌 6. Code Style

### Python

- Use clear, explicit code  
- Avoid unnecessary abstractions  
- Prefer readability over cleverness  
- Keep scripts portable (no external dependencies)  

### Markdown

- Use clean, readable Markdown  
- Avoid HTML unless necessary  
- Keep docs short and practical  

---

## 📌 7. Testing

Before submitting a PR:

- Ensure the memory tools run without errors  
- Validate safe-path behavior  
- Test writing, searching, and indexing  
- Confirm Obsidian opens the vault without warnings  

---

## 📌 8. Documentation

If you add or change functionality, update:

- `docs/USAGE.md`  
- `docs/INSTALL.md`  
- `README.md` (only if user-facing behavior changes)  

---

## 📌 9. Security & Safety

Kai Memories is designed to be **local-first and safe by default**.

All contributions must respect:

- Safe path handling  
- No writing outside `memory/`  
- No destructive operations  
- No external dependencies  
- No network calls  

---

## 📌 10. Opening Issues

When opening an issue, include:

- What you expected  
- What happened  
- Steps to reproduce  
- Your environment (OS, Python version, Obsidian version)  

For feature requests:

- Explain the use case  
- Keep scope small and modular  

---

## 📌 11. Pull Request Template

Every PR must include:

- Summary of the change  
- Motivation / problem solved  
- SPEC or reasoning (for AI agents)  
- Testing steps  
- Screenshots if relevant  

---

## 📌 12. License

By contributing, you agree that your contributions will be licensed under the repository’s license.

---

Thank you for helping improve Kai Memories.  
Your contributions make the ecosystem stronger.
