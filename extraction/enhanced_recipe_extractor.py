#!/usr/bin/env python3
"""
Enhanced HSCA Recipe Extractor
Specifically designed for culinary school PDF format with lesson numbers and structured layout.
"""

import pdfplumber
import pytesseract
import re
import json
import random
import os
from typing import List, Dict, Tuple, Optional
from datetime import datetime
from collections import defaultdict

# Configuration
PDF_PATH = "../../HSCARECIPES/HSCA_Recipes.pdf"
OUTPUT_DIR = "enhanced_extracted_recipes"

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

# Valid units and mapping
VALID_UNITS = ['cup', 'cups', 'tsp', 'tbsp', 'oz', 'lb', '', 'can', 'large', 'medium', 'small', 'pint']
UNIT_MAPPING = {
    'pound': 'lb', 'pounds': 'lb', 'clove': '', 'cloves': '', 'pieces': '', 'piece': '',
    'quart': 'cup', 'quarts': 'cup', 'tablespoon': 'tbsp', 'tablespoons': 'tbsp',
    'teaspoon': 'tsp', 'teaspoons': 'tsp', 'ounce': 'oz', 'ounces': 'oz'
}

# Comprehensive OCR character correction mapping
OCR_CORRECTIONS = {
    # Fraction symbols - most common OCR errors
    '¥': '1/4',  # OCR often reads ¼ as ¥
    '\\': '1/2',  # OCR often reads ½ as \\
    '§': '1/8',  # OCR misreads ⅛
    'À': '3/4',  # OCR misreads ¾
    '«': '1/3',  # OCR misreads ⅓
    '»': '2/3',  # OCR misreads ⅔
    'Â': '3/8',  # OCR misreads ⅜
    'È': '5/8',  # OCR misreads ⅝
    'Ç': '7/8',  # OCR misreads ⅞
    
    # Common number misreads
    'O': '0',    # Letter O to number 0
    'l': '1',    # Lowercase L to number 1 (context dependent)
    'I': '1',    # Capital I to number 1 (context dependent)
    'S': '5',    # S to 5 (context dependent)
    
    # Common character corruptions
    'º': 'degrees',
    '°': 'degrees',
    'â€™': "'",  # Smart quote corruption
    'â€œ': '"',  # Smart quote corruption
    'â€': '"',   # Smart quote corruption
    'Â ': ' ',   # Non-breaking space corruption
    
    # Unit corruptions
    'Ibs': 'lbs',
    'Ib': 'lb',
    'teaspoons': 'tsp',
    'tablespoons': 'tbsp',
    'TBSP': 'tbsp',
    'TSP': 'tsp',
    'CUP': 'cup',
    'CUPS': 'cups',
}

# Improved fraction mapping with decimals
FRACTION_MAP = {
    # Standard Unicode fractions
    '⅛': 0.125, '¼': 0.25, '⅓': 0.333, '½': 0.5,
    '⅔': 0.667, '¾': 0.75, '⅞': 0.875,
    '⅐': 0.143, '⅑': 0.111, '⅒': 0.1, '⅓': 0.333,
    
    # Text fractions
    '1/8': 0.125, '1/4': 0.25, '1/3': 0.333, '1/2': 0.5,
    '2/3': 0.667, '3/4': 0.75, '7/8': 0.875,
    '1/16': 0.0625, '3/16': 0.1875, '5/16': 0.3125,
    '7/16': 0.4375, '9/16': 0.5625, '11/16': 0.6875,
    '13/16': 0.8125, '15/16': 0.9375,
    
    # OCR corrupted fractions (from our analysis)
    '¥': 0.25,    # OCR reads ¼ as ¥
    '\\': 0.5,    # OCR reads ½ as \\
    '1%': 1.5,    # OCR misread of 1½
    'L': 0.5,     # Sometimes OCR reads ½ as L
    'Lounce': 1,  # OCR corruption of "1 ounce"
    'Lcup': 0.5,  # OCR corruption of "½ cup"
    'L tablespoon': 0.5,  # OCR corruption of "½ tablespoon"
    
    # Additional OCR corruption patterns
    '§': 0.125,   # OCR reads ⅛ as §
    'À': 0.75,    # OCR reads ¾ as À
    '«': 0.333,   # OCR reads ⅓ as «
    '»': 0.667,   # OCR reads ⅔ as »
    'Â': 0.375,   # OCR reads ⅜ as Â
    'È': 0.625,   # OCR reads ⅝ as È
    'Ç': 0.875,   # OCR reads ⅞ as Ç
    
    # Number sequences that should be fractions
    '1 4': 0.25, '1 2': 0.5, '3 4': 0.75,
    '1 3': 0.333, '2 3': 0.667, '1 8': 0.125,
    '3 8': 0.375, '5 8': 0.625, '7 8': 0.875,
}

