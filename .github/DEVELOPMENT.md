# Development Notes

This document explains the automation workflows, scripts, and development practices for this repository.

## 🤖 GitHub Actions Workflows

All workflows run automatically on **push to `main`** and **pull requests targeting `main`**.

### 1. Lint and Validate (`lint.yml`)

**Triggers:** Push/PR to `main`

**What it does:**
- Lints all Markdown files (excluding upstream docs and legacy content)
- Runs ShellCheck on all `.sh` and `.bash` scripts
- Checks for broken Markdown links
- Verifies no trailing whitespace in source files
- Checks file permissions for shell scripts

**Excluded from linting:**
- `Base 44 Documentation index.md` (upstream doc)
- `obsidian-native-git-bridge-0.6.7/**` (upstream project)
- `README.md`, `Untitled*.md`, `San Francisco*`, `Unti.md`, `The Form*`, `Synthesis*` (legacy content)
- `.png`, `.zip` (binary files)
- `.yml`, `.yaml`, `.sh`, `.bash` (formatting exceptions)

**Config file:** `.markdownlint-cli2.jsonc`

---

### 2. ShellCheck (`shellcheck.yml`)

**Triggers:** Push/PR to `main` when shell scripts change

**What it does:**
- Installs ShellCheck
- Runs `shellcheck --severity=error` on all shell scripts
- Fails if any errors are found

**Paths:** `**/*.sh`, `**/*.bash`

---

### 3. Markdown Lint (`markdown-lint.yml`)

**Triggers:** Push/PR to `main` when Markdown files change

**What it does:**
- Runs markdownlint-cli2 with custom config
- Uses same exclusions as the combined lint workflow
- Non-blocking (`continue-on-error: true`)

**Config file:** `.markdownlint-cli2.jsonc`

---

### 4. Pydroid Automation Test (`pydroid-automation.yml`)

**Triggers:** Push/PR to `main` when Pydroid scripts change

**Paths:** `scripts/pydroid/**`, `Scripts/**`

**What it does:**
1. Sets up Python 3.x
2. Tests `pydroid-automate.sh` in dry-run mode
3. Runs `pydroid-automate.sh` for real with sample script
4. Verifies output files are created
5. Cleans up test files

---

## 📁 Repository Structure

```
.
├── .github/
│   ├── DEVELOPMENT.md          # This file
│   ├── workflows/              # GitHub Actions workflows
│   │   ├── lint.yml
│   │   ├── markdown-lint.yml
│   │   ├── shellcheck.yml
│   │   └── pydroid-automation.yml
│   └── markdownlint-cli2.jsonc  # Markdown lint config
├── scripts/
│   ├── dedup-md.sh             # Markdown deduplication tool
│   └── pydroid/
│       ├── README.md
│       ├── pydroid-automate.sh  # Pydroid automation script
│       └── sample-script.py     # Example Python script
├── Scripts/                   # Pydroid 3 scripts (auto-processed)
├── Outputs/                   # Generated outputs
├── Notes/                     # Generated notes
└── ... (existing content)
```

---

## 🚀 Push Workflow

### When you push to `main`:

1. **All 4 workflows trigger** (if their path filters match)
2. **Lint and Validate** runs first:
   - Checks Markdown formatting
   - Lints shell scripts
   - Checks links
   - Verifies no trailing whitespace
3. **ShellCheck** runs in parallel:
   - Deep shell script analysis
4. **Markdown Lint** runs in parallel:
   - Dedicated Markdown checking
5. **Pydroid Automation Test** runs if scripts changed:
   - Tests the automation workflow

### Expected behavior:
- ✅ Green checkmark = All checks passed
- ❌ Red X = One or more checks failed
- ⚠️ Yellow = Some checks have warnings

---

## 🔀 Pull Request Workflow

### When you open a PR targeting `main`:

Same as push workflow - all 4 workflows run automatically.

### PR status:
- **Required checks:** Lint and Validate, ShellCheck
- **Optional checks:** Markdown Lint, Pydroid Automation Test
- PR cannot be merged if required checks fail

---

## 🛠️ Automation Scripts

### 1. Deduplication Script (`scripts/dedup-md.sh`)

**Purpose:** Find and handle duplicate Markdown files.

**Usage:**
```bash
# List duplicates
./scripts/dedup-md.sh --list

# Generate report
./scripts/dedup-md.sh --report

# Delete duplicates (BACKUP FIRST!)
./scripts/dedup-md.sh --delete

# Replace with hardlinks
./scripts/dedup-md.sh --hardlink

# Dry run (default)
./scripts/dedup-md.sh
```

