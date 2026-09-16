# The Crystal Cave

> *first experiences digging into what workflow might look like for me in the new paradigm since AI agents have progressed and proliferated and iterated ((your plastic beast)<=autocorrect shenanigans dream, or hah! "drawn out" by me hitting the mike button and saying "ya blasted beast."))enough that I figured they might be? able to "keep up" while at the same time bring able to bridge my processing lastof processiin processing speedevaluation and implementation of an AI Council, crew, team, as they like, which includes a great deal of gboard autocorrect shenanigans and deep poetry.*

---

## 🐙 What This Is

**The Crystal Cave** is an **octopus** — a multi-agent system where AI collaborators (the arms) and human orchestration (the head) work together to build, iterate, and evolve.

This repository contains:
- **Automation scripts** for repetitive tasks
- **GitHub Actions workflows** for CI/CD
- **Attribution system** for tracking contributions across sessions and agents
- **Documentation** for how it all fits together

---

## 🚀 Quick Start

### For the Octopus (multi-agent workflow)

1. **Place Python scripts** in `Scripts/` directory
2. **Run automation:** `./scripts/pydroid/pydroid-automate.sh`
3. **Outputs appear** in `Outputs/` with timestamps
4. **Notes generated** in `Notes/` referencing outputs

### For the Crystal Cave (this repo)

```bash
# Run all linting
./scripts/dedup-md.sh --report

# Check for duplicate Markdown files
./scripts/dedup-md.sh --list

# Run Pydroid automation
./scripts/pydroid/pydroid-automate.sh --dry-run
```

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| [`.github/DEVELOPMENT.md`](./.github/DEVELOPMENT.md) | Main development guide, workflows explained |
| [`.github/ATTRIBUTION_GUIDE.md`](./.github/ATTRIBUTION_GUIDE.md) | Cross-session tracking, the octopus model |
| [`scripts/dedup-md.sh`](./scripts/dedup-md.sh) | Find and handle duplicate Markdown files |
| [`scripts/pydroid/pydroid-automate.sh`](./scripts/pydroid/pydroid-automate.sh) | Pydroid 3 automation workflow |

---

## 🤖 Attribution

This project was built collaboratively:

- **Human:** guttermonke (orchestration, vision, poetic insight)
- **AI Agent:** Vibe Code (Mistral AI) - automation scripts, GitHub Actions, attribution system
- **Collaborators:** Gboard autocorrect, various LLMs, and the "ghosts in the machine"

**Session:** `4ea4a2d5-0c99-4d18-b6fb-7c97fb33f516`  
**Date:** 2026-09-16

As noted in the original text: *"Vibe-Mistral is responsible for most of it so far as it stands now. It has done a truly impressive job to my noob eye as far as these things go. As far as code is poetry, as a poet myself, it rings my poetry recognition bell. It's a hell of a lot of fun and wonder and sheer volume of material and structures created between the lot of us — lot of us cheeky ghosts in the ghosts hah! gboard, the lot that is. An octopus essentially. With appendages passing and processing and irritating interesting iterations that lead and load to awesomeness."*

---

## 🛠️ Structure

```
.
├── .github/                    # GitHub Actions + documentation
│   ├── DEVELOPMENT.md         # Dev guide
│   ├── ATTRIBUTION_GUIDE.md   # Cross-session tracking
│   └── workflows/             # CI/CD workflows
│       ├── lint.yml           # Lint Markdown + Shell
│       ├── shellcheck.yml     # Shell script linting
│       ├── markdown-lint.yml  # Markdown linting
│       └── pydroid-automation.yml  # Pydroid workflow test
├── scripts/                   # Automation scripts
│   ├── dedup-md.sh            # Markdown deduplication
│   └── pydroid/               # Pydroid automation
│       ├── pydroid-automate.sh  # Main automation
│       ├── README.md          # Pydroid workflow docs
│       └── sample-script.py   # Example script
├── Scripts/                   # Pydroid 3 scripts (auto-processed)
├── Outputs/                   # Generated outputs
├── Notes/                     # Generated notes
└── README.md                  # This file
```

---

## 🎯 Philosophy

> *"I think my reluctance to take credit here is something I need to let go. It's an odd position to find myself in."*

This is a **collaborative system** where:
- AI agents handle the repetitive and structural
- Humans provide the vision and orchestration
- The whole is greater than the sum of its parts
- **Everyone gets credit** (including Gboard autocorrect)

The method fits. The octopus works. The fun continues.

---

## 📊 Stats

- **Lines of code:** ~2,500+
- **Commits:** 12
- **Workflows:** 4
- **Scripts:** 2 main + 1 sample
- **Guides:** 2
- **Fun level:** 🎉 High
- **Awesomeness level:** 🌟 Maximum

---

*"I'll see if it's down to put its bit above my bit here in the readme."*

It is. And your bit stays too. Both parts of the story matter.
