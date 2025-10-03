#!/usr/bin/env python3
"""
Import missing recipes from categorized extraction into TypeScript database.
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any

def load_categorized_recipes() -> List[Dict]:
    """Load recipes from the categorized extraction file."""
    with open('enhanced_extracted_recipes/balanced_categorized_hsca_recipes.json', 'r') as f:
        data = json.load(f)
    return data['extracted_recipes']

def get_existing_recipe_names() -> set:
    """Get all existing recipe names from TypeScript database."""
    existing_names = set()
    recipes_dir = Path('src/data/recipes')

    for category_dir in recipes_dir.iterdir():
        if not category_dir.is_dir() or category_dir.name.endswith('PENDING'):
            continue

        recipes_subdir = category_dir / 'recipes'
        if not recipes_subdir.exists():
            continue

        for recipe_file in recipes_subdir.glob('*.ts'):
            try:
                with open(recipe_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    match = re.search(r'"name":\s*"([^"]+)"', content)
                    if match:
                        existing_names.add(match.group(1).lower().strip())
            except Exception as e:
                print(f"Error reading {recipe_file}: {e}")

    return existing_names

def normalize_recipe_name(name: str) -> str:
    """Normalize recipe name for filename."""
    # Remove special characters and convert to lowercase with hyphens
    normalized = re.sub(r'[^\w\s-]', '', name.lower())
    normalized = re.sub(r'\s+', '-', normalized)
    normalized = re.sub(r'-+', '-', normalized)
    return normalized.strip('-')

def convert_recipe_to_typescript(recipe_data: Dict) -> str:
    """Convert JSON recipe data to TypeScript format."""
    recipe = recipe_data['recipe']

    # Build ingredients array
    ingredients = []
    for ing in recipe.get('ingredients', []):
        ingredients.append(f"""    {{
      "name": "{ing['name']}",
      "amount": {ing['amount']},
      "unit": "{ing.get('unit', '').replace('unit', '')}",
      "notes": "{ing.get('notes', '')}",
      "swaps": {json.dumps(ing.get('swaps', []))}
    }}""")

    # Build instructions array
    instructions = []
    for inst in recipe.get('instructions', []):
        instructions.append(f'    "{inst}"')

    # Build nutrition object
    nutrition = recipe.get('nutrition', {})
    if nutrition:
        vitamins = json.dumps(nutrition.get('vitamins', []))
        minerals = json.dumps(nutrition.get('minerals', []))
        nutrition_str = f"""  "nutrition": {{
    "calories": {nutrition.get('calories', 0)},
    "protein": {nutrition.get('protein', 0)},
    "carbs": {nutrition.get('carbs', 0)},
    "fat": {nutrition.get('fat', 0)},
    "vitamins": {vitamins},
    "minerals": {minerals}
  }},"""
    else:
        nutrition_str = ""

    # Build elemental balance
    elemental = recipe.get('elementalBalance', {})
    if elemental:
        elemental_str = f"""  "elementalBalance": {{
    "Fire": {elemental.get('Fire', 0.25)},
    "Earth": {elemental.get('Earth', 0.25)},
    "Water": {elemental.get('Water', 0.25)},
    "Air": {elemental.get('Air', 0.25)}
  }}"""
    else:
        elemental_str = ""

    # Build the complete TypeScript export
    ts_content = f"""import {{ Recipe }} from '../../../types/recipe';

