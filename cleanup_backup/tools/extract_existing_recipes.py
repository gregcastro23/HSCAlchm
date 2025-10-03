#!/usr/bin/env python3
"""
Extract actual recipe names from TypeScript files for cross-referencing
"""
import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

def extract_recipe_names_from_ts(file_path: str) -> List[str]:
    """Extract only the actual recipe names from TypeScript recipe files"""
    recipe_names = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the main recipe array export
        array_match = re.search(r'export\s+const\s+\w+Recipes:\s*Recipe\[\]\s*=\s*\[(.*?)\];', content, re.DOTALL)
        if array_match:
            array_content = array_match.group(1)
            
            # Look for recipe objects by finding the pattern that starts with { followed by
            # name: 'recipe name' and then description: - this is unique to recipe objects
            pattern = r'\{\s*name:\s*[\'"]([^\'"]+)[\'"],\s*description:'
            recipe_matches = re.findall(pattern, array_content, re.DOTALL)
            
            for recipe_name in recipe_matches:
                recipe_names.append(recipe_name)
    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return recipe_names

def scan_all_recipe_categories() -> Dict[str, List[str]]:
    """Scan all recipe categories and extract recipe names"""
    recipe_dir = Path("src/data/recipes")
    all_recipes = {}
    
    category_dirs = [d for d in recipe_dir.iterdir() if d.is_dir()]
    
    for category_dir in category_dirs:
        category_name = category_dir.name
        index_file = category_dir / "index.ts"
        
        if index_file.exists():
            recipes = extract_recipe_names_from_ts(str(index_file))
            all_recipes[category_name] = recipes
            
    return all_recipes

def create_recipe_database() -> Dict[str, Dict[str, str]]:
    """Create a searchable database of existing recipes"""
    categories = scan_all_recipe_categories()
    recipe_db = {}
    
    for category, recipes in categories.items():
        for recipe in recipes:
            # Create a searchable key (lowercase, no punctuation)
            search_key = re.sub(r'[^a-z0-9\s]', '', recipe.lower()).strip()
            search_key = re.sub(r'\s+', ' ', search_key)
            
            recipe_db[search_key] = {
                'name': recipe,
                'category': category,
                'original_name': recipe
            }
    
    return recipe_db

def save_recipe_database(recipe_db: Dict[str, Dict[str, str]], filename: str = "existing_recipes_db.json"):
    """Save the recipe database to a JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(recipe_db, f, indent=2, ensure_ascii=False)

def main():
    print("=== EXTRACTING EXISTING RECIPES FROM TYPESCRIPT ===")
    
    # Extract all recipe names by category
    categories = scan_all_recipe_categories()
    
    total_recipes = 0
    print("\nRecipe counts by category:")
    for category, recipes in categories.items():
        print(f"  {category}: {len(recipes)} recipes")
        total_recipes += len(recipes)
    
    print(f"\nTotal existing recipes: {total_recipes}")
    
    # Create searchable database
    recipe_db = create_recipe_database()
    
    # Save database
    save_recipe_database(recipe_db)
    
    print(f"\nSearchable recipe database saved to: existing_recipes_db.json")
    print(f"Database contains {len(recipe_db)} searchable entries")
    
    # Print some examples
    print("\nExample recipe names:")
    for category, recipes in categories.items():
        if recipes:
            print(f"  {category}: {recipes[0]}")
    
    # Show some search keys
    print("\nExample search keys:")
    for i, (key, data) in enumerate(list(recipe_db.items())[:5]):
        print(f"  '{key}' → {data['name']} ({data['category']})")

if __name__ == "__main__":
    main()