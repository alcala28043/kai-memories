# Skills

This directory contains the skills that define how the agent interacts with the Kai Memories vault.

Skills do NOT register tools.  
They only teach the LLM how and when to use them.

---

## Included skills

### `memory_skill.md`
Main memory behavior:
- When to search memory
- When to write memory
- How to avoid duplicates
- How to write atomic notes

### `memory_tools.md`
Detailed instructions for using:
- `memory_search`
- `memory_write`

### `memory_index_skill.md`
Allows the agent to:
- Trigger incremental indexing
- Trigger full indexing
- Refresh the index after manual edits

### `activation_prompt.md`
Helper prompt that tells the agent to load the memory skill.

---

## Notes

- Skills assume the tools are already registered in the agent  
- Skills do not modify agent configuration  
- Skills are modular and can be extended  
