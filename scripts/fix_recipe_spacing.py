#!/usr/bin/env python3
"""
Comprehensive fix for recipe spacing and capitalization issues.
This script addresses OCR artifacts where spaces were removed between words.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any


class RecipeTextFixer:
    def __init__(self):
        # Common OCR errors to fix
        self.ocr_fixes = {
            'onveon': 'olive oil',
            'onveen': 'olive oil',
            'Onveon': 'olive oil',
            'Onveen': 'olive oil',
            'snced': 'sliced',
            'Snced': 'sliced',
            'Fineiy': 'Finely',
            'fineiy': 'finely',
            'Fineiychopped': 'Finely chopped',
            'fineiychopped': 'finely chopped',
            'Fineiysn': 'Finely sli',
            'wen': 'well',
            'untn': 'until',
            'Preheatovento': 'Preheat oven to',
            'preheatovento': 'preheat oven to',
            'Ipound': '1 pound',
            'Ounce': 'ounce',
            'ounce': 'ounce',
            'Tabiespoons': 'Tablespoons',
            'tabiespoons': 'tablespoons',
            'Tabiespoon': 'Tablespoon',
            'tabiespoon': 'tablespoon',
            'Bouquetgami': 'Bouquet garni',
            'bouquetgami': 'bouquet garni',
            'Seededandchopped': 'Seeded and chopped',
            'seededandchopped': 'seeded and chopped',
            'Chopped': 'chopped',
            'garn': 'garlic',
            'vegetabie': 'vegetable',
            'Vegetabie': 'Vegetable',
            'vegetabies': 'vegetables',
            'Vegetabies': 'Vegetables',
            'stir': 'stir',
            'Stir': 'Stir',
            'Sbiack': 'black',
            'sbiack': 'black',
            'Biack': 'Black',
            'biack': 'black',
            'gamonpot': 'gallon pot',
            'Ganonpot': 'Gallon pot',
            'Ganonpan': 'Gallon pan',
            'Ciarification': 'Clarification',
            'ciarification': 'clarification',
            'Ciarified': 'Clarified',
            'ciarified': 'clarified',
            'Trainandreserve': 'Strain and reserve',
            'trainandreserve': 'strain and reserve',
            'Strainandreserve': 'Strain and reserve',
            'strainandreserve': 'strain and reserve',
            'Transfersautedmushrooms': 'Transfer sauteed mushrooms',
            'degiazing': 'deglazing',
            'Degiazing': 'Deglazing',
            'chincisnedwithmanyiayersofcheesecioth': 'chinois lined with many layers of cheesecloth',
            'papertoweis': 'paper towels',
            'Nstituteofcunaryeducation': 'Institute of Culinary Education',
            'nstituteofcunaryeducation': 'institute of culinary education',
            'Instituteofcunaryeducation': 'Institute of Culinary Education',
            'instituteofcunaryeducation': 'institute of culinary education',
            'Lessonba': 'Lesson',
            'lessonba': 'lesson',
            'spaandretreatcooking': 'spa and retreat cooking',
            'Spaandretreatcooking': 'Spa and retreat cooking',
            'Courset': 'Course',
            'courset': 'course',
            'Ripetomatoes': 'Ripe tomatoes',
            'ripetomatoes': 'ripe tomatoes',
            'Tomatovinaigrette': 'Tomato Vinaigrette',
            'tomatovinaigrette': 'tomato vinaigrette',
            'Ycupdicedredonion': '1/2 cup diced red onion',
            'ycupdicedredonion': '1/2 cup diced red onion',
            'Cupvegetabiestock': 'Cup vegetable stock',
            'cupvegetabiestock': 'cup vegetable stock',
            'Tabiespoonsredwinevinegar': 'Tablespoons red wine vinegar',
            'tabiespoonsredwinevinegar': 'tablespoons red wine vinegar',
            'Tabiespoonsextravirginonveon': 'Tablespoons extra virgin olive oil',
            'tabiespoonsextravirginonveon': 'tablespoons extra virgin olive oil',
            'extravirginonveon': 'extra virgin olive oil',
            'Teaspoongroundbiackpepper': 'Teaspoon ground black pepper',
            'teaspoongroundbiackpepper': 'teaspoon ground black pepper',
            'Pinchofsait': 'Pinch of salt',
            'pinchofsait': 'pinch of salt',
            'Itabiespoonfreshbasnieaves': '1 tablespoon fresh basil leaves',
            'itabiespoonfreshbasnieaves': '1 tablespoon fresh basil leaves',
            'freshbasnieaves': 'fresh basil leaves',
            'basnieaves': 'basil leaves',
            'combineaningrecientsinbienderandpureeuntnsmooth': 'combine all ingredients in blender and puree until smooth',
            'o.scupgreekyogurt': '0.5 cup greek yogurt',
            'Whisktogetheraningredientsinsmanbowi': 'Whisk together all ingredients in small bowl',
            'whisktogetheraningredientsinsmanbowi': 'whisk together all ingredients in small bowl',
            'smanbowi': 'small bowl',
            'aningredients': 'all ingredients',
            'roastvegetabiesuntnwen': 'roast vegetables until well',
            'Caramenzed': 'Caramelized',
            'caramenzed': 'caramelized',
            'Toeominutes': 'to 10 minutes',
            'toeominutes': 'to 10 minutes',
            'Ini2': 'In 12',
            'ini2': 'in 12',
            'Ini': 'In',
            'ini': 'in',
            'Sautepan': 'Saute pan',
            'sautepan': 'saute pan',
            'Sautebuttonmushrooms': 'Saute button mushrooms',
            'sautebuttonmushrooms': 'saute button mushrooms',
            'Poundsbuttonmushrooms': 'Pounds button mushrooms',
            'poundsbuttonmushrooms': 'pounds button mushrooms',
            'buttonmushrooms': 'button mushrooms',
            'Degiazepanoverhighheat': 'Deglaze pan over high heat',
            'degiazepanoverhighheat': 'deglaze pan over high heat',
            'Transfersauted': 'Transfer sauteed',
            'transfersauted': 'transfer sauteed',
            'Theirdegiazingnquid': 'their deglazing liquid',
            'theirdegiazingnquid': 'their deglazing liquid',
            'Androastedvegetabiestoi': 'and roasted vegetables to 1',
            'androastedvegetabiestoi': 'and roasted vegetables to 1',
            'Addbouquetgamiandremainingstock': 'Add bouquet garni and remaining stock',
            'addbouquetgamiandremainingstock': 'add bouquet garni and remaining stock',
            'bouquetgamiandvegetabies': 'bouquet garni and vegetables',
            'discardingbouquetgamiandvegetabies': 'discarding bouquet garni and vegetables',
            'reducebrothtoabout': 'reduce broth to about',
            'Addciarificationtopot': 'Add clarification to pot',
            'addciarificationtopot': 'add clarification to pot',
            'Mixingwen': 'Mixing well',
            'mixingwen': 'mixing well',
            'Heatbrothtesimmer': 'Heat broth to simmer',
            'heatbrothtesimmer': 'heat broth to simmer',
            'Stirringoccasionany': 'Stirring occasionally',
            'stirringoccasionany': 'stirring occasionally',
            'Simmerisreached': 'Simmer is reached',
            'simmerisreached': 'simmer is reached',
            'Ceasestirring': 'Cease stirring',
            'ceasestirring': 'cease stirring',
            'Ciarificationwnirisetotop': 'Clarification will rise to top',
            'ciarificationwnirisetotop': 'clarification will rise to top',
            'Formingraft': 'Forming raft',
            'formingraft': 'forming raft',
            'Strainresuitingconsomme': 'Strain resulting consomme',
            'strainresuitingconsomme': 'strain resulting consomme',
            'Degreasesurfaceofconsommewithpapertoweis': 'Degrease surface of consomme with paper towels',
            'degreasesurfaceofconsommewithpapertoweis': 'degrease surface of consomme with paper towels',
            'Ifnecessary': 'If necessary',
            'ifnecessary': 'if necessary',
            'seasonwithsaitand': 'season with salt and',
            'ladiesoupinbowisandgamishwithchives': 'ladle soup in bowls and garnish with chives',
            'Ipoundfeneibuib': '1 pound fennel bulb',
            'ipoundfeneibuib': '1 pound fennel bulb',
            'feneibuib': 'fennel bulb',
            'o.sounceceiery': '0.5 ounce celery',
            'ceiery': 'celery',
            'Itabiespoonpius': '1 tablespoon plus',
            'itabiespoonpius': '1 tablespoon plus',
            'Iteaspoononveon': '1 teaspoon olive oil',
            'iteaspoononveon': '1 teaspoon olive oil',
            'Ipiumtemato': '1 plum tomato',
            'ipiumtemato': '1 plum tomato',
            'piumtemato': 'plum tomato',
            'Seededandchopped': 'Seeded and chopped',
            'seededandchopped': 'seeded and chopped',
            'Bciovesgarnc': '8 cloves garlic',
            'bciovesgarnc': '8 cloves garlic',
            'ciovesgarnc': 'cloves garlic',
            'Cupmadeirawine': 'Cup madeira wine',
            'cupmadeirawine': 'cup madeira wine',
            'madeirawine': 'madeira wine',
            'Aeggwhites': '4 egg whites',
            'aeggwhites': '4 egg whites',
            'eggwhites': 'egg whites',
            'Tabiespoonssonveen': 'Tablespoons olive oil',
            'tabiespoonssonveen': 'tablespoons olive oil',
            'Gamish': 'Garnish',
            'gamish': 'garnish',
            'Bouquetgami': 'Bouquet garni',
            'bouquetgami': 'bouquet garni',
            'o.souncechives': '0.5 ounce chives',
            'Fineiysnced': 'Finely sliced',
            'fineiysnced': 'finely sliced',
            'Ouncefreshparsieystems': 'Ounce fresh parsley stems',
            'ouncefreshparsieystems': 'ounce fresh parsley stems',
            'parsieystems': 'parsley stems',
            'Bayieaves': 'Bay leaves',
            'bayieaves': 'bay leaves',
            'Funsprigsthyme': '4 sprigs thyme',
            'funsprigsthyme': '4 sprigs thyme',
            'sprigsthyme': 'sprigs thyme',
            'Sbiackpeppercoms': 'Black peppercorns',
            'sbiackpeppercoms': 'black peppercorns',
            'peppercoms': 'peppercorns',
            'Porcinis': 'Porcini',
            'porcinis': 'porcini',
            'andkombuwithwaterin2': 'and kombu with water in 2',
            'kombuwithwaterin': 'kombu with water in',
            'simmerstock2o': 'simmer stock 20',
            'Minutes': 'minutes',
            'Strainandreservestock': 'Strain and reserve stock',
            'strainandreservestock': 'strain and reserve stock',
            'discardingmushroomsandkombu': 'discarding mushrooms and kombu',
            'Tessonion': 'Toss onion',
            'tessonion': 'toss onion',
            'Carrotandfeneiwithon': 'carrot and fennel with oil',
            'carrotandfeneiwithon': 'carrot and fennel with oil',
            'feneiwithon': 'fennel with oil',
            'addtomatoesandgarncforiastio': 'add tomatoes and garlic for last 10',
            'Trainandreservebroth': 'Strain and reserve broth',
            'trainandreservebroth': 'strain and reserve broth',
            'skimmingsurface': 'skimming surface',
            'driedshntakemushrooms': 'dried shiitake mushrooms',
            'shntakemushrooms': 'shiitake mushrooms',
            'sprigsparsiey': 'sprigs parsley',
            'Lemonandmaple': 'Lemon and Maple',
            'lemonandmaple': 'lemon and maple',
            'Zestof': 'Zest of',
            'zestof': 'zest of',
            'Nemon': 'lemon',
            'nemon': 'lemon',
            'Iatspmapiesyrup': '1 1/2 tsp maple syrup',
            'iatspmapiesyrup': '1 1/2 tsp maple syrup',
            'mapiesyrup': 'maple syrup',
            'Berrysorbet': 'Berry sorbet',
            'berrysorbet': 'berry sorbet',
            'Tablespoonsvodka': 'Tablespoons vodka',
            'tablespoonsvodka': 'tablespoons vodka',
            'Flavoredyogurt': 'Flavored Yogurt',
            'flavoredyogurt': 'flavored yogurt',
            'greekyogurt': 'greek yogurt',
        }

        # Common measurement abbreviations
        self.measurements = [
            'cup', 'cups', 'tbsp', 'tsp', 'oz', 'lb', 'lbs', 'pound', 'pounds',
            'ounce', 'ounces', 'teaspoon', 'teaspoons', 'tablespoon', 'tablespoons',
            'pint', 'pints', 'quart', 'quarts', 'gallon', 'gallons', 'inch', 'inches'
        ]

        # Additional word fixes
        self.word_fixes = {
            'Ipound': '1 pound',
            'Icup': '1 cup',
            'Itsp': '1 tsp',
            'Itbsp': '1 tbsp',
            'Ioz': '1 oz',
            'Ilb': '1 lb',
            'Iounce': '1 ounce',
            'Iteaspoon': '1 teaspoon',
            'Itablespoon': '1 tablespoon',
        }

    def fix_common_ocr_errors(self, text: str) -> str:
        """Fix common OCR errors first."""
        if not text:
            return text

        # Apply OCR fixes (order matters - do longest matches first)
        for wrong, correct in sorted(self.ocr_fixes.items(), key=lambda x: -len(x[0])):
            text = text.replace(wrong, correct)

        return text

    def add_spaces_to_concatenated_words(self, text: str) -> str:
        """Add spaces between concatenated words using various heuristics."""
        if not text or len(text) < 3:
            return text

        # Fix specific patterns first
        patterns = [
            # Number followed by unit
            (r'(\d+)(cup|cups|tbsp|tsp|oz|lb|lbs|pound|pounds|ounce|ounces|teaspoon|teaspoons|tablespoon|tablespoons)', r'\1 \2'),
            # Lowercase letter followed by uppercase letter (but not within abbreviations)
            (r'([a-z])([A-Z])', r'\1 \2'),
            # Number followed by uppercase letter
            (r'(\d)([A-Z][a-z])', r'\1 \2'),
            # Common cooking terms concatenated
            (r'(chop|slice|dice|mince)(d?)(fine|rough)ly', r'\1\2 \3ly'),
            # Fix concatenated measurements at start
            (r'^(\d+\.?\d*)(cup|tbsp|tsp|oz|lb|pound|ounce)', r'\1 \2'),
            # Word concatenated with "and"
            (r'([a-z])(and)([A-Z])', r'\1 \2 \3'),
            # Common word concatenations
            (r'([a-z])(of)([A-Z])', r'\1 \2 \3'),
            (r'([a-z])(to|in|on|at|for|with)([A-Z])', r'\1 \2 \3'),
        ]

        for pattern, replacement in patterns:
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

        return text

    def capitalize_sentence(self, text: str) -> str:
        """Properly capitalize sentences."""
        if not text:
            return text

        # Capitalize first letter
        text = text[0].upper() + text[1:] if len(text) > 1 else text.upper()

        # Capitalize after periods
        text = re.sub(r'\.(\s+)([a-z])', lambda m: '.' + m.group(1) + m.group(2).upper(), text)

        return text

    def clean_ingredient_name(self, name: str) -> str:
        """Clean up ingredient names."""
        if not name:
            return name

        # First apply OCR fixes
        name = self.fix_common_ocr_errors(name)

        # Apply word fixes
        for wrong, correct in self.word_fixes.items():
            name = name.replace(wrong, correct)

        # Add spaces
        name = self.add_spaces_to_concatenated_words(name)

        # Remove leading numbers that should be in amount/unit (but keep fractions in text)
        name = re.sub(r'^(\d+\.?\d*)\s+', '', name)

        # Remove weird artifacts
        if 'combine' in name.lower() and 'ingredient' in name.lower():
            return ''  # This is an instruction, not an ingredient

        if 'institute' in name.lower() and 'culinary' in name.lower():
            return ''  # This is metadata, not an ingredient

        if name.startswith('o.s ') or name.startswith('O.s '):
            return ''  # Malformed data

        if len(name) < 2:
            return ''  # Too short to be meaningful

        # Fix capitalization - ingredients should be lowercase unless proper nouns
        if name and not any(word[0].isupper() for word in name.split()[1:] if word):
            name = name.lower()

        # Clean up spacing
        name = ' '.join(name.split())

        return name.strip()

    def clean_instruction(self, instruction: str) -> str:
        """Clean up instruction text."""
        if not instruction:
            return instruction

        # First apply OCR fixes
        instruction = self.fix_common_ocr_errors(instruction)

        # Add spaces
        instruction = self.add_spaces_to_concatenated_words(instruction)

        # Remove metadata lines
        if 'institute' in instruction.lower() and 'culinary' in instruction.lower():
            return ''

        if 'lesson' in instruction.lower() and 'spa and retreat' in instruction.lower():
            return ''

        # Capitalize properly
        instruction = self.capitalize_sentence(instruction)

        # Clean up spacing
        instruction = ' '.join(instruction.split())

        return instruction.strip()

    def clean_recipe_name(self, name: str) -> str:
        """Clean up recipe names."""
        if not name:
            return name

        # Apply OCR fixes
        name = self.fix_common_ocr_errors(name)

        # Add spaces between words
        name = self.add_spaces_to_concatenated_words(name)

        # Title case
        name = ' '.join(word.capitalize() for word in name.split())

        return name.strip()

    def fix_recipe(self, recipe: Dict[str, Any]) -> Dict[str, Any]:
        """Fix a single recipe."""
        # Fix recipe name
        if 'name' in recipe:
            recipe['name'] = self.clean_recipe_name(recipe['name'])

        # Fix description
        if 'description' in recipe:
            recipe['description'] = self.capitalize_sentence(
                self.fix_common_ocr_errors(recipe['description'])
            )

        # Fix ingredients
        if 'ingredients' in recipe and isinstance(recipe['ingredients'], list):
            cleaned_ingredients = []
            for ing in recipe['ingredients']:
                if isinstance(ing, dict) and 'name' in ing:
                    cleaned_name = self.clean_ingredient_name(ing['name'])
                    if cleaned_name:  # Only keep non-empty ingredients
                        ing['name'] = cleaned_name
                        cleaned_ingredients.append(ing)
            recipe['ingredients'] = cleaned_ingredients

        # Fix instructions
        if 'instructions' in recipe and isinstance(recipe['instructions'], list):
            cleaned_instructions = []
            for inst in recipe['instructions']:
                if isinstance(inst, str):
                    cleaned_inst = self.clean_instruction(inst)
                    if cleaned_inst and len(cleaned_inst) > 10:  # Only keep meaningful instructions
                        cleaned_instructions.append(cleaned_inst)
            recipe['instructions'] = cleaned_instructions

        return recipe


def main():
    """Main function to fix recipe data."""
    input_file = Path(__file__).parent.parent / 'cleanup_backup' / 'enhanced_extracted_recipes' / 'hybrid_hsca_recipes_database.json'
    output_file = Path(__file__).parent / 'fixed_recipes_database.json'

    print(f"Reading recipes from: {input_file}")

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixer = RecipeTextFixer()

    total_recipes = len(data.get('extracted_recipes', []))
    print(f"Found {total_recipes} recipes to fix")

    fixed_count = 0

    for i, recipe_data in enumerate(data.get('extracted_recipes', [])):
        if 'recipe' in recipe_data:
            recipe_data['recipe'] = fixer.fix_recipe(recipe_data['recipe'])
            fixed_count += 1

            if (i + 1) % 50 == 0:
                print(f"Fixed {i + 1}/{total_recipes} recipes...")

    # Save fixed data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    file_size_kb = output_file.stat().st_size / 1024

    print(f"\nFix complete!")
    print(f"Successfully fixed: {fixed_count} recipes")
    print(f"Fixed recipes saved to: {output_file}")
    print(f"File size: {file_size_kb:.1f} KB")


if __name__ == '__main__':
    main()