class PageInfo:
    """Structure to hold page metadata and raw text"""
    def __init__(self, page_num: int, text: str):
        self.page_num = page_num
        self.text = text
        self.lesson_num = self._extract_lesson_number()
        self.course_info = self._extract_course_info()
    
    def _extract_lesson_number(self) -> Optional[int]:
        """Extract lesson number from upper right corner"""
        # Handle both \"Lesson 85\" and \"Lesson85\" formats  
        match = re.search(r'Lesson\s*(\d+)', self.text, re.IGNORECASE)
        return int(match.group(1)) if match else None
    
    def _extract_course_info(self) -> Dict[str, str]:
        """Extract course and page info from footer"""
        info = {}
        # Look for "Institute of Culinary Education - Course X YY" pattern
        course_match = re.search(r'Institute of Culinary Education\s*-\s*Course\s+(\d+)\s+(\d+)', self.text)
        if course_match:
            info['course'] = course_match.group(1)
            info['course_page'] = course_match.group(2)
        return info
    
    def _extract_recipes(self) -> List[Dict]:
        """Extract recipes from this page"""
        recipes = []
        
        # Look for recipe titles (usually in ALL CAPS)
        recipe_pattern = r'^([A-Z][A-Z\s&\-()]{10,})$'
        lines = self.text.split('\n')
        
        current_recipe = None
        in_ingredients = False
        in_procedure = False
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Check if this is a recipe title
            if re.match(recipe_pattern, line) and 'Lesson' not in line and 'Institute' not in line:
                # Save previous recipe if exists
                if current_recipe:
                    recipes.append(current_recipe)
                
                # Start new recipe
                current_recipe = {
                    'name': line,
                    'yield': '',
                    'ingredients': [],
                    'procedure': [],
                    'lesson_num': self.lesson_num,
                    'course_info': self.course_info,
                    'page_num': self.page_num + 1
                }
                in_ingredients = False
                in_procedure = False
                continue
            
            if not current_recipe:
                continue
            
            # Look for yield information
            if line.startswith('Yield:'):
                current_recipe['yield'] = line.replace('Yield:', '').strip()
                in_ingredients = True  # Ingredients typically follow yield
                continue
            
            # Detect procedure section (numbered steps)
            if re.match(r'^\d+\.', line):
                in_procedure = True
                in_ingredients = False
            
            # Add to appropriate section
            if in_procedure:
                current_recipe['procedure'].append(line)
            elif in_ingredients:
                # Skip obvious non-ingredient lines
                if not any(skip_word in line.lower() for skip_word in ['lesson', 'institute', 'course', 'assembly']):
                    current_recipe['ingredients'].append(line)
        
        # Don't forget the last recipe
        if current_recipe:
            recipes.append(current_recipe)
        
        return recipes

def extract_page_with_ocr(pdf_path: str, page_num: int) -> PageInfo:
    """Extract text from a single page using OCR with improved settings"""
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_num]
        # Try higher resolution for better OCR accuracy
        page_image = page.to_image(resolution=200)
        # Use better OCR configuration
        custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,/:;()\- '
        page_text = pytesseract.image_to_string(page_image.original, config=custom_config)
        
        # Try to reconstruct line breaks by detecting sentence patterns
        structured_text = reconstruct_text_structure(page_text)
        
        # Clean OCR artifacts immediately
        cleaned_text = clean_ocr_text(structured_text)
        return PageInfo(page_num, cleaned_text)

def reconstruct_text_structure(text: str) -> str:
    """Reconstruct text structure from OCR output that may have lost line breaks"""
    if not text:
        return text
    
    # Insert line breaks at logical points
    structured = text
    
    # Break at lesson numbers
    structured = re.sub(r'(Lesson\d+)', r'\n\1', structured)
    
    # Break at recipe titles (ALL CAPS sequences)
    structured = re.sub(r'([a-z])([A-Z][A-Z][A-Z][A-Z][A-Z]+)', r'\1\n\2', structured)
    
    # Break at yield statements
    structured = re.sub(r'([a-z])(Yield)', r'\1\n\2', structured)
    structured = re.sub(r'([a-z])(Yie1d)', r'\1\n\2', structured)
    
    # Break at numbered instructions
    structured = re.sub(r'([a-z])(\d+\.)([A-Z])', r'\1\n\2\3', structured)
    
    # Break at Institute footer
    structured = re.sub(r'([a-z])(Institute)', r'\1\n\2', structured)
    structured = re.sub(r'([a-z])(1nstitute)', r'\1\n\2', structured)
    
    # Break at course information
    structured = re.sub(r'([a-z])(Course)', r'\1\n\2', structured)
    
    # Break at measurement patterns (likely ingredients)
    structured = re.sub(r'([a-z])(\d+[a-zA-Z]+)', r'\1\n\2', structured)
    
    # Clean up multiple newlines
    structured = re.sub(r'\n+', '\n', structured)
    
    return structured.strip()