**Example output:**
```
========================================
Markdown File Deduplication Report
========================================
----------------------------------------
Hash: 7d5128690acc3931535ca9fd272298a3
Size: 10382 bytes
Files (2 total):
  - ./The Form Of Sound.md
  - ./Untitled 2.md
Action: None (dry run)
  To delete duplicates, run: --delete
  To hardlink duplicates, run: --hardlink
========================================
Summary
========================================
Total duplicate groups: 1
Total duplicate files: 1
Potential space saved: 10 KB
```

---

### 2. Pydroid Automation (`scripts/pydroid/pydroid-automate.sh`)

**Purpose:** Automate Pydroid 3 Python script execution and output organization.

**Workflow:**
1. Monitors `Scripts/` directory for `.py` files
2. Executes each script using Python 3
3. Moves outputs to `Outputs/` with timestamp prefixes
4. Generates Markdown notes in `Notes/` referencing outputs

**Usage:**
```bash
# Dry run (test without changes)
./scripts/pydroid/pydroid-automate.sh --dry-run --verbose

# Real execution
./scripts/pydroid/pydroid-automate.sh --verbose

# Custom directories
./scripts/pydroid/pydroid-automate.sh \
  --scripts-dir ./my-scripts \
  --output-dir ./my-outputs \
  --notes-dir ./my-notes \
  --python python3

# Clean up processed scripts
./scripts/pydroid/pydroid-automate.sh --cleanup
```

**Options:**
- `--scripts-dir DIR` - Directory with Python scripts (default: `./Scripts`)
- `--output-dir DIR` - Directory for outputs (default: `./Outputs`)
- `--notes-dir DIR` - Directory for notes (default: `./Notes`)
- `--python CMD` - Python command (default: `python3`)
- `--dry-run` - Show what would happen without making changes
- `--verbose` - Show detailed output
- `--cleanup` - Remove processed scripts after execution
- `--help` - Show help message

**Output naming:**
- Script: `my_script.py`
- Timestamp: `20260916_120000`
- Output file: `Outputs/my_script_20260916_120000_report.json`
- Note file: `Notes/my_script_20260916_120000_report.md`

**Supported output types:**
- JSON: Embeds preview + download link
- PNG/JPG/GIF/SVG: Embeds image + view link
- TXT/LOG/MD: Embeds text preview + view link
- CSV: Embeds preview + download link
- Other: File info + download link

---

## 📝 Development Practices

### Before Committing:

1. **Run linting locally:**
   ```bash
   # Check Markdown
   npx markdownlint-cli2 **/*.md --config .markdownlint-cli2.jsonc
   
   # Check shell scripts
   shellcheck scripts/**/*.sh
   
   # Check for trailing whitespace
   git ls-files | xargs grep -l "[[:space:]]$" | grep -v ".png\|.zip\|.yml"
   ```

2. **Test automation scripts:**
   ```bash
   # Test deduplication
   ./scripts/dedup-md.sh --dry-run --report
   
   # Test Pydroid automation
   ./scripts/pydroid/pydroid-automate.sh --dry-run --verbose
   ```

### File Organization:

- **New Python scripts:** Place in `Scripts/` for auto-processing
- **New shell scripts:** Place in `scripts/` with executable permissions
- **New Markdown:** Follow standard formatting (see `.markdownlint-cli2.jsonc`)

### Branch Strategy:

- `main`: Production branch (protected)
- Feature branches: `feature/name` or `vibe/name`
- Hotfix branches: `hotfix/name`

---

## 🐛 Troubleshooting

### Workflow fails with "Configuration file unrecognized"

**Cause:** Wrong config file name or format.

**Fix:** Ensure config file is named `.markdownlint-cli2.jsonc` (not `.markdown-link-check.json`).

### Workflow fails with "Files with trailing whitespace found"

**Cause:** Source files have trailing spaces.

**Fix:** 
```bash
# Remove trailing whitespace
sed -i 's/[[:space:]]$//' FILE

# Or use pre-commit hook
```

### ShellCheck fails

**Cause:** Shell script has syntax errors or issues.

**Fix:**
```bash
# Run locally
shellcheck scripts/your-script.sh

# Fix issues, then commit
```

### Pydroid automation fails

**Cause:** Python script has errors or missing dependencies.

**Fix:**
```bash
# Test locally
python3 scripts/pydroid/sample-script.py

# Check dependencies
pip install -r requirements.txt
```

---

## 📚 Additional Resources

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2)
- [ShellCheck](https://www.shellcheck.net/)
- [markdown-link-check](https://github.com/gaurav-nelson/github-action-markdown-link-check)

---

## 💡 Tips

1. **Use `--dry-run` first** when testing automation scripts
2. **Check CI before merging** - All workflows must pass
3. **Exclusions are intentional** - Legacy files are excluded from strict linting
4. **The `dedup-report.md`** is auto-generated - don't edit manually
5. **Pydroid automation** works best with simple scripts that output files

---

*Last updated: 2026-09-16*
