# Context Directory

This folder contains declarative knowledge about the Entrepreneurship Club.
It is **not** instructional — Claude reads it but does not execute it as a procedure.

## Loading Order

When invoking `tools/read_context.py`, files are loaded in this priority order:

1. `club.md` — Who we are: mission, structure, team, key dates
2. `brand.md` — How we sound and look: tone, visual identity, language policy
3. `audience.md` — Who we speak to: audience segments and their characteristics
4. `channels.md` — Where we publish: platforms, cadence, content types
5. `assets.md` — Where things live: Canva, Drive folders, templates, press kits

## Rules

- All files in this folder are written in **Hebrew**
- Update context files using `workflows/brand/ingest_brand_context.md`
- Never put procedural instructions here — those belong in `workflows/`
- When a context file grows large, keep a 3–5 line summary at the top of the file
