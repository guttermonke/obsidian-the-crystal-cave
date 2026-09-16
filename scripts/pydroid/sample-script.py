#!/usr/bin/env python3
"""
Sample Pydroid 3 script for demonstration.

This script:
1. Creates a sample data analysis report
2. Generates a JSON output file
3. Creates a simple text summary

Usage: python3 sample-script.py
"""

import json
import os
from datetime import datetime

# Sample data
sample_data = {
    "timestamp": datetime.now().isoformat(),
    "analysis_type": "text_parsing",
    "input_files": 5,
    "processed_files": 5,
    "total_words": 1542,
    "total_lines": 234,
    "unique_words": 456,
    "top_keywords": ["poetry", "freedom", "dream", "light", "soul"],
    "sentiment_score": 0.78,
    "processing_time_seconds": 2.34
}

# Output directory (will be overridden by pydroid-automate.sh)
output_dir = os.path.dirname(os.path.abspath(__file__))

# Save JSON report
json_output = {
    "metadata": {
        "generated_at": datetime.now().isoformat(),
        "script": os.path.basename(__file__),
        "version": "1.0.0"
    },
    "data": sample_data
}

json_path = os.path.join(output_dir, "report.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(json_output, f, indent=2)

print(f"Saved JSON report to: {json_path}")

# Save text summary
text_summary = f"""Text Analysis Summary
=====================

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Script: {os.path.basename(__file__)}

Analysis Results:
- Total words: {sample_data['total_words']}
- Total lines: {sample_data['total_lines']}
- Unique words: {sample_data['unique_words']}
- Sentiment score: {sample_data['sentiment_score']:.2f}
- Processing time: {sample_data['processing_time_seconds']:.2f}s

Top Keywords:
{', '.join(sample_data['top_keywords'])}

Status: Complete
"""

text_path = os.path.join(output_dir, "summary.txt")
with open(text_path, "w", encoding="utf-8") as f:
    f.write(text_summary)

print(f"Saved text summary to: {text_path}")
print("\nDone.")
