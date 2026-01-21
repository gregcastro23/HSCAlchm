#!/usr/bin/env python3
"""
Script to update category index.ts files to include all recipes in their directories.
"""

import os
import re
from pathlib import Path

def to_camel_case(filename):
    """Convert filename to camelCase for import/export."""
    # Remove .ts extension and convert to camelCase
    name = filename.replace('.ts', '')
    # Replace hyphens and underscores with spaces, then camelCase
    words = re.split(r'[-_]', name)
    if not words:
        return name
    # First word lowercase, subsequent words capitalized
    camel_case = words[0].lower()
    for word in words[1:]:
        camel_case += word.capitalize()
    return camel_case

def extract_export_name(file_path):
    """Extract the export name from a recipe file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for export const name = ... or export const name: Recipe = ...
            match = re.search(r'export const (\w+)\s*[:=]', content)
            if match:
                return match.group(1)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def update_category_index(category_path):
    """Update the index.ts file for a category."""
    recipes_dir = category_path / 'recipes'
    index_file = category_path / 'index.ts'

    if not recipes_dir.exists():
        print(f"No recipes directory for {category_path.name}")
        return

    # Get all .ts files in recipes directory
    recipe_files = sorted(recipes_dir.glob('*.ts'))

    if not recipe_files:
        print(f"No recipe files in {category_path.name}")
        return

    # Extract export names
    imports = []
    exports = []

    for recipe_file in recipe_files:
        filename = recipe_file.name
        export_name = extract_export_name(recipe_file)

        if not export_name:
            # Fallback to camelCase conversion
            export_name = to_camel_case(filename)
            print(f"Using fallback export name for {filename}: {export_name}")

        imports.append(f"import {{ {export_name} }} from './recipes/{filename}';")
        exports.append(f"  {export_name},")

    # Create the index.ts content
    content = "import { Recipe } from '../../../types/recipe';\n"
    content += '\n'.join(imports)
    content += '\n\n'
    content += f"export const {category_path.name}Recipes: Recipe[] = [\n"
    content += '\n'.join(exports)
    content += '\n];'

    # Write the index file
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {category_path.name} index.ts with {len(recipe_files)} recipes")

def main():
    base_path = Path('/Users/GregCastro/Desktop/untitled folder 3/HSCAlchm/src/data/recipes')

    categories = [
        'appetizers', 'beverages', 'breakfast', 'condiments', 'desserts',
        'dinner', 'lunch', 'salads', 'sauces', 'sides', 'soups'
    ]

    for category in categories:
        category_path = base_path / category
        if category_path.exists():
            print(f"\n=== Updating {category} ===")
            update_category_index(category_path)
        else:
            print(f"Category {category} not found")

if __name__ == '__main__':
    main()
