#!/usr/bin/env python3
"""
Transform HSCAlchm recipes to front-end format for Vercel deployment.

This script converts 328 recipes from the HSCAlchm database format to the
v0-recipe-collection-front-end expected format.
"""

import json
import re
from typing import Dict, List, Any
from pathlib import Path


def create_slug(name: str) -> str:
    """Create URL-friendly slug from recipe name."""
    slug = name.lower()
    # Remove special characters and replace spaces with hyphens
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')


def transform_ingredient(ingredient: Dict[str, Any]) -> Dict[str, Any]:
    """Transform ingredient from HSCAlchm format to front-end format."""
    quantity = f"{ingredient['amount']} {ingredient['unit']}".strip()

    transformed = {
        "quantity": quantity if quantity else str(ingredient['amount']),
        "item": ingredient['name']
    }

    # Add alternatives if swaps exist
    if ingredient.get('swaps') and len(ingredient['swaps']) > 0:
        transformed["alternatives"] = ", ".join(ingredient['swaps'])

    return transformed


def transform_elemental_balance(balance: Dict[str, float]) -> Dict[str, int]:
    """Convert elemental balance from decimals (0.0-1.0) to percentages (0-100)."""
    return {
        "fire": int(balance.get("Fire", 0.25) * 100),
        "earth": int(balance.get("Earth", 0.25) * 100),
        "water": int(balance.get("Water", 0.25) * 100),
        "air": int(balance.get("Air", 0.25) * 100)
    }


def map_category(category: str) -> str:
    """Map HSCAlchm category to front-end category format."""
    category_map = {
        'beverages': 'Beverages',
        'breakfast': 'Breakfast',
        'desserts': 'Dessert',
        'dinner': 'Dinner',
        'lunch': 'Lunch',
        'salads': 'Salad',
        'sauces': 'Sauce',
        'sides': 'Side',
        'soups': 'Soup',
        'appetizers': 'Appetizer',
        'condiments': 'Condiment'
    }
    return category_map.get(category.lower(), 'Dinner')


def transform_recipe(item: Dict[str, Any]) -> Dict[str, Any]:
    """Transform a single recipe from HSCAlchm format to front-end format."""
    recipe = item['recipe']
    category = item.get('category', 'dinner')

    # Generate ID and slug from recipe name
    recipe_id = create_slug(recipe['name'])

    # Transform ingredients
    ingredients = [
        transform_ingredient(ing)
        for ing in recipe.get('ingredients', [])
    ]

    # Get instructions (or empty array if missing)
    instructions = recipe.get('instructions', [])
    if not instructions:
        instructions = []

    # Transform nutrition data
    nutrition_data = recipe.get('nutrition', {})
    nutrition = {
        "calories": nutrition_data.get('calories', 0),
        "protein": nutrition_data.get('protein', 0),
        "carbohydrates": nutrition_data.get('carbs', 0),  # Map carbs -> carbohydrates
        "fat": nutrition_data.get('fat', 0)
    }

    # Build transformed recipe
    transformed = {
        "id": recipe_id,
        "slug": recipe_id,
        "title": recipe['name'],
        "description": recipe.get('description', ''),
        "category": map_category(category),
        "cuisine": recipe.get('cuisine', 'HSCA'),
        "prepTime": recipe.get('timeToMake', '30 minutes'),
        "ingredients": ingredients,
        "instructions": instructions,
        "elementalBalance": transform_elemental_balance(
            recipe.get('elementalBalance', {})
        ),
        "nutrition": nutrition
    }

    # Add vitamins if available
    if nutrition_data.get('vitamins'):
        transformed["vitamins"] = nutrition_data['vitamins']

    # Add minerals if available
    if nutrition_data.get('minerals'):
        transformed["minerals"] = nutrition_data['minerals']

    return transformed


def main():
    """Main transformation process."""
    # Paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Use most recent fixed database if available (prefer improved, then aggressive fix)
    improved_fix = script_dir / 'fixed_recipes_database_improved.json'
    aggressive_fix = script_dir / 'fixed_recipes_database_aggressive.json'
    fixed_file = script_dir / 'fixed_recipes_database.json'
    default_file = project_root / 'cleanup_backup/enhanced_extracted_recipes/hybrid_hsca_recipes_database.json'

    if improved_fix.exists():
        source_file = improved_fix
        print(f"✓ Using IMPROVED database with better descriptions and spacing fixes")
    elif aggressive_fix.exists():
        source_file = aggressive_fix
        print(f"✓ Using AGGRESSIVELY FIXED database with comprehensive spacing corrections")
    elif fixed_file.exists():
        source_file = fixed_file
        print(f"✓ Using FIXED database with spacing corrections")
    else:
        source_file = default_file
    
    output_file = project_root / 'scripts/transformed_recipes_clean.json'
    print(f"Reading recipes from: {source_file}")

    # Load source data
    with open(source_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    recipes = data['extracted_recipes']
    print(f"Found {len(recipes)} recipes to transform")

    # Transform all recipes
    transformed_recipes = []
    errors = []

    for idx, item in enumerate(recipes, 1):
        try:
            transformed = transform_recipe(item)
            transformed_recipes.append(transformed)

            if idx % 50 == 0:
                print(f"Transformed {idx}/{len(recipes)} recipes...")
        except Exception as e:
            recipe_name = item.get('recipe', {}).get('name', 'Unknown')
            errors.append(f"Recipe '{recipe_name}': {str(e)}")
            print(f"ERROR transforming recipe {idx}: {recipe_name}")

    print(f"\nTransformation complete!")
    print(f"Successfully transformed: {len(transformed_recipes)} recipes")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\nErrors encountered:")
        for error in errors[:10]:  # Show first 10 errors
            print(f"  - {error}")

    # Category distribution
    categories = {}
    for recipe in transformed_recipes:
        cat = recipe['category']
        categories[cat] = categories.get(cat, 0) + 1

    print("\nCategory distribution:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}")

    # Recipes without instructions
    without_instructions = sum(
        1 for r in transformed_recipes
        if not r['instructions'] or len(r['instructions']) == 0
    )
    print(f"\nRecipes without instructions: {without_instructions}")

    # Save transformed data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(transformed_recipes, f, indent=2, ensure_ascii=False)

    print(f"\nTransformed recipes saved to: {output_file}")
    print(f"File size: {output_file.stat().st_size / 1024:.1f} KB")


if __name__ == '__main__':
    main()
