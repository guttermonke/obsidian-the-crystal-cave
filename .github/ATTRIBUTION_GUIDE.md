# Attribution Guide: Cross-Session Tracking

This guide explains how the Octopus Attribution System handles content that moves between sessions, agents, and collaborators.

## ✅ Yes, It Works for Cross-Session Copy/Pasting

The tagging system is **designed specifically** for tracking content across sessions. Since tags are embedded in file content (not git metadata), they travel with the text when you copy/paste.

---

## 📋 How It Works

### The Core Principle

**Tags are part of the content itself**, not external metadata. This means:

```
Content + Tags = Single portable unit
```

When you copy content, the tags come with it automatically.

---

## 🎯 Cross-Session Workflow Patterns

### Pattern 1: Copy Whole File

**Source (Session A):**
```markdown
---
tags:
  - attribution/author:vibe-code
  - attribution/session:abc123
  - attribution/date:2026-09-15
  - attribution/type:automation
---

# File content here...
```

**After copy/paste to Session B:**
```markdown
---
tags:
  - attribution/author:vibe-code
  - attribution/session:abc123
  - attribution/date:2026-09-15
  - attribution/type:automation
---

# File content here...
```

**Result:** All original attribution preserved ✅

---

### Pattern 2: Copy Section of File

**Source (Session A):**
```markdown
Some intro text.

---
tags:
  - attribution/author:vibe-code
  - attribution/session:abc123
  - attribution/type:content
---

This section was created in Session A.

More text.
```

**After copy/paste to Session B:**
```markdown
---
tags:
  - attribution/author:your-name
  - attribution/session:xyz789
  - attribution/date:2026-09-16
---

Some new intro.

---
tags:
  - attribution/author:vibe-code
  - attribution/session:abc123
  - attribution/type:content
---

This section was created in Session A.

New text from Session B.
```

**Result:** Both sessions tracked in same file ✅

---

### Pattern 3: Merge/Mashup Content

**Combining content from 3 different sessions:**

```markdown
---
tags:
  - attribution/author:your-name
  - attribution/session:current-session
  - attribution/date:2026-09-16
  - attribution/type:content
---

# My New Document

---
tags:
  - attribution/author:vibe-code
  - attribution/session:4ea4a2d5-0c99-4d18-b6fb-7c97fb33f516
  - attribution/type:automation
---

## Automation Section (from Session 4ea4a2d5)

This content came from the automation session.

---
tags:
  - attribution/author:another-agent
  - attribution/session:def456
  - attribution/type:feature
---

## Feature Section (from Session def456)

This content came from a feature session.

---
tags:
  - attribution/author:your-name
  - attribution/session:current-session
  - attribution/type:integration
---

## Integration Notes (current session)

This ties it all together.
```

**Result:** Full provenance chain preserved ✅

---

## 🔧 Tools for Working with Cross-Session Content

### 1. Extract Tags from a Section

```bash
# Extract all attribution tags from a file
grep -E "attribution/" my-file.md

# Extract specific session tags
grep "attribution/session:" my-file.md

# Extract all authors
grep "attribution/author:" my-file.md
```

### 2. Validate Tags in a File

```bash
# Check if file has required attribution
grep -q "attribution/author:" my-file.md && echo "Has author" || echo "Missing author"
grep -q "attribution/session:" my-file.md && echo "Has session" || echo "Missing session"
grep -q "attribution/date:" my-file.md && echo "Has date" || echo "Missing date"
```

### 3. Add Your Session Tags When Modifying

```bash
# Add your session tag to a file that's missing it
cat my-file.md | sed '/^---$/a\  - attribution/session:YOUR-SESSION-ID' > temp.md && mv temp.md my-file.md
```

### 4. Generate a Provenance Report

```bash
# Show all sessions that contributed to a file
echo "Sessions in $(basename my-file.md):"
grep "attribution/session:" my-file.md | sed 's/.*: //'

# Show all authors
echo "Authors in $(basename my-file.md):"
grep "attribution/author:" my-file.md | sed 's/.*: //' | sort | uniq
```

---

## 📊 Cross-Session Query Examples

### Find All Files with Content from Session ABC123

```bash
# Simple search
grep -r "attribution/session:abc123" .

# Only Markdown files
grep -r "attribution/session:abc123" --include="*.md" .

# With context (show surrounding lines)
grep -r -A2 -B2 "attribution/session:abc123" .
```

### Find Files Modified in Multiple Sessions

```bash
# Files that have BOTH session abc123 AND xyz789
comm -12 <(grep -rl "attribution/session:abc123" . | sort) <(grep -rl "attribution/session:xyz789" . | sort)
```

### Show Full Provenance of All Files

```bash
# Create a provenance report
echo "=== PROVENANCE REPORT ===" > provenance-report.md
echo "" >> provenance-report.md
echo "Generated: $(date)" >> provenance-report.md
echo "" >> provenance-report.md

for file in $(find . -name "*.md" -o -name "*.sh" | grep -v ".git"); do
  SESSIONS=$(grep "attribution/session:" "$file" 2>/dev/null | sed 's/.*: //' | tr '\n' ',' | sed 's/,$//')
  AUTHORS=$(grep "attribution/author:" "$file" 2>/dev/null | sed 's/.*: //' | tr '\n' ',' | sed 's/,$//')
  [ -n "$SESSIONS" ] && echo "- $file: sessions=$SESSIONS, authors=$AUTHORS" >> provenance-report.md
done

cat provenance-report.md
```

