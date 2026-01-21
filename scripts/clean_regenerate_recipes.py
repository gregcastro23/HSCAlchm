#!/usr/bin/env python3
"""
Clean regeneration: Remove all recipe TypeScript files and regenerate cleanly
from the extracted database. This ensures no duplicates or placeholders.
"""

import json
from pathlib import Path
from typing import Dict, List

from update_recipes_from_fixed import (
    normalize_recipe_name, to_export_name, escape_single_quote,
    convert_recipe_to_typescript, map_category_to_folder
)


def remove_all_recipe_files():
    """Remove all recipe TypeScript files."""
    recipes_dir = Path('src/data/recipes')
    removed_count = 0
    
    print("🗑️  Removing all existing recipe files...")
    for category_dir in recipes_dir.iterdir():
        if not category_dir.is_dir():
            continue
        recipes_subdir = category_dir / 'recipes'
        if not recipes_subdir.exists():
            continue
        
        for recipe_file in recipes_subdir.glob('*.ts'):
            try:
                recipe_file.unlink()
                removed_count += 1
            except Exception as e:
                print(f"  Error removing {recipe_file}: {e}")
    
    print(f"  ✓ Removed {removed_count} files\n")
    return removed_count


def load_extracted_database():
    """Load the best available extracted database."""
    script_dir = Path(__file__).parent
    
    improved_file = script_dir / 'fixed_recipes_database_improved.json'
    aggressive_file = script_dir / 'fixed_recipes_database_aggressive.json'
    fixed_file = script_dir / 'fixed_recipes_database.json'
    
    if improved_file.exists():
        source_file = improved_file
        print(f"📖 Loading IMPROVED database from: {source_file.name}")
    elif aggressive_file.exists():
        source_file = aggressive_file
        print(f"📖 Loading AGGRESSIVELY FIXED database from: {source_file.name}")
    elif fixed_file.exists():
        source_file = fixed_file
        print(f"📖 Loading FIXED database from: {source_file.name}")
    else:
        print("❌ No fixed database found!")
        return None
    
    with open(source_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return data.get('extracted_recipes', [])


def regenerate_recipes():
    """Regenerate all recipe TypeScript files from extracted database."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Remove all existing files
    remove_all_recipe_files()
    
    # Load extracted database
    print("📖 Loading extracted recipes...")
    recipes = load_extracted_database()
    if not recipes:
        return
    
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
    
    print("\n🎉 Clean regeneration complete!")
    print(f"   {total_converted} recipes from extracted database")
    print("   No duplicates or placeholders")


if __name__ == '__main__':
    regenerate_recipes()
