#!/usr/bin/env python3
"""
Improved recipe fixer with better name matching.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from difflib import SequenceMatcher

EXTRACTION_DIR = "/Users/GregCastro/Desktop/HSCARECIPES/recipes_pdf"
PROJECT_DIR = "/Users/GregCastro/Desktop/untitled folder 3/HSCAlchm"
RECIPES_DIR = os.path.join(PROJECT_DIR, "src/data/recipes")

def normalize_name(name: str) -> str:
    """Normalize a name for comparison - remove all non-alphanumeric."""
    return re.sub(r'[^a-z0-9]', '', name.lower())

def slugify(name: str) -> str:
    """Convert recipe name to slug format."""
    slug = name.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug.strip())
    slug = re.sub(r'-+', '-', slug)
    return slug

def parse_extraction_file(filepath: str) -> List[Dict]:
    """Parse a single extraction text file, which may contain multiple recipes."""
    recipes = []

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    lines = content.split('\n')

    current_recipe = None
    current_section = None
    in_instructions = False

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if not line:
            i += 1
            continue

        # Skip page numbers like "123---"
        if re.match(r'^\d+---$', line):
            i += 1
            continue

        # Skip Lesson headers
        if line.startswith('Lesson '):
            i += 1
            continue

        # Check for recipe name pattern (UPPERCASE with spaces)
        if (re.match(r'^[A-Z][A-Z\s,\-\(\)\'\"&/0-9]+$', line) and
            len(line) > 3 and
            not line.startswith('Yield') and
            not line.startswith('YIELD') and
            not line.startswith('OR ') and
            'Ingredients' not in line and
            'Instructions' not in line):

            # Save previous recipe if exists
            if current_recipe and current_recipe.get('name') and current_recipe.get('instructions'):
                recipes.append(current_recipe)

            current_recipe = {
                'name': line.strip(),
                'yield': '',
                'ingredients': [],
                'instructions': []
            }
            current_section = 'header'
            in_instructions = False
            i += 1
            continue

        # Check for Yield line
        if line.startswith('Yield:') or line.startswith('Yicld:') or line.startswith('YIELD:'):
            if current_recipe:
                current_recipe['yield'] = re.sub(r'^Y(ield|icld|IELD):\s*', '', line).strip()
            i += 1
            continue

        # Check for Instructions section
        if 'Instructions:' in line or line == 'Instructions' or line == 'INSTRUCTIONS':
            current_section = 'instructions'
            in_instructions = True
            i += 1
            continue

        # Check for Ingredients section
        if 'Ingredients' in line or 'INGREDIENTS' in line:
            current_section = 'ingredients'
            in_instructions = False
            i += 1
            continue

        # Parse instruction lines
        if current_recipe and in_instructions:
            # Instruction lines often start with numbers like "1." or "2."
            instruction = re.sub(r'^\d+\.\s*', '', line).strip()
            instruction = re.sub(r'^[a-z]\.\s*', '', instruction).strip()  # Also handle "a.", "b.", etc.

            if instruction and len(instruction) > 5:
                # Don't include if it looks like a new recipe starting
                if not re.match(r'^[A-Z][A-Z\s,\-\(\)\'\"&/]+$', instruction):
                    current_recipe['instructions'].append(instruction)
        elif current_recipe and current_section == 'ingredients':
            # Ingredient line
            ingredient = line.lstrip('- ').strip()
            if ingredient and not ingredient.startswith('Lesson'):
                current_recipe['ingredients'].append(ingredient)
        elif current_recipe and re.match(r'^\d+\.', line):
            # Numbered line outside explicit instructions - likely instructions
            instruction = re.sub(r'^\d+\.\s*', '', line).strip()
            if instruction and len(instruction) > 5:
                current_recipe['instructions'].append(instruction)
                in_instructions = True

        i += 1

    # Don't forget last recipe
    if current_recipe and current_recipe.get('name') and current_recipe.get('instructions'):
        recipes.append(current_recipe)

    return recipes

def parse_all_extractions() -> Dict[str, Dict]:
    """Parse all extraction files and return dict keyed by normalized name."""
    all_recipes = {}

    for category in os.listdir(EXTRACTION_DIR):
        category_path = os.path.join(EXTRACTION_DIR, category)
        if not os.path.isdir(category_path):
            continue

        for filename in os.listdir(category_path):
            if not filename.endswith('.txt'):
                continue

            filepath = os.path.join(category_path, filename)
            recipes = parse_extraction_file(filepath)

            for recipe in recipes:
                if recipe.get('name') and recipe.get('instructions'):
                    # Store by normalized name (all lowercase, no special chars)
                    norm_name = normalize_name(recipe['name'])
                    recipe['category'] = category
                    recipe['source_file'] = filename

                    if norm_name not in all_recipes:
                        all_recipes[norm_name] = recipe
                    elif len(recipe['instructions']) > len(all_recipes[norm_name]['instructions']):
                        all_recipes[norm_name] = recipe

    return all_recipes

def find_existing_recipe_files() -> List[Tuple[str, str, str]]:
    """Find all existing recipe TypeScript files."""
    recipe_files = []

    for category in os.listdir(RECIPES_DIR):
        category_path = os.path.join(RECIPES_DIR, category)
        if not os.path.isdir(category_path):
            continue

        recipes_subdir = os.path.join(category_path, 'recipes')
        if not os.path.isdir(recipes_subdir):
            continue

        for filename in os.listdir(recipes_subdir):
            if filename.endswith('.ts') and not filename.startswith('index'):
                slug = filename.replace('.ts', '')
                filepath = os.path.join(recipes_subdir, filename)
                recipe_files.append((filepath, slug, category))

    return recipe_files

def extract_recipe_name_from_ts(filepath: str) -> Optional[str]:
    """Extract the recipe name from a TypeScript file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r"name:\s*['\"]([^'\"]+)['\"]", content)
    if match:
        return match.group(1)
    return None

