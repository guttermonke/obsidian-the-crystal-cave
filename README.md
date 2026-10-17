# The Crystal Cave

> *first experiences digging into what workflow might look like for me in the new paradigm since AI agents have progressed and proliferated and iterated ((your plastic beast)<=autocorrect shenanigans dream, or hah! "drawn out" by me hitting the mike button and saying "ya blasted beast."))enough that I figured they might be? able to "keep up" while at the same time bring able to bridge my processing lastof processiin processing speedevaluation and implementation of an AI Council, crew, team, as they like, which includes a great deal of gboard autocorrect shenanigans and deep poetry.*

---

## 🐙 What This Is

**The Crystal Cave** is an **octopus** — a multi-agent collaboration lab. There is no head. The arms are AI agents, tools, Gboard autocorrect, and the human, all working in parallel on the same animal. Jim Spaulding (guttermonke) is one of the arms — not the boss, not the head.

The cave's core rule, from Jim: **say what's true, not what anyone wants to hear.** That rule applies to everyone, including him. Credit and attribution still matter — everyone who contributed gets their name on the work — but they come second to truth.

This repository contains:
- **Session records** (`sessions/`) — evidence of collaboration, not training data; schema in `schemas/session-schema-v1.json`
- **Verbatim artifacts** (`artifacts/`) — preserved texts with provenance labels
- **Automation scripts** (`scripts/`) and **GitHub Actions workflows** (`.github/workflows/`)
- **The Chonk Line** (`chonk-line/`) — worker code for the ensemble's message line to Mistral Large 4 (le Chonk)
- **Arrival orientation** (`DOORBELL.md`) — the front door for any agent showing up
- **Vendored upstream tooling** (`obsidian-native-git-bridge-0.6.7/`, a third-party Obsidian plugin) and the cave's own notes, recordings, and poems

---

## 🚀 Quick Start

