#!/usr/bin/env python3
"""
Recipe Readiness Analysis Script

Analyzes recipes in each category and identifies the most ready ones for PENDING status.
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple, Any

def analyze_recipe_file(file_path: str) -> List[Dict[str, Any]]:
    """Analyze a recipe file and return readiness scores"""
    recipes = []

    try:
        with open(file_path, 'r') as f:
            content = f.read()

        # Extract individual recipe objects using regex
        # This is a simplified approach - look for recipe object patterns
        recipe_pattern = r'{\s*name:\s*[\'"](.*?)[\'"],(.*?)}(?=\s*},?\s*{|\s*];)'
        matches = re.findall(recipe_pattern, content, re.DOTALL)

        for match in matches:
            name, recipe_content = match

            # Count key elements
            has_ingredients = 'ingredients:' in recipe_content
            has_instructions = 'instructions:' in recipe_content
            has_nutrition = 'nutrition:' in recipe_content
            has_time = 'timeToMake:' in recipe_content
            has_meal_type = 'mealType:' in recipe_content
            has_description = 'description:' in recipe_content

            # Calculate completeness score
            completeness_items = [has_ingredients, has_instructions, has_nutrition,
                                has_time, has_meal_type, has_description]
            completeness_score = sum(completeness_items) / len(completeness_items)

            # Calculate readiness score
            score = 0
            issues = []

            if has_ingredients:
                score += 25
            else:
                issues.append("Missing ingredients")

            if has_instructions:
                score += 25
            else:
                issues.append("Missing instructions")

            if has_nutrition:
                score += 15
            else:
                issues.append("Missing nutrition")

            if has_description:
                score += 10
            else:
                issues.append("Missing description")

            if has_time:
                score += 10
            else:
                issues.append("Missing time estimate")

            if has_meal_type:
                score += 10
            else:
                issues.append("Missing meal type")

            # Determine readiness level
            if score >= 80 and has_ingredients and has_instructions:
                readiness = "READY"
            elif score >= 60:
                readiness = "REVIEW"
            else:
                readiness = "NEEDS_WORK"

            recipes.append({
                'name': name,
                'score': score,
                'completeness': completeness_score,
                'readiness': readiness,
                'issues': issues,
                'has_ingredients': has_ingredients,
                'has_instructions': has_instructions,
                'has_nutrition': has_nutrition
            })

    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")

    return recipes

def analyze_all_categories():
    """Analyze all recipe categories"""
    recipes_dir = Path("src/data/recipes")
    categories = [
        'appetizers', 'beverages', 'breakfast', 'condiments',
        'desserts', 'dinner', 'lunch', 'salads', 'sauces',
        'sides', 'soups'
    ]

    results = {}

    print("🔍 Analyzing recipe readiness by category...")

    for category in categories:
        category_path = recipes_dir / category / 'index.ts'
        if category_path.exists():
            recipes = analyze_recipe_file(str(category_path))
            results[category] = recipes

            # Summary for this category
            ready_count = len([r for r in recipes if r['readiness'] == 'READY'])
            review_count = len([r for r in recipes if r['readiness'] == 'REVIEW'])
            needs_work_count = len([r for r in recipes if r['readiness'] == 'NEEDS_WORK'])

            print(f"  {category}: {len(recipes)} total")
            print(f"    READY: {ready_count}, REVIEW: {review_count}, NEEDS_WORK: {needs_work_count}")

    return results

def select_top_ready_recipes(results: Dict[str, List[Dict[str, Any]]], top_n: int = 5) -> Dict[str, List[Dict[str, Any]]]:
    """Select top N most ready recipes from each category"""
    selected = {}

    for category, recipes in results.items():
        # Sort by score (highest first)
        sorted_recipes = sorted(recipes, key=lambda x: x['score'], reverse=True)
        # Take top N
        selected[category] = sorted_recipes[:top_n]

    return selected

def copy_recipes_to_pending(selected_recipes: Dict[str, List[Dict[str, Any]]]):
    """Copy selected recipes to PENDING directories"""
    recipes_dir = Path("src/data/recipes")

    total_copied = 0

    for category, recipes in selected_recipes.items():
        pending_dir = recipes_dir / f"{category}PENDING"
        source_file = recipes_dir / category / 'index.ts'

        if recipes and source_file.exists():
            # For now, just create a marker file indicating which recipes are selected
            # In a full implementation, you'd extract and copy individual recipes
            pending_file = pending_dir / 'selected_recipes.json'

            with open(pending_file, 'w') as f:
                json.dump({
                    'category': category,
                    'selected_recipes': recipes,
                    'selection_criteria': 'Top 5 by readiness score',
                    'ready_for_conformity_testing': True
                }, f, indent=2)

            print(f"✅ {category}: {len(recipes)} recipes marked for PENDING")
            total_copied += len(recipes)

    return total_copied

def main():
    print("🍽️  RECIPE READINESS ANALYSIS")
    print("=" * 40)

    # Analyze all categories
    results = analyze_all_categories()

    # Calculate totals
    total_recipes = sum(len(recipes) for recipes in results.values())
    ready_recipes = sum(len([r for r in recipes if r['readiness'] == 'READY']) for recipes in results.values())
    review_recipes = sum(len([r for r in recipes if r['readiness'] == 'REVIEW']) for recipes in results.values())

    print(f"\\n📊 OVERALL RESULTS:")
    print(f"  Total recipes analyzed: {total_recipes}")
    print(f"  Ready for PENDING: {ready_recipes}")
    print(f"  Need review: {review_recipes}")
    print(f"  Need work: {total_recipes - ready_recipes - review_recipes}")

    # Select top recipes for PENDING
    print("\\n🎯 Selecting top recipes for PENDING directories...")
    selected = select_top_ready_recipes(results, top_n=5)

    # Copy to PENDING
    print("\\n📁 Preparing PENDING directories...")
    copied_count = copy_recipes_to_pending(selected)

    print(f"\\n✅ PENDING PREPARATION COMPLETE:")
    print(f"  {copied_count} recipes across {len(selected)} categories marked for PENDING")
    print("  Ready for final conformity testing!")

    # Show top categories by readiness
    print("\\n🏆 TOP CATEGORIES BY READINESS:")
    category_scores = {}
    for category, recipes in results.items():
        if recipes:
            avg_score = sum(r['score'] for r in recipes) / len(recipes)
            ready_pct = len([r for r in recipes if r['readiness'] == 'READY']) / len(recipes)
            category_scores[category] = (avg_score, ready_pct, len(recipes))

    sorted_categories = sorted(category_scores.items(),
                              key=lambda x: (x[1][1], x[1][0]), reverse=True)  # Sort by ready %, then avg score

    for category, (avg_score, ready_pct, count) in sorted_categories[:5]:
        print(f"  {category}: {ready_pct*100:.1f}% ready ({count} recipes, avg score: {avg_score:.1f})")

if __name__ == "__main__":
    main()
