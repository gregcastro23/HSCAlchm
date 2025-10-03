#!/usr/bin/env python3
"""
Filter duplicates from extracted recipes based on cross-reference results
"""
import json
from typing import Dict, List

def load_cross_reference_report(path: str = "cross_reference_report.json") -> Dict:
    """Load cross-reference report"""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_extracted_recipes(path: str = "enhanced_extracted_recipes/enhanced_hsca_recipes.json") -> Dict:
    """Load extracted recipes"""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def filter_duplicates(extracted_data: Dict, cross_ref_data: Dict, confidence_threshold: float = 0.8) -> Dict:
    """Filter out duplicates based on cross-reference confidence scores"""
    
    # Get list of duplicate recipe names
    duplicate_names = set()
    for duplicate in cross_ref_data.get('duplicates', []):
        duplicate_names.add(duplicate['extracted_name'])
    
    # Get high confidence matches if we want to filter them too
    high_confidence_names = set()
    for match in cross_ref_data.get('high_confidence_matches', []):
        if match['confidence_score'] >= confidence_threshold:
            high_confidence_names.add(match['extracted_name'])
    
    # Filter recipes
    filtered_recipes = []
    skipped_duplicates = []
    
    for recipe in extracted_data.get('extracted_recipes', []):
        recipe_name = recipe.get('recipe', {}).get('name', '')
        
        if recipe_name in duplicate_names:
            skipped_duplicates.append({
                'recipe': recipe,
                'reason': 'duplicate',
                'confidence': 'high'
            })
        elif recipe_name in high_confidence_names:
            skipped_duplicates.append({
                'recipe': recipe,
                'reason': 'high_confidence_match',
                'confidence': 'high'
            })
        else:
            filtered_recipes.append(recipe)
    
    # Create filtered output
    filtered_data = {
        'extracted_recipes': filtered_recipes,
        'summary': {
            'total_extracted': len(extracted_data.get('extracted_recipes', [])),
            'filtered_recipes': len(filtered_recipes),
            'duplicates_removed': len(skipped_duplicates),
            'recipes_by_category': {},
            'recipes_by_lesson': {}
        },
        'skipped_duplicates': skipped_duplicates,
        'cross_reference_stats': {
            'total_matches': cross_ref_data.get('statistics', {}).get('total_matches', 0),
            'duplicates': cross_ref_data.get('statistics', {}).get('duplicates', 0),
            'high_confidence': cross_ref_data.get('statistics', {}).get('high_confidence', 0),
            'no_matches': cross_ref_data.get('statistics', {}).get('no_matches', 0)
        }
    }
    
    # Calculate filtered statistics
    for recipe in filtered_recipes:
        category = recipe.get('category', 'unknown')
        lesson = recipe.get('lesson', 'unknown')
        
        if category not in filtered_data['summary']['recipes_by_category']:
            filtered_data['summary']['recipes_by_category'][category] = 0
        filtered_data['summary']['recipes_by_category'][category] += 1
        
        if lesson not in filtered_data['summary']['recipes_by_lesson']:
            filtered_data['summary']['recipes_by_lesson'][lesson] = 0
        filtered_data['summary']['recipes_by_lesson'][lesson] += 1
    
    return filtered_data

def save_filtered_results(filtered_data: Dict, output_path: str = "enhanced_extracted_recipes/filtered_hsca_recipes.json"):
    """Save filtered results"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, indent=2, ensure_ascii=False)

def main():
    print("=== FILTERING DUPLICATES FROM EXTRACTION ===")
    
    # Load data
    cross_ref_data = load_cross_reference_report()
    extracted_data = load_extracted_recipes()
    
    print(f"Loaded {len(extracted_data.get('extracted_recipes', []))} extracted recipes")
    print(f"Cross-reference found {cross_ref_data.get('statistics', {}).get('duplicates', 0)} duplicates")
    print(f"Cross-reference found {cross_ref_data.get('statistics', {}).get('high_confidence', 0)} high confidence matches")
    
    # Filter duplicates
    filtered_data = filter_duplicates(extracted_data, cross_ref_data)
    
    # Save results
    save_filtered_results(filtered_data)
    
    print(f"\n=== FILTERING RESULTS ===")
    print(f"Original recipes: {filtered_data['summary']['total_extracted']}")
    print(f"Filtered recipes: {filtered_data['summary']['filtered_recipes']}")
    print(f"Duplicates removed: {filtered_data['summary']['duplicates_removed']}")
    print(f"Removal rate: {(filtered_data['summary']['duplicates_removed'] / filtered_data['summary']['total_extracted']) * 100:.1f}%")
    
    print(f"\n=== REMOVED DUPLICATES ===")
    for skip in filtered_data['skipped_duplicates']:
        print(f"  {skip['recipe']['recipe']['name']} ({skip['reason']})")
    
    print(f"\n=== FILTERED CATEGORIES ===")
    for category, count in filtered_data['summary']['recipes_by_category'].items():
        print(f"  {category}: {count}")
    
    print(f"\nFiltered results saved to: enhanced_extracted_recipes/filtered_hsca_recipes.json")

if __name__ == "__main__":
    main()