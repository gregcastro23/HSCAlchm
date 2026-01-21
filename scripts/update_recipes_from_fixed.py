#!/usr/bin/env python3
"""
Update all TypeScript recipe files from the fixed recipes database.
This script converts the fixed_recipes_database.json to TypeScript files,
ensuring all spacing fixes are applied to the frontend.
"""

import json
import re
from pathlib import Path
from typing import Dict, Any

def normalize_recipe_name(name: str) -> str:
    """Normalize recipe name for filename."""
    # Remove special characters and convert to lowercase with hyphens
    normalized = re.sub(r'[^\w\s-]', '', name.lower())
    normalized = re.sub(r'\s+', '-', normalized)
    normalized = re.sub(r'-+', '-', normalized)
    return normalized.strip('-')

def to_export_name(name: str) -> str:
    """Convert recipe name to export name (camelCase, no hyphens)."""
    # Remove special characters
    cleaned = re.sub(r'[^\w\s-]', '', name)
    # Split by hyphens or spaces
    words = re.split(r'[-_\s]+', cleaned.lower())
    if not words:
        return name.lower().replace('-', '').replace(' ', '')
    # First word lowercase, rest capitalized
    export = words[0]
    for word in words[1:]:
        export += word.capitalize()
    return export

def escape_single_quote(s: str) -> str:
    """Escape single quotes for TypeScript string literals."""
    if not s:
        return "''"
    # Escape backslashes first
    s = s.replace('\\', '\\\\')
    # Escape single quotes
    s = s.replace("'", "\\'")
    # Escape newlines
    s = s.replace('\n', '\\n')
    return f"'{s}'"

def convert_recipe_to_typescript(recipe_data: Dict) -> str:
    """Convert JSON recipe data to TypeScript format."""
    recipe = recipe_data['recipe']
    
    # Get export name
    export_name = to_export_name(recipe['name'])

    # Build ingredients array
    ingredients = []
    for ing in recipe.get('ingredients', []):
        ing_parts = [f"    {{ name: {escape_single_quote(ing['name'])}"]
        ing_parts.append(f"      amount: {ing.get('amount', 0)}")
        
        unit = ing.get('unit', '').strip()
        if unit:
            ing_parts.append(f"      unit: {escape_single_quote(unit)}")
        
        notes = ing.get('notes', '').strip()
        if notes:
            ing_parts.append(f"      notes: {escape_single_quote(notes)}")
        
        swaps = ing.get('swaps', [])
        if swaps:
            # Convert to TypeScript array format
            swap_str = "[" + ", ".join(escape_single_quote(swap) for swap in swaps) + "]"
            ing_parts.append(f"      swaps: {swap_str}")
        
        # Join parts and close object
        ingredients.append(',\n'.join(ing_parts) + ' },')

    # Build instructions array
    instructions = []
    for inst in recipe.get('instructions', []):
        if inst and inst.strip():
            instructions.append(f"    {escape_single_quote(inst.strip())},")

    # Build nutrition object
    nutrition = recipe.get('nutrition', {})
    nutrition_parts = []
    if nutrition:
        nutrition_parts.append(f"    calories: {nutrition.get('calories', 0)}")
        nutrition_parts.append(f"    protein: {nutrition.get('protein', 0)}")
        nutrition_parts.append(f"    carbs: {nutrition.get('carbs', 0)}")
        nutrition_parts.append(f"    fat: {nutrition.get('fat', 0)}")
        
        vitamins = nutrition.get('vitamins', [])
        if vitamins:
            vit_str = "[" + ", ".join(escape_single_quote(v) for v in vitamins) + "]"
            nutrition_parts.append(f"    vitamins: {vit_str}")
        else:
            nutrition_parts.append("    vitamins: []")
        
        minerals = nutrition.get('minerals', [])
        if minerals:
            min_str = "[" + ", ".join(escape_single_quote(m) for m in minerals) + "]"
            nutrition_parts.append(f"    minerals: {min_str}")
        else:
            nutrition_parts.append("    minerals: []")
    
    nutrition_str = '  nutrition: {\n' + ',\n'.join(nutrition_parts) + '\n  },'

    # Build elemental balance
    elemental = recipe.get('elementalBalance', {})
    elemental_parts = []
    if elemental:
        elemental_parts.append(f"    Fire: {elemental.get('Fire', 0.25)}")
        elemental_parts.append(f"    Earth: {elemental.get('Earth', 0.25)}")
        elemental_parts.append(f"    Water: {elemental.get('Water', 0.25)}")
        elemental_parts.append(f"    Air: {elemental.get('Air', 0.25)}")
    
    elemental_str = '  elementalBalance: {\n' + ',\n'.join(elemental_parts) + '\n  }'

    # Build the complete TypeScript export
    season_arr = recipe.get('season', ['all'])
    season_str = "[" + ", ".join(escape_single_quote(s) for s in season_arr) + "]"
    
    meal_type_arr = recipe.get('mealType', ['Health Supportive'])
    meal_type_str = "[" + ", ".join(escape_single_quote(mt) for mt in meal_type_arr) + "]"

    ts_content = f"""import {{ Recipe }} from '../../../types/recipe';

export const {export_name}: Recipe = {{
  name: {escape_single_quote(recipe['name'])},
  description: {escape_single_quote(recipe.get('description', ''))},
  ingredients: [
{chr(10).join(ingredients)}
  ],
  instructions: [
{chr(10).join(instructions)}
  ],
  {nutrition_str}
  timeToMake: {escape_single_quote(recipe.get('timeToMake', ''))},
  season: {season_str},
  cuisine: {escape_single_quote(recipe.get('cuisine', 'HSCA'))},
  mealType: {meal_type_str},
  {elemental_str}
}};
"""

    return ts_content

