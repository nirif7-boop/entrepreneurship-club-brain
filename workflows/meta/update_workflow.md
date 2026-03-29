# Workflow: Update a Workflow

**Trigger:** An existing workflow needs to be improved — due to a failure, a better method discovered, a new constraint, or a recurring pattern that should be formalized.
**Purpose:** Capture learnings permanently so the system improves over time. No lesson should live only in a single session.
**Rule:** Never update a workflow without user approval first.

---

## Step 1 — Identify What Needs Updating

Clearly state:
- **Which file** needs to be updated (full path)
- **Why** — what happened? (error, new constraint, better approach, new pattern)
- **What specifically** should change (add a step, fix an instruction, update a constraint, add a note)

Example triggers:
- A tool failed with a rate limit → add a note about rate limits + the workaround
- A better API endpoint was found → update the tool invocation step
- A new content format was used successfully → add it to the relevant content workflow
- A recurring edge case appeared → add it to the "Edge Cases" section

---

## Step 2 — Draft the Proposed Change

Write out the exact proposed change:
- What text/section will be **removed or replaced**
- What text will be **added**
- Where in the file the change belongs

Keep the diff minimal — only change what needs to change.

---

## Step 3 — Present to User for Approval

Show the user the proposed change before writing anything. Format:

> **File:** `workflows/[path]/[file].md`
> **Reason:** [one sentence explaining why]
> **Change:**
> ```
> [OLD]
> ...
>
> [NEW]
> ...
> ```

Do **not** write to the file until the user approves.

---

## Step 4 — Apply the Update

Once approved:
1. Edit the target workflow file with the approved change
2. Add a changelog comment at the top of the file if one doesn't exist yet:
   ```
   <!-- Last updated: YYYY-MM-DD | Reason: [brief description] -->
   ```
3. Confirm to the user that the update was applied

---

## Notes

- This workflow is self-referential — it can be used to update itself
- Treat every failure as a chance to improve the system, not just a one-off fix
- When in doubt about whether to create a new workflow vs. updating an existing one: update existing unless the new pattern is truly distinct in domain
