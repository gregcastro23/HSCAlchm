#!/usr/bin/env python3
"""
Aggressive fix for recipe spacing issues using comprehensive pattern matching.
This script fixes OCR errors where spaces were incorrectly inserted in the middle of words.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any


class AggressiveSpacingFixer:
    def __init__(self):
        # Common words that appear broken with " at ", " on ", " in " in the middle
        self.broken_word_patterns = {
            # Common cooking terms
            r'g\s+in\s+ger': 'ginger',
            r'G\s+In\s+Ger': 'Ginger',
            r'G\s+in\s+ger': 'Ginger',
            r'g\s+in\s+ger': 'ginger',
            
            r'cul\s+in\s+ary': 'culinary',
            r'Cul\s+In\s+Ary': 'Culinary',
            r'Cul\s+in\s+ary': 'Culinary',
            r'cul\s+in\s+ary': 'culinary',
            
            r'f\s+on\s+due': 'fondue',
            r'F\s+On\s+Due': 'Fondue',
            r'F\s+on\s+due': 'Fondue',
            r'f\s+on\s+due': 'fondue',
            
            r'w\s+at\s+er': 'water',
            r'W\s+At\s+Er': 'Water',
            r'W\s+at\s+er': 'Water',
            r'w\s+at\s+er': 'water',
            
            r'w\s+at\s+ermelon': 'watermelon',
            r'W\s+At\s+Ermelon': 'Watermelon',
            r'W\s+at\s+ermelon': 'Watermelon',
            r'w\s+at\s+ermelon': 'watermelon',
            
            r'w\s+at\s+ercress': 'watercress',
            r'W\s+At\s+Ercress': 'Watercress',
            r'W\s+at\s+ercress': 'Watercress',
            r'w\s+at\s+ercress': 'watercress',
            
            r'c\s+on\s+diment': 'condiment',
            r'C\s+On\s+Diment': 'Condiment',
            r'C\s+on\s+diment': 'Condiment',
            r'c\s+on\s+diment': 'condiment',
            
            r'v\s+in\s+aigrette': 'vinaigrette',
            r'V\s+In\s+Aigrette': 'Vinaigrette',
            r'V\s+in\s+aigrette': 'Vinaigrette',
            r'v\s+in\s+aigrette': 'vinaigrette',
            
            r'p\s+in\s+to': 'pinto',
            r'P\s+In\s+To': 'Pinto',
            r'P\s+in\s+to': 'Pinto',
            r'p\s+in\s+to': 'pinto',
            
            r'chocol\s+at\s+e': 'chocolate',
            r'Chocol\s+At\s+E': 'Chocolate',
            r'Chocol\s+at\s+e': 'Chocolate',
            r'chocol\s+at\s+e': 'chocolate',
            
            r'lem\s+on': 'lemon',
            r'Lem\s+On': 'Lemon',
            r'Lem\s+on': 'Lemon',
            r'lem\s+on': 'lemon',
            
            r'c\s+on\s+ut': 'coconut',
            r'C\s+On\s+Ut': 'Coconut',
            r'C\s+on\s+ut': 'Coconut',
            r'c\s+on\s+ut': 'coconut',
            
            r'h\s+or\s+seradish': 'horseradish',
            r'H\s+Or\s+Seradish': 'Horseradish',
            r'H\s+or\s+seradish': 'Horseradish',
            r'h\s+or\s+seradish': 'horseradish',
            
            r'holl\s+and\s+aise': 'hollandaise',
            r'Holl\s+And\s+Aise': 'Hollandaise',
            r'Holl\s+and\s+aise': 'Hollandaise',
            r'holl\s+and\s+aise': 'hollandaise',
            
            r'ichib\s+and\s+ashi': 'ichiban dashi',
            r'Ichib\s+And\s+Ashi': 'Ichiban Dashi',
            r'Ichib\s+and\s+ashi': 'Ichiban Dashi',
            
            r'zucch\s+in\s+i': 'zucchini',
            r'Zucch\s+In\s+I': 'Zucchini',
            r'Zucch\s+in\s+i': 'Zucchini',
            r'zucch\s+in\s+i': 'zucchini',
            
            r'sweetpot\s+at\s+o': 'sweetpotato',
            r'Sweetpot\s+At\s+O': 'Sweetpotato',
            r'Sweetpot\s+at\s+o': 'Sweetpotato',
            r'sweetpot\s+at\s+o': 'sweetpotato',
            
            r'crou\s+to\s+ns': 'croutons',
            r'Crou\s+To\s+Ns': 'Croutons',
            r'Crou\s+to\s+ns': 'Croutons',
            r'crou\s+to\s+ns': 'croutons',
            
            r'crou\s+to\s+n': 'crouton',
            r'Crou\s+To\s+N': 'Crouton',
            r'Crou\s+to\s+n': 'Crouton',
            r'crou\s+to\s+n': 'crouton',
            
            r'gra\s+in': 'grain',
            r'Gra\s+In': 'Grain',
            r'Gra\s+in': 'Grain',
            r'gra\s+in': 'grain',
            
            r'on\s+ion': 'onion',
            r'On\s+Ion': 'Onion',
            r'On\s+ion': 'Onion',
            r'on\s+ion': 'onion',
            
            r'roma\s+in\s+e': 'romaine',
            r'Roma\s+In\s+E': 'Romaine',
            r'Roma\s+in\s+e': 'Romaine',
            r'roma\s+in\s+e': 'romaine',
            
            r'polent\s+at\s+an': 'polenta',
            r'Polent\s+At\s+An': 'Polenta',
            r'Polent\s+at\s+an': 'Polenta',
            r'polent\s+at\s+an': 'polenta',
        }
        
        # Common OCR errors (spaces removed between words)
        self.ocr_replacements = {
            'onveon': 'olive oil',
            'onveen': 'olive oil',
            'extravirginonveon': 'extra virgin olive oil',
            'greekyogurt': 'greek yogurt',
            'tomatovinaigrette': 'tomato vinaigrette',
            'preheatovento': 'preheat oven to',
            'vegetabie': 'vegetable',
            'vegetabies': 'vegetables',
            'biack': 'black',
            'garn': 'garlic',
            'snced': 'sliced',
            'fineiy': 'finely',
            'wen': 'well',
            'untn': 'until',
            'ceiery': 'celery',
            'tabiespoons': 'tablespoons',
            'tabiespoon': 'tablespoon',
        }

    def fix_text(self, text: str) -> str:
        """Fix spacing issues in text."""
        if not text:
            return text
        
        # First, fix broken word patterns (spaces in middle of words)
        for pattern, replacement in self.broken_word_patterns.items():
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        
        # Fix OCR replacements (spaces removed)
        for wrong, correct in sorted(self.ocr_replacements.items(), key=lambda x: -len(x[0])):
            text = text.replace(wrong, correct)
            text = text.replace(wrong.capitalize(), correct.capitalize())
            text = text.replace(wrong.title(), correct.title())
        
        # Fix common patterns in instructions
        text = self._fix_instruction_patterns(text)
        
        # Clean up extra spaces
        text = ' '.join(text.split())
        
        return text.strip()

    def _fix_instruction_patterns(self, text: str) -> str:
        """Fix common patterns in instruction text."""
        # Fix " on " in instruction context (often should be " onion ")
        # But be careful - only fix obvious cases
        text = re.sub(r'\b(on)\s+(sheet|tray|pan|pot|dish|plate)\b', r'on \2', text, flags=re.IGNORECASE)
        
        # Fix common instruction patterns
        patterns = [
            (r'\bo\.s\b', '0.5'),
            (r'\bI\s+(cup|tbsp|tsp|oz|lb|pound)\b', r'1 \1'),
            (r'(\d+)(cup|cups|tbsp|tsp|oz|lb)\b', r'\1 \2'),
        ]
        
        for pattern, replacement in patterns:
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        
        return text

    def fix_recipe(self, recipe: Dict[str, Any]) -> Dict[str, Any]:
        """Fix a single recipe."""
        # Fix name
        if 'name' in recipe:
            recipe['name'] = self.fix_text(recipe['name'])
        
        # Fix description
        if 'description' in recipe:
            recipe['description'] = self.fix_text(recipe['description'])
        
        # Fix ingredients
        if 'ingredients' in recipe and isinstance(recipe['ingredients'], list):
            for ing in recipe['ingredients']:
                if isinstance(ing, dict) and 'name' in ing:
                    ing['name'] = self.fix_text(ing['name'])
                if isinstance(ing, dict) and 'notes' in ing:
                    ing['notes'] = self.fix_text(ing['notes'])
        
        # Fix instructions
        if 'instructions' in recipe and isinstance(recipe['instructions'], list):
            fixed_instructions = []
            for inst in recipe['instructions']:
                if isinstance(inst, str) and inst.strip():
                    fixed = self.fix_text(inst)
                    if fixed and len(fixed) > 5:
                        fixed_instructions.append(fixed)
            recipe['instructions'] = fixed_instructions
        
        return recipe


def main():
    """Main function to fix recipe database."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Input: original database
    input_file = project_root / 'cleanup_backup/enhanced_extracted_recipes/hybrid_hsca_recipes_database.json'
    
    # Output: aggressively fixed database
    output_file = script_dir / 'fixed_recipes_database_aggressive.json'
    
    print("🔧 AGGRESSIVE SPACING FIX")
    print("=" * 60)
    print(f"Reading from: {input_file}")
    
    # Load data
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    recipes = data.get('extracted_recipes', [])
    print(f"Found {len(recipes)} recipes to fix\n")
    
    # Initialize fixer
    fixer = AggressiveSpacingFixer()
    
    # Fix all recipes
    fixed_count = 0
    for idx, item in enumerate(recipes, 1):
        if 'recipe' in item:
            item['recipe'] = fixer.fix_recipe(item['recipe'])
            fixed_count += 1
        
        if idx % 50 == 0:
            print(f"Fixed {idx}/{len(recipes)} recipes...")
    
    print(f"\n✅ Fixed {fixed_count} recipes")
    
    # Update metadata
    data['extraction_methodology'] = data.get('extraction_methodology', '') + ' | Aggressive spacing fix applied'
    data['summary']['total_recipes'] = len(recipes)
    
    # Save fixed database
    print(f"\n💾 Saving to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    file_size = output_file.stat().st_size / 1024
    print(f"✓ File size: {file_size:.1f} KB")
    print("\n🎉 Aggressive fix complete!")


if __name__ == '__main__':
    main()
