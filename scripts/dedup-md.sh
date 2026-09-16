#!/bin/bash
# dedup-md.sh - Find and handle duplicate Markdown files
# Usage: ./dedup-md.sh [--dry-run] [--delete] [--list]
#   --dry-run: Show duplicates without taking action (default)
#   --delete: Delete duplicates (keeps the first encountered)
#   --list:   List all duplicates and exit
#   --hardlink: Replace duplicates with hardlinks to the first copy
#   --report: Generate a report file (dedup-report.md)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Defaults
DRY_RUN=true
DELETE=false
LIST_ONLY=false
HARDLINK=false
REPORT=false

# Parse arguments
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
    --delete) DELETE=true ; DRY_RUN=false ;;
    --list) LIST_ONLY=true ;;
    --hardlink) HARDLINK=true ; DRY_RUN=false ;;
    --report) REPORT=true ;;
  esac
done

# Temporary files
TMP_DIR=$(mktemp -d)
trap "rm -rf $TMP_DIR" EXIT

# Find all Markdown files (excluding .git)
find . -type f -name "*.md" -not -path "./.git/*" | sort > "$TMP_DIR/files.txt"

# Calculate MD5 hashes and store as hash\tfile
while IFS= read -r file; do
  hash=$(md5sum "$file" | awk '{print $1}')
  echo -e "${hash}\t${file}" >> "$TMP_DIR/hashes.txt"
done < "$TMP_DIR/files.txt"

# Sort by hash
sort "$TMP_DIR/hashes.txt" > "$TMP_DIR/hashes-sorted.txt"

# Find duplicates (files with same hash) - group by hash and find groups with >1 file
# Using awk to group by first field (hash) and output groups with count > 1
awk -F'\t' '{
  hash = $1
  file = $2
  if (hash in files) {
    files[hash] = files[hash] "\t" file
    count[hash]++
  } else {
    files[hash] = file
    count[hash] = 1
  }
} END {
  for (hash in count) {
    if (count[hash] > 1) {
      print count[hash] "\t" hash "\t" files[hash]
    }
  }
}' "$TMP_DIR/hashes-sorted.txt" > "$TMP_DIR/duplicates.txt" 2>/dev/null || true

# Process duplicates
if [ ! -s "$TMP_DIR/duplicates.txt" ]; then
  echo "No duplicate Markdown files found."
  exit 0
fi

# Group duplicates by hash
declare -A HASH_GROUPS
declare -A HASH_COUNTS

while IFS=$'\t' read -r dup_count hash files_list; do
  HASH_GROUPS[$hash]="$files_list"
  HASH_COUNTS[$hash]="$dup_count"
done < "$TMP_DIR/duplicates.txt"

# Output header
echo "========================================"
echo "Markdown File Deduplication Report"
echo "========================================"
echo ""

# Track stats
TOTAL_DUPES=0
TOTAL_BYTES_SAVED=0

# Process each hash group
for hash in "${!HASH_GROUPS[@]}"; do
  files_list="${HASH_GROUPS[$hash]}"
  dup_count="${HASH_COUNTS[$hash]}"
  
  # Convert tab-separated list to array
  IFS=$'\t' read -ra files <<< "$files_list"
  
  TOTAL_DUPES=$((TOTAL_DUPES + dup_count - 1))
  
  # Get size of first file
  FIRST_FILE="${files[0]}"
  FILE_SIZE=$(stat -c%s "$FIRST_FILE" 2>/dev/null || stat -f%z "$FIRST_FILE" 2>/dev/null || echo 0)
  BYTES_SAVED=$((FILE_SIZE * (${#files[@]} - 1)))
  TOTAL_BYTES_SAVED=$((TOTAL_BYTES_SAVED + BYTES_SAVED))
  
  echo "----------------------------------------"
  echo "Hash: $hash"
  echo "Size: $FILE_SIZE bytes"
  echo "Files (${#files[@]} total):"
  
  # Print all files in the group
  for file in "${files[@]}"; do
    echo "  - $file"
  done
  
  echo ""
  
  if [ "$LIST_ONLY" = true ]; then
    continue
  fi
  
  # Determine action
  if [ "$DELETE" = true ]; then
    echo "Action: DELETE duplicates (keeping: ${files[0]})"
    for file in "${files[@]:1}"; do
      if [ "$DRY_RUN" = false ]; then
        echo "  Deleting: $file"
        rm -f "$file"
      else
        echo "  [DRY RUN] Would delete: $file"
      fi
    done
  elif [ "$HARDLINK" = true ]; then
    echo "Action: HARDLINK duplicates to first copy"
    for file in "${files[@]:1}"; do
      if [ "$DRY_RUN" = false ]; then
        echo "  Hardlinking $file -> ${files[0]}"
        rm -f "$file"
        ln "${files[0]}" "$file"
      else
        echo "  [DRY RUN] Would hardlink $file -> ${files[0]}"
      fi
    done
  else
    echo "Action: None (dry run)"
    echo "  To delete duplicates, run: --delete"
    echo "  To hardlink duplicates, run: --hardlink"
  fi
  
  echo ""
done

echo "========================================"
echo "Summary"
echo "========================================"
echo "Total duplicate groups: $(echo "${!HASH_GROUPS[@]}" | wc -w)"
echo "Total duplicate files: $TOTAL_DUPES"
echo "Potential space saved: $((TOTAL_BYTES_SAVED / 1024)) KB"
echo ""

# Generate report if requested
if [ "$REPORT" = true ]; then
  REPORT_FILE="$REPO_ROOT/dedup-report.md"
  echo "Generating report: $REPORT_FILE"
  
  {
    echo "# Markdown Deduplication Report"
    echo ""
    echo "Generated: $(date)"
    echo ""
    echo "## Summary"
    echo ""
    echo "- **Total duplicate groups:** $(echo "${!HASH_GROUPS[@]}" | wc -w)"
    echo "- **Total duplicate files:** $TOTAL_DUPES"
    echo "- **Potential space saved:** $((TOTAL_BYTES_SAVED / 1024)) KB"
    echo ""
    echo "## Duplicate Groups"
    echo ""
    
    for hash in "${!HASH_GROUPS[@]}"; do
      files_list="${HASH_GROUPS[$hash]}"
      dup_count="${HASH_COUNTS[$hash]}"
      
      # Convert tab-separated list to array
      IFS=$'\t' read -ra files <<< "$files_list"
      
      echo "### Group: ${hash:0:8}..."
      echo ""
      echo "Files:"
      for file in "${files[@]}"; do
        echo "- \`$file\`"
      done
      echo ""
    done
    
    echo "## Recommendations"
    echo ""
    echo "1. Review each group and decide which file to keep"
    echo "2. Run \`./scripts/dedup-md.sh --delete\` to remove duplicates"
    echo "3. Or run \`./scripts/dedup-md.sh --hardlink\` to replace with hardlinks"
    echo "4. Always back up your repository before running destructive operations"
  } > "$REPORT_FILE"
  
  echo "Report saved to: $REPORT_FILE"
fi

echo "Done."
