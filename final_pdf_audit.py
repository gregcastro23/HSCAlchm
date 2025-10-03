#!/usr/bin/env python3
"""
Final comprehensive audit of PDF recipes vs database to identify any missed recipes.
"""

import os
import json
import re
from pathlib import Path

def extract_recipe_names_from_pdf(pdf_path):
    """Extract all recipe names from the PDF using text extraction."""
    import subprocess

    try:
        # Use pdftotext to extract text from PDF
        result = subprocess.run(
            ['pdftotext', '-layout', pdf_path, '-'],
            capture_output=True,
            text=True,
            check=True
        )

        text = result.stdout

        # Look for recipe patterns - typically capitalized titles
        # Common patterns: "RECIPE NAME", "Recipe Name", or lines that look like titles
        recipe_patterns = [
            r'^([A-Z][A-Z\s]{3,50})$',  # All caps titles
            r'^([A-Z][A-Za-z\s]{3,50})$',  # Title case
        ]

        potential_recipes = set()

        for line in text.split('\n'):
            line = line.strip()
            if not line:
                continue

            for pattern in recipe_patterns:
                match = re.match(pattern, line)
                if match:
                    recipe_name = match.group(1).strip()
                    # Filter out common non-recipe titles
                    if not any(skip in recipe_name.lower() for skip in [
                        'chapter', 'section', 'page', 'table', 'figure',
                        'introduction', 'conclusion', 'appendix', 'index',
                        'contents', 'recipe', 'recipes', 'ingredients',
                        'instructions', 'method', 'directions'
                    ]):
                        potential_recipes.add(recipe_name)

        return sorted(list(potential_recipes))

    except Exception as e:
        print(f"Error extracting from PDF: {e}")
        return []

def extract_recipe_names_from_database():
    """Extract all recipe names from our database."""
    recipes_dir = Path('src/data/recipes')
    recipe_names = set()

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

                    # Extract recipe name from the export
                    match = re.search(r'"name":\s*"([^"]+)"', content)
                    if match:
                        recipe_names.add(match.group(1).strip())

            except Exception as e:
                print(f"Error reading {recipe_file}: {e}")

    return sorted(list(recipe_names))

def main():
    pdf_path = "../../HSCARECIPES/HSCA_Recipes.pdf"

    print("🔍 FINAL PDF RECIPE AUDIT")
    print("=" * 50)

    # Extract recipe names from PDF
    print("📖 Extracting recipe names from PDF...")
    pdf_recipes = extract_recipe_names_from_pdf(pdf_path)
    print(f"Found {len(pdf_recipes)} potential recipes in PDF")

    # Extract recipe names from database
    print("📊 Extracting recipe names from database...")
    db_recipes = extract_recipe_names_from_database()
    print(f"Found {len(db_recipes)} recipes in database")

    # Compare
    pdf_set = set(r.lower() for r in pdf_recipes)
    db_set = set(r.lower() for r in db_recipes)

    missing_in_db = pdf_set - db_set
    extra_in_db = db_set - pdf_set

    print("\n📋 AUDIT RESULTS:")
    print(f"Recipes in PDF: {len(pdf_recipes)}")
    print(f"Recipes in Database: {len(db_recipes)}")
    print(f"Missing from Database: {len(missing_in_db)}")
    print(f"Extra in Database: {len(extra_in_db)}")

    if missing_in_db:
        print("\n⚠️  POTENTIALLY MISSING RECIPES:")
        for recipe in sorted(missing_in_db):
            print(f"  - {recipe}")

    if extra_in_db:
        print("\nℹ️  RECIPES IN DB NOT FOUND IN PDF:")
        for recipe in sorted(list(extra_in_db)[:20]):  # Show first 20
            print(f"  - {recipe}")
        if len(extra_in_db) > 20:
            print(f"  ... and {len(extra_in_db) - 20} more")

    # Save detailed results
    results = {
        'pdf_recipes': pdf_recipes,
        'database_recipes': db_recipes,
        'missing_from_db': sorted(list(missing_in_db)),
        'extra_in_db': sorted(list(extra_in_db)),
        'summary': {
            'pdf_count': len(pdf_recipes),
            'db_count': len(db_recipes),
            'missing_count': len(missing_in_db),
            'extra_count': len(extra_in_db)
        }
    }

    with open('final_pdf_audit_results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n📄 Detailed results saved to final_pdf_audit_results.json")

    if len(missing_in_db) == 0:
        print("✅ AUDIT COMPLETE: All PDF recipes appear to be captured in database!")
    else:
        print(f"⚠️  AUDIT COMPLETE: {len(missing_in_db)} recipes may be missing from database.")

if __name__ == '__main__':
    main()
