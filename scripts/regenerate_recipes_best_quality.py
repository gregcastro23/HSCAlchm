#!/usr/bin/env python3
"""
Comprehensive recipe regeneration script.
Merges best quality data from:
1. PDF extraction (better instruction quality with proper spacing)
2. Merged database (recipe metadata, categories, ingredients)
Generates clean TypeScript files.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from difflib import SequenceMatcher

# Paths
PROJECT_DIR = "/Users/GregCastro/Desktop/untitled folder 3/HSCAlchm"
PDF_EXTRACTION_DB = os.path.join(PROJECT_DIR, "scripts/extraction_database.json")
MERGED_DB = os.path.join(PROJECT_DIR, "scripts/fixed_recipes_database_with_instructions.json")
RECIPES_DIR = os.path.join(PROJECT_DIR, "src/data/recipes")

def normalize_name(name: str) -> str:
    """Normalize recipe name for matching."""
    return re.sub(r'[^a-z0-9]', '', name.lower())

def slugify(name: str) -> str:
    """Convert name to URL-friendly slug."""
    slug = name.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug.strip())
    slug = re.sub(r'-+', '-', slug)
    return slug

def to_camel_case(slug: str) -> str:
    """Convert slug to camelCase for variable names."""
    parts = slug.split('-')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def fix_spacing(text: str) -> str:
    """Fix common OCR spacing issues in text."""
    if not text:
        return text

    # If text has no spaces but should, try to fix it
    if ' ' not in text and len(text) > 20:
        # Add space before capital letters (camelCase artifacts)
        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
        # Add space before common words
        common_words = ['and', 'the', 'with', 'for', 'into', 'until', 'from', 'over',
                       'heat', 'add', 'mix', 'stir', 'cook', 'bake', 'pour', 'place',
                       'combine', 'transfer', 'remove', 'let', 'set', 'cover']
        for word in common_words:
            text = re.sub(rf'([a-z])({word})', rf'\1 \2', text, flags=re.IGNORECASE)
        # Add space after punctuation
        text = re.sub(r'([.,;:])([A-Za-z])', r'\1 \2', text)

    # Clean up multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def escape_string(s: str) -> str:
    """Escape string for TypeScript single quotes."""
    return s.replace("\\", "\\\\").replace("'", "\\'")

def format_ingredients(ingredients: List[Dict]) -> str:
    """Format ingredients list for TypeScript."""
    if not ingredients:
        return "[]"

    lines = []
    for ing in ingredients:
        name = escape_string(ing.get('name', ''))
        amount = ing.get('amount', 1.0)
        unit = ing.get('unit', '')
        notes = ing.get('notes', '')

        parts = [f"name: '{name}'"]
        parts.append(f"amount: {amount}")
        if unit:
            parts.append(f"unit: '{escape_string(unit)}'")
        if notes:
            parts.append(f"notes: '{escape_string(notes)}'")

        lines.append("    { " + ", ".join(parts) + " }")

    return "[\n" + ",\n".join(lines) + ",\n  ]"

def format_instructions(instructions: List[str]) -> str:
    """Format instructions list for TypeScript."""
    if not instructions:
        return "[]"

    lines = []
    for inst in instructions:
        # Fix spacing and escape
        fixed = fix_spacing(inst)
        escaped = escape_string(fixed)
        if escaped and len(escaped) > 3:
            lines.append(f"    '{escaped}'")

    if not lines:
        return "[]"

    return "[\n" + ",\n".join(lines) + ",\n  ]"

def generate_recipe_ts(recipe: Dict, variable_name: str) -> str:
    """Generate TypeScript content for a recipe."""
    name = escape_string(recipe.get('name', 'Unknown Recipe'))
    description = escape_string(recipe.get('description', 'A delicious recipe.'))
    ingredients = format_ingredients(recipe.get('ingredients', []))
    instructions = format_instructions(recipe.get('instructions', []))

    nutrition = recipe.get('nutrition', {})
    time_to_make = recipe.get('timeToMake', '30 minutes')
    season = recipe.get('season', ['all'])
    cuisine = recipe.get('cuisine', 'HSCA')
    meal_type = recipe.get('mealType', ['Health Supportive'])
    elemental = recipe.get('elementalBalance', {'Fire': 0.25, 'Earth': 0.25, 'Water': 0.25, 'Air': 0.25})

    # Format arrays with single quotes
    vitamins = nutrition.get('vitamins', ['C', 'K'])
    minerals = nutrition.get('minerals', ['Potassium', 'Iron'])
    vitamins_str = "[" + ", ".join(f"'{v}'" for v in vitamins) + "]"
    minerals_str = "[" + ", ".join(f"'{m}'" for m in minerals) + "]"
    season_str = "[" + ", ".join(f"'{s}'" for s in season) + "]"
    meal_type_str = "[" + ", ".join(f"'{m}'" for m in meal_type) + "]"

    return f"""import {{ Recipe }} from '../../../../types/recipe';

