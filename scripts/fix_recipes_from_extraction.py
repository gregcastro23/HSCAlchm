#!/usr/bin/env python3
"""
Fix recipe files using improved PDF extraction data.
Parses extracted text files and updates TypeScript recipe files with proper instructions.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional

EXTRACTION_DIR = "/Users/GregCastro/Desktop/HSCARECIPES/recipes_pdf"
PROJECT_DIR = "/Users/GregCastro/Desktop/untitled folder 3/HSCAlchm"
RECIPES_DIR = os.path.join(PROJECT_DIR, "src/data/recipes")

def slugify(name: str) -> str:
    """Convert recipe name to slug format."""
    # Remove special characters and convert to lowercase
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

    # Split by recipe patterns - look for UPPERCASE recipe names
    # Pattern: Line starting with capital letters (recipe name)
    lines = content.split('\n')

    current_recipe = None
    current_section = None

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Skip empty lines at start
        if not line:
            i += 1
            continue

        # Check for recipe name pattern (UPPERCASE with spaces, parentheses allowed)
        # Recipe names are typically in ALL CAPS
        if (re.match(r'^[A-Z][A-Z\s,\-\(\)\'\"&/]+$', line) and
            len(line) > 3 and
            not line.startswith('Yield') and
            not line.startswith('Ingredients') and
            not line.startswith('Instructions') and
            not line.startswith('Lesson') and
            not re.match(r'^\d+---$', line)):

            # Save previous recipe if exists
            if current_recipe and current_recipe.get('name'):
                recipes.append(current_recipe)

            current_recipe = {
                'name': line.strip(),
                'yield': '',
                'ingredients': [],
                'instructions': []
            }
            current_section = 'header'
            i += 1
            continue

        # Check for Yield line
        if line.startswith('Yield:') or line.startswith('Yicld:'):
            if current_recipe:
                current_recipe['yield'] = line.replace('Yield:', '').replace('Yicld:', '').strip()
            i += 1
            continue

        # Check for Ingredients section
        if 'Ingredients' in line:
            current_section = 'ingredients'
            i += 1
            continue

        # Check for Instructions section
        if 'Instructions:' in line or line == 'Instructions':
            current_section = 'instructions'
            i += 1
            continue

        # Parse based on current section
        if current_recipe:
            if current_section == 'ingredients' or (line.startswith('- ') and current_section != 'instructions'):
                # Ingredient line
                ingredient = line.lstrip('- ').strip()
                if ingredient and not re.match(r'^\d+---$', ingredient) and not ingredient.startswith('Lesson'):
                    current_recipe['ingredients'].append(ingredient)
            elif current_section == 'instructions' or re.match(r'^\d+\.', line):
                # Instruction line
                instruction = re.sub(r'^\d+\.\s*', '', line).strip()
                if instruction and not re.match(r'^\d+---$', instruction):
                    current_recipe['instructions'].append(instruction)

        i += 1

    # Don't forget last recipe
    if current_recipe and current_recipe.get('name'):
        recipes.append(current_recipe)

    return recipes

def parse_all_extractions() -> Dict[str, Dict]:
    """Parse all extraction files and return dict keyed by slugified name."""
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
                    slug = slugify(recipe['name'])
                    recipe['category'] = category
                    recipe['source_file'] = filename
                    all_recipes[slug] = recipe

                    # Also store with variations
                    # Remove parenthetical notes
                    simple_name = re.sub(r'\([^)]+\)', '', recipe['name']).strip()
                    simple_slug = slugify(simple_name)
                    if simple_slug != slug:
                        all_recipes[simple_slug] = recipe

    return all_recipes

def find_existing_recipe_files() -> List[Tuple[str, str, str]]:
    """Find all existing recipe TypeScript files. Returns list of (filepath, slug, category)."""
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

    # Look for name: 'Recipe Name' or name: "Recipe Name"
    match = re.search(r"name:\s*['\"]([^'\"]+)['\"]", content)
    if match:
        return match.group(1)
    return None

def format_instructions_for_ts(instructions: List[str]) -> str:
    """Format instructions list for TypeScript file."""
    if not instructions:
        return "[]"

    formatted = []
    for inst in instructions:
        # Escape single quotes and clean up the instruction
        clean_inst = inst.replace("'", "\\'").replace('\n', ' ').strip()
        # Remove multiple spaces
        clean_inst = re.sub(r'\s+', ' ', clean_inst)
        if clean_inst:
            formatted.append(f"    '{clean_inst}'")

    if not formatted:
        return "[]"

    return "[\n" + ",\n".join(formatted) + "\n  ]"

def update_recipe_file(filepath: str, instructions: List[str]) -> bool:
    """Update a recipe TypeScript file with new instructions."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if instructions array is empty
    if 'instructions: [' not in content:
        return False

    # Pattern to match instructions array (empty or with content)
    # This handles both empty arrays and arrays with content
    pattern = r'instructions:\s*\[\s*\]'

    if not re.search(pattern, content):
        # Instructions already has content, check if it's minimal
        pattern2 = r'instructions:\s*\[[^\]]*\]'
        match = re.search(pattern2, content)
        if match:
            existing = match.group(0)
            # Count non-empty instruction items
            items = re.findall(r"'[^']+?'", existing)
            if len(items) >= 3:  # Already has substantial instructions
                return False

    # Format new instructions
    new_instructions = format_instructions_for_ts(instructions)

    # Replace empty instructions array
    if re.search(r'instructions:\s*\[\s*\]', content):
        new_content = re.sub(r'instructions:\s*\[\s*\]', f'instructions: {new_instructions}', content)
    else:
        # Replace minimal instructions
        new_content = re.sub(r'instructions:\s*\[[^\]]*\]', f'instructions: {new_instructions}', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def match_recipe_name(ts_name: str, extraction_db: Dict[str, Dict]) -> Optional[Dict]:
    """Try to match a TypeScript recipe name to an extraction."""
    # Direct slug match
    slug = slugify(ts_name)
    if slug in extraction_db:
        return extraction_db[slug]

    # Try without common suffixes/prefixes
    simplified = ts_name.lower()
    for prefix in ['vegan ', 'gluten-free ', 'raw ', 'organic ']:
        simplified = simplified.replace(prefix, '')

    simple_slug = slugify(simplified)
    if simple_slug in extraction_db:
        return extraction_db[simple_slug]

    # Try partial matching - find best match
    best_match = None
    best_score = 0

    for key, recipe in extraction_db.items():
        # Calculate similarity
        ts_words = set(slug.replace('-', ' ').split())
        ext_words = set(key.replace('-', ' ').split())

        if not ts_words or not ext_words:
            continue

        # Jaccard similarity
        intersection = len(ts_words & ext_words)
        union = len(ts_words | ext_words)
        score = intersection / union if union > 0 else 0

        if score > best_score and score > 0.5:  # Threshold
            best_score = score
            best_match = recipe

    return best_match

def main():
    print("Parsing extraction files...")
    extraction_db = parse_all_extractions()
    print(f"Found {len(extraction_db)} recipes in extraction")

    print("\nFinding existing recipe files...")
    recipe_files = find_existing_recipe_files()
    print(f"Found {len(recipe_files)} recipe files")

    updated = 0
    not_matched = []
    already_has = []

    for filepath, slug, category in recipe_files:
        # Get recipe name from file
        ts_name = extract_recipe_name_from_ts(filepath)
        if not ts_name:
            continue

        # Try to match with extraction
        extraction = match_recipe_name(ts_name, extraction_db)

        if extraction and extraction.get('instructions'):
            result = update_recipe_file(filepath, extraction['instructions'])
            if result:
                print(f"✓ Updated: {ts_name}")
                updated += 1
            else:
                already_has.append(ts_name)
        else:
            not_matched.append((ts_name, slug))

    print(f"\n=== Summary ===")
    print(f"Updated: {updated}")
    print(f"Already had instructions: {len(already_has)}")
    print(f"No match found: {len(not_matched)}")

    if not_matched:
        print("\nRecipes without matches:")
        for name, slug in not_matched[:20]:
            print(f"  - {name} ({slug})")
        if len(not_matched) > 20:
            print(f"  ... and {len(not_matched) - 20} more")

    # Save extraction database for reference
    output_path = os.path.join(PROJECT_DIR, "scripts/extraction_database.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(extraction_db, f, indent=2)
    print(f"\nSaved extraction database to {output_path}")

if __name__ == "__main__":
    main()