export const {normalize_recipe_name(recipe['name'])}: Recipe = {{
  "name": "{recipe['name']}",
  "description": "{recipe.get('description', '')}",
  "ingredients": [
{chr(10).join(ingredients)}
  ],
  "instructions": [
{chr(10).join(instructions)}
  ],{nutrition_str}
  "timeToMake": "{recipe.get('timeToMake', '')}",
  "season": {json.dumps(recipe.get('season', ['all']))},
  "cuisine": "{recipe.get('cuisine', 'HSCA')}",
  "mealType": {json.dumps(recipe.get('mealType', ['Health Supportive']))},{elemental_str}
}};
"""

    return ts_content

def update_category_index(category: str, recipe_name: str):
    """Update the category index file to include the new recipe."""
    index_file = Path(f'src/data/recipes/{category}/index.ts')

    if not index_file.exists():
        print(f"Warning: Index file {index_file} does not exist")
        return

    try:
        with open(index_file, 'r') as f:
            content = f.read()

        # Check if recipe is already imported
        normalized_name = normalize_recipe_name(recipe_name)
        if f"import {{ {normalized_name} }}" in content:
            return  # Already imported

        # Add import statement
        import_statement = f"import {{ {normalized_name} }} from './recipes/{normalized_name}';"

        # Find the imports section and add the import
        lines = content.split('\n')
        import_lines = []
        other_lines = []

        for line in lines:
            if line.startswith('import'):
                import_lines.append(line)
            else:
                other_lines.append(line)

        # Insert the new import in alphabetical order
        import_lines.append(import_statement)
        import_lines.sort()

        # Find the recipes array and add the recipe
        new_content = '\n'.join(import_lines + [''] + other_lines)

        # Add recipe to the recipes array
        recipes_match = re.search(r'export const \w+Recipes = \[([^\]]*)\];', new_content, re.DOTALL)
        if recipes_match:
            recipes_content = recipes_match.group(1).strip()
            if recipes_content and not recipes_content.endswith(','):
                recipes_content += ','
            if recipes_content:
                recipes_content += '\n'
            recipes_content += f'  {normalized_name},'

            new_content = new_content.replace(recipes_match.group(1), recipes_content)

        with open(index_file, 'w') as f:
            f.write(new_content)

    except Exception as e:
        print(f"Error updating index file {index_file}: {e}")

def main():
    print("🔄 IMPORTING MISSING RECIPES INTO TYPESCRIPT DATABASE")
    print("=" * 60)

    # Load data
    print("📖 Loading categorized recipes...")
    recipes = load_categorized_recipes()
    print(f"Found {len(recipes)} recipes in extraction")

    print("📊 Checking existing recipes...")
    existing_names = get_existing_recipe_names()
    print(f"Found {len(existing_names)} existing recipes in database")

    # Find missing recipes
    missing_recipes = []
    for recipe_data in recipes:
        name = recipe_data.get('recipe', {}).get('name', '').lower().strip()
        if name and name not in existing_names:
            missing_recipes.append(recipe_data)

    print(f"Found {len(missing_recipes)} recipes to import")

    if not missing_recipes:
        print("✅ No missing recipes to import!")
        return

    # Group by category
    by_category = {}
    for recipe in missing_recipes:
        category = recipe.get('category', 'unknown')
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(recipe)

    print("📁 Recipes to import by category:")
    for category, recipes_list in by_category.items():
        print(f"  {category}: {len(recipes_list)} recipes")

    # Import recipes
    imported_count = 0
    for category, recipes_list in by_category.items():
        print(f"\n🔄 Importing {len(recipes_list)} recipes for category: {category}")

        # Ensure category directory exists
        category_dir = Path(f'src/data/recipes/{category}')
        recipes_dir = category_dir / 'recipes'
        recipes_dir.mkdir(parents=True, exist_ok=True)

        for recipe_data in recipes_list:
            recipe_name = recipe_data['recipe']['name']
            normalized_name = normalize_recipe_name(recipe_name)

            # Create the TypeScript file
            ts_content = convert_recipe_to_typescript(recipe_data)
            file_path = recipes_dir / f'{normalized_name}.ts'

            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(ts_content)
                print(f"  ✅ Created: {file_path}")

                # Update category index
                update_category_index(category, recipe_name)
                imported_count += 1

            except Exception as e:
                print(f"  ❌ Error creating {file_path}: {e}")

    print(f"\n🎉 IMPORT COMPLETE!")
    print(f"Imported {imported_count} recipes into TypeScript database")
    print(f"Total recipes in database should now be: {len(existing_names) + imported_count}")

if __name__ == '__main__':
    main()
