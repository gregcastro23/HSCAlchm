#!/usr/bin/env python3
"""
Fix duplicate slugs in the transformed recipes JSON.
"""

import json
from pathlib import Path
from collections import Counter

def fix_duplicate_slugs(recipes):
    """Add numeric suffixes to duplicate slugs."""
    slug_counts = Counter(r['slug'] for r in recipes)
    duplicates = {slug for slug, count in slug_counts.items() if count > 1}

    if not duplicates:
        print("No duplicate slugs found!")
        return recipes

    print(f"Found {len(duplicates)} duplicate slugs:")
    for slug in sorted(duplicates):
        print(f"  - {slug} ({slug_counts[slug]} occurrences)")

    # Track which occurrence we're on for each duplicate
    occurrence_tracker = {slug: 0 for slug in duplicates}

    # Update slugs
    fixed_recipes = []
    for recipe in recipes:
        slug = recipe['slug']
        if slug in duplicates:
            occurrence_tracker[slug] += 1
            if occurrence_tracker[slug] > 1:
                # Add suffix to make unique
                new_slug = f"{slug}-{occurrence_tracker[slug]}"
                print(f"  Renaming: {slug} -> {new_slug} (for '{recipe['title']}')")
                recipe['slug'] = new_slug
                recipe['id'] = new_slug
        fixed_recipes.append(recipe)

    # Verify all slugs are now unique
    final_slugs = [r['slug'] for r in fixed_recipes]
    final_slug_counts = Counter(final_slugs)
    remaining_duplicates = {slug for slug, count in final_slug_counts.items() if count > 1}

    if remaining_duplicates:
        print(f"\n⚠️  WARNING: Still have {len(remaining_duplicates)} duplicates!")
        return recipes  # Return original if fix didn't work

    print(f"\n✓ All slugs are now unique! ({len(final_slugs)} recipes)")
    return fixed_recipes

def main():
    # Paths
    script_dir = Path(__file__).parent
    source_file = script_dir / 'transformed_recipes.json'
    output_file = script_dir / 'transformed_recipes_fixed.json'

    # Load recipes
    with open(source_file, 'r', encoding='utf-8') as f:
        recipes = json.load(f)

    print(f"Loaded {len(recipes)} recipes")

    # Fix duplicates
    fixed_recipes = fix_duplicate_slugs(recipes)

    # Save fixed data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(fixed_recipes, f, indent=2, ensure_ascii=False)

    print(f"\nFixed recipes saved to: {output_file}")
    print(f"File size: {output_file.stat().st_size / 1024:.1f} KB")

if __name__ == '__main__':
    main()
