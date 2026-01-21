#!/usr/bin/env python3
"""
Clean up duplicate recipes and ensure frontend only has recipes from extracted database.
Removes old files with broken spacing and placeholder recipes.
"""

import json
import re
from pathlib import Path
from typing import Dict, Set, List


def normalize_name(name: str) -> str:
    """Normalize recipe name for comparison (remove spacing issues)."""
    # Remove common spacing issues for comparison
    name = name.lower()
    name = re.sub(r'\s+in\s+', 'in', name)
    name = re.sub(r'\s+at\s+', 'at', name)
    name = re.sub(r'\s+on\s+', 'on', name)
    name = re.sub(r'\s+or\s+', 'or', name)
    name = re.sub(r'\s+and\s+', 'and', name)
    name = re.sub(r'[^a-z0-9]', '', name)
    return name


def load_extracted_recipes() -> Dict[str, Dict]:
    """Load extracted recipes and create lookup by normalized name."""
    improved_file = Path('scripts/fixed_recipes_database_improved.json')
    aggressive_file = Path('scripts/fixed_recipes_database_aggressive.json')
    
    if improved_file.exists():
        source_file = improved_file
    elif aggressive_file.exists():
        source_file = aggressive_file
    else:
        print("❌ No fixed database found!")
        return {}
    
    with open(source_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    recipes = {}
    for item in data.get('extracted_recipes', []):
        if 'recipe' not in item:
            continue
        recipe = item['recipe']
        name = recipe.get('name', '')
        normalized = normalize_name(name)
        recipes[normalized] = {
            'original_name': name,
            'recipe': recipe,
            'category': item.get('category', 'dinner')
        }
    
    return recipes


def find_recipe_files() -> Dict[str, List[Dict]]:
    """Find all recipe TypeScript files and group by normalized name."""
    recipes_dir = Path('src/data/recipes')
    recipe_files = {}
    
    for category_dir in recipes_dir.iterdir():
        if not category_dir.is_dir():
            continue
        recipes_subdir = category_dir / 'recipes'
        if not recipes_subdir.exists():
            continue
        
        for recipe_file in recipes_subdir.glob('*.ts'):
            try:
                with open(recipe_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    name_match = re.search(r"name:\s*['\"]([^'\"]+)['\"]", content)
                    if name_match:
                        name = name_match.group(1)
                        normalized = normalize_name(name)
                        
                        if normalized not in recipe_files:
                            recipe_files[normalized] = []
                        
                        recipe_files[normalized].append({
                            'file': recipe_file,
                            'category': category_dir.name,
                            'name': name,
                            'normalized': normalized
                        })
            except Exception as e:
                print(f"Error reading {recipe_file}: {e}")
    
    return recipe_files


def main():
    """Main cleanup function."""
    print("🧹 CLEANING UP DUPLICATE RECIPES")
    print("=" * 60)
    
    # Load extracted recipes
    print("📖 Loading extracted recipes...")
    extracted = load_extracted_recipes()
    print(f"Found {len(extracted)} unique recipes in extracted database\n")
    
    # Find all recipe files
    print("🔍 Finding recipe files...")
    recipe_files = find_recipe_files()
    print(f"Found {sum(len(files) for files in recipe_files.values())} recipe files")
    print(f"Grouped into {len(recipe_files)} normalized names\n")
    
    # Find duplicates and files to remove
    files_to_remove = []
    files_to_keep = set()
    placeholders = []
    
    for normalized, files in recipe_files.items():
        if len(files) > 1:
            # Multiple files for same recipe - check which one matches extracted
            matching_file = None
            for f in files:
                if f['name'].lower().strip() in [r['original_name'].lower().strip() for r in extracted.values()]:
                    matching_file = f
                    break
            
            if matching_file:
                # Keep the matching file
                files_to_keep.add(str(matching_file['file']))
                # Remove others
                for f in files:
                    if str(f['file']) != str(matching_file['file']):
                        files_to_remove.append(f['file'])
                        print(f"  Removing duplicate: {f['name']} ({f['category']})")
            else:
                # None match exactly - check if any are in extracted
                # For now, keep the one with fixed spacing (no " In ", " At ", etc.)
                fixed_spacing_file = None
                for f in files:
                    if not re.search(r'\s+(In|At|On|Or)\s+', f['name']):
                        fixed_spacing_file = f
                        break
                
                if fixed_spacing_file:
                    files_to_keep.add(str(fixed_spacing_file['file']))
                    for f in files:
                        if str(f['file']) != str(fixed_spacing_file['file']):
                            files_to_remove.append(f['file'])
                else:
                    # Keep first one, remove others
                    files_to_keep.add(str(files[0]['file']))
                    for f in files[1:]:
                        files_to_remove.append(f['file'])
        
        elif normalized in extracted:
            # Single file and it's in extracted - keep it
            files_to_keep.add(str(files[0]['file']))
        else:
            # Single file but not in extracted - might be placeholder
            name_lower = files[0]['name'].lower()
            if 'recovered' in name_lower or 'placeholder' in name_lower:
                placeholders.append(files[0]['file'])
                print(f"  Found placeholder: {files[0]['name']} ({files[0]['category']})")
            else:
                # Check if it's a spacing-variant of an extracted recipe
                found_match = False
                for extracted_normalized, extracted_data in extracted.items():
                    if normalized == extracted_normalized:
                        files_to_keep.add(str(files[0]['file']))
                        found_match = True
                        break
                
                if not found_match:
                    files_to_remove.append(files[0]['file'])
                    print(f"  Removing orphan: {files[0]['name']} ({files[0]['category']})")
    
    # Remove placeholder files
    files_to_remove.extend(placeholders)
    
    print(f"\n📊 Summary:")
    print(f"  Files to keep: {len(files_to_keep)}")
    print(f"  Files to remove: {len(files_to_remove)}")
    print(f"  Placeholders: {len(placeholders)}")
    
    # Actually remove files
    if files_to_remove:
        print(f"\n🗑️  Removing {len(files_to_remove)} files...")
        for file_path in files_to_remove:
            try:
                file_path.unlink()
                print(f"  ✓ Removed: {file_path.name}")
            except Exception as e:
                print(f"  ✗ Error removing {file_path}: {e}")
    
    print("\n✅ Cleanup complete!")
    print("\n⚠️  Next step: Run update_recipes_from_fixed.py to regenerate missing recipes")


if __name__ == '__main__':
    main()