def clean_ocr_text(text: str) -> str:
    """Clean OCR artifacts and character corruptions from text"""
    if not text:
        return text
    
    cleaned = text
    
    # Apply OCR corrections
    for corrupt, correct in OCR_CORRECTIONS.items():
        cleaned = cleaned.replace(corrupt, correct)
    
    # Fix common OCR number/letter confusions in context
    # Only fix l->1 and I->1 when they're clearly errors
    cleaned = re.sub(r'\bf1our\b', 'flour', cleaned, flags=re.IGNORECASE)  # "f1our" -> "flour"
    cleaned = re.sub(r'\bsa1t\b', 'salt', cleaned, flags=re.IGNORECASE)    # "sa1t" -> "salt"
    cleaned = re.sub(r'\boi1\b', 'oil', cleaned, flags=re.IGNORECASE)      # "oi1" -> "oil"
    
    # Additional OCR corrections for common cooking terms
    cleaned = re.sub(r'\bju1ce\b', 'juice', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bsm00th1e\b', 'smoothie', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bsa1ad\b', 'salad', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bch1cken\b', 'chicken', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bqu1n0a\b', 'quinoa', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bcrepe5\b', 'crepes', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bbr0wn1e5\b', 'brownies', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bcru5t\b', 'crust', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bw1th\b', 'with', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bdr3ss1ng\b', 'dressing', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bst1rfry\b', 'stirfry', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bbech4mel\b', 'bechamel', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bwaterme10n\b', 'watermelon', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bYie1d\b', 'Yield', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bapproximate1y\b', 'approximately', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bservings?\b', 'servings', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\btab1espoons?\b', 'tablespoons', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bteaspoons?\b', 'teaspoons', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bminc3d\b', 'minced', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bchapp3d\b', 'chopped', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bslic3d\b', 'sliced', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bgrat3d\b', 'grated', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bfr3sh\b', 'fresh', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\borganicr?\b', 'organic', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bseed1ess\b', 'seedless', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bunb1eached\b', 'unbleached', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bwho1e\b', 'whole', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bwh3at\b', 'wheat', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bcocon[u0]t\b', 'coconut', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\balmonds?\b', 'almonds', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bsha11ot\b', 'shallot', cleaned, flags=re.IGNORECASE)
    
    # Fix common measurement corruptions
    cleaned = re.sub(r'\bLcup\b', '1/2 cup', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bLteaspoon\b', '1/2 teaspoon', cleaned, flags=re.IGNORECASE) 
    cleaned = re.sub(r'\bLtablespoon\b', '1/2 tablespoon', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bLounce\b', '1/2 ounce', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\bLpound\b', '1/2 pound', cleaned, flags=re.IGNORECASE)
    
    # Fix number sequences that should be fractions
    cleaned = re.sub(r'\b1 4\b', '1/4', cleaned)
    cleaned = re.sub(r'\b1 2\b', '1/2', cleaned)
    cleaned = re.sub(r'\b3 4\b', '3/4', cleaned)
    cleaned = re.sub(r'\b1 3\b', '1/3', cleaned)
    cleaned = re.sub(r'\b2 3\b', '2/3', cleaned)
    cleaned = re.sub(r'\b1 8\b', '1/8', cleaned)
    cleaned = re.sub(r'\b3 8\b', '3/8', cleaned)
    cleaned = re.sub(r'\b5 8\b', '5/8', cleaned)
    cleaned = re.sub(r'\b7 8\b', '7/8', cleaned)
    
    # Clean up whitespace but preserve newlines
    lines = cleaned.split('\n')
    cleaned_lines = []
    for line in lines:
        # Clean spaces within lines but preserve line structure
        cleaned_line = re.sub(r'\s+', ' ', line.strip())
        # Remove isolated single characters that are likely OCR artifacts
        cleaned_line = re.sub(r'\b[^a-zA-Z0-9]\b', ' ', cleaned_line)
        # Clean up multiple spaces again
        cleaned_line = re.sub(r'\s+', ' ', cleaned_line.strip())
        if cleaned_line:  # Only add non-empty lines
            cleaned_lines.append(cleaned_line)
    
    cleaned = '\n'.join(cleaned_lines)
    
    return cleaned

def normalize_unit(unit: str) -> str:
    """Convert unit to valid TypeScript Unit type with OCR corruption handling."""
    if not unit:
        return ''
    
    unit = unit.lower().strip()
    # Clean OCR artifacts from unit
    unit = clean_ocr_text(unit)
    
    # Additional OCR unit corrections
    unit_corrections = {
        'cup5': 'cups',
        'tab1espoon': 'tablespoon',
        'tab1espoons': 'tablespoons',
        'teaspoon5': 'teaspoons',
        'pound5': 'pounds',
        'ounce5': 'ounces',
        'cupo': 'cup',
        'cupso': 'cups',
        'tsp5': 'tsp',
        'tbsp5': 'tbsp',
        'lb5': 'lbs',
        'oz5': 'oz'
    }
    
    unit = unit_corrections.get(unit, unit)
    
    return UNIT_MAPPING.get(unit, unit if unit in VALID_UNITS else '')

def parse_fraction_to_decimal(fraction_str: str) -> float:
    """Convert fraction string to decimal with OCR corruption handling"""
    if not fraction_str:
        return 1.0
    
    # Clean the fraction string first
    cleaned = clean_ocr_text(fraction_str)
    
    # Check our comprehensive fraction mapping first
    if cleaned in FRACTION_MAP:
        return FRACTION_MAP[cleaned]
    
    try:
        # Handle mixed numbers like "1 1/2"
        if ' ' in cleaned and '/' in cleaned:
            parts = cleaned.split(' ')
            whole = float(parts[0])
            frac_part = parts[1]
            if '/' in frac_part:
                num, den = frac_part.split('/')
                return whole + (float(num) / float(den))
        
        # Handle simple fractions like "1/2"
        if '/' in cleaned:
            num, den = cleaned.split('/')
            return float(num) / float(den)
        
        # Handle decimals
        return float(cleaned)
    except (ValueError, ZeroDivisionError):
        return 1.0

def is_yield_statement(line: str) -> bool:
    """Check if line is a yield statement (not an ingredient)"""
    line_lower = line.lower().strip()
    yield_patterns = [
        r'^yield:?\s*',
        r'^yie1d:?\s*',  # OCR corruption
        r'^serves?:?\s*\d+',
        r'^portions?:?\s*\d+',
        r'^makes:?\s*\d+',
        r'\d+\s*(servings?|portions?|pieces?)\s*$',
        r'^\d+\s*-?\s*ounce\s+portions?',
        r'^six\s+\d+\s*-?\s*ounce\s+portions?',
        r'^approximately?\s*\d+',
        r'^approximate1y\s*\d+',  # OCR corruption
        r'\d+\s*(quarts?|cups?|servings?)\s*$',
        r'^\d+\s*(brownies?|crepes?|portions?)\s*$',
        r'^one\s+\d+\s*inch\s+crust',
        r'^0ne\s+\d+\s*inch\s+crust'  # OCR corruption
    ]
    
    return any(re.search(pattern, line_lower) for pattern in yield_patterns)

def is_valid_ingredient_line(line: str) -> bool:
    """Check if line is a valid ingredient (not metadata)"""
    line_lower = line.lower().strip()
    
    # Skip empty lines
    if not line_lower:
        return False
    
    # Skip yield statements
    if is_yield_statement(line):
        return False
    
    # Skip obvious non-ingredients
    skip_patterns = [
        r'^lesson\s+\d+',
        r'^institute\s+of\s+culinary',
        r'^course\s+\d+',
        r'^page\s+\d+',
        r'^assembly:?',
        r'^procedure:?',
        r'^method:?',
        r'^directions:?',
        r'^preparation:?',
        r'^\d+\.\s+',  # Numbered instructions
        r'^\d+\s+[A-Z]',  # Numbered instructions without periods
        r'^\([A-Z\d\s]+\)$',  # Seasonal indicators like "(SPRING SUMMER)"
        r'^\([a-z\d\s]+\)$',  # Seasonal indicators like "(spring summer)"
        r'^\([A-Z0-9\s]+\)$',  # Seasonal indicators like "(5PR1NG 5UMMER)"
        r'^[A-Z]+:?\s*$',  # Section headers like "GLAZE:" or "STIRFRY:"
        r'^[A-Z0-9]+:?\s*$',  # Section headers like "G1AZE:" or "5T1RFRY:"
        r'^vegan\s*$',  # Single word descriptors
        r'^vegetarian\s*$',  # Single word descriptors
        r'^gluten.free\s*$',  # Single word descriptors
        r'^dairy.free\s*$',  # Single word descriptors
    ]
    
    if any(re.search(pattern, line_lower) for pattern in skip_patterns):
        return False
    
    # Must have some length
    if len(line.strip()) < 3:
        return False
    
    return True

def parse_ingredient_line(line: str) -> Dict:
    """Parse a single ingredient line into structured format with improved accuracy"""
    if not is_valid_ingredient_line(line):
        return None
    
    # Clean OCR artifacts first
    cleaned_line = clean_ocr_text(line)
    
    # Convert fractions to decimals using our comprehensive mapping
    processed_line = cleaned_line
    for symbol, decimal in FRACTION_MAP.items():
        processed_line = processed_line.replace(symbol, str(decimal))
    
    # Enhanced regex patterns to handle various ingredient formats including OCR corruption
    patterns = [
        # "2 cups flour" or "2 cup flour" (with OCR fixes)
        r'^([0-9.]+(?:\s+[0-9.]+)?(?:/[0-9.]+)?)\s+([a-zA-Z10]+)\s+(.+)$',
        # "1/2 cup flour" or "1 1/2 cups flour" (with OCR fixes)
        r'^([0-9./]+(?:\s+[0-9./]+)?)\s+([a-zA-Z10]+)\s+(.+)$',
        # "2-3 cups flour" (ranges)
        r'^([0-9.]+)\s*[-–]\s*([0-9.]+)\s+([a-zA-Z10]+)\s+(.+)$',
        # "L cup flour" (OCR corruption of 1/2)
        r'^([L\\¥])\s+([a-zA-Z10]+)\s+(.+)$',
        # "cups flour, 2" (quantity at end)
        r'^([a-zA-Z10]+)\s+([^,]+),\s*([0-9.]+(?:\.[0-9]+)?)\s*$',
        # "flour, 2 cups" (ingredient first)
        r'^([^,]+),\s*([0-9.]+(?:\.[0-9]+)?)\s+([a-zA-Z10]+)\s*$',
        # Just "flour" (no quantity) - with OCR fixes
        r'^([a-zA-Z10][^0-9]*?)\s*$'
    ]
    
    for i, pattern in enumerate(patterns):
        match = re.match(pattern, processed_line.strip())
        if match:
            groups = match.groups()
            
            if i == 0 or i == 1:  # Standard "amount unit name" format
                amount_str, unit, name = groups
                amount = parse_fraction_to_decimal(amount_str)
                unit = normalize_unit(unit)
                name = name.split(',')[0].strip()  # Take part before comma
                
            elif i == 2:  # Range format "2-3 cups flour"
                amount1, amount2, unit, name = groups
                amount = (float(amount1) + float(amount2)) / 2  # Use average
                unit = normalize_unit(unit)
                name = name.strip()
                
            elif i == 3:  # "L cup flour" (OCR corruption) format
                fraction_symbol, unit, name = groups
                amount = FRACTION_MAP.get(fraction_symbol, 0.5)  # Default to 1/2
                unit = normalize_unit(unit)
                name = name.strip()
                
            elif i == 4:  # "cups flour, 2" format
                unit, name, amount_str = groups
                amount = parse_fraction_to_decimal(amount_str)
                unit = normalize_unit(unit)
                
            elif i == 5:  # "flour, 2 cups" format
                name, amount_str, unit = groups
                amount = parse_fraction_to_decimal(amount_str)
                unit = normalize_unit(unit)
                
            elif i == 6:  # Just ingredient name
                name = groups[0]
                amount = 1.0
                unit = ''
            
            # Clean up the name
            name = re.sub(r'\s+', ' ', name.strip())
            
            return {
                'name': name,
                'amount': amount,
                'unit': unit,
                'notes': '',
                'swaps': []
            }
    
    # If no pattern matches but it's a valid ingredient line, treat as ingredient name
    return {
        'name': processed_line.strip(),
        'amount': 1.0,
        'unit': '',
        'notes': '',
        'swaps': []
    }

def suggest_category(recipe_name: str, lesson_num: Optional[int] = None, yield_info: str = "", ingredients: List[str] = None) -> str:
    """Enhanced category suggestion with better food type detection"""
    # Clean OCR corruption first for better categorization
    clean_name = clean_ocr_text(recipe_name).lower()
    text = f'{clean_name} {yield_info}'.lower()
    ingredients_text = ' '.join(ingredients or []).lower()
    combined_text = f'{text} {ingredients_text}'
    
    # Enhanced beverage detection - most specific first
    beverage_indicators = [
        'juice', 'smoothie', 'drink', 'tea', 'coffee', 'milk', 'agua', 'cooler', 
        'elixir', 'brew', 'tonic', 'lemonade', 'punch', 'cocktail', 'mocktail',
        'hibiscus', 'kombucha', 'kefir', 'cleanse', 'detox', 'water'
    ]
    if any(word in combined_text for word in beverage_indicators):
        return 'beverages'
    
    # Enhanced bread/baked goods detection
    bread_indicators = [
        'bread', 'roll', 'bun', 'loaf', 'dough', 'biscuit', 'scone', 'bagel',
        'pretzel', 'focaccia', 'ciabatta', 'sourdough', 'rye', 'wheat', 'spelt'
    ]
    if any(word in combined_text for word in bread_indicators):
        return 'breakfast'  # Breads often served at breakfast
    
    # Enhanced dessert detection - check before other categories
    dessert_indicators = [
        'chocolate', 'brownie', 'cookie', 'pudding', 'mousse', 'cake', 'ice cream', 'tart', 
        'frosting', 'dessert', 'sweet', 'candy', 'fudge', 'pie', 'crisp', 'crumble',
        'cobbler', 'sorbet', 'gelato', 'custard', 'soufflé', 'truffle', 'kanten',
        'flan', 'phyllo', 'fondue'
    ]
    if any(word in combined_text for word in dessert_indicators):
        return 'desserts'
    
    # Enhanced sauce/dressing detection - very specific
    sauce_indicators = [
        'vinaigrette', 'dressing', 'sauce', 'pesto', 'marinade', 'glaze',
        'reduction', 'emulsion', 'aioli', 'mayo', 'mayonnaise', 'ketchup',
        'cream sauce', 'bechamel', 'hollandaise'
    ]
    if any(word in combined_text for word in sauce_indicators):
        return 'sauces'
    
    # Condiment detection - specific patterns
    condiment_indicators = ['condiment', 'chutney', 'relish', 'pickle', 'dulse', 'nori']
    if any(word in combined_text for word in condiment_indicators):
        return 'condiments'
    
    # Enhanced salad detection (but not egg salad, chicken salad, etc.)
    if 'salad' in combined_text:
        # Exclude protein salads that are main dishes
        protein_exclusions = ['egg', 'chicken', 'tuna', 'salmon', 'shrimp', 'crab', 'lobster']
        if not any(protein in combined_text for protein in protein_exclusions):
            return 'salads'
        else:
            return 'lunch'  # Protein salads are lunch items
    
    # Enhanced soup detection
    soup_indicators = ['soup', 'broth', 'consommé', 'bisque', 'chowder', 'stew', 'gazpacho']
    if any(word in combined_text for word in soup_indicators):
        return 'soups'
    
    # Enhanced breakfast detection
    breakfast_indicators = [
        'pancake', 'oats', 'oatmeal', 'frittata', 'porridge', 'muffin', 'cereal',
        'granola', 'toast', 'breakfast', 'morning', 'brunch', 'crepe'
    ]
    if any(word in combined_text for word in breakfast_indicators):
        return 'breakfast'
    
    # Enhanced appetizer detection
    appetizer_indicators = [
        'dip', 'hummus', 'appetizer', 'skewer', 'bruschetta', 'canapé', 
        'tartine', 'crostini', 'bite', 'small plate', 'starter', 'fondue'
    ]
    if any(word in combined_text for word in appetizer_indicators):
        return 'appetizers'
    
    # Enhanced burger/wrap detection
    if any(word in combined_text for word in ['burger', 'wrap', 'sandwich', 'panini', 'burrito']):
        return 'lunch'
    
    # Enhanced main dish detection - proteins and cooking methods
    main_dish_indicators = [
        'roasted', 'grilled', 'braised', 'seared', 'baked', 'broiled', 'glazed',
        'chicken', 'beef', 'pork', 'fish', 'salmon', 'cod', 'tuna', 'duck',
        'lamb', 'turkey', 'pasta', 'risotto', 'curry', 'stir fry', 'seitan',
        'tempeh', 'tofu', 'char', 'sausage'
    ]
    
    # Check for main proteins/cooking methods
    if any(word in combined_text for word in main_dish_indicators):
        # Exclude sauces and sides
        exclusions = ['sauce', 'dressing', 'side', 'accompaniment', 'garnish', 'condiment']
        if not any(word in combined_text for word in exclusions):
            return 'dinner'
    
    # Enhanced side dish detection
    side_indicators = [
        'side', 'roasted vegetable', 'steamed', 'sautéed', 'quinoa', 'rice',
        'beans', 'lentils', 'vegetables', 'greens', 'stuffed pepper', 'stuffed mushroom',
        'root vegetables', 'brussels sprouts', 'squash', 'arame', 'hiziki'
    ]
    if any(word in combined_text for word in side_indicators):
        return 'sides'
    
    # Lesson-based categorization with better logic
    if lesson_num:
        if lesson_num in [84, 85, 88]:  # Spa/Detox/Juice lessons
            # Only default to beverages if no other category detected
            if not any(word in combined_text for word in ['burger', 'salad', 'bread', 'sauce']):
                return 'beverages'
        elif lesson_num in [71, 72, 73]:  # Baking lessons
            # Only default to desserts if clearly baked goods
            if any(word in combined_text for word in ['bread', 'dough', 'baked', 'flour']):
                return 'desserts'
    
    # Analyze ingredients for final categorization
    if ingredients:
        ingredient_text = ' '.join(ingredients).lower()
        
        # Check for dessert ingredients
        dessert_ingredients = ['sugar', 'chocolate', 'vanilla', 'cocoa', 'flour', 'butter', 'cream']
        if sum(1 for ing in dessert_ingredients if ing in ingredient_text) >= 2:
            return 'desserts'
        
        # Check for beverage ingredients
        beverage_ingredients = ['water', 'juice', 'liquid', 'ice', 'blend']
        if sum(1 for ing in beverage_ingredients if ing in ingredient_text) >= 2:
            return 'beverages'
        
        # Check for protein main dishes
        protein_ingredients = ['chicken', 'fish', 'beef', 'pork', 'tofu', 'tempeh', 'seitan']
        if any(ing in ingredient_text for ing in protein_ingredients):
            return 'dinner'
    
    # More intelligent default based on recipe characteristics
    if yield_info:
        yield_lower = yield_info.lower()
        if any(word in yield_lower for word in ['cup', 'glass', 'serving', 'drink']):
            return 'beverages'
        elif any(word in yield_lower for word in ['loaf', 'slice', 'piece']):
            return 'desserts'
    
    # Final default - if nothing else matches, likely a main dish
    return 'dinner'

def check_for_duplicates(recipe_name: str) -> Dict:
    """Check if recipe name already exists in the inventory with OCR-aware matching."""
    # First clean the OCR corruption from the recipe name
    cleaned_name = clean_ocr_text(recipe_name)
    normalized_name = cleaned_name.lower().strip()
    
    # Remove common words that might cause false matches
    normalized_name = re.sub(r'\b(recipe|dish|meal|food|the|a|an|and|or|with|of|in|on|to|for)\b', '', normalized_name)
    normalized_name = re.sub(r'\s+', ' ', normalized_name).strip()
    
    for category, recipes in existing_recipes.items():
        for existing_recipe in recipes:
            normalized_existing = existing_recipe.lower().strip()
            normalized_existing = re.sub(r'\b(recipe|dish|meal|food|the|a|an|and|or|with|of|in|on|to|for)\b', '', normalized_existing)
            normalized_existing = re.sub(r'\s+', ' ', normalized_existing).strip()
            
            # Exact match after cleaning
            if normalized_name == normalized_existing:
                return {'is_duplicate': True, 'category': category, 'exact_match': existing_recipe}
            
            # Only consider it a duplicate if it's a very close match (80%+ similarity)
            if len(normalized_name) > 10 and len(normalized_existing) > 10:
                # Check if the core recipe name is contained (must be substantial match)
                if (normalized_name in normalized_existing or normalized_existing in normalized_name) and \
                   len(normalized_name) >= 0.8 * len(normalized_existing):
                    return {'is_duplicate': True, 'category': category, 'similar_match': existing_recipe}
    
    return {'is_duplicate': False}

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

def extract_yield_from_text(text: str) -> str:
    """Extract yield information from recipe text with OCR corruption handling"""
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if is_yield_statement(line):
            # Clean up the yield statement with OCR corrections
            yield_text = re.sub(r'^yie1d:?\s*', '', line, flags=re.IGNORECASE)
            yield_text = re.sub(r'^yield:?\s*', '', yield_text, flags=re.IGNORECASE)
            yield_text = re.sub(r'approximate1y', 'approximately', yield_text, flags=re.IGNORECASE)
            yield_text = re.sub(r'0ne', 'one', yield_text, flags=re.IGNORECASE)
            return yield_text.strip()
    return ''

def process_recipe_data(recipe_data: Dict) -> Dict:
    """Convert raw recipe data to structured format with improved parsing"""
    # Parse ingredients, filtering out yield statements and invalid lines
    ingredients = []
    ingredient_names = []
    
    for ing_line in recipe_data['ingredients']:
        if ing_line.strip():
            parsed_ing = parse_ingredient_line(ing_line)
            if parsed_ing:  # Only add if valid ingredient
                ingredients.append(parsed_ing)
                ingredient_names.append(parsed_ing['name'])
    
    # Generate category with ingredient context
    category = suggest_category(
        recipe_data['name'], 
        recipe_data.get('lesson_num'), 
        recipe_data.get('yield', ''),
        ingredient_names
    )
    
    # Create description
    description_parts = []
    if recipe_data.get('yield'):
        description_parts.append(f"Yield: {recipe_data['yield']}")
    if recipe_data.get('lesson_num'):
        description_parts.append(f"From Lesson {recipe_data['lesson_num']}")
    if recipe_data.get('course_info', {}).get('course'):
        description_parts.append(f"Course {recipe_data['course_info']['course']}")
    
    description = "A delicious HSCA recipe. " + ". ".join(description_parts)
    
    # Create structured recipe
    structured_recipe = {
        'name': recipe_data['name'],
        'description': description,
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
        'instructions': [step.strip() for step in recipe_data['procedure'] if step.strip()]
    }
    
    return {
        'recipe': structured_recipe,
        'category': category,  # Top-level category for easier access
        'lesson': recipe_data.get('lesson_num'),  # Top-level lesson for easier access
        'suggested_category': category,
        'metadata': {
            'lesson_num': recipe_data.get('lesson_num'),
            'course_info': recipe_data.get('course_info'),
            'page_nums': recipe_data.get('page_nums'),
            'yield': recipe_data.get('yield'),
            'ingredient_count': len(ingredients),
            'instruction_count': len(structured_recipe['instructions'])
        }
    }

def parse_lesson_recipes(lesson_num: int, combined_text: str, pages: List[PageInfo]) -> List[Dict]:
    """Parse recipes from concatenated lesson text with improved accuracy"""
    recipes = []
    
    # Clean the combined text first
    cleaned_text = clean_ocr_text(combined_text)
    
    # Split into lines
    lines = [line.strip() for line in cleaned_text.split('\n') if line.strip()]
    
    current_recipe = None
    in_ingredients = False
    in_procedure = False
    
    for i, line in enumerate(lines):
        # Enhanced recipe title detection with OCR corruption handling
        is_recipe_title = (
            # Enhanced pattern for OCR-corrupted ALL CAPS with numbers
            re.match(r'^[A-Z0-9][A-Z0-9\s&\-(),.]{6,}$', line) and 
            # Not lesson/course info
            'LESSON' not in line and 'INSTITUTE' not in line and 'COURSE' not in line and
            # Not yield statements
            not is_yield_statement(line) and
            # Enhanced food name detection including OCR corruptions
            (
                any(food_word in line.lower() for food_word in [
                    'soup', 'salad', 'sauce', 'chicken', 'beef', 'fish', 'pasta', 'rice', 
                    'bread', 'cake', 'juice', 'smoothie', 'roasted', 'grilled', 'baked',
                    'with', 'and', 'over', 'in', 'cream', 'chocolate', 'quinoa', 'lentil',
                    'burger', 'roll', 'pie', 'tart', 'mousse', 'custard', 'fondue',
                    'crepe', 'brownie', 'crust', 'dressing', 'stirfry', 'bechamel',
                    'watermelon', 'kasha', 'seitan', 'chickpea', 'arugula', 'frisee',
                    'glazed', 'vegan', 'dough', 'ghirardelli', 'pressed', 'nut'
                ]) or
                # OCR-corrupted food words
                any(food_word in line.lower() for food_word in [
                    'ju1ce', 'sm00th1e', 'sa1ad', 'ch1cken', 'f1sh', 'r1ce', 'bread',
                    'cak3', 'ch0c0late', 'qu1n0a', 'crepe5', 'br0wn1e5', 'cru5t',
                    'w1th', 'dr3ss1ng', 'st1rfry', 'bech4mel', 'waterme10n', 'ka5ha',
                    '5e1tan', 'ch1ckpea', 'arugu1a', 'fr15ee', 'g1azed', 'vegan',
                    'd0ugh', 'gh1rardell1', 'pre55ed', 'nut', 'carr0t5', 'rad15he5',
                    'av0cad0', 'cucumber', 'mushroom', 'sp1nach', 'art1choke',
                    'br0cc0li', 'caulifl0wer', 'z0cch1n1', 'eggp1ant', 'tomato',
                    't0mat0', 'peppe7', 'pepper5', 'on10n', 'garlick', 'gar1ic',
                    'herbs', 'her5s', 'sp1ces', 'season1ng', 'mar1nade', 'gl4ze'
                ]) or
                # Common cooking terms in OCR
                any(cooking_term in line.lower() for cooking_term in [
                    'roasted', 'grilled', 'baked', 'steamed', 'sauteed', 'braised',
                    'r0asted', 'gr1lled', 'bak3d', 'steam3d', 'saut33d', 'bra1sed',
                    'stir', 'fry', 'fried', 'boiled', 'poached', 'stuffed', 'filled',
                    'marinated', 'glazed', 'seasoned', 'spiced', 'herbed', 'crusted'
                ])
            )
        )
        
        if is_recipe_title:
            # Save previous recipe
            if current_recipe and (current_recipe['ingredients'] or current_recipe['procedure']):
                recipes.append(current_recipe)
            
            # Start new recipe
            current_recipe = {
                'name': line,
                'yield': '',
                'ingredients': [],
                'procedure': [],
                'lesson_num': lesson_num,
                'course_info': pages[0].course_info if pages else {},
                'page_nums': [p.page_num + 1 for p in pages]
            }
            in_ingredients = False
            in_procedure = False
            
            # Look ahead for yield in next few lines
            for j in range(i+1, min(i+5, len(lines))):
                if is_yield_statement(lines[j]):
                    yield_line = lines[j]
                    yield_line = re.sub(r'^yie1d:?\s*', '', yield_line, flags=re.IGNORECASE)
                    yield_line = re.sub(r'^yield:?\s*', '', yield_line, flags=re.IGNORECASE)
                    yield_line = re.sub(r'approximate1y', 'approximately', yield_line, flags=re.IGNORECASE)
                    yield_line = re.sub(r'0ne', 'one', yield_line, flags=re.IGNORECASE)
                    current_recipe['yield'] = yield_line.strip()
                    break
            
            continue
        
        if not current_recipe:
            continue
        
        # Handle yield statements
        if is_yield_statement(line):
            yield_line = line
            yield_line = re.sub(r'^yie1d:?\s*', '', yield_line, flags=re.IGNORECASE)
            yield_line = re.sub(r'^yield:?\s*', '', yield_line, flags=re.IGNORECASE)
            yield_line = re.sub(r'approximate1y', 'approximately', yield_line, flags=re.IGNORECASE)
            yield_line = re.sub(r'0ne', 'one', yield_line, flags=re.IGNORECASE)
            current_recipe['yield'] = yield_line.strip()
            in_ingredients = True  # Ingredients typically follow yield
            continue
        
        # Detect procedure section - enhanced patterns
        procedure_starters = ['procedure', 'method', 'directions', 'assembly', 'preparation']
        is_procedure_start = (
            any(line.lower().startswith(starter) for starter in procedure_starters) or
            re.match(r'^\d+\.\s+', line) or  # Numbered steps like "1. Mix flour"
            re.match(r'^\d+\s+[A-Z]', line)  # Steps without periods like "1 Mix flour"
        )
        
        if is_procedure_start:
            in_procedure = True
            in_ingredients = False
            # If it's a numbered step, add it to procedure
            if re.match(r'^\d+[\.\s]+', line):
                current_recipe['procedure'].append(line)
            continue
        
        # Detect ingredients vs procedure content
        if in_procedure:
            current_recipe['procedure'].append(line)
        elif in_ingredients or not in_procedure:
            # Enhanced ingredient detection with OCR corruption
            amount_patterns = [
                r'^\d+',  # Starts with number
                r'^\d+/\d+',  # Fraction
                r'^\d+\s+\d+/\d+',  # Mixed number
                r'^\d+\.\d+',  # Decimal
                r'^\d+\s*-\s*\d+',  # Range
                r'^[¼½¾⅓⅔⅛⅜⅝⅞]',  # Unicode fractions
                r'^[\\¥L§ÀÂÈÇ«»]',  # OCR corrupted fractions
                r'^\d+\s+\d+',  # Space-separated numbers (OCR corruption)
                r'^[L]\s*cup',  # L cup (OCR corruption of 1/2 cup)
                r'^[L]\s*teaspoon',  # L teaspoon
                r'^[L]\s*tablespoon',  # L tablespoon
                r'^[L]\s*ounce',  # L ounce
                r'^[L]\s*pound',  # L pound
            ]
            
            looks_like_ingredient = (
                any(re.match(pattern, line) for pattern in amount_patterns) or
                in_ingredients
            )
            
            if looks_like_ingredient and is_valid_ingredient_line(line):
                current_recipe['ingredients'].append(line)
            elif not in_procedure and not is_yield_statement(line):
                # Could be an unlisted ingredient or instruction
                if len(line) > 10 and not re.match(r'^\d+\.', line):
                    current_recipe['ingredients'].append(line)
    
    # Don't forget the last recipe
    if current_recipe and (current_recipe['ingredients'] or current_recipe['procedure']):
        recipes.append(current_recipe)
    
    return recipes

def main():
    """Main extraction function with enhanced processing"""
    if not os.path.exists(PDF_PATH):
        print(f"PDF file not found: {PDF_PATH}")
        return
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Get total pages
    with pdfplumber.open(PDF_PATH) as pdf:
        total_pages = len(pdf.pages)
    
    print(f"Enhanced extraction from {total_pages} page culinary school PDF")
    print("Grouping pages by lesson numbers and processing structured recipes...")
    
    # Group pages by lesson
    lessons = defaultdict(list)
    
    # Collect page info and group by lesson - FULL EXTRACTION MODE
    for page_num in range(total_pages):
        try:
            print(f"Processing page {page_num + 1}/{total_pages}", end='\r')
            page_info = extract_page_with_ocr(PDF_PATH, page_num)
            if page_info.lesson_num:
                lessons[page_info.lesson_num].append(page_info)
        except Exception as e:
            print(f"\nError processing page {page_num + 1}: {e}")
            continue
    
    # Now process each lesson
    all_recipes = []
    all_warnings = []
    
    for lesson_num, pages in lessons.items():
        if not pages:
            continue
        
        # Concatenate text from all pages in this lesson
        combined_text = '\n'.join([p.text for p in pages])
        
        # Parse recipes from combined text
        lesson_recipes = parse_lesson_recipes(lesson_num, combined_text, pages)
        
        for recipe_data in lesson_recipes:
            if len(recipe_data['name']) > 5:
                duplicate_check = check_for_duplicates(recipe_data['name'])
                
                if duplicate_check['is_duplicate']:
                    warning = {
                        'recipe': recipe_data['name'],
                        'category': duplicate_check['category'],
                        'match': duplicate_check.get('exact_match') or duplicate_check.get('similar_match'),
                        'type': 'exact' if 'exact_match' in duplicate_check else 'similar',
                        'lesson_num': lesson_num,
                        'pages': recipe_data.get('page_nums')
                    }
                    all_warnings.append(warning)
                    print(f"\nDUPLICATE: {recipe_data['name']} (Lesson {lesson_num}, Pages {recipe_data.get('page_nums')})")
                else:
                    processed_recipe = process_recipe_data(recipe_data)
                    all_recipes.append(processed_recipe)
                    print(f"\nNEW: {recipe_data['name']} ({processed_recipe['suggested_category']}) - Lesson {lesson_num}")
    
    print(f"\n\nProcessing complete!")
    print(f"Found {len(all_recipes)} valid recipes, skipped {len(all_warnings)} duplicates")
    
    # Create detailed lesson summary
    lesson_summary = {}
    total_ingredient_errors = 0
    total_categorization_checks = 0
    
    for lesson_num, pages in lessons.items():
        if not pages:
            continue
        
        combined_text = '\n'.join([p.text for p in pages])
        lesson_recipes = parse_lesson_recipes(lesson_num, combined_text, pages)
        
        # Count valid recipes
        valid_recipes = [r for r in lesson_recipes if len(r['name']) > 5 and (r['ingredients'] or r['procedure'])]
        
        lesson_summary[lesson_num] = {
            'page_count': len(pages),
            'recipes_found': len(valid_recipes),
            'recipe_names': [r['name'] for r in valid_recipes],
            'course_info': pages[0].course_info if pages else {},
            'avg_ingredients_per_recipe': sum(len(r['ingredients']) for r in valid_recipes) / max(len(valid_recipes), 1),
            'avg_instructions_per_recipe': sum(len(r['procedure']) for r in valid_recipes) / max(len(valid_recipes), 1)
        }
    
    # Final output
    final_output = {
        'extraction_date': datetime.now().isoformat(),
        'source_pdf': PDF_PATH,
        'total_pages_processed': total_pages,
        'lessons_found': len(lessons),
        'lesson_summary': lesson_summary,
        'extracted_recipes': all_recipes,
        'duplicate_warnings': all_warnings,
        'summary': {
            'new_recipes_found': len(all_recipes),
            'duplicates_skipped': len(all_warnings),
            'recipes_by_category': {},
            'recipes_by_lesson': {}
        }
    }
    
    # Count by category
    for recipe_data in all_recipes:
        category = recipe_data['suggested_category']
        final_output['summary']['recipes_by_category'][category] = final_output['summary']['recipes_by_category'].get(category, 0) + 1
    
    # Count by lesson
    for recipe_data in all_recipes:
        lesson_num = recipe_data['metadata'].get('lesson_num')
        if lesson_num:
            final_output['summary']['recipes_by_lesson'][lesson_num] = final_output['summary']['recipes_by_lesson'].get(lesson_num, 0) + 1
    
    # Save results
    with open(f"{OUTPUT_DIR}/enhanced_hsca_recipes.json", 'w') as f:
        json.dump(final_output, f, indent=2)
    
    print(f"\n=== ENHANCED EXTRACTION COMPLETE ===")
    print(f"New recipes found: {len(all_recipes)}")
    print(f"Duplicates skipped: {len(all_warnings)}")
    print(f"Lessons processed: {len(lessons)}")
    print(f"Results saved to: {OUTPUT_DIR}/enhanced_hsca_recipes.json")
    
    # Enhanced quality metrics
    ingredient_counts = [len(r['recipe']['ingredients']) for r in all_recipes]
    instruction_counts = [len(r['recipe']['instructions']) for r in all_recipes]
    
    print(f"\n=== QUALITY METRICS ===")
    print(f"Average ingredients per recipe: {sum(ingredient_counts)/len(ingredient_counts):.1f}" if ingredient_counts else "No ingredients found")
    print(f"Average instructions per recipe: {sum(instruction_counts)/len(instruction_counts):.1f}" if instruction_counts else "No instructions found")
    print(f"Recipes with >5 ingredients: {sum(1 for c in ingredient_counts if c > 5)}")
    print(f"Recipes with >5 instructions: {sum(1 for c in instruction_counts if c > 5)}")
    
    # Print summaries
    print(f"\nRecipes by category:")
    for category, count in sorted(final_output['summary']['recipes_by_category'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {category}: {count}")
    
    print(f"\nTop lessons by recipe count:")
    lesson_counts = final_output['summary']['recipes_by_lesson']
    for lesson_num, count in sorted(lesson_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  Lesson {lesson_num}: {count} recipes")
    
    # Check for potential issues
    print(f"\n=== POTENTIAL ISSUES ===")
    empty_ingredient_recipes = [r for r in all_recipes if len(r['recipe']['ingredients']) == 0]
    empty_instruction_recipes = [r for r in all_recipes if len(r['recipe']['instructions']) == 0]
    
    if empty_ingredient_recipes:
        print(f"⚠️  {len(empty_ingredient_recipes)} recipes have no ingredients")
    if empty_instruction_recipes:
        print(f"⚠️  {len(empty_instruction_recipes)} recipes have no instructions")
    
    print(f"✅ Extraction completed with improved OCR correction and parsing!")

if __name__ == "__main__":
    main() 