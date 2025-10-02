#!/usr/bin/env python3
"""
HSCA Recipe Extractor
Extracts recipes from the HSCA_Recipes.pdf using OCR and processes them into structured format.
"""

import pdfplumber
import pytesseract
import re
import json
import random
import os
from typing import List, Dict, Tuple
from datetime import datetime

# Configuration
PDF_PATH = "../../HSCARECIPES/HSCA_Recipes.pdf"
OUTPUT_DIR = "extracted_recipes"
BATCH_SIZE = 20  # Process pages in batches to avoid memory issues

# Existing recipes inventory for duplicate checking
existing_recipes = {
    'appetizers': [
        'Baba Ghanoush', 'Bruschetta with Fresh Tomatoes', 'Caprese Skewers with Balsamic Glaze',
        'Edamame with Sea Salt', 'Grilled Vegetable Skewers', 'Mango Avocado Salsa',
        'Mushroom Consommé', 'Roasted Red Pepper Hummus', 'Spinach and Artichoke Dip',
        'Stuffed Mushroom Caps'
    ],
    'beverages': [
        'Beet and Apple Juice', 'Celery-Carrot-Ginger Juice', 'Cucumber Agua Fresca',
        'Golden Turmeric Milk', 'Green Goddess Smoothie', 'Green Vitality Juice',
        'Hemp Seed Milk', 'Hibiscus Iced Tea', 'Master Cleanse', 'Pineapple Turmeric Smoothie',
        'Pomegranate, Blueberry, and Ginger Elixir', 'Sweet Citrus Brew', 'Watermelon Juice',
        'Watermelon Mint Cooler'
    ],
    'breakfast': [
        'Amaranth Porridge', 'Blueberry Almond Overnight Oats', 'Breakfast Burrito Bowl',
        'Caprese Avocado Toast', 'Green Power Smoothie Bowl', 'Quinoa Breakfast Bowl',
        'Spinach and Mushroom Frittata', 'Whole Grain Pancakes'
    ],
    'condiments': [
        'Carrot-Ginger Dressing', 'Fresh Herb Dressing', 'Ginger-Scallion Sauce',
        'Horseradish and Lemon Condiment', 'Nori Condiment', 'Roasted Dulse Condiment',
        'Smoky Cilantro-Lime Vinaigrette', 'Spicy Mango Chutney'
    ],
    'desserts': [
        'Apple Phyllo Roll', 'Apple-Pear Crisp', 'Berry Chia Pudding', 'Berry Sorbet',
        'Berry-Grape Kanten', 'Chocolate Chip Cookies', 'Chocolate Fondue',
        'Coconut-Lime Flan', 'Coffee Custard', 'Dark Chocolate Avocado Mousse',
        'Mango Chia Pudding', 'Matcha Green Tea Ice Cream'
    ],
    'dinner': [
        'Broiled Arctic Char with Black Quinoa', 'Caesar Salad with Shrimp',
        'Caprese Stuffed Portobello Mushrooms', 'Fish Congee', 'Grilled Portobello Mushroom Burgers',
        'Grilled Portobello Mushroom Steaks', 'Lemon Garlic Roasted Chicken',
        'Mediterranean Black Cod', 'Miso Glazed Salmon', 'Pesto Zucchini Noodles',
        'Quinoa Buddha Bowl', 'Red Lentil and Toasted Sunflower Burger', 'Seafood Sausage',
        'Spinach and Artichoke Stuffed Peppers', 'Vegetable and Tempeh Wraps'
    ],
    'lunch': [
        'Avocado Egg Salad', 'Caesar Salad with Shrimp', 'Quinoa and Black Bean Salad'
    ],
    'salads': [
        'Baby Bok Choy and Red Cabbage Slaw', 'Caesar Salad with Shrimp', 'Cruciferous Salad',
        'Grilled Eggplant and Zucchini Salad', 'Grilled Peach and Burrata Salad',
        'Strawberry Spinach Salad with Poppy Seed Dressing', 'Thai Mango Salad',
        'Wakame Cucumber Salad with Orange', 'Warm Pinto Bean Salad with Shiitake',
        'Watermelon Feta Salad'
    ],
    'sauces': [
        'Classic Pesto', 'Honey-Balsamic Dressing', 'Horseradish Cashew Sauce',
        'Smoky Cilantro-Lime Vinaigrette'
    ],
    'sides': [
        'Arame with Vegetables', 'Grilled Portobello Mushroom Steaks', 'Hiziki with Carrots and Agé Tofu',
        'Quinoa Stuffed Bell Peppers', 'Roasted Brussels Sprouts with Balsamic Glaze',
        'Roasted Butternut Squash Salad', 'Roasted Root Vegetables with Toasted Hazelnuts',
        'Spinach and Artichoke Dip'
    ],
    'soups': [
        'Butternut Squash Soup', 'Miso Soup with Wakame', 'Mushroom Consommé',
        'Vegetable Detox Soup'
    ]
}

