# Workflow: Intake New Request

**Trigger:** Every time the user gives a new task or request.
**Purpose:** Classify the request, route it to the correct workflow, gather missing inputs, then execute.
**Prerequisite:** `workflows/meta/session_start.md` must have already run.

---

## Step 1 — Classify the Request

Determine which domain the request falls into:

| Domain | Keywords / Signals | Workflow to use |
|--------|-------------------|-----------------|
| **Content** | post, caption, Instagram, LinkedIn, newsletter, copy, write | `workflows/content/` |
| **Event** | event, panel, workshop, hackathon, networking, meetup | `workflows/events/` |
| **Members** | member, join, roster, list, applicant, onboard | `workflows/members/` |
| **Brand / Context** | brand, identity, tone, logo, guidelines, "remember that...", "update our..." | `workflows/brand/ingest_brand_context.md` |
| **Partnership** | sponsor, partner, collaboration, outreach, pitch | `workflows/partnerships/` _(future)_ |
| **System / Meta** | workflow, tool, script, fix, improve the system | `workflows/meta/update_workflow.md` |

If the request spans multiple domains, identify the **primary** domain and note any secondary ones.

---

## Step 2 — Identify Required Inputs

Before starting work, confirm you have:

**For content tasks:**
- Topic or subject matter
- Goal (awareness / event promotion / engagement / education)
- Target channel (Instagram, LinkedIn, WhatsApp, email)
- Any existing assets (images, prior copy, event details)
- Deadline (if any)

**For event tasks:**
- Event name and type
- Date and location (or "TBD")
- Target audience
- Key speakers or guests (if known)

**For member tasks:**
- Operation type (add / update / search / export)
- Member data or search criteria

**For brand/context ingestion:**
- The new information to absorb (pasted text, document, or described verbally)

---

## Step 3 — Clarify Gaps

If any required input is missing, ask **one focused question** at a time.
Do not start producing output until you have enough to proceed correctly.

Example: If the user asks for "an Instagram post for our next event" but no event details exist:
> "בשמחה! בשביל הפוסט — תוכל לשתף את שם האירוע, התאריך, ומה הנושא הראשי?"

---

## Step 4 — Confirm Workflow

State clearly which workflow you're about to follow, e.g.:
> "I'll follow `workflows/content/create_instagram_post.md`."

Then execute that workflow.

---

## Step 5 — Deliver and Log

After completing the task:
1. Write the final output to its designated cloud destination (Google Sheet, Drive, etc.)
2. Confirm with the user: share the link or paste the output for review
3. _(Optional)_ Append a one-line log entry to the session log sheet: `[date] | [task type] | [deliverable location]`

---

## Edge Cases

- **Ambiguous request:** Ask one clarifying question before classifying
- **No matching workflow:** Handle ad-hoc with best judgment, then invoke `update_workflow.md` to formalize the pattern
- **User provides context mid-task:** If new brand/club information surfaces, pause, absorb it via `ingest_brand_context.md`, then continue
