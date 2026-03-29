# How We Work — Team Guide

## First-Time Setup

1. Download [GitHub Desktop](https://desktop.github.com/)
2. Sign in with your GitHub account
3. Clone this repository: File → Clone Repository → paste the repo URL
4. Done — you now have the full project on your computer

---

## Daily Workflow (Every Time You Work)

```
1. Open GitHub Desktop
2. Click "Fetch origin" → then "Pull" — get the latest changes from the team
3. Make your changes
4. Write a commit message describing what you did (see examples below)
5. Click "Commit to main"
6. Click "Push origin" — upload your changes
```

**Always pull before you start. Always push when you're done.**

---

## Commit Message Examples

Good:
- `Added Pitch Night promotion workflow`
- `Fixed empty row bug in sheets_write.py`
- `Updated brand.md with new tone guidelines`
- `Added M Club context to club.md`

Bad:
- `changes`
- `update`
- `fixed stuff`

The message is for your teammates (and future you). Make it readable.

---

## Who Owns What

To avoid conflicts, each person primarily works in their domain:

| Domain | Files |
|--------|-------|
| Content & Brand | `workflows/content/`, `context/brand.md`, `context/channels.md` |
| Events | `workflows/events/` |
| Operations & Members | `workflows/members/`, `context/club.md` |
| Tools & Tech | `tools/`, `workflows/meta/` |
| Context & Assets | `context/assets.md`, `context/audience.md` |

_Fill in team names next to each domain._

---

## Files You Should NEVER Commit

- `.env` — your personal API keys. Every team member has their own.
- `credentials.json` / `token.json` — Google OAuth files. Personal.
- Anything in `.tmp/` — disposable processing files.

These are already in `.gitignore` so GitHub Desktop will ignore them automatically.

---

## If You Get a Conflict

A conflict happens when two people edited the same part of the same file.
GitHub Desktop will flag it — it looks scary but it's simple:

1. Open the conflicted file in any text editor
2. You'll see two versions marked clearly
3. Keep the one you want (or combine them)
4. Save, commit, push

When in doubt — ask before overwriting someone else's work.

---

## Questions?

Ask in the team chat before doing anything you're unsure about.