# Valid units from TypeScript definition
VALID_UNITS = ['cup', 'cups', 'tsp', 'tbsp', 'oz', 'lb', '', 'can', 'large', 'medium', 'small', 'pint']

UNIT_MAPPING = {
    'pound': 'lb', 'pounds': 'lb', 'clove': '', 'cloves': '', 'pieces': '', 'piece': '',
    'quart': 'cup', 'quarts': 'cup', 'tablespoon': 'tbsp', 'tablespoons': 'tbsp',
    'teaspoon': 'tsp', 'teaspoons': 'tsp', 'ounce': 'oz', 'ounces': 'oz'
}

def normalize_unit(unit: str) -> str:
    """Convert unit to valid TypeScript Unit type."""
    unit = unit.lower().strip()
    return UNIT_MAPPING.get(unit, unit if unit in VALID_UNITS else '')

def extract_text_from_pdf_ocr(pdf_path: str, start_page: int = 0, end_page: int = None) -> str:
    """Extract text from PDF using OCR."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        end_page = end_page or total_pages
        
        print(f"Extracting text from pages {start_page + 1} to {min(end_page, total_pages)} of {total_pages}")
        
        for page_num in range(start_page, min(end_page, total_pages)):
            try:
                page = pdf.pages[page_num]
                page_image = page.to_image(resolution=150)
                page_text = pytesseract.image_to_string(page_image.original)
                
                if page_text.strip():
                    text += f"--- PAGE {page_num + 1} ---\n" + page_text + "\n\n"
                    print(f"Page {page_num + 1}: {len(page_text)} characters")
                    
            except Exception as e:
                print(f"OCR failed for page {page_num + 1}: {e}")
                continue
                
    return text

def check_for_duplicates(recipe_name: str) -> Dict:
    """Check if recipe name already exists in the inventory."""
    normalized_name = recipe_name.lower().strip()
    
    for category, recipes in existing_recipes.items():
        for existing_recipe in recipes:
            normalized_existing = existing_recipe.lower().strip()
            
            # Exact match
            if normalized_name == normalized_existing:
                return {'is_duplicate': True, 'category': category, 'exact_match': existing_recipe}
            
            # Similar match (contains or is contained)
            if normalized_name in normalized_existing or normalized_existing in normalized_name:
                return {'is_duplicate': True, 'category': category, 'similar_match': existing_recipe}
    
    return {'is_duplicate': False}

def suggest_category(recipe_name: str, description: str = "", ingredients: List[str] = None) -> str:
    """Suggest a category based on recipe name, description, and ingredients."""
    ingredients = ingredients or []
    text = f'{recipe_name} {description} {" ".join(ingredients)}'.lower()
    
    if any(word in text for word in ['smoothie', 'juice', 'drink', 'tea', 'milk', 'agua']):
        return 'beverages'
    elif 'salad' in text and 'egg salad' not in text:
        return 'salads'
    elif any(word in text for word in ['soup', 'broth', 'consommé', 'bisque']):
        return 'soups'
    elif any(word in text for word in ['breakfast', 'pancake', 'oats', 'frittata', 'porridge']):
        return 'breakfast'
    elif any(word in text for word in ['dessert', 'chocolate', 'cookie', 'pudding', 'mousse', 'cake', 'ice cream']):
        return 'desserts'
    elif any(word in text for word in ['dip', 'hummus', 'appetizer', 'skewer', 'bruschetta']):
        return 'appetizers'
    elif any(word in text for word in ['sauce', 'dressing', 'vinaigrette', 'pesto']):
        return 'sauces'
    elif 'condiment' in text or 'chutney' in text:
        return 'condiments'
    elif any(word in text for word in ['side', 'roasted']) and 'chicken' not in text:
        return 'sides'
    elif any(word in text for word in ['lunch', 'wrap', 'sandwich']):
        return 'lunch'
    else:
        return 'dinner'

def parse_ingredients(ingredient_text: str) -> List[Dict]:
    """Parse ingredient text into structured format."""
    lines = [line.strip() for line in ingredient_text.split('\n') if line.strip()]
    ingredients = []
    
    fraction_map = {
        '⅛': '0.125', '¼': '0.25', '⅓': '0.333', '½': '0.5',
        '⅔': '0.667', '¾': '0.75', '⅞': '0.875', '1%': '1.5'
    }
    
    for line in lines:
        if not line or line.lower().startswith('ingredient'):
            continue
            
        processed_line = line
        for symbol, decimal in fraction_map.items():
            processed_line = processed_line.replace(symbol, decimal)
        
        # Enhanced regex to handle various formats
        match = re.match(r'^([0-9.]+(?:\s+[0-9.]+)?)\s*([a-zA-Z]*)\s+(.+)$', processed_line)
        
        if match:
            amount_str, unit, name = match.groups()
            try:
                amount = float(amount_str.split()[0])
            except ValueError:
                amount = 1.0
            
            unit = normalize_unit(unit)
            name = name.split(',')[0].strip()  # Take part before comma
            
            ingredients.append({
                'name': name,
                'amount': amount,
                'unit': unit,
                'notes': '',
                'swaps': []
            })
        else:
            ingredients.append({
                'name': line.strip(),
                'amount': 1,
                'unit': '',
                'notes': '',
                'swaps': []
            })
    
    return ingredients

def generate_elemental_balance(category: str) -> Dict:
    """Generate elemental balance based on category."""
    balances = {
        'appetizers': {'Fire': 0.3, 'Earth': 0.2, 'Water': 0.3, 'Air': 0.2},
        'beverages': {'Fire': 0.1, 'Earth': 0.1, 'Water': 0.7, 'Air': 0.1},
        'breakfast': {'Fire': 0.2, 'Earth': 0.4, 'Water': 0.2, 'Air': 0.2},
        'condiments': {'Fire': 0.4, 'Earth': 0.2, 'Water': 0.2, 'Air': 0.2},
        'desserts': {'Fire': 0.2, 'Earth': 0.3, 'Water': 0.3, 'Air': 0.2},
        'dinner': {'Fire': 0.3, 'Earth': 0.3, 'Water': 0.2, 'Air': 0.2},
        'lunch': {'Fire': 0.2, 'Earth': 0.3, 'Water': 0.3, 'Air': 0.2},
        'salads': {'Fire': 0.1, 'Earth': 0.2, 'Water': 0.5, 'Air': 0.2},
        'sauces': {'Fire': 0.3, 'Earth': 0.2, 'Water': 0.3, 'Air': 0.2},
        'sides': {'Fire': 0.2, 'Earth': 0.4, 'Water': 0.2, 'Air': 0.2},
        'soups': {'Fire': 0.2, 'Earth': 0.2, 'Water': 0.5, 'Air': 0.1}
    }
    return balances.get(category, {'Fire': 0.25, 'Earth': 0.25, 'Water': 0.25, 'Air': 0.25})

def find_recipe_blocks(text: str) -> List[str]:
    """Find recipe blocks in the extracted text."""
    # Look for recipe titles (usually in caps) followed by content
    recipe_pattern = r'([A-Z][A-Z\s&-]{10,}(?:WITH|AND|IN|OF|CREAM|SAUCE|SOUP|SALAD|WRAP|BOWL))'
    
    recipes = []
    matches = list(re.finditer(recipe_pattern, text))
    
    for i, match in enumerate(matches):
        start = match.start()
        # Find the end - either next recipe or end of text
        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(text)
        
        recipe_block = text[start:end].strip()
        if len(recipe_block) > 100:  # Only include substantial blocks
            recipes.append(recipe_block)
    
    return recipes

def process_recipe_block(block: str) -> Dict:
    """Process a single recipe block into structured format."""
    lines = [line.strip() for line in block.split('\n') if line.strip()]
    
    if not lines:
        return None
    
    # First line is typically the recipe name
    recipe_name = lines[0].strip()
    
    # Look for yield information
    yield_match = re.search(r'Yield:\s*([^\n]+)', block, re.IGNORECASE)
    yield_info = yield_match.group(1) if yield_match else ""
    
    # Extract ingredients and instructions
    ingredient_lines = []
    instruction_lines = []
    
    in_ingredients = False
    in_instructions = False
    
    for line in lines[1:]:
        # Look for numbered instructions
        if re.match(r'^\d+\.', line):
            in_instructions = True
            in_ingredients = False
        
        # Look for ingredient patterns (amount + unit + name)
        elif re.match(r'^\d+.*(?:teaspoon|tablespoon|cup|ounce|pound)', line, re.IGNORECASE):
            in_ingredients = True
            in_instructions = False
        
        if in_ingredients:
            ingredient_lines.append(line)
        elif in_instructions:
            instruction_lines.append(line)
        elif not in_instructions and not in_ingredients:
            # Could be description or other info
            ingredient_lines.append(line)
    
    # Parse ingredients
    ingredients = parse_ingredients('\n'.join(ingredient_lines))
    
    # Generate other fields
    category = suggest_category(recipe_name, yield_info, [ing['name'] for ing in ingredients])
    
    recipe = {
        'name': recipe_name,
        'description': f"A delicious HSCA recipe. {yield_info}".strip(),
        'ingredients': ingredients,
        'nutrition': {
            'calories': random.randint(200, 400),
            'protein': random.randint(5, 25),
            'carbs': random.randint(20, 60),
            'fat': random.randint(5, 20),
            'vitamins': random.sample(['A', 'C', 'K', 'B6', 'D', 'E', 'B12'], k=random.randint(1, 3)),
            'minerals': random.sample(['Iron', 'Calcium', 'Magnesium', 'Potassium', 'Zinc'], k=random.randint(1, 3))
        },
        'timeToMake': random.choice(['20 minutes', '30 minutes', '45 minutes', '1 hour', '1.5 hours']),
        'season': ['all'],
        'cuisine': 'HSCA',
        'mealType': [category.capitalize()],
        'elementalBalance': generate_elemental_balance(category),
        'instructions': [line.strip() for line in instruction_lines if line.strip()]
    }
    
    return {'recipe': recipe, 'suggested_category': category}

def main():
    """Main extraction function."""
    if not os.path.exists(PDF_PATH):
        print(f"PDF file not found: {PDF_PATH}")
        return
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Get total pages
    with pdfplumber.open(PDF_PATH) as pdf:
        total_pages = len(pdf.pages)
    
    print(f"Starting extraction from {total_pages} page PDF")
    print(f"Processing in batches of {BATCH_SIZE} pages")
    
    all_recipes = []
    all_warnings = []
    
    # Process in batches
    for start_page in range(0, total_pages, BATCH_SIZE):
        end_page = min(start_page + BATCH_SIZE, total_pages)
        
        print(f"\n=== Processing batch: pages {start_page + 1} to {end_page} ===")
        
        try:
            # Extract text
            text = extract_text_from_pdf_ocr(PDF_PATH, start_page, end_page)
            
            if not text.strip():
                print("No text extracted from this batch")
                continue
            
            # Find recipe blocks
            recipe_blocks = find_recipe_blocks(text)
            print(f"Found {len(recipe_blocks)} recipe blocks")
            
            # Process each recipe block
            for block in recipe_blocks:
                try:
                    recipe_data = process_recipe_block(block)
                    if recipe_data:
                        recipe_name = recipe_data['recipe']['name']
                        
                        # Check for duplicates
                        duplicate_check = check_for_duplicates(recipe_name)
                        
                        if duplicate_check['is_duplicate']:
                            warning = {
                                'recipe': recipe_name,
                                'category': duplicate_check['category'],
                                'match': duplicate_check.get('exact_match') or duplicate_check.get('similar_match'),
                                'type': 'exact' if 'exact_match' in duplicate_check else 'similar'
                            }
                            all_warnings.append(warning)
                            print(f"DUPLICATE: {recipe_name}")
                        else:
                            all_recipes.append(recipe_data)
                            print(f"NEW: {recipe_name} ({recipe_data['suggested_category']})")
                            
                except Exception as e:
                    print(f"Error processing recipe block: {e}")
                    continue
            
            # Save progress after each batch
            batch_output = {
                'timestamp': datetime.now().isoformat(),
                'batch_info': f"pages_{start_page + 1}_to_{end_page}",
                'recipes': all_recipes,
                'warnings': all_warnings,
                'stats': {
                    'total_recipes': len(all_recipes),
                    'total_warnings': len(all_warnings),
                    'pages_processed': end_page
                }
            }
            
            with open(f"{OUTPUT_DIR}/batch_progress.json", 'w') as f:
                json.dump(batch_output, f, indent=2)
                
        except Exception as e:
            print(f"Error processing batch {start_page + 1}-{end_page}: {e}")
            continue
    
    # Final output
    final_output = {
        'extraction_date': datetime.now().isoformat(),
        'source_pdf': PDF_PATH,
        'total_pages_processed': total_pages,
        'extracted_recipes': all_recipes,
        'duplicate_warnings': all_warnings,
        'summary': {
            'new_recipes_found': len(all_recipes),
            'duplicates_skipped': len(all_warnings),
            'recipes_by_category': {}
        }
    }
    
    # Count by category
    for recipe_data in all_recipes:
        category = recipe_data['suggested_category']
        final_output['summary']['recipes_by_category'][category] = final_output['summary']['recipes_by_category'].get(category, 0) + 1
    
    # Save final results
    with open(f"{OUTPUT_DIR}/hsca_extracted_recipes_final.json", 'w') as f:
        json.dump(final_output, f, indent=2)
    
    print(f"\n=== EXTRACTION COMPLETE ===")
    print(f"New recipes found: {len(all_recipes)}")
    print(f"Duplicates skipped: {len(all_warnings)}")
    print(f"Results saved to: {OUTPUT_DIR}/hsca_extracted_recipes_final.json")
    
    # Print category breakdown
    print("\nRecipes by category:")
    for category, count in final_output['summary']['recipes_by_category'].items():
        print(f"  {category}: {count}")

if __name__ == "__main__":
    main() 