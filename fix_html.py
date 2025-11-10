#!/usr/bin/env python3
"""Fix the index.html file by removing duplicate functions and orphaned code."""

with open('index.html', 'r') as f:
    lines = f.readlines()

# Find the line numbers for the duplicate parseDateRange and orphaned code
# Line 754 starts with "function parseDateRange" (the duplicate)
# Line 838 ends with "return filtered;" and closes the orphaned code block
# We need to remove lines 754-838 (inclusive, 0-indexed: 753-837)

# Remove lines 754-838 (85 lines)
fixed_lines = lines[:753] + lines[838:]

with open('index.html', 'w') as f:
    f.writelines(fixed_lines)

print(f"Removed {len(lines) - len(fixed_lines)} lines")
print(f"Original: {len(lines)} lines, Fixed: {len(fixed_lines)} lines")