export const {variable_name}: Recipe = {{
  name: '{name}',
  description: '{description}',
  ingredients: {ingredients},
  instructions: {instructions},
  nutrition: {{
    calories: {nutrition.get('calories', 200)},
    protein: {nutrition.get('protein', 8)},
    carbs: {nutrition.get('carbs', 25)},
    fat: {nutrition.get('fat', 12)},
    vitamins: {vitamins_str},
    minerals: {minerals_str},
  }},
  timeToMake: '{time_to_make}',
  season: {season_str},
  cuisine: '{cuisine}',
  mealType: {meal_type_str},
  elementalBalance: {{
    Fire: {elemental.get('Fire', 0.25)},
    Earth: {elemental.get('Earth', 0.25)},
    Water: {elemental.get('Water', 0.25)},
    Air: {elemental.get('Air', 0.25)},
  }},
}};
"""

def generate_index_ts(category: str, recipes: List[Dict]) -> str:
    """Generate index.ts for a category."""
    imports = {}
    exports = {}

    for recipe in recipes:
        slug = recipe['slug']
        var_name = recipe['variable_name']
        # Use dict to avoid duplicates
        imports[var_name] = f"import {{ {var_name} }} from './recipes/{slug}';"
        exports[var_name] = f"  {var_name},"

    imports_str = "\n".join(sorted(imports.values()))
    exports_str = "\n".join(sorted(exports.values()))

    return f"""import {{ Recipe }} from '../../../types/recipe';
{imports_str}

