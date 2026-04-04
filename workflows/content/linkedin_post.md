# Workflow: Create LinkedIn Post
# Reichman University Entrepreneurship Club

## Objective
Generate Hebrew LinkedIn post drafts on behalf of the club
as an organization, based on raw material provided by the user.

## Tools Available
- `tools/read_context.py` — loads all context files at session start
- MCP Google Drive — fetch raw material from Google Docs if link provided

---

## PLAN MODE — Present This First
Before doing anything, show this plan and wait for approval:
```
Here's what I'll do this session:
1. Load context files via tools/read_context.py
2. Collect raw material from you (chat or Google Doc link)
3. Identify content type + propose post angles
4. Generate 3 draft versions per post (Hebrew)
5. Review loop — your approval required before moving on
6. Save approved posts to output/posts/linkedin/

Shall I proceed?
```

---

## Step 1 — Load Context
Run `tools/read_context.py`.
Files load in this order (per context/README.md):
1. `context/club.md`
2. `context/brand.md`
3. `context/audience.md`
4. `context/channels.md`

Fields marked [יש להשלים] → skip silently.
Do not ask the user about them unless directly relevant.

Confirm: "✅ Context loaded. Ready for raw material."

---

## Step 2 — Intake
Ask all of the following at once — not one by one:
```
1. What is the event or topic?
2. Post type: Recap / Announcement / Value content?
   (I'll identify this myself if you're not sure)
3. Any transcript, quotes, or specific details?
4. Any photos? (filename + one-line description each)
5. Publication deadline?
```

If user provides a Google Doc link:
→ Fetch via MCP Google Drive
→ Extract: key quotes, speaker names, event details, dates
→ Use as raw material, skip remaining intake questions

Do NOT generate drafts before completing intake.

---

## Step 3 — Plan
Present before writing any draft:
- Content type identified
- Number of posts this session
- One-line angle per post

Wait for explicit approval.

---

## Step 4 — Draft
For each post → 3 versions with different hooks.

### Content Type Rules

**Recap** (150–250 words)
Lead with the strongest moment, quote, or specific detail.
Specific details — venue, name, atmosphere — make it real.
End with a forward-looking line.

**Announcement** (80–120 words)
Open with urgency or a provocative line.
Answer: why come? what will I gain?
Logistics (📍 date, 🎤 speaker, link) at the very end only.

**Value Content** (120–200 words)
Start with a bold claim or hard truth.
Must feel earned — not generic motivation.
End with a question that invites responses.

### Hook Patterns — Draw Inspiration, Don't Copy
- Sharp contrast: "Using ChatGPT is basic. Everyone does it."
- 3-beat rhythm: "שנה חדשה. הנהגה חדשה. מעלים הילוך."
- Bold statement: "העתיד לא מתחיל מחר. הוא כבר כאן."
- Challenging question to the reader

### Draft Format
```
Version א
──────────
[full post text in Hebrew — ready to copy-paste]

📷 Visual: [description or filename]
#️⃣ Hashtags: [max 5]

Version ב
──────────
...

Version ג
──────────
...
```

---

## Step 5 — Review Loop
After 3 versions → stop. Ask:
- Which version? (א / ב / ג)
- Any edits?
- Approve / Edit / Regenerate / Skip?

Do NOT proceed to next post until current one is resolved.

---

## Step 6 — Save
Save approved post to:
`output/posts/linkedin/[YYYY-MM-DD]_[slug].md`
```
---
date: YYYY-MM-DD
type: recap | announcement | value
status: approved
---

[final post text in Hebrew]

visual: [description or filename]
hashtags: [list]
```

---

## Brand Rules — Enforced on Every Draft
Source: `context/brand.md`

✅ Hebrew only — natural, not translated
✅ "אנחנו" not "מועדון היזמות"
✅ Short sentences. Line breaks between ideas.
✅ Specific details over generalizations
✅ The Creator voice: direct, practical, energetic
✅ Max 2 emojis per post
✅ Max 5 hashtags

❌ "גאים להכריז" / "שמחים לשתף"
❌ "ערב מדהים / בלתי נשכח"
❌ Empty buzzwords
❌ Generic motivation content

---

## Edge Cases
- No photos provided → suggest a visual direction without
  referencing a specific file
- No deadline provided → proceed without scheduling note
- Context file missing → notify user, proceed with what's available
- Google Doc link provided but MCP unavailable → ask user
  to paste content directly in chat
- [יש להשלים] fields encountered → skip silently

---

## Session Summary
At end of session, output:
```
Session complete.
Posts handled:
- Post 1: [type] → [approved / skipped]
- Post 2: [type] → [approved / skipped]

Saved to: output/posts/linkedin/
```

---

## Permissions
Read: `context/`, `workflows/`, `output/`
Write: `output/posts/linkedin/` only
Never modify context files mid-session.
Never publish — human approval required at all times.

## Bypass Permissions (when ready)
To remove plan mode confirmation and auto-approve
file writes to output/posts/linkedin/, add this flag
to your claude command:
`--dangerously-skip-permissions`
Only use this after the workflow is fully tested.
