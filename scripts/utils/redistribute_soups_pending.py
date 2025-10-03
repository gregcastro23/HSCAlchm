#!/usr/bin/env python3
"""
Script to redistribute misclassified recipes from soupsPENDING to correct categories.
"""

import os
import shutil
import re
from pathlib import Path

# Define categorization rules based on recipe names
CATEGORY_KEYWORDS = {
    'desserts': [
        'cake', 'tart', 'pie', 'cookie', 'brownie', 'cheesecake', 'icecream', 'pudding',
        'custard', 'meringue', 'pastry', 'cream', 'frosting', 'muffin', 'bread', 'bagel',
        'scone', 'biscotti', 'gelato', 'truffle', 'fondue', 'compote', 'tart', 'flan',
        'parfait', 'terrine', 'macaroon', 'brittle', 'crostata', 'linzer'
    ],
    'breakfast': [
        'waffle', 'pancake', 'crepe', 'muffin', 'scone', 'toast', 'cereal', 'oatmeal',
        'yogurt', 'smoothie', 'juice', 'coffee', 'tea', 'cappuccino', 'latte'
    ],
    'appetizers': [
        'pate', 'crostini', 'bruschetta', 'antipasto', 'tapenade', 'dip', 'spread',
        'croquette', 'dumpling', 'springroll', 'wontons', 'ravioli', 'pierogi'
    ],
    'salads': [
        'salad', 'greens', 'slaw', 'coleslaw', 'dressing', 'vinaigrette', 'salsa'
    ],
    'sauces': [
        'sauce', 'marinade', 'pesto', 'pesto', 'coulis', 'reduction', 'gravy',
        'mayonnaise', 'aioli', 'hollandaise', 'bechamel', 'veloute'
    ],
    'condiments': [
        'ketchup', 'mustard', 'mayonnaise', 'relish', 'chutney', 'jam', 'jelly',
        'preserve', 'pickle', 'dressing', 'vinaigrette'
    ],
    'sides': [
        'rice', 'potato', 'bread', 'roll', 'bun', 'pilaf', 'quinoa', 'couscous',
        'pasta', 'noodle', 'risotto', 'polenta', 'latke', 'croquette'
    ],
    'dinner': [
        'chicken', 'beef', 'pork', 'fish', 'seafood', 'tofu', 'seitan', 'tempeh',
        'turkey', 'lamb', 'duck', 'veal', 'bison', 'salmon', 'tuna', 'shrimp',
        'scallop', 'crab', 'lobster', 'steak', 'roast', 'grill', 'bake', 'fry',
        'stirfry', 'curry', 'stew', 'casserole', 'lasagna', 'paella'
    ],
    'lunch': [
        'sandwich', 'wrap', 'burger', 'taco', 'burrito', 'quesadilla', 'pizza',
        'pasta', 'noodle', 'soup', 'stew', 'casserole'
    ],
    'beverages': [
        'juice', 'smoothie', 'tea', 'coffee', 'milk', 'elixir', 'brew', 'punch',
        'lemonade', 'soda', 'cappuccino', 'latte', 'espresso', 'mocha'
    ]
}

def categorize_recipe(recipe_name):
    """Categorize a recipe based on its name."""
    recipe_lower = recipe_name.lower()

    # Check each category for matching keywords
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in recipe_lower:
                return category

    # Default to dinner if no specific category matches
    return 'dinner'

def main():
    base_path = Path('/Users/GregCastro/Desktop/untitled folder 3/HSCAlchm/src/data/recipes')
    soups_pending_path = base_path / 'soupsPENDING' / 'recipes'

    # Recipes that are correctly categorized as soups (should stay)
    correct_soups = {
        'curriedredlentilsoupwithcoconutmilk-vegan.ts',
        'creamysweetpotatobisquewithcashewcremefraicheandcandied.ts',
        'darkonionsoupwithwholegraincroutons.ts',
        'creamofmushroomsoup.ts',
        'shntakebrothwithshrimpsobaandbabybokchoy.ts',
        'creamofasparagussoup.ts',
        'seitanstew.ts',
        'creamofbroccolisoup.ts',
        'buttemutminestrone.ts',
        'creamycarrotsoupwithpotato.ts'
    }

    # Track moves
    moves = {}

    # Process all recipes in soupsPENDING
    for recipe_file in soups_pending_path.glob('*.ts'):
        recipe_name = recipe_file.name

        # Skip correct soups
        if recipe_name in correct_soups:
            continue

        # Categorize the recipe
        category = categorize_recipe(recipe_name)
        target_dir = base_path / category / 'recipes'

        # Ensure target directory exists
        target_dir.mkdir(parents=True, exist_ok=True)

        # Move the file
        target_path = target_dir / recipe_name
        shutil.move(str(recipe_file), str(target_path))

        # Track the move
        if category not in moves:
            moves[category] = []
        moves[category].append(recipe_name)

        print(f"Moved {recipe_name} → {category}")

    # Print summary
    print("\n=== REDISTRIBUTION SUMMARY ===")
    for category, recipes in moves.items():
        print(f"{category}: {len(recipes)} recipes")
        if len(recipes) <= 10:  # Show details for small categories
            for recipe in sorted(recipes):
                print(f"  - {recipe}")

    total_moved = sum(len(recipes) for recipes in moves.values())
    print(f"\nTotal recipes redistributed: {total_moved}")

if __name__ == '__main__':
    main()
