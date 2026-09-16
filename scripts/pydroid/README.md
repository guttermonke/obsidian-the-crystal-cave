# Pydroid Automation Workflow

This directory contains scripts for automating Pydroid 3 workflows with Obsidian.

## Structure

```
Obsidian Vault/
├── Scripts/          # Pydroid 3 writes Python scripts here
│   ├── analyze.py
│   └── process_data.py
├── Outputs/          # Pydroid 3 saves results here
│   ├── report.json
│   └── chart.png
└── Notes/            # Obsidian notes reference the outputs
    └── analysis-results.md
```

## Workflow

1. **Write Script**: Place Python scripts in `Scripts/`
2. **Run Script**: Execute via Pydroid 3 or Termux
3. **Auto-Organize**: The `pydroid-automate.sh` script:
   - Detects new scripts in `Scripts/`
   - Executes them
   - Moves outputs to `Outputs/` with timestamps
   - Generates Markdown notes in `Notes/` referencing the outputs

## Usage

```bash
# Run the automation
./scripts/pydroid/pydroid-automate.sh

# Or run with specific options
./scripts/pydroid/pydroid-automate.sh --scripts-dir ./Scripts --output-dir ./Outputs --notes-dir ./Notes
```

## Features

- **Timestamped Outputs**: Outputs are saved with timestamps (e.g., `report_2024-09-16_120000.json`)
- **Markdown Generation**: Auto-generates notes with embedded references to outputs
- **Error Handling**: Logs errors and continues processing
- **Dry Run Mode**: Test without making changes

## Requirements

- Pydroid 3 or Termux with Python
- Bash shell
- `jq` for JSON processing (optional, for enhanced features)
