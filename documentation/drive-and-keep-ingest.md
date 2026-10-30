# Drive / Keep ingest for the Crystal Cave

The cave's material is scattered across Google Drive, Google Keep, the phone's
local storage (Obsidian + Pydroid 3 vaults), and the laptops' OneDrive/Windows
drives. Only Google Drive is reachable by agents in this session (read/search;
no delete or OneDrive connector), so Drive is the consolidation point.

## How to feed the cave from each source

| Source | How it gets in |
|---|---|
| Google Drive | Already reachable directly via the `google_drive_mcp` connector (search/read). Nothing to do. |
| Google Keep | No Keep connector exists. Export via **Google Takeout** (takeout.google.com, select Keep) and drop the zip in Drive root — it lands as `Takeout/Keep/*.html`/`*.json`, which `scripts/drive-index.py --from-takeout` can search. |
| Phone local storage (Obsidian/Pydroid vaults) | Copy the vault folders into Drive, or zip them and upload. |
| OneDrive / Windows drives (Dell, UFO) | Sync-selectively copy cave-relevant folders into Google Drive. Do NOT let a repo clone sit inside a OneDrive-synced folder — that is how 14GB of audio got sucked into a commit attempt. `.gitignore` now blocks audio/cloud-sync patterns. |

## Searching

- Repo content: `./scripts/search-cave.py "query" [--by-arm NAME] [--sessions-only]`
- Drive/Keep content: `./scripts/drive-index.py --from-takeout Takeout/ --query "gardener"`
  (or `--from-manifest cave-drive-index.json` once an agent exports a Drive manifest)

## Security note (2026-10-29)

The GCP service-account key `moonlit-gamma-*.json` was committed to this repo
2026-09-10, purged from git history 2026-10-29, and deleted at Google Cloud.
Four copies of the file still exist in Google Drive (created 2026-09-09..15,
2399 bytes each, in two folders). The Drive connector here is read-only, so
deletion must be done manually: in Drive, search `moonlit-gamma`, select the
four files, Move to trash, then empty trash. The key is dead at Google, so the
Drive copies are inert — but delete them anyway.

Gitleaks now runs on every push/PR (`.github/workflows/gitleaks.yml`) to catch
any future secret before it sits in history.
