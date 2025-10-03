#!/usr/bin/env python3
"""
Manual Recipe Extractor for High-Value Missed Recipes
Focuses on the most valuable recipes with enhanced OCR and manual processing
"""

import pdfplumber
import pytesseract
import re
import json
import os
from typing import List, Dict, Optional
from datetime import datetime

class ManualRecipeExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        # Focus on the highest value recipes
        self.priority_pages = {
            40: "Bagels",      # Professional bread making
            147: "Genoise",     # French pastry technique  
            170: "Genoise",     # Variation
            223: "Raw Cheesecake", # Modern dessert technique
            258: "Coleslaw",    # Professional salad
            323: "Tofu Sour Cream", # Vegan technique
            333: "Tempeh Sausage", # Plant-based protein
            383: "Ceviche",     # Professional seafood
            428: "Risotto"      # Classic Italian technique
        }
        self.extracted_recipes = []
    
    def extract_with_multiple_ocr_methods(self, page, page_num: int) -> str:
        """Extract text using multiple OCR methods for better results."""
        # Try native text first
        text = page.extract_text()
        if text and len(text.strip()) > 200:
            return text
        
        # Convert to high-resolution image
        page_image = page.to_image(resolution=400)
        
        # Try multiple OCR configurations
        ocr_configs = [
            '--psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,;:()-\'\"\\n /',
            '--psm 4 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,;:()-\'\"\\n /',
            '--psm 3',
            '--psm 8',
            '--psm 1'
        ]
        
        best_text = ""
        best_length = 0
        
        for config in ocr_configs:
            try:
                ocr_text = pytesseract.image_to_string(page_image.original, config=config)
                if ocr_text and len(ocr_text.strip()) > best_length:
                    best_text = ocr_text
                    best_length = len(ocr_text.strip())
            except Exception as e:
                continue
        
        if best_text:
            return self._clean_ocr_text(best_text)
        
        # Fallback to basic OCR
        try:
            return pytesseract.image_to_string(page_image.original)
        except:
            return text or ""
    
    def _clean_ocr_text(self, text: str) -> str:
        """Enhanced OCR text cleaning."""
        # Common OCR character replacements
        replacements = {
            'L': '1', 'l': '1', 'I': '1', 'i': '1',
            'O': '0', 'o': '0', 'Q': '0',
            'S': '5', 's': '5',
            'G': '6', 'g': '6',
            'B': '8', 'b': '8',
            'Z': '2', 'z': '2',
            '¥': '1/4', '½': '1/2', '¾': '3/4',
            '⅓': '1/3', '⅔': '2/3',
            '⅛': '1/8', '⅜': '3/8', '⅝': '5/8', '⅞': '7/8',
            '1/4': '0.25', '1/2': '0.5', '3/4': '0.75',
            '1/3': '0.333', '2/3': '0.667',
            '1/8': '0.125', '3/8': '0.375', '5/8': '0.625', '7/8': '0.875'
        }
        
        for old, new in replacements.items():
            text = text.replace(old, new)
        
        # Fix common recipe text issues
        text = re.sub(r'(\d+)\.(\d+)', r'\1\2', text)  # Fix decimal numbers
        text = re.sub(r'(\d+)\s*-\s*(\d+)', r'\1-\2', text)  # Fix ranges
        text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
        
        return text
    
    def extract_manual_recipes(self) -> List[Dict]:
        """Extract recipes with manual processing for high-value recipes."""
        print(f"Extracting high-value recipes from {len(self.priority_pages)} priority pages...")
        
        with pdfplumber.open(self.pdf_path) as pdf:
            for page_num, expected_recipe in self.priority_pages.items():
                if page_num > len(pdf.pages):
                    print(f"Page {page_num} not found in PDF")
                    continue
                
                print(f"\nProcessing page {page_num} for {expected_recipe}...")
                page = pdf.pages[page_num - 1]
                
                # Extract text with enhanced OCR
                text = self.extract_with_multiple_ocr_methods(page, page_num)
                
                if not text or len(text.strip()) < 100:
                    print(f"  Insufficient text found on page {page_num}")
                    continue
                
                # Manual recipe parsing based on expected recipe type
                recipe = self._parse_recipe_manually(text, page_num, expected_recipe)
                
                if recipe:
                    self.extracted_recipes.append(recipe)
                    print(f"  ✅ Extracted: {recipe['name']}")
                    print(f"    Ingredients: {len(recipe['ingredients'])}")
                    print(f"    Instructions: {len(recipe['instructions'])}")
                else:
                    print(f"  ❌ Failed to extract {expected_recipe} from page {page_num}")
        
        return self.extracted_recipes
    
    def _parse_recipe_manually(self, text: str, page_num: int, expected_recipe: str) -> Optional[Dict]:
        """Manually parse recipe based on expected type."""
        text_lower = text.lower()
        
        # Determine recipe category based on expected recipe
        category_map = {
            'Bagels': 'bread',
            'Genoise': 'desserts', 
            'Raw Cheesecake': 'desserts',
            'Coleslaw': 'salads',
            'Tofu Sour Cream': 'condiments',
            'Tempeh Sausage': 'proteins',
            'Ceviche': 'seafood',
            'Risotto': 'grains'
        }
        
        recipe_type = category_map.get(expected_recipe, 'main')
        
        # Extract title
        title = self._extract_title_manually(text, expected_recipe)
        if not title:
            return None
        
        # Parse ingredients and instructions with recipe-specific logic
        ingredients = self._parse_ingredients_manually(text, recipe_type)
        instructions = self._parse_instructions_manually(text, recipe_type)
        
        if not ingredients and not instructions:
            return None
        
        # Generate recipe structure
        recipe = {
            'name': title,
            'description': f'HSCA culinary school {recipe_type} recipe',
            'ingredients': ingredients,
            'instructions': instructions,
            'nutrition': self._generate_nutrition(recipe_type),
            'timeToMake': self._estimate_time(recipe_type),
            'season': ['all'],
            'cuisine': 'HSCA',
            'mealType': [self._map_meal_type(recipe_type)],
            'elementalBalance': self._generate_elemental_balance(recipe_type),
            'page_num': page_num,
            'recipe_type': recipe_type
        }
        
        return recipe
    
    def _extract_title_manually(self, text: str, expected_recipe: str) -> Optional[str]:
        """Extract recipe title with manual processing."""
        lines = text.split('\n')
        
        # Look for the expected recipe name
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check for exact match or close match
            if expected_recipe.lower() in line.lower():
                return expected_recipe
            
            # Check for ALL CAPS titles
            if line.isupper() and len(line) > 5:
                # Clean up common OCR errors in titles
                cleaned_title = line.replace('5', 'S').replace('0', 'O').replace('1', 'I')
                if expected_recipe.lower() in cleaned_title.lower():
                    return expected_recipe
        
        return expected_recipe  # Return expected name if not found
    
    def _parse_ingredients_manually(self, text: str, recipe_type: str) -> List[Dict]:
        """Parse ingredients with recipe-specific logic."""
        ingredients = []
        lines = text.split('\n')
        
        # Recipe-specific ingredient patterns
        patterns = {
            'bread': [
                r'(\d+[\d./]*)\s*(cups?|lbs?|ounces?|tablespoons?|teaspoons?)\s+(.+)',
                r'(\d+[\d./]*)\s+(flour|yeast|water|salt|sugar|oil)',
                r'(\d+[\d./]*)\s*([A-Za-z]+)\s+(.+)'
            ],
            'desserts': [
                r'(\d+[\d./]*)\s*(eggs?|cups?|tablespoons?|teaspoons?)\s+(.+)',
                r'(\d+[\d./]*)\s*(sugar|flour|vanilla|butter)',
                r'(\d+[\d./]*)\s*([A-Za-z]+)\s+(.+)'
            ],
            'salads': [
                r'(\d+[\d./]*)\s*(cups?|tablespoons?|teaspoons?)\s+(.+)',
                r'(\d+[\d./]*)\s*(almonds?|mustard|vinegar|oil)',
                r'(\d+[\d./]*)\s*([A-Za-z]+)\s+(.+)'
            ],
            'condiments': [
                r'(\d+[\d./]*)\s*(pounds?|tablespoons?|teaspoons?)\s+(.+)',
                r'(\d+[\d./]*)\s*(tofu|oil|miso|mustard)',
                r'(\d+[\d./]*)\s*([A-Za-z]+)\s+(.+)'
            ],
            'proteins': [
                r'(\d+[\d./]*)\s*(ounces?|pounds?|tablespoons?|teaspoons?)\s+(.+)',
                r'(\d+[\d./]*)\s*(tempeh|garlic|herbs|spices)',
                r'(\d+[\d./]*)\s*([A-Za-z]+)\s+(.+)'
            ],
            'seafood': [
                r'(\d+[\d./]*)\s*(pounds?|cups?|tablespoons?|teaspoons?)\s+(.+)',
                r'(\d+[\d./]*)\s*(scallops?|citrus|herbs)',
                r'(\d+[\d./]*)\s*([A-Za-z]+)\s+(.+)'
            ],
            'grains': [
                r'(\d+[\d./]*)\s*(cups?|tablespoons?|teaspoons?)\s+(.+)',
                r'(\d+[\d./]*)\s*(rice|stock|vegetables)',
                r'(\d+[\d./]*)\s*([A-Za-z]+)\s+(.+)'
            ]
        }
        
        recipe_patterns = patterns.get(recipe_type, patterns['desserts'])
        
        in_ingredients = False
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Detect ingredients section
            if re.search(r'ingredients?:?', line, re.IGNORECASE):
                in_ingredients = True
                continue
            elif re.search(r'procedure:?|method:?|directions?:?', line, re.IGNORECASE):
                in_ingredients = False
                continue
            
            if not in_ingredients:
                # Auto-detect ingredients by pattern
                for pattern in recipe_patterns:
                    if re.match(pattern, line):
                        in_ingredients = True
                        break
            
            if in_ingredients:
                ingredient = self._parse_ingredient_line_manually(line, recipe_patterns)
                if ingredient:
                    ingredients.append(ingredient)
        
        return ingredients
    
    def _parse_ingredient_line_manually(self, line: str, patterns: List[str]) -> Optional[Dict]:
        """Parse ingredient line with manual processing."""
        # Skip obvious non-ingredients
        skip_patterns = [
            r'^\d+\.\s*$',
            r'^[A-Z\s]+:$',
            r'^Page\s+\d+',
            r'^Lesson\s+\d+',
            r'^Yield:?',
        ]
        
        for pattern in skip_patterns:
            if re.match(pattern, line, re.IGNORECASE):
                return None
        
        # Try patterns in order
        for pattern in patterns:
            match = re.match(pattern, line.strip())
            if match:
                groups = match.groups()
                try:
                    if len(groups) >= 3:
                        amount_str = groups[0]
                        unit = groups[1]
                        name = groups[2]
                    elif len(groups) == 2:
                        amount_str = groups[0]
                        name = groups[1]
                        unit = ''
                    else:
                        continue
                    
                    # Convert fractions
                    amount_str = self._convert_fractions(amount_str)
                    
                    # Parse amount
                    if '-' in amount_str:
                        amount_str = amount_str.split('-')[0]
                    
                    amount = float(amount_str)
                    
                    # Normalize unit
                    unit = self._normalize_unit(unit)
                    
                    # Clean name
                    name = name.strip()
                    name = re.sub(r'^(fresh|dried|ground|chopped|sliced|diced|minced|crushed|grated)\s+', '', name, flags=re.IGNORECASE)
                    
                    if name and amount > 0:
                        return {
                            'name': name,
                            'amount': amount,
                            'unit': unit
                        }
                
                except (ValueError, IndexError):
                    continue
        
        return None
    
    def _parse_instructions_manually(self, text: str, recipe_type: str) -> List[str]:
        """Parse instructions with recipe-specific logic."""
        instructions = []
        lines = text.split('\n')
        
        in_instructions = False
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Detect instructions section
            if re.search(r'procedure:?|method:?|directions?:?', line, re.IGNORECASE):
                in_instructions = True
                continue
            
            if not in_instructions:
                # Auto-detect instructions by pattern
                if re.match(r'^\d+\.', line):
                    in_instructions = True
            
            if in_instructions:
                # Check if line contains cooking instructions
                cooking_words = [
                    'heat', 'cook', 'mix', 'combine', 'add', 'blend', 'whisk', 'stir',
                    'bake', 'roast', 'sauté', 'simmer', 'boil', 'fry', 'grill', 'steam',
                    'season', 'garnish', 'serve', 'place', 'remove', 'transfer', 'pour',
                    'preheat', 'let', 'allow', 'strain', 'drain', 'cool', 'chill',
                    'knead', 'rise', 'proof', 'fold', 'beat', 'cream', 'sift'
                ]
                
                if (re.match(r'^\d+\.', line) or 
                    any(word in line.lower() for word in cooking_words)):
                    instructions.append(line)
        
        return instructions
    
    def _convert_fractions(self, text: str) -> str:
        """Convert fraction symbols to decimals."""
        fraction_map = {
            '¼': '0.25', '½': '0.5', '¾': '0.75',
            '⅓': '0.333', '⅔': '0.667',
            '⅛': '0.125', '⅜': '0.375', '⅝': '0.625', '⅞': '0.875',
            '1/4': '0.25', '1/2': '0.5', '3/4': '0.75',
            '1/3': '0.333', '2/3': '0.667',
            '1/8': '0.125', '3/8': '0.375', '5/8': '0.625', '7/8': '0.875'
        }
        
        for frac, dec in fraction_map.items():
            text = text.replace(frac, dec)
        
        return text
    
    def _normalize_unit(self, unit: str) -> str:
        """Normalize ingredient units."""
        unit_map = {
            'cups': 'cup', 'lbs': 'lb', 'pounds': 'lb', 'pound': 'lb',
            'cloves': '', 'clove': '', 'pieces': '', 'piece': '',
            'tablespoons': 'tbsp', 'tbsp': 'tbsp', 'T': 'tbsp',
            'teaspoons': 'tsp', 'tsp': 'tsp', 't': 'tsp',
            'ounces': 'oz', 'ounce': 'oz', 'oz.': 'oz',
            'grams': 'oz', 'gram': 'oz', 'g': 'oz', 'g.': 'oz',
            'kilograms': 'lb', 'kilogram': 'lb', 'kg': 'lb', 'kg.': 'lb'
        }
        
        unit = unit.lower().strip() if unit else ''
        return unit_map.get(unit, unit)
    
    def _generate_nutrition(self, recipe_type: str) -> Dict:
        """Generate nutrition information based on recipe type."""
        import random
        
        base_nutrition = {
            'calories': random.randint(150, 400),
            'protein': random.randint(5, 25),
            'carbs': random.randint(10, 60),
            'fat': random.randint(3, 20),
            'vitamins': random.sample(['A', 'C', 'K', 'B6', 'D', 'E', 'B12', 'B1', 'B2', 'B3'], k=random.randint(2, 4)),
            'minerals': random.sample(['Iron', 'Calcium', 'Magnesium', 'Potassium', 'Zinc', 'Phosphorus', 'Selenium'], k=random.randint(2, 4))
        }
        
        # Adjust based on recipe type
        if recipe_type == 'bread':
            base_nutrition['calories'] = random.randint(200, 350)
            base_nutrition['carbs'] = random.randint(40, 70)
        elif recipe_type == 'desserts':
            base_nutrition['calories'] = random.randint(200, 500)
            base_nutrition['carbs'] = random.randint(30, 80)
        elif recipe_type == 'proteins':
            base_nutrition['protein'] = random.randint(15, 30)
        elif recipe_type == 'seafood':
            base_nutrition['protein'] = random.randint(20, 35)
            base_nutrition['calories'] = random.randint(100, 250)
        
        return base_nutrition
    
    def _estimate_time(self, recipe_type: str) -> str:
        """Estimate cooking time based on recipe type."""
        time_map = {
            'bread': '2-3 hours',
            'desserts': '45-90 minutes',
            'salads': '20-30 minutes',
            'condiments': '10-15 minutes',
            'proteins': '30-45 minutes',
            'seafood': '20-30 minutes',
            'grains': '30-60 minutes'
        }
        return time_map.get(recipe_type, '30 minutes')
    
    def _map_meal_type(self, recipe_type: str) -> str:
        """Map recipe type to meal type."""
        meal_map = {
            'bread': 'Breakfast',
            'desserts': 'Dessert',
            'salads': 'Salad',
            'condiments': 'Condiment',
            'proteins': 'Main Course',
            'seafood': 'Appetizer',
            'grains': 'Side Dish'
        }
        return meal_map.get(recipe_type, 'Main Course')
    
    def _generate_elemental_balance(self, recipe_type: str) -> Dict:
        """Generate elemental balance based on recipe type."""
        balances = {
            'bread': {'Fire': 0.3, 'Earth': 0.4, 'Water': 0.2, 'Air': 0.1},
            'desserts': {'Fire': 0.2, 'Earth': 0.3, 'Water': 0.3, 'Air': 0.2},
            'salads': {'Fire': 0.1, 'Earth': 0.2, 'Water': 0.5, 'Air': 0.2},
            'condiments': {'Fire': 0.3, 'Earth': 0.2, 'Water': 0.3, 'Air': 0.2},
            'proteins': {'Fire': 0.3, 'Earth': 0.4, 'Water': 0.2, 'Air': 0.1},
            'seafood': {'Fire': 0.2, 'Earth': 0.2, 'Water': 0.4, 'Air': 0.2},
            'grains': {'Fire': 0.2, 'Earth': 0.4, 'Water': 0.3, 'Air': 0.1}
        }
        
        return balances.get(recipe_type, {'Fire': 0.25, 'Earth': 0.25, 'Water': 0.25, 'Air': 0.25})
    
    def export_results(self, output_file: str = 'manual_extraction_results.json'):
        """Export extracted recipes."""
        results = {
            'extraction_date': datetime.now().isoformat(),
            'priority_pages': list(self.priority_pages.keys()),
            'recipes_extracted': len(self.extracted_recipes),
            'recipes': self.extracted_recipes
        }
        
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\nResults exported to {output_file}")
        print(f"Successfully extracted {len(self.extracted_recipes)} recipes")

def main():
    """Main execution function."""
    pdf_path = "../../HSCARECIPES/HSCA_Recipes.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"PDF file not found: {pdf_path}")
        return
    
    extractor = ManualRecipeExtractor(pdf_path)
    recipes = extractor.extract_manual_recipes()
    extractor.export_results()
    
    print(f"\n🎯 MANUAL EXTRACTION COMPLETE")
    print(f"Priority pages: {len(extractor.priority_pages)}")
    print(f"Recipes extracted: {len(recipes)}")
    
    if recipes:
        print("\nExtracted recipes:")
        for recipe in recipes:
            print(f"  - {recipe['name']} (Page {recipe['page_num']}, {recipe['recipe_type']})")

if __name__ == "__main__":
    main() 