---

## 🎨 Best Practices for Cross-Session Work

### ✅ DO:

1. **Keep the YAML frontmatter** when copying whole files
2. **Add your own session tags** when modifying copied content
3. **Preserve original tags** - don't delete them
4. **Use nested tags** for sections from different sources
5. **Document the flow** - note where content came from

### ❌ DON'T:

1. **Strip tags** when copying content
2. **Replace all tags** with just your own
3. **Mix tagged and untagged content** without adding tags to the untagged parts
4. **Remove original attribution** - that breaks the provenance chain

---

## 📈 Real-World Example: Session Merging

**Scenario:** You're working on Session XYZ and want to incorporate content from Session ABC and Session DEF.

**Step 1: Copy from Session ABC**
```bash
# Copy the file but keep the tags
cp /path/to/session-abc/file.md ./my-new-file.md
```

**Step 2: Add your session context**
```markdown
---
tags:
  - attribution/author:your-name
  - attribution/session:xyz789
  - attribution/date:2026-09-16
  - attribution/type:integration
---

# Content from Session ABC (tags preserved below)
```

**Step 3: Paste content from Session DEF**
```markdown
---
tags:
  - attribution/author:your-name
  - attribution/session:xyz789
  - attribution/date:2026-09-16
  - attribution/type:integration
---

# Content from Session ABC
---
tags:
  - attribution/author:agent-abc
  - attribution/session:abc123
  - attribution/type:automation
---

Original automation content...

# Content from Session DEF
---
tags:
  - attribution/author:agent-def
  - attribution/session:def456
  - attribution/type:feature
---

Original feature content...

# Integration notes from Session XYZ
This ties everything together.
```

**Result:** Full provenance chain: ABC → XYZ, DEF → XYZ, all tracked ✅

---

## 🔄 Handling Edge Cases

### What if tags conflict?

**Example:** You copy content that has `author:agent-abc` but you modified it significantly.

**Solution:** Add both:
```markdown
---
tags:
  - attribution/author:agent-abc  # Original
  - attribution/author:your-name   # Modifier
  - attribution/session:abc123
  - attribution/session:xyz789
  - attribution/type:automation
  - attribution/type:refactor
---
```

### What if I don't know the original session?

**Solution:** Use a placeholder:
```markdown
---
tags:
  - attribution/author:unknown
  - attribution/session:unknown-2026-09
  - attribution/note:needs-attribution-review
---
```

Then search for these later:
```bash
grep -r "attribution/session:unknown" .
```

---

## 📝 Quick Reference Card

| Action | Command/Format |
|--------|---------------|
| Copy file with tags | Just copy - tags come with it |
| Copy section with tags | Copy the section + its tag block |
| Add your session tag | Add to YAML frontmatter |
| Find files from session | `grep -r "attribution/session:ID" .` |
| Find all sessions in file | `grep "attribution/session:" file.md` |
| Validate file has tags | `grep -q "attribution/" file.md` |
| Count sessions per file | `grep -c "attribution/session:" file.md` |

---

## 🧠 The Octopus Metaphor in Practice

Think of each piece of content as a **tentacle** with **suction cups** (tags):

```
Octopus Head (main branch)
    ├─ Arm 1 (Session ABC)
    │   └─ Tentacle (file.md)
    │       ├─ Suction Cup: author=agent-abc
    │       ├─ Suction Cup: session=abc123
    │       └─ Suction Cup: type=automation
    │
    ├─ Arm 2 (Session DEF)
    │   └─ Tentacle (feature.md)
    │       ├─ Suction Cup: author=agent-def
    │       └─ Suction Cup: session=def456
    │
    └─ Arm 3 (Your Session XYZ)
        └─ Tentacle (integration.md)
            ├─ Suction Cup: author=your-name
            ├─ Suction Cup: session=xyz789
            ├─ Suction Cup: author=agent-abc (from copied content)
            ├─ Suction Cup: session=abc123 (from copied content)
            └─ Suction Cup: author=agent-def (from other copied content)
```

When you copy a tentacle from one arm to another, **the suction cups stay attached**. The octopus doesn't lose track of where each tentacle came from.

---

## 🎓 Summary

| Question | Answer |
|----------|--------|
| Do tags travel with copied content? | ✅ Yes, they're embedded in the content |
| Can I track content across sessions? | ✅ Yes, by session ID tags |
| Can multiple sessions be in one file? | ✅ Yes, add multiple session tags |
| Can I find all files from a session? | ✅ Yes, `grep -r "attribution/session:ID" .` |
| Does this work for copy/paste? | ✅ Yes, that's the primary use case |

**The system is specifically designed for your workflow of moving content between sessions.**

---

*See also: [DEVELOPMENT.md](./DEVELOPMENT.md) for the main development guide*
