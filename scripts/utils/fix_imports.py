#!/usr/bin/env python3
"""
Fix import statements in index.ts files to include .ts extensions.
"""

import os
import re
from pathlib import Path

def fix_imports_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Pattern to match imports missing .ts extension
    pattern = r"from '\./recipes/([^']*)';$"

    def replace_func(match):
        filename = match.group(1)
        if not filename.endswith('.ts'):
            return f"from './recipes/{filename}.ts';"
        return match.group(0)

    # Fix imports
    fixed_content = re.sub(pattern, replace_func, content, flags=re.MULTILINE)

    if fixed_content != content:
        with open(filepath, 'w') as f:
            f.write(fixed_content)
        print(f'Fixed imports in {filepath}')

# Process all index.ts files
for index_file in Path('src/data/recipes').rglob('index.ts'):
    fix_imports_in_file(index_file)

print('All import statements fixed')