export const {category}Recipes: Recipe[] = [
{exports_str}
];
"""

def load_pdf_extraction() -> Dict[str, Dict]:
    """Load PDF extraction database."""
    with open(PDF_EXTRACTION_DB, 'r') as f:
        return json.load(f)

def load_merged_database() -> List[Dict]:
    """Load merged database recipes."""
    with open(MERGED_DB, 'r') as f:
        data = json.load(f)
    return data.get('extracted_recipes', [])

def find_best_instructions(recipe_name: str, pdf_db: Dict) -> Optional[List[str]]:
    """Find best quality instructions from PDF extraction."""
    norm_name = normalize_name(recipe_name)

    # Direct match
    if norm_name in pdf_db:
        return pdf_db[norm_name].get('instructions', [])

    # Fuzzy match
    best_match = None
    best_score = 0

    for key, recipe in pdf_db.items():
        score = SequenceMatcher(None, norm_name, key).ratio()
        if score > best_score and score > 0.7:
            best_score = score
            best_match = recipe

    if best_match:
        return best_match.get('instructions', [])

    return None

def has_good_spacing(text: str) -> bool:
    """Check if text has reasonable spacing."""
    if not text:
        return False
    words = text.split()
    return len(words) >= 3 and len(text) / max(len(words), 1) < 15

def main():
    print("Loading databases...")
    pdf_db = load_pdf_extraction()
    merged_recipes = load_merged_database()

    print(f"PDF extraction: {len(pdf_db)} recipes")
    print(f"Merged database: {len(merged_recipes)} recipes")

    # Organize by category
    categories = {}
    stats = {
        'total': 0,
        'pdf_instructions': 0,
        'merged_instructions': 0,
        'no_instructions': 0,
        'good_spacing': 0,
        'fixed_spacing': 0,
    }

    seen_slugs = set()  # Track seen slugs to avoid duplicates

    for item in merged_recipes:
        recipe = item.get('recipe', {})
        category = item.get('category', 'uncategorized')

        if category not in categories:
            categories[category] = []

        name = recipe.get('name', 'Unknown')
        slug = slugify(name)

        # Skip duplicates
        category_slug = f"{category}/{slug}"
        if category_slug in seen_slugs:
            continue
        seen_slugs.add(category_slug)

        var_name = to_camel_case(slug)

        # Get best instructions
        pdf_instructions = find_best_instructions(name, pdf_db)
        merged_instructions = recipe.get('instructions', [])

        # Choose best source
        if pdf_instructions and any(has_good_spacing(i) for i in pdf_instructions):
            recipe['instructions'] = pdf_instructions
            stats['pdf_instructions'] += 1
            stats['good_spacing'] += 1
        elif merged_instructions:
            # Check if merged has good spacing
            if any(has_good_spacing(i) for i in merged_instructions):
                stats['good_spacing'] += 1
            else:
                stats['fixed_spacing'] += 1
            recipe['instructions'] = merged_instructions
            stats['merged_instructions'] += 1
        else:
            recipe['instructions'] = []
            stats['no_instructions'] += 1

        categories[category].append({
            'recipe': recipe,
            'slug': slug,
            'variable_name': var_name,
        })
        stats['total'] += 1

    print(f"\nInstruction sources:")
    print(f"  From PDF extraction: {stats['pdf_instructions']}")
    print(f"  From merged database: {stats['merged_instructions']}")
    print(f"  No instructions: {stats['no_instructions']}")
    print(f"  Good spacing: {stats['good_spacing']}")
    print(f"  Needs spacing fix: {stats['fixed_spacing']}")

    # Generate files
    print("\nGenerating TypeScript files...")

    for category, recipes in categories.items():
        category_dir = os.path.join(RECIPES_DIR, category)
        recipes_dir = os.path.join(category_dir, 'recipes')

        # Create directories
        os.makedirs(recipes_dir, exist_ok=True)

        # Generate recipe files
        for item in recipes:
            recipe = item['recipe']
            slug = item['slug']
            var_name = item['variable_name']

            filepath = os.path.join(recipes_dir, f"{slug}.ts")
            content = generate_recipe_ts(recipe, var_name)

            with open(filepath, 'w') as f:
                f.write(content)

        # Generate index file
        index_path = os.path.join(category_dir, 'index.ts')
        index_content = generate_index_ts(category, recipes)

        with open(index_path, 'w') as f:
            f.write(index_content)

        print(f"  {category}: {len(recipes)} recipes")

    # Update main recipes index
    main_index = os.path.join(RECIPES_DIR, 'index.ts')
    category_names = sorted(categories.keys())

    imports = [f"import {{ {cat}Recipes }} from './{cat}';" for cat in category_names]
    spreads = [f"  ...{cat}Recipes," for cat in category_names]

    main_content = f"""import {{ Recipe }} from '../../types/recipe';
{chr(10).join(imports)}

export const allRecipes: Recipe[] = [
{chr(10).join(spreads)}
];
"""

    with open(main_index, 'w') as f:
        f.write(main_content)

    print(f"\nGenerated {stats['total']} recipes across {len(categories)} categories")
    print("Done!")

if __name__ == "__main__":
    main()
