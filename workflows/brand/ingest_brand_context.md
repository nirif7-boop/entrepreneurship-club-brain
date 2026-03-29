# Workflow: Ingest Brand Context

**Trigger:** The user provides new information about the club's brand, identity, structure, audience, channels, or assets.
**Purpose:** Absorb new knowledge permanently into the `context/` files so it's available in all future sessions.
**Key rule:** Never silently update a context file. Always show the user what you're about to write and get confirmation.

---

## Step 1 — Receive the New Content

Accept the new information in any form:
- Pasted text
- Described verbally in the conversation
- Linked document (use `tools/scrape_page.py` if a URL is provided)
- Uploaded file

Read and understand the content fully before proceeding.

---

## Step 2 — Classify: Which File Does This Belong In?

| Information Type | Target File |
|-----------------|-------------|
| Mission, team structure, history, social handles, key dates | `context/club.md` |
| Tone of voice, visual identity, language policy, naming conventions | `context/brand.md` |
| Audience segments, their motivations, characteristics | `context/audience.md` |
| Platforms, posting cadence, content types per channel | `context/channels.md` |
| Canva links, Drive folder IDs, Sheets IDs, logo files | `context/assets.md` |

If information spans multiple files, split it and handle each file separately.

---

## Step 3 — Identify Conflicts

Read the relevant context file(s) and check:
- Does the new information **contradict** anything already there?
- Does it **duplicate** existing content?
- Does it **update** or **replace** a placeholder?

If a conflict exists, flag it to the user before writing:
> "שים לב — יש סתירה: הקובץ הנוכחי אומר X, והמידע החדש אומר Y. איזה מהם נכון?"

---

## Step 4 — Propose the Update

Show the user exactly what will be written:

> **קובץ:** `context/[file].md`
> **מה ישתנה:**
> ```
> [BEFORE]
> ...
>
> [AFTER]
> ...
> ```

Wait for explicit approval before writing.

---

## Step 5 — Write to the Context File

Once approved:
1. Edit the relevant section(s) of the context file
2. Remove placeholder text (`_[יש להשלים]_`) where real content is now available
3. Keep the 3–5 line summary at the top of the file up to date

---

## Step 6 — Confirm

Tell the user:
> "עודכן ✓ — [שם הקובץ] כולל עכשיו את [תיאור קצר של מה שנוסף]."

---

## Notes

- Run this workflow any time the user says "תזכור ש...", "עדכן את...", "אנחנו בעצם...", or provides factual information about the club
- After several ingestion sessions, run `tools/read_context.py` to verify the full context snapshot looks coherent
- Never store operational links (Zoom meeting links, one-time calendar invites) in context files — those are ephemeral