def map_category_to_folder(category: str) -> str:
    """Map category name to folder name."""
    category_map = {
        'breakfast': 'breakfast',
        'lunch': 'lunch',
        'dinner': 'dinner',
        'appetizers': 'appetizers',
        'appetizer': 'appetizers',
        'sides': 'sides',
        'side': 'sides',
        'sauces': 'sauces',
        'sauce': 'sauces',
        'desserts': 'desserts',
        'dessert': 'desserts',
        'salads': 'salads',
        'salad': 'salads',
        'beverages': 'beverages',
        'beverage': 'beverages',
        'condiments': 'condiments',
        'condiment': 'condiments',
        'soups': 'soups',
        'soup': 'soups'
    }
    return category_map.get(category.lower(), 'dinner')

def main():
    """Main conversion process."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    print("🔄 UPDATING RECIPES FROM FIXED DATABASE")
    print("=" * 60)
    
    # Load most recent fixed database (prefer improved, then aggressive fix)
    improved_fix = script_dir / 'fixed_recipes_database_improved.json'
    aggressive_fix = script_dir / 'fixed_recipes_database_aggressive.json'
    fixed_file = script_dir / 'fixed_recipes_database.json'
    
    if improved_fix.exists():
        fixed_file = improved_fix
        print(f"📖 Loading IMPROVED database (with better descriptions) from: {fixed_file}")
    elif aggressive_fix.exists():
        fixed_file = aggressive_fix
        print(f"📖 Loading AGGRESSIVELY FIXED database from: {fixed_file}")
    elif fixed_file.exists():
        print(f"📖 Loading fixed database from: {fixed_file}")
    else:
        print(f"❌ Error: No fixed database found!")
        print("Please run fix_recipe_spacing_v2.py or fix_recipe_spacing_aggressive.py first.")
        return
    with open(fixed_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    recipes = data.get('extracted_recipes', [])
    print(f"Found {len(recipes)} recipes to convert\n")
    
    # Group recipes by category
    by_category = {}
    for recipe_data in recipes:
        category = recipe_data.get('category', 'dinner')
        folder_name = map_category_to_folder(category)
        if folder_name not in by_category:
            by_category[folder_name] = []
        by_category[folder_name].append(recipe_data)
    
    # Convert and write recipes
    recipes_dir_base = project_root / 'src' / 'data' / 'recipes'
    total_converted = 0
    errors = []
    
    for category, recipes_list in sorted(by_category.items()):
        print(f"📁 Processing {category}: {len(recipes_list)} recipes")
        
        # Ensure category directory exists
        category_dir = recipes_dir_base / category
        recipes_dir = category_dir / 'recipes'
        recipes_dir.mkdir(parents=True, exist_ok=True)
        
        for recipe_data in recipes_list:
            try:
                recipe_name = recipe_data['recipe']['name']
                normalized_name = normalize_recipe_name(recipe_name)
                
                # Convert to TypeScript
                ts_content = convert_recipe_to_typescript(recipe_data)
                
                # Write file
                file_path = recipes_dir / f'{normalized_name}.ts'
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(ts_content)
                
                total_converted += 1
                
            except Exception as e:
                recipe_name = recipe_data.get('recipe', {}).get('name', 'Unknown')
                errors.append(f"{recipe_name}: {str(e)}")
                print(f"  ❌ Error converting {recipe_name}: {e}")
    
    print(f"\n✅ Conversion complete!")
    print(f"Converted {total_converted} recipes")
    
    if errors:
        print(f"\n⚠️  {len(errors)} errors encountered:")
        for error in errors[:10]:
            print(f"  - {error}")
    
    # Update category indexes
    print("\n🔄 Updating category indexes...")
    import sys
    sys.path.insert(0, str(script_dir))
    from utils.update_category_indexes import update_category_index
    
    for category in sorted(by_category.keys()):
        category_path = recipes_dir_base / category
        if category_path.exists():
            update_category_index(category_path)
    
    print("\n🎉 All recipes updated with spacing fixes!")

if __name__ == '__main__':
    main()
