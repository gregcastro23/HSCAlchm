#!/usr/bin/env python3
"""
Merge instructions from recipes_with_improved_ocr_instructions.json
into the current fixed database to achieve 100% instruction coverage.
"""

import json
from pathlib import Path
from typing import Dict, List, Any


def load_databases():
    """Load both databases."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Current database (with spacing fixes and improved descriptions)
    current_file = script_dir / 'fixed_recipes_database_improved.json'
    
    # Improved OCR database (100% instruction coverage)
    improved_ocr_file = project_root / 'cleanup_backup/enhanced_extracted_recipes/recipes_with_improved_ocr_instructions.json'
    
    print("📖 Loading databases...")
    print(f"  Current: {current_file.name}")
    print(f"  Improved OCR: {improved_ocr_file.name}")
    
    with open(current_file, 'r', encoding='utf-8') as f:
        current_data = json.load(f)
    
    with open(improved_ocr_file, 'r', encoding='utf-8') as f:
        improved_ocr_data = json.load(f)
    
    current_recipes = current_data.get('extracted_recipes', [])
    improved_recipes = improved_ocr_data.get('extracted_recipes', improved_ocr_data.get('recipes', []))
    
    # Create lookup by name
    improved_lookup = {}
    for item in improved_recipes:
        recipe = item.get('recipe', item)
        name = recipe.get('name', '').lower().strip()
        if name:
            improved_lookup[name] = item
    
    return current_data, current_recipes, improved_lookup


def has_valid_instructions(recipe: Dict) -> bool:
    """Check if recipe has valid instructions."""
    instructions = recipe.get('instructions', [])
    if not instructions:
        return False
    valid_inst = [inst for inst in instructions if inst and inst.strip()]
    return len(valid_inst) > 0


def merge_instructions(current_data: Dict, current_recipes: List[Dict], improved_lookup: Dict) -> Dict:
    """Merge instructions from improved OCR database into current database."""
    merged_count = 0
    kept_count = 0
    not_found = []
    
    print("\n🔄 Merging instructions...")
    
    for item in current_recipes:
        if 'recipe' not in item:
            continue
        
        recipe = item['recipe']
        name = recipe.get('name', '')
        name_lower = name.lower().strip()
        
        # Check if current recipe has instructions
        if has_valid_instructions(recipe):
            kept_count += 1
            continue
        
        # Look for instructions in improved OCR database
        if name_lower in improved_lookup:
            improved_item = improved_lookup[name_lower]
            improved_recipe = improved_item.get('recipe', improved_item)
            improved_instructions = improved_recipe.get('instructions', [])
            
            if has_valid_instructions(improved_recipe):
                # Merge instructions
                recipe['instructions'] = improved_instructions
                merged_count += 1
                print(f"  ✓ Merged: {name}")
            else:
                not_found.append(name)
        else:
            not_found.append(name)
    
    print(f"\n✅ Merge complete!")
    print(f"  Recipes kept (already had instructions): {kept_count}")
    print(f"  Recipes merged (added instructions): {merged_count}")
    if not_found:
        print(f"  Recipes still without instructions: {len(not_found)}")
        if len(not_found) <= 20:
            for name in not_found:
                print(f"    - {name}")
    
    return current_data


def main():
    """Main function to merge instructions."""
    script_dir = Path(__file__).parent
    
    print("🔗 MERGING INSTRUCTIONS FROM IMPROVED OCR DATABASE")
    print("=" * 60)
    
    # Load databases
    current_data, current_recipes, improved_lookup = load_databases()
    
    print(f"\nCurrent database: {len(current_recipes)} recipes")
    print(f"Improved OCR database: {len(improved_lookup)} recipes")
    
    # Merge instructions
    merged_data = merge_instructions(current_data, current_recipes, improved_lookup)
    
    # Update metadata
    merged_data['extraction_methodology'] = merged_data.get('extraction_methodology', '') + ' | Instructions merged from improved OCR database'
    
    # Save merged database
    output_file = script_dir / 'fixed_recipes_database_with_instructions.json'
    print(f"\n💾 Saving merged database to: {output_file.name}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, indent=2, ensure_ascii=False)
    
    file_size = output_file.stat().st_size / 1024
    print(f"✓ File size: {file_size:.1f} KB")
    
    # Verify final coverage
    final_recipes = merged_data.get('extracted_recipes', [])
    with_inst = sum(1 for r in final_recipes if has_valid_instructions(r.get('recipe', {})))
    print(f"\n📊 Final coverage: {with_inst}/{len(final_recipes)} recipes with instructions ({with_inst/len(final_recipes)*100:.1f}%)")
    
    print("\n🎉 Merge complete!")
    print("\nNext step: Run update_recipes_from_fixed.py to regenerate TypeScript files with merged instructions")


if __name__ == '__main__':
    main()
