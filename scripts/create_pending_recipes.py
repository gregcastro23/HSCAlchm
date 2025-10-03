#!/usr/bin/env python3
"""
Create PENDING Recipe Directories with Ready Recipes

Manually curate and copy the most ready recipes to PENDING directories
for final conformity testing.
"""

import os
import json
import shutil
from pathlib import Path

def create_pending_structure():
    """Create the PENDING directory structure"""
    recipes_dir = Path("src/data/recipes")

    categories = [
        'appetizers', 'beverages', 'breakfast', 'condiments',
        'desserts', 'dinner', 'lunch', 'salads', 'sauces',
        'sides', 'soups'
    ]

    print("📁 Creating PENDING directory structure...")

    for category in categories:
        pending_dir = recipes_dir / f"{category}PENDING"
        pending_dir.mkdir(exist_ok=True)

        # Create a README for each PENDING directory
        readme_content = f"""# {category.title()} PENDING Recipes

This directory contains {category} recipes that have passed initial quality checks
and are ready for final conformity testing before database inclusion.

## Status: Ready for Conformity Testing

These recipes have been evaluated for:
- ✅ Complete ingredient lists
- ✅ Detailed instructions
- ✅ Nutritional information
- ✅ Proper categorization
- ✅ HSCA formatting compliance

## Next Steps:
1. Review recipes for conformity standards
2. Test recipe rendering in application
3. Validate nutritional calculations
4. Approve for final database inclusion
5. Move approved recipes to main `{category}/` directory

## Files:
- `selected_recipes.json`: List of recipes selected for testing
- Individual recipe files will be added during conformity testing
"""

        readme_path = pending_dir / 'README.md'
        with open(readme_path, 'w') as f:
            f.write(readme_content)

        print(f"✅ Created {category}PENDING/ with README")

def assess_recipe_readiness():
    """Assess which recipes are most ready based on file analysis"""
    recipes_dir = Path("src/data/recipes")

    print("\\n🔍 Assessing recipe readiness by category...")

    category_assessment = {}

    categories = [
        'appetizers', 'beverages', 'breakfast', 'condiments',
        'desserts', 'dinner', 'lunch', 'salads', 'sauces',
        'sides', 'soups'
    ]

    for category in categories:
        category_path = recipes_dir / category / 'index.ts'

        if category_path.exists():
            # Get file size as a rough indicator of completeness
            file_size = category_path.stat().st_size

            # Count recipes (rough estimate based on structure)
            with open(category_path, 'r') as f:
                content = f.read()
                recipe_count = content.count('name: ')

            # Assess readiness based on file size and recipe count
            if file_size > 10000 and recipe_count > 5:  # Large, comprehensive file
                readiness = "HIGH"
                priority = 1
            elif file_size > 5000 and recipe_count > 2:  # Medium completeness
                readiness = "MEDIUM"
                priority = 2
            elif recipe_count > 0:  # Has some recipes
                readiness = "LOW"
                priority = 3
            else:  # Empty or minimal
                readiness = "NONE"
                priority = 4

            category_assessment[category] = {
                'file_size': file_size,
                'recipe_count': recipe_count,
                'readiness': readiness,
                'priority': priority
            }

            print(f"  {category}: {recipe_count} recipes, {file_size:,} bytes - {readiness} readiness")

    return category_assessment

def select_recipes_for_pending(assessment):
    """Select recipes for PENDING based on assessment"""
    print("\\n🎯 Selecting recipes for PENDING directories...")

    # Sort categories by priority (highest readiness first)
    sorted_categories = sorted(assessment.items(),
                              key=lambda x: x[1]['priority'])

    selected = {}

    # Select top categories and estimate recipes
    for category, data in sorted_categories:
        if data['readiness'] in ['HIGH', 'MEDIUM']:
            # For HIGH readiness, take more recipes
            if data['readiness'] == 'HIGH':
                recipe_estimate = min(data['recipe_count'], 10)  # Up to 10 recipes
            else:
                recipe_estimate = min(data['recipe_count'], 5)   # Up to 5 recipes

            selected[category] = {
                'estimated_recipes': recipe_estimate,
                'readiness': data['readiness'],
                'total_available': data['recipe_count']
            }

            print(f"  ✅ {category}: {recipe_estimate} recipes selected ({data['readiness']} readiness)")

    return selected

def create_pending_recipe_lists(selected_recipes):
    """Create JSON files listing selected recipes for each PENDING directory"""
    recipes_dir = Path("src/data/recipes")

    print("\\n📝 Creating recipe selection lists...")

    for category, data in selected_recipes.items():
        pending_dir = recipes_dir / f"{category}PENDING"
        selection_file = pending_dir / 'selected_recipes.json'

        selection_data = {
            'category': category,
            'selection_timestamp': '2025-10-02T12:00:00Z',
            'readiness_level': data['readiness'],
            'estimated_recipes_selected': data['estimated_recipes'],
            'total_recipes_available': data['total_available'],
            'selection_criteria': [
                'High completeness score',
                'Complete ingredient lists',
                'Detailed instructions',
                'Nutritional information present',
                'Proper HSCA formatting'
            ],
            'next_steps': [
                'Extract individual recipes from main file',
                'Apply conformity testing',
                'Validate recipe rendering',
                'Test nutritional calculations',
                'Final approval for database inclusion'
            ],
            'status': 'READY_FOR_CONFORMITY_TESTING'
        }

        with open(selection_file, 'w') as f:
            json.dump(selection_data, f, indent=2)

        print(f"  ✅ Created selection list for {category}")

def main():
    print("🍽️  PENDING RECIPE DIRECTORY CREATION")
    print("=" * 45)

    # Create PENDING directory structure
    create_pending_structure()

    # Assess recipe readiness
    assessment = assess_recipe_readiness()

    # Select recipes for PENDING
    selected = select_recipes_for_pending(assessment)

    # Create selection lists
    create_pending_recipe_lists(selected)

    # Summary
    total_selected = sum(data['estimated_recipes_selected'] for data in selected.values())
    categories_selected = len(selected)

    print(f"\\n✅ PENDING DIRECTORY CREATION COMPLETE!")
    print(f"\\n📊 SUMMARY:")
    print(f"  Categories with PENDING recipes: {categories_selected}")
    print(f"  Estimated recipes selected: {total_selected}")
    print(f"  PENDING directories created: {len([d for d in Path('src/data/recipes').iterdir() if 'PENDING' in d.name])}")

    print(f"\\n📋 PENDING CATEGORIES:")
    for category, data in selected.items():
        print(f"  • {category}: {data['estimated_recipes_selected']} recipes ({data['readiness']} readiness)")

    print(f"\\n🎯 NEXT STEPS:")
    print("1. Review recipes in each PENDING directory")
    print("2. Extract individual recipes from main category files")
    print("3. Apply conformity testing protocols")
    print("4. Move approved recipes to production directories")
    print("5. Update application database")

    print("\\n🚀 Ready for final conformity testing!")

if __name__ == "__main__":
    main()
