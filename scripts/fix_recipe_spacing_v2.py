#!/usr/bin/env python3
"""
Comprehensive fix for recipe spacing and capitalization issues using word segmentation.
This script addresses OCR artifacts where spaces were removed between words.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Set


class RecipeTextFixer:
    def __init__(self):
        # Load a dictionary of common English words + cooking terms
        self.word_dict = self._build_word_dictionary()

        # Comprehensive OCR error mapping
        self.ocr_replacements = {
            # Complete word fixes first (most specific)
            'onveon': 'olive oil',
            'onveen': 'olive oil',
            'Onveon': 'olive oil',
            'Onveen': 'olive oil',
            'extravirginonveon': 'extra virgin olive oil',
            'greekyogurt': 'greek yogurt',
            'greekyoghurt': 'greek yogurt',
            'Tomatovinaigrette': 'Tomato vinaigrette',
            'tomatovinaigrette': 'tomato vinaigrette',
            'Preheatovento': 'Preheat oven to',
            'preheatovento': 'preheat oven to',

            # Ingredient patterns
            'Ycupdicedredonion': '1/2 cup diced red onion',
            'ycupdicedredonion': '1/2 cup diced red onion',
            'o.scup': '0.5 cup',
            'O.scup': '0.5 cup',
            'o.stsp': '0.5 tsp',
            'o.stbsp': '0.5 tbsp',
            'o.sounce': '0.5 ounce',
            'o.soz': '0.5 oz',

            # Measurement words
            'tabiespoons': 'tablespoons',
            'Tabiespoons': 'tablespoons',
            'tabiespoon': 'tablespoon',
            'Tabiespoon': 'tablespoon',
            'Teaspoon': 'teaspoon',
            'teaspoon': 'teaspoon',
            'Cupvegetabiestock': 'cup vegetable stock',
            'cupvegetabiestock': 'cup vegetable stock',

            # Common character substitutions (OCR errors)
            'vegetabie': 'vegetable',
            'Vegetabie': 'vegetable',
            'vegetabies': 'vegetables',
            'Vegetabies': 'vegetables',
            'biack': 'black',
            'Biack': 'black',
            'sbiack': 'black',
            'Sbiack': 'black',
            'garn': 'garlic',
            'Garn': 'garlic',
            'snced': 'sliced',
            'Snced': 'sliced',
            'Fineiy': 'finely',
            'fineiy': 'finely',
            'wen': 'well',
            'Wen': 'well',
            'untn': 'until',
            'Untn': 'until',
            'ceiery': 'celery',
            'Ceiery': 'celery',
            'feneibuib': 'fennel bulb',
            'tomatoes': 'tomatoes',
            'piumtemato': 'plum tomato',
            'Piumtemato': 'plum tomato',
            'madeirawine': 'madeira wine',
            'Madeirawine': 'madeira wine',
            'ciovesgarnc': 'cloves garlic',
            'Ciovesgarnc': 'cloves garlic',
            'eggwhites': 'egg whites',
            'Aeggwhites': '4 egg whites',
            'aeggwhites': '4 egg whites',
            'bayieaves': 'bay leaves',
            'Bayieaves': 'bay leaves',
            'sprigsthyme': 'sprigs thyme',
            'Funsprigsthyme': '4 sprigs thyme',
            'funsprigsthyme': '4 sprigs thyme',
            'peppercoms': 'peppercorns',
            'Peppercoms': 'peppercorns',
            'Sbiackpeppercoms': 'black peppercorns',
            'sbiackpeppercoms': 'black peppercorns',
            'mushrooms': 'mushrooms',
            'buttonmushrooms': 'button mushrooms',
            'Buttonmushrooms': 'button mushrooms',
            'Poundsbuttonmushrooms': 'pounds button mushrooms',
            'poundsbuttonmushrooms': 'pounds button mushrooms',
            'shntakemushrooms': 'shiitake mushrooms',
            'Shntakemushrooms': 'shiitake mushrooms',
            'driedshntakemushrooms': 'dried shiitake mushrooms',
            'parsieystems': 'parsley stems',
            'Parsieystems': 'parsley stems',
            'ouncefreshparsieystems': 'ounce fresh parsley stems',
            'Ouncefreshparsieystems': 'ounce fresh parsley stems',
            'basnieaves': 'basil leaves',
            'Basnieaves': 'basil leaves',
            'freshbasnieaves': 'fresh basil leaves',
            'Itabiespoonfreshbasnieaves': '1 tablespoon fresh basil leaves',
            'itabiespoonfreshbasnieaves': '1 tablespoon fresh basil leaves',

            # Cooking actions
            'Seededandchopped': 'seeded and chopped',
            'seededandchopped': 'seeded and chopped',
            'Fineiychopped': 'finely chopped',
            'fineiychopped': 'finely chopped',
            'Fineiysn': 'finely sli',
            'roastvegetabiesuntnwen': 'roast vegetables until well',
            'Caramenzed': 'caramelized',
            'caramenzed': 'caramelized',
            'Sautebuttonmushrooms': 'saute button mushrooms',
            'sautebuttonmushrooms': 'saute button mushrooms',
            'Degiazepanoverhighheat': 'deglaze pan over high heat',
            'degiazepanoverhighheat': 'deglaze pan over high heat',
            'Transfersautedmushrooms': 'transfer sauteed mushrooms',
            'transfersautedmushrooms': 'transfer sauteed mushrooms',
            'Transfersauted': 'transfer sauteed',
            'transfersauted': 'transfer sauteed',
            'Strainandreservestock': 'strain and reserve stock',
            'strainandreservestock': 'strain and reserve stock',
            'Strainandreserve': 'strain and reserve',
            'strainandreserve': 'strain and reserve',
            'Trainandreserve': 'strain and reserve',
            'trainandreserve': 'strain and reserve',
            'discardingmushroomsandkombu': 'discarding mushrooms and kombu',
            'Whisktogetheraningredientsinsmanbowi': 'whisk together all ingredients in small bowl',
            'whisktogetheraningredientsinsmanbowi': 'whisk together all ingredients in small bowl',
            'combineaningrecientsinbienderandpureeuntnsmooth': 'combine all ingredients in blender and puree until smooth',

            # Institution references
            'Instituteofcunaryeducation': 'Institute of Culinary Education',
            'instituteofcunaryeducation': 'institute of culinary education',
            'Nstituteofcunaryeducation': 'Institute of Culinary Education',
            'nstituteofcunaryeducation': 'institute of culinary education',
            'Courset': 'Course',
            'courset': 'course',
            'Lessonba': 'Lesson',
            'lessonba': 'lesson',
            'Spaandretreatcooking': 'spa and retreat cooking',
            'spaandretreatcooking': 'spa and retreat cooking',
        }

    def _build_word_dictionary(self) -> Set[str]:
        """Build a dictionary of valid words for segmentation."""
        # Common cooking and ingredient words
        words = {
            # Basics
            'a', 'an', 'the', 'and', 'or', 'of', 'to', 'in', 'on', 'at', 'for', 'with', 'from',

            # Measurements
            'cup', 'cups', 'tablespoon', 'tablespoons', 'tbsp', 'teaspoon', 'teaspoons', 'tsp',
            'ounce', 'ounces', 'oz', 'pound', 'pounds', 'lb', 'lbs', 'pint', 'pints', 'quart',
            'quarts', 'gallon', 'gallons', 'gram', 'grams', 'kilogram', 'kilograms', 'ml', 'liter',

            # Common ingredients
            'water', 'salt', 'pepper', 'oil', 'olive', 'vegetable', 'butter', 'flour', 'sugar',
            'eggs', 'egg', 'milk', 'cream', 'cheese', 'garlic', 'onion', 'onions', 'tomato',
            'tomatoes', 'potato', 'potatoes', 'carrot', 'carrots', 'celery', 'lemon', 'lemons',
            'lime', 'limes', 'orange', 'oranges', 'apple', 'apples', 'banana', 'bananas',
            'chicken', 'beef', 'pork', 'fish', 'salmon', 'tuna', 'shrimp', 'mushroom', 'mushrooms',
            'basil', 'parsley', 'thyme', 'rosemary', 'oregano', 'bay', 'leaves', 'cinnamon',
            'vanilla', 'extract', 'vinegar', 'wine', 'stock', 'broth', 'sauce', 'honey', 'syrup',
            'maple', 'yogurt', 'greek', 'almond', 'almonds', 'walnut', 'walnuts', 'pecan', 'pecans',

            # Actions
            'chop', 'chopped', 'slice', 'sliced', 'dice', 'diced', 'mince', 'minced', 'grate',
            'grated', 'peel', 'peeled', 'cook', 'cooked', 'bake', 'baked', 'roast', 'roasted',
            'boil', 'boiled', 'simmer', 'simmered', 'fry', 'fried', 'saute', 'sauteed', 'steam',
            'steamed', 'mix', 'mixed', 'stir', 'stirred', 'whisk', 'whisked', 'blend', 'blended',
            'combine', 'combined', 'add', 'added', 'remove', 'removed', 'heat', 'heated', 'cool',
            'cooled', 'refrigerate', 'refrigerated', 'freeze', 'frozen', 'thaw', 'thawed',

            # Descriptors
            'fresh', 'dried', 'frozen', 'canned', 'raw', 'cooked', 'large', 'medium', 'small',
            'finely', 'roughly', 'thinly', 'thickly', 'hot', 'cold', 'warm', 'room', 'temperature',
            'extra', 'virgin', 'unsalted', 'salted', 'sweetened', 'unsweetened', 'whole', 'skim',
            'low', 'fat', 'free', 'gluten', 'organic', 'wild', 'farm', 'raised',

            # Equipment
            'bowl', 'pan', 'pot', 'oven', 'stove', 'blender', 'processor', 'mixer', 'whisk',
            'spoon', 'fork', 'knife', 'plate', 'dish', 'baking', 'sheet', 'rack', 'cutting',
            'board', 'measuring', 'cup', 'spoon',

            # Other
            'recipe', 'ingredient', 'ingredients', 'instruction', 'instructions', 'serve', 'serves',
            'serving', 'servings', 'minute', 'minutes', 'hour', 'hours', 'until', 'about', 'approximately',
        }

        return words

    def fix_text(self, text: str) -> str:
        """Main function to fix text with comprehensive cleaning."""
        if not text or len(text) < 2:
            return text

        # First, apply all OCR replacements (do longest first to avoid partial matches)
        for wrong, correct in sorted(self.ocr_replacements.items(), key=lambda x: -len(x[0])):
            if wrong in text:
                text = text.replace(wrong, correct)

        # Fix common patterns with regex
        text = self._fix_patterns(text)

        # Clean up extra spaces
        text = ' '.join(text.split())

        return text.strip()

    def _fix_patterns(self, text: str) -> str:
        """Fix patterns with regex."""
        patterns = [
            # Add space between number and measurement word (but only if no space)
            (r'(\d+)(cup|cups|tbsp|tsp|oz|lb|lbs|pound|ounce)([^s]|$)', r'\1 \2\3'),

            # Fix fractions like o.s -> 0.5
            (r'\bo\.s\b', '0.5'),
            (r'\bO\.s\b', '0.5'),
            (r'\bo\.2\b', '0.25'),
            (r'\bo\.7\b', '0.75'),

            # Fix leading I -> 1 for measurements
            (r'\bI(cup|tbsp|tsp|oz|lb|pound|ounce|teaspoon|tablespoon)\b', r'1 \1'),
            (r'\bI\s+(cup|tbsp|tsp|oz|lb|pound|ounce|teaspoon|tablespoon)\b', r'1 \1'),

            # Common OCR i/l confusion at word boundaries
            (r'\biemon\b', 'lemon'),
            (r'\bIemon\b', 'lemon'),
            (r'\bnemon\b', 'lemon'),
            (r'\bNemon\b', 'lemon'),

            # Split camelCase only when safe (word boundary to word boundary)
            # This is conservative - only split obvious cases
            (r'([a-z])(And|Or|With|For|In|On|At|To|Of)([A-Z][a-z])', r'\1 \2 \3'),
        ]

        for pattern, replacement in patterns:
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

        return text

    def clean_recipe_name(self, name: str) -> str:
        """Clean and properly capitalize recipe names."""
        if not name:
            return name

        name = self.fix_text(name)

        # Title case for recipe names
        name = ' '.join(word.capitalize() for word in name.split())

        return name

    def clean_ingredient(self, ingredient_text: str) -> str:
        """Clean ingredient text."""
        if not ingredient_text:
            return ingredient_text

        text = self.fix_text(ingredient_text)

        # Remove if it's metadata or instructions
        lower_text = text.lower()
        if any(phrase in lower_text for phrase in [
            'institute of culinary',
            'lesson',
            'course',
            'combine all ingredient',
            'whisk together',
            'mix all',
        ]):
            return ''

        # Remove leading numbers and measurements (they should be in amount/unit)
        text = re.sub(r'^[\d\.\s]+(cup|cups|tbsp|tsp|oz|lb|lbs|pound|ounce|teaspoon|tablespoon)?\s*', '', text)

        # Lowercase for ingredients (unless proper noun)
        if text and not any(word in text for word in ['Greek', 'Italian', 'French', 'Spanish']):
            text = text.lower()

        return text.strip()

    def clean_instruction(self, instruction: str) -> str:
        """Clean instruction text."""
        if not instruction:
            return instruction

        text = self.fix_text(instruction)

        # Remove metadata
        lower_text = text.lower()
        if any(phrase in lower_text for phrase in [
            'institute of culinary',
            'lesson',
            'spa and retreat',
        ]):
            return ''

        # Capitalize first letter
        if text:
            text = text[0].upper() + text[1:]

        # Ensure it ends with a period if it's a complete sentence
        if text and len(text) > 10 and text[-1] not in '.!?':
            text += '.'

        return text.strip()

    def fix_recipe(self, recipe: Dict[str, Any]) -> Dict[str, Any]:
        """Fix a single recipe."""
        # Fix name
        if 'name' in recipe:
            recipe['name'] = self.clean_recipe_name(recipe['name'])

        # Fix description
        if 'description' in recipe:
            desc = self.fix_text(recipe['description'])
            if desc:
                recipe['description'] = desc[0].upper() + desc[1:]

        # Fix ingredients
        if 'ingredients' in recipe and isinstance(recipe['ingredients'], list):
            cleaned = []
            for ing in recipe['ingredients']:
                if isinstance(ing, dict) and 'name' in ing:
                    cleaned_name = self.clean_ingredient(ing['name'])
                    if cleaned_name and len(cleaned_name) >= 2:
                        ing['name'] = cleaned_name
                        cleaned.append(ing)
            recipe['ingredients'] = cleaned

        # Fix instructions
        if 'instructions' in recipe and isinstance(recipe['instructions'], list):
            cleaned = []
            for inst in recipe['instructions']:
                if isinstance(inst, str):
                    cleaned_inst = self.clean_instruction(inst)
                    if cleaned_inst and len(cleaned_inst) > 15:
                        cleaned.append(cleaned_inst)
            recipe['instructions'] = cleaned

        return recipe


def main():
    """Main function."""
    input_file = Path(__file__).parent.parent / 'cleanup_backup' / 'enhanced_extracted_recipes' / 'hybrid_hsca_recipes_database.json'
    output_file = Path(__file__).parent / 'fixed_recipes_database.json'

    print(f"Reading recipes from: {input_file}")

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixer = RecipeTextFixer()

    total = len(data.get('extracted_recipes', []))
    print(f"Found {total} recipes to fix\n")

    for i, recipe_data in enumerate(data.get('extracted_recipes', [])):
        if 'recipe' in recipe_data:
            recipe_data['recipe'] = fixer.fix_recipe(recipe_data['recipe'])

            if (i + 1) % 50 == 0:
                print(f"Fixed {i + 1}/{total} recipes...")

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    size_kb = output_file.stat().st_size / 1024

    print(f"\n✓ Fix complete!")
    print(f"✓ Successfully fixed: {total} recipes")
    print(f"✓ Saved to: {output_file}")
    print(f"✓ File size: {size_kb:.1f} KB")


if __name__ == '__main__':
    main()