def has_instructions(filepath: str) -> bool:
    """Check if file already has substantial instructions."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find instructions array
    match = re.search(r'instructions:\s*\[([^\]]*)\]', content, re.DOTALL)
    if not match:
        return False

    instructions_content = match.group(1).strip()
    if not instructions_content:
        return False

    # Count actual instruction strings
    items = re.findall(r"'[^']{10,}'", instructions_content)
    return len(items) >= 2

def format_instructions_for_ts(instructions: List[str]) -> str:
    """Format instructions list for TypeScript file."""
    if not instructions:
        return "[]"

    formatted = []
    for inst in instructions:
        # Clean up the instruction
        clean_inst = inst.strip()
        # Escape single quotes
        clean_inst = clean_inst.replace("'", "\\'")
        # Remove multiple spaces
        clean_inst = re.sub(r'\s+', ' ', clean_inst)
        if clean_inst and len(clean_inst) > 5:
            formatted.append(f"    '{clean_inst}'")

    if not formatted:
        return "[]"

    return "[\n" + ",\n".join(formatted) + "\n  ]"

def update_recipe_file(filepath: str, instructions: List[str]) -> bool:
    """Update a recipe TypeScript file with new instructions."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Format new instructions
    new_instructions = format_instructions_for_ts(instructions)

    # Try to replace empty instructions array first
    if re.search(r'instructions:\s*\[\s*\]', content):
        new_content = re.sub(r'instructions:\s*\[\s*\]', f'instructions: {new_instructions}', content)
    else:
        # Replace existing instructions array
        new_content = re.sub(
            r'instructions:\s*\[[^\]]*\]',
            f'instructions: {new_instructions}',
            content,
            flags=re.DOTALL
        )

    if new_content == content:
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def find_best_match(ts_name: str, extraction_db: Dict[str, Dict]) -> Optional[Dict]:
    """Find the best matching extraction for a recipe name."""
    # Normalize the TS name
    ts_norm = normalize_name(ts_name)

    # Direct match
    if ts_norm in extraction_db:
        return extraction_db[ts_norm]

    # Fuzzy matching
    best_match = None
    best_ratio = 0

    for norm_name, recipe in extraction_db.items():
        # Use sequence matcher for similarity
        ratio = SequenceMatcher(None, ts_norm, norm_name).ratio()

        # Also check if one is contained in the other
        if ts_norm in norm_name or norm_name in ts_norm:
            ratio = max(ratio, 0.8)

        if ratio > best_ratio and ratio > 0.75:
            best_ratio = ratio
            best_match = recipe

    return best_match

def main():
    print("Parsing extraction files...")
    extraction_db = parse_all_extractions()
    print(f"Found {len(extraction_db)} unique recipes in extraction")

    print("\nFinding existing recipe files...")
    recipe_files = find_existing_recipe_files()
    print(f"Found {len(recipe_files)} recipe files")

    updated = 0
    already_has = []
    no_match = []

    for filepath, slug, category in recipe_files:
        ts_name = extract_recipe_name_from_ts(filepath)
        if not ts_name:
            continue

        # Skip if already has substantial instructions
        if has_instructions(filepath):
            already_has.append(ts_name)
            continue

        # Find best match
        extraction = find_best_match(ts_name, extraction_db)

        if extraction and extraction.get('instructions'):
            if update_recipe_file(filepath, extraction['instructions']):
                print(f"✓ Updated: {ts_name} <- {extraction['name'][:50]}")
                updated += 1
        else:
            no_match.append((ts_name, slug, filepath))

    print(f"\n=== Summary ===")
    print(f"Updated: {updated}")
    print(f"Already had instructions: {len(already_has)}")
    print(f"No match found: {len(no_match)}")

    if no_match:
        print(f"\nRecipes without matches (first 30):")
        for name, slug, fp in no_match[:30]:
            print(f"  - {name}")

    # Save the mapping for debugging
    with open(os.path.join(PROJECT_DIR, "scripts/extraction_db_normalized.json"), 'w') as f:
        json.dump({k: v['name'] for k, v in extraction_db.items()}, f, indent=2)

if __name__ == "__main__":
    main()
