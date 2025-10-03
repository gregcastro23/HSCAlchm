#!/usr/bin/env python3
"""
Script to extract recipe names from TypeScript files and generate a comprehensive duplicate checker
"""
import os
import re
from pathlib import Path

def extract_recipe_names_from_ts(file_path):
    """Extract recipe names from TypeScript recipe files"""
    recipes = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find recipe objects starting with { and containing name property first
        # Use regex to find recipe objects, looking for the pattern where name is the first property
        recipe_pattern = r'\{\s*name:\s*[\'"]([^\'"]+)[\'"]'
        matches = re.findall(recipe_pattern, content)
        
        for match in matches:
            recipes.append(match)
            
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return recipes

def scan_all_recipe_files():
    """Scan all recipe category files in the TypeScript project"""
    recipe_dir = Path("src/data/recipes")
    all_recipes = {}
    
    # Scan each category directory
    for category_dir in recipe_dir.iterdir():
        if category_dir.is_dir() and category_dir.name != '__pycache__':
            category_name = category_dir.name
            index_file = category_dir / "index.ts"
            
            if index_file.exists():
                recipes = extract_recipe_names_from_ts(index_file)
                all_recipes[category_name] = recipes
                print(f"Found {len(recipes)} recipes in {category_name}:")
                for recipe in recipes:
                    print(f"  - {recipe}")
                print()
    
    return all_recipes

def generate_python_dict(all_recipes):
    """Generate Python dictionary code for use in the extraction script"""
    print("# Updated existing_recipes dictionary for enhanced_recipe_extractor.py")
    print("existing_recipes = {")
    
    for category, recipes in all_recipes.items():
        print(f"    '{category}': [")
        for recipe in recipes:
            # Escape single quotes in recipe names
            escaped_recipe = recipe.replace("'", "\\'")
            print(f"        '{escaped_recipe}',")
        print(f"    ],")
    
    print("}")

def main():
    print("=== SCANNING EXISTING TYPESCRIPT RECIPES ===")
    all_recipes = scan_all_recipe_files()
    
    total_recipes = sum(len(recipes) for recipes in all_recipes.values())
    print(f"Total recipes found: {total_recipes}")
    print(f"Categories: {list(all_recipes.keys())}")
    
    print("\n" + "="*60)
    generate_python_dict(all_recipes)

if __name__ == "__main__":
    main()