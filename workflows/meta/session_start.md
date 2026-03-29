# Workflow: Session Start

**Trigger:** The beginning of every Claude session in this project.
**Purpose:** Load all institutional context, anchor operating constraints, and prepare for the user's request.
**Output:** A ready-to-operate agent with full club context in working memory.

---

## Steps

### Step 1 — Load Club Context

Run `tools/read_context.py` to load and concatenate all files from `context/` in priority order:
1. `context/club.md`
2. `context/brand.md`
3. `context/audience.md`
4. `context/channels.md`
5. `context/assets.md`

If any file is missing or empty (contains only placeholder text), note it but continue.
Do **not** ask the user to fill in missing context during this step — that happens in a dedicated session.

### Step 2 — Confirm Tool Inventory

Scan `tools/` and list available scripts. Before any task, verify the required tool exists.
If a required tool is missing, check `CLAUDE.md` — "look for existing tools first" before building new ones.

### Step 3 — Re-anchor Operating Constraints

Silently review the following rules from `CLAUDE.md`:
- All deliverables go to cloud (Google Sheets, Drive, etc.) — never leave final outputs as local files
- `.tmp/` is for intermediate processing only — disposable
- Secrets and API keys live exclusively in `.env`
- Always check `tools/` before creating a new script

### Step 4 — Receive and Route the Request

Once context is loaded and constraints are anchored, receive the user's request.
Proceed immediately to `workflows/meta/intake_new_request.md`.

---

## Notes

- This workflow runs at the start of **every** session — no exceptions
- If the user jumps straight into a task, run steps 1–3 silently in the background before responding
- Context files may be incomplete (placeholders) early in the project — that is expected and acceptable
