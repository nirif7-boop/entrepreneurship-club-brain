# Onboarding Guide — Innovation & AI Division

Welcome to the brain of the Entrepreneurship Club.
This document explains what we built, how it works, and exactly how to contribute to it.

Read the whole thing before touching anything.

---

## Part 1: What Is "The Brain"?

We built a system that lets Claude (Anthropic's AI) act as a smart agent for the club — not just answer questions, but **execute real tasks** consistently and reliably.

### The problem it solves

Without a system, every AI conversation starts from zero — no memory, no context, no consistency. You'd have to re-explain who we are, what our tone is, and what we want every single time.

With the brain, every session starts with:
- Full context about the club, our brand, our audience, and our content channels
- Clear instructions for each type of task
- Automated tools that handle the technical execution

The result: Claude behaves like a team member who deeply understands the organization — not like a search engine you have to re-brief every time.

---

## Part 2: The WAT Framework

The system is built on a three-layer architecture called **WAT**:

```
W — Workflows   (what to do)
A — Agent       (who decides)
T — Tools       (what executes)
```

### Layer 1: Workflows — The Instructions

The `workflows/` folder contains Markdown files that explain **how to execute each type of task**.

Each workflow is an SOP (Standard Operating Procedure) — like a briefing document you'd write for a new team member: what the goal is, what inputs are needed, which tools to use, what the expected output looks like.

Examples:
- `workflows/content/create_instagram_post.md` — how to write an Instagram post
- `workflows/events/plan_event.md` — how to plan an event from start to finish
- `workflows/meta/session_start.md` — what Claude does at the start of every session

### Layer 2: Agent — The Decision-Maker

This is Claude. It reads the relevant workflow, runs the tools in the right order, handles errors, and asks clarifying questions when needed.

**It doesn't guess — it follows instructions.**

### Layer 3: Tools — The Executor

The `tools/` folder contains Python scripts that do the deterministic work: reading and writing to Google Sheets, scraping, exporting to Drive, etc.

**The rule:** AI handles decisions. Code handles execution.

---

## Part 3: File Structure

Here's what every folder and file does:

```
entrepreneurship club/
│
├── CLAUDE.md              ← Operating instructions for Claude. Do not edit or delete.
│
├── ONBOARDING.md          ← This file. The starting point for new contributors.
│
├── context/               ← Who we are (written in Hebrew — intentional)
│   ├── club.md            ← Mission, structure, plans, key people
│   ├── brand.md           ← Tone of voice, persona, visual identity
│   ├── audience.md        ← Target audiences and how to speak to them
│   ├── channels.md        ← Platforms we use and what content goes where
│   └── assets.md          ← Links to Canva, Drive, Google Sheets
│
├── workflows/             ← How to do everything (written in English)
│   ├── meta/              ← System-level instructions (session start, routing)
│   ├── brand/             ← How to onboard a new brand context
│   ├── content/           ← Posts, newsletters, content creation
│   ├── events/            ← Event planning and promotion
│   └── members/           ← Member management
│
├── tools/                 ← Python scripts for technical execution
│
├── .env                   ← Your personal API keys (never shared, never uploaded)
│
└── .tmp/                  ← Temporary processing files (not uploaded to GitHub)
```

### What you'll actually edit

Most contributors will only ever touch files inside `context/` and `workflows/`. These are plain text files (Markdown format — more on that below). No coding required.

The `tools/` folder contains Python scripts. Only edit these if you know what you're doing, and always check with the team first.

---

## Part 4: Local vs. GitHub — Understanding the Two Versions

This is the most important concept to understand before anything else.

There are **two copies** of the project at all times:

```
Your computer (local)          GitHub (cloud / remote)
─────────────────────          ──────────────────────
Your personal copy             The shared "official" version
You edit files here            Everyone can see this
Changes stay private           Changes are visible to the team
  until you push them
```

Think of it like a Google Doc, except:
- You work on your own offline copy
- Changes only sync when you explicitly choose to sync them
- Every sync is logged with a message explaining what changed

**GitHub is the source of truth.** Whatever is on GitHub is what the system actually uses. Your local copy is just your workspace.

---

## Part 5: Git Concepts — Everything You Need to Know

Git is the system that tracks changes to files over time. GitHub is the website that hosts those files and makes collaboration possible. GitHub Desktop is the app that lets you use Git without typing commands.

Here are the six concepts you need:

---

### Repository (Repo)

The project folder — containing all the files. It exists both on your computer (local) and on GitHub (remote). Everyone on the team works from the same repository.

---

### Commit

A commit is a **saved snapshot with a message**. It's how you officially record a change.

Every time you finish a meaningful piece of work, you make a commit. The message explains what you changed and why.

```
Good commit messages:
✓ "Add Instagram workflow for event promotion"
✓ "Update brand tone guidelines in brand.md"
✓ "Fix broken link in assets.md"

Bad commit messages:
✗ "changes"
✗ "update"
✗ "stuff"
```

The message is for your teammates (and your future self). Make it readable. Six months from now, someone will need to understand what you did.

A commit does not automatically upload anything. It just saves the snapshot locally. You still need to push.

---

### Branch

A branch is an **isolated copy of the project** where you can work without affecting anyone else.

The main version of the project lives on a branch called `main`. This is the official version — what Claude actually uses. You never work directly on `main`.

Instead, when you start a task, you create a new branch with a descriptive name:

```
Examples of good branch names:
  update-audience-context
  add-newsletter-workflow
  fix-event-planning-steps
```

Your branch is completely separate from `main`. You can make as many changes as you want, and nothing happens to the live system until your branch is reviewed and approved.

```
main (official, protected)
  │
  ├── update-audience-context   ← your branch, isolated
  └── add-newsletter-workflow   ← someone else's branch, also isolated
```

---

### Push

Push = **upload your commits from your computer to GitHub**.

After you commit, your changes are saved locally but not visible on GitHub yet. Push sends them to the cloud so the rest of the team can see them.

---

### Pull

Pull = **download the latest changes from GitHub to your computer**.

Before you start working, always pull. This makes sure you're starting from the most up-to-date version of the project, including any changes your teammates made since you last worked.

---

### Pull Request (PR)

A Pull Request is a **formal request to merge your branch into `main`**.

When your work is done, you open a PR on GitHub. This notifies the team, shows exactly what you changed (line by line), and asks for approval before anything gets merged.

**Until your PR is approved and merged, your changes have zero effect on the live system.** This is intentional — it's the safety layer.

The process looks like this:

```
You work on your branch
        ↓
You open a Pull Request on GitHub
        ↓
Niri reviews what you changed
        ↓
Approved → merged into main ✓
  or
Changes requested → you update your branch → re-review
```

You'll get feedback directly in the PR on GitHub. If Niri requests changes, make them on the same branch, commit again, and push — the PR updates automatically.

---

## Part 6: API Keys — What They Are and Why They're Personal

Some of the tools in this project connect to external services: the Claude API, Google Sheets, etc. To use these services, you need **API keys** — essentially passwords that identify you to the service.

### What is an API key?

An API key is a long string of random characters, like:

```
sk-ant-api03-xK9mZ2....(many more characters)
```

It acts as your personal credential. When a script runs and calls an external service, it sends the key to prove it's allowed to use that service.

### Why are they personal?

- They're tied to billing — if someone uses your key, the charges go to your account
- They give access to your data — a Google key can read your Drive, your Sheets, etc.
- They should never be shared or committed to GitHub

### Where do they live?

All API keys go in the `.env` file in the root of the project:

```
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_SHEETS_ID=...
```

This file is in `.gitignore`, which means GitHub Desktop will never include it in a commit, no matter what. It stays on your machine only.

**If you don't have the `.env` file yet:** ask Niri directly. He'll send you the values over a private channel — not in a group chat, not in a GitHub comment.

### Never do this

- Never paste an API key into a workflow file, a context file, or anywhere in the repo
- Never send an API key over Telegram, WhatsApp, or email
- If you accidentally commit a key to GitHub, tell Niri immediately so it can be revoked

---

## Part 7: Setup — One Time Only

### Step 1: Create a GitHub account

Go to [github.com](https://github.com) and create a free account. Send your username to Niri so he can add you as a collaborator on the repository.

You'll get an email invitation — **you must accept it** before you have any access.

### Step 2: Install GitHub Desktop

Download GitHub Desktop from [desktop.github.com](https://desktop.github.com). This is a visual app that lets you use Git without any command-line knowledge.

Open it and sign in with the GitHub account you just created.

### Step 3: Clone the repository

Cloning means downloading a local copy of the project to your computer.

1. In GitHub Desktop, click **File → Clone repository**
2. Find `nirif7-boop/entrepreneurship-club-brain` (or paste the URL)
3. Choose a folder on your computer where you want it to live
4. Click **Clone**

You now have the full project on your machine. GitHub Desktop will keep it in sync with GitHub.

### Step 4: Get your `.env` file

Ask Niri for the API keys. Create a file called `.env` in the root of the project folder and paste the values in. This file will never appear in GitHub Desktop (it's gitignored).

---

## Part 8: The Daily Workflow

> **Rule #1:** Never push directly to `main`. All work happens on a branch and goes through a Pull Request.

---

### Before you start working

```
┌─────────────────────────────────────────────────────┐
│  1. Open GitHub Desktop                             │
│  2. Make sure the current branch shows "main"       │
│  3. Click "Fetch origin" then "Pull origin"         │
│     → This downloads any changes your teammates     │
│       made since you last worked                    │
│  4. Click Branch → New Branch                       │
│  5. Give it a short, descriptive name:              │
│       update-instagram-workflow                     │
│       add-event-checklist                           │
│       fix-brand-tone-description                    │
│  6. Click "Create Branch"                           │
│     → You are now on your own isolated branch       │
└─────────────────────────────────────────────────────┘
```

Now go do your work — edit files, add content, update workflows. All changes are isolated to your branch.

---

### When you're done

```
┌─────────────────────────────────────────────────────┐
│  7. Open GitHub Desktop                             │
│  8. You'll see your changed files listed on         │
│     the left side                                   │
│  9. Click each file to review what changed          │
│     Green = line added   Red = line removed         │
│  10. Write a commit message in the text box         │
│      at the bottom left                             │
│  11. Click "Commit to [your-branch-name]"           │
│  12. Click "Push origin"                            │
│      → Your branch is now on GitHub                 │
│  13. Click "Create Pull Request"                    │
│      → A browser window opens on GitHub             │
│  14. Write a short title and description of         │
│      what you changed and why                       │
│  15. Click "Create Pull Request"                    │
│      → Niri gets notified and will review it        │
└─────────────────────────────────────────────────────┘
```

---

### What GitHub Desktop looks like

```
┌──────────────────┬──────────────────────────────────┐
│ Changes          │                                  │
│                  │  Green line = added              │
│ ✓ context/       │  Red line   = removed            │
│   brand.md       │                                  │
│                  │  This panel shows you exactly    │
│                  │  what changed in the file        │
├──────────────────┤                                  │
│ Summary          │                                  │
│ [______________] │                                  │
│ Description      │                                  │
│ [______________] │                                  │
│                  │                                  │
│ [Commit to       │                                  │
│  your-branch]    │                                  │
└──────────────────┴──────────────────────────────────┘
```

The **History** tab shows every commit ever made — who made it, when, and what changed.

---

## Part 9: What Is Markdown?

All the files in this project (`.md` files) are written in Markdown — a simple text format that uses plain characters for basic formatting.

You don't need to learn much. The basics:

```
# Big heading
## Medium heading
### Small heading

**bold text**
_italic text_

- bullet point
- another bullet point

`code or file name`
```

You can edit `.md` files in any text editor (Notepad, VS Code, even GitHub's web editor). No special software needed.

---

## Part 10: Ownership — Who Owns What

Each person is the primary owner of their domain. If you're editing a file outside your domain, check with the owner first.

| Domain | Files | Owner |
|--------|-------|-------|
| Content & brand | `workflows/content/`, `context/brand.md`, `context/channels.md` | |
| Events | `workflows/events/` | |
| Members & operations | `workflows/members/`, `context/club.md` | |
| Technical tools | `tools/`, `workflows/meta/` | Niri |
| Context & assets | `context/assets.md`, `context/audience.md` | |

_Fill in the names._

---

## Part 11: Files That Must Never Be Uploaded

These files are already protected by `.gitignore` — GitHub Desktop will automatically exclude them from every commit. But you should know why.

| File | Why it must stay local |
|------|------------------------|
| `.env` | Your personal API keys. Each person has their own. Never shared. |
| `credentials.json` | Google OAuth credentials. Personal. |
| `token.json` | Google OAuth session token. Personal. |
| `.tmp/` | Temporary processing files. Regenerated as needed. |

If GitHub Desktop ever shows one of these files as a change to commit — stop, and ask Niri.

---

## Part 12: When Things Go Wrong

### Merge conflict

A merge conflict happens when two people edited the **same line of the same file** at the same time. GitHub can't automatically decide which version to keep, so it asks you to resolve it manually.

This is rare if everyone sticks to their own domain. When it does happen — take a screenshot and post it in the team chat. We'll resolve it together.

### You committed something you didn't mean to

Don't panic. Tell Niri immediately. Git keeps full history — nothing is truly lost, and mistakes can be undone.

### You're not sure what to do

Pull first. Ask second. Never guess.

---

## Questions?

Post in the team chat. Don't make changes you're unsure about — ask first. The branch system exists precisely so that nothing irreversible happens by accident.