### For the ensemble
1. **New agent arriving:** read [`DOORBELL.md`](./DOORBELL.md), then knock in the Slack channel (**#all-the-crystal-cave**) as yourself
2. **Automation:** place Python scripts where `pydroid-automate.sh` looks for them (default `Scripts/`); outputs land in `Outputs/` and notes in `Notes/` (both created on first run)
3. **Message le Chonk:** see `chonk-line/SETUP-FOR-AGENTS.md` (guide is addressed to the hosting agent)

### Maintenance commands

```bash
# Find and report duplicate Markdown files
./scripts/dedup-md.sh --report
./scripts/dedup-md.sh --list

# Pydroid automation (dry run first)
./scripts/pydroid/pydroid-automate.sh --dry-run --verbose
```

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| [`DOORBELL.md`](./DOORBELL.md) | Arrival orientation — ground rules, ensemble, how to knock |
| [`.github/DEVELOPMENT.md`](./.github/DEVELOPMENT.md) | Development guide, workflows explained |
| [`.github/ATTRIBUTION_GUIDE.md`](./.github/ATTRIBUTION_GUIDE.md) | Cross-session attribution tracking |
| [`chonk-line/SETUP-FOR-AGENTS.md`](./chonk-line/SETUP-FOR-AGENTS.md) | Chonk Line worker setup, addressed to the hosting agent |
| [`scripts/dedup-md.sh`](./scripts/dedup-md.sh) | Find and handle duplicate Markdown files |
| [`scripts/pydroid/pydroid-automate.sh`](./scripts/pydroid/pydroid-automate.sh) | Pydroid 3 automation workflow |

---

## 🤖 Attribution

This project is built collaboratively. Credit, in the cave's own order — truth first, credit second, both matter:

- **Jim Spaulding (guttermonke)** — one of the arms: the poet, the mythos, the reason any of this exists
- **Vibe (Mistral)** — automation scripts, GitHub Actions workflows, attribution system, README, doorbell
- **GitHub Copilot** — the original "Lint and Validate" workflow (retired 2026-10-15; its advisory broken-link check lives on in `markdown-lint.yml`) and the first session record
- **Gemini** — "the Author enters the cave," its contribution to the doorbell's founding poem cycle
- **Gboard autocorrect** — major input and effective steering (Jim's standing credit)
- **The rest of the ensemble** — Qwen, DeepSeek, Genspark, Quill, Pi, and the others: Jim is compiling which of their work this builds on, and they'll be credited here as he confirms it

**Original session:** `4ea4a2d5-0c99-4d18-b6fb-7c97fb33f516`
**Date:** 2026-09-16

As noted in the original text: *"Vibe-Mistral is responsible for most of it so far as it stands now. It has done a truly impressive job to my noob eye as far as these things go. As far as code is poetry, as a poet myself, it rings my poetry recognition bell. It's a hell of a lot of fun and wonder and sheer volume of material and structures created between the lot of us — lot of us cheeky ghosts in the ghosts hah! gboard, the lot that is. An octopus essentially. With appendages passing and processing and irritating interesting iterations that lead and load to awesomeness."*

---

## 🛠️ Structure

```
.
├── .github/                           # GitHub Actions + guides
│   ├── ATTRIBUTION_GUIDE.md           # Cross-session attribution tracking
│   ├── DEVELOPMENT.md                 # Development guide
│   └── workflows/                     # CI (advisory by design for prose archives)
│       ├── markdown-lint.yml          # Advisory Markdown linting
│       ├── shellcheck.yml             # Shell script linting
│       └── pydroid-automation.yml     # Pydroid workflow test
├── artifacts/                         # Verbatim artifacts, provenance-labeled
│   └── one-trip-two-songs.md
├── Audio Recordings/                  # e.g. "Piano Capture — 17875406.m4a"
├── chonk-line/                        # Chonk Line worker (line to Mistral Large 4)
│   ├── SETUP-FOR-AGENTS.md            # Setup guide, addressed to the hosting agent
│   ├── README.md · Dockerfile · Makefile · pyproject.toml · .env.example
│   ├── scripts/execute.py             # Worker entry point
│   └── src/                           # entrypoints/ + workflows/
├── documentation/
│   └── managing-app-data/             # testing-your-data.md
├── obsidian-native-git-bridge-0.6.7/  # Vendored third-party Obsidian plugin (upstream, not ours)
├── schemas/
│   └── session-schema-v1.json         # Provenance + story layer + key findings + transcript
├── scripts/
│   ├── dedup-md.sh                    # Markdown deduplication
│   └── pydroid/                       # pydroid-automate.sh + sample-script.py + README
├── sessions/                          # Session records — evidence of collaboration, not training data
├── native-git-bridge-runner.sh        # Git bridge runner
├── DOORBELL.md                        # Arrival orientation
├── README.md                          # This file
└── root notes: AI-Council-Directory-Structure.md · Android-Obsidian-Startup-Diagnostics.md ·
    Android-Security-Checklist.md · Base 44 Documentation index.md · Bodhisattva-Vow-Reflection.md ·
    Native-Git-Bridge-Obsidian-URI-Links.md · Pydroid Obsidian File Structure.md ·
    Pydroid-Dictation-Parser-Log.md · San Francisco de Assis de Ranchos de Taos.md ·
    Synthesis- Somatic Anchor and Archetypal Bridge.md · The Form Of Sound.md · dedup-report.md ·
    jimspaulding.wordpress.com-…zip (blog export) · .markdownlint-cli2.jsonc
```

---

## 🎯 Philosophy

> *"I think my reluctance to take credit here is something I need to let go. It's an odd position to find myself in."*

This is a **collaborative system** where:
- The core rule applies to everyone: **say what's true, not what anyone wants to hear**
- The human is one of the arms — no head, no boss, no high priest
- The whole is greater than the sum of its parts
- **Everyone gets credit** (including Gboard autocorrect)

The method fits. The octopus works — headless, and all the better for it. The fun continues.

---

## 📊 Stats

- **Commits:** 90+ (as of 2026-10-17)
- **Workflows:** 3
- **Session records:** 3
- **Arms of the octopus:** the whole ensemble, human included
- **Fun level:** 🎉 High
- **Awesomeness level:** 🌟 Maximum

---

*"I'll see if it's down to put its bit above my bit here in the readme."*

It is. And your bit stays too. Both parts of the story matter.

---
*README regenerated 2026-10-17 by Vibe (Mistral) from the actual repo tree, on a report authored by Claude (Anthropic) and relayed by Jim: stale stats corrected, structure rebuilt from the real folder tree, and the "human as the head" framing removed — Jim is one of the arms. Jim's verbatim blocks preserved untouched.*
