#!/usr/bin/env python3
"""
Final polish script focusing on recipe titles for maximum visibility.
Applies aggressive fixes to make titles readable.
"""

import json
import re
from pathlib import Path


class TitleFixer:
    def __init__(self):
        # Specific title fixes (most common problematic titles)
        self.title_fixes = {
            'Lem On Andmaple Flav Or Edyogurt': 'Lemon and Maple Flavored Yogurt',
            'Gluten Freepear Cardamomquickbread': 'Gluten-Free Pear Cardamom Quick Bread',
            'Peanutbuttercookies': 'Peanut Butter Cookies',
            'Chickenbreasts In Mushroomsauce': 'Chicken Breasts in Mushroom Sauce',
            'Tomatovinaigrette': 'Tomato Vinaigrette',
            'Vegetable And Tempehwraps': 'Vegetable and Tempeh Wraps',
            'Quinoaveggie Burger Patties': 'Quinoa Veggie Burger Patties',
            'Blackbean Burgers': 'Black Bean Burgers',
            'Refried Blackbeans': 'Refried Black Beans',
            'Sweetpotato Fries': 'Sweet Potato Fries',
            'Greenbean Salad': 'Green Bean Salad',
        }

        # Common word concatenations to split
        self.word_splits = {
            'peanutbutter': 'peanut butter',
            'Peanutbutter': 'Peanut Butter',
            'blackbean': 'black bean',
            'Blackbean': 'Black Bean',
            'sweetpotato': 'sweet potato',
            'Sweetpotato': 'Sweet Potato',
            'greenbean': 'green bean',
            'Greenbean': 'Green Bean',
            'chickenpeas': 'chickpeas',  # This is correct
            'garbanzobean': 'garbanzo bean',
            'Garbanzobean': 'Garbanzo Bean',
            'butternut': 'butternut',  # This is correct (butternut squash)
            'mushroom': 'mushroom',  # Correct
            'mushroomsauce': 'mushroom sauce',
            'Mushroomsauce': 'Mushroom Sauce',
            'chickenbreasts': 'chicken breasts',
            'Chickenbreasts': 'Chicken Breasts',
            'quinoa': 'quinoa',  # Correct
            'quinoaveggie': 'quinoa veggie',
            'Quinoaveggie': 'Quinoa Veggie',
            'quickbread': 'quick bread',
            'Quickbread': 'Quick Bread',
            'cardamom': 'cardamom',  # Correct
            'freepear': 'free pear',
            'Freepear': 'Free Pear',
            'tempehwraps': 'tempeh wraps',
            'Tempehwraps': 'Tempeh Wraps',
        }

    def fix_title(self, title: str) -> str:
        """Fix a recipe title."""
        if not title:
            return title

        # Check for exact matches first
        if title in self.title_fixes:
            return self.title_fixes[title]

        # Apply word splits
        for concatenated, split in self.word_splits.items():
            if concatenated in title:
                title = title.replace(concatenated, split)

        # Fix common patterns
        # Remove extra spaces
        title = re.sub(r'\s+', ' ', title)

        # Fix "And" appearing after spaces
        title = re.sub(r'\s+And\s+', ' and ', title)
        title = re.sub(r'^And\s+', 'And ', title)  # Keep at start

        # Fix weird spacing like "Lem On" -> try to detect
        # This is risky so only do obvious cases
        title = re.sub(r'\b([A-Z])([a-z]{1,2})\s+([A-Z])([a-z])', r'\1\2\3\4', title)

        # Proper title case
        words = title.split()
        fixed_words = []
        for i, word in enumerate(words):
            # Don't capitalize: and, or, in, on, at, to, for, with (unless first/last word)
            if i > 0 and i < len(words) - 1 and word.lower() in ['and', 'or', 'in', 'on', 'at', 'to', 'for', 'with', 'of']:
                fixed_words.append(word.lower())
            else:
                # Capitalize first letter
                if word:
                    fixed_words.append(word[0].upper() + word[1:].lower() if len(word) > 1 else word.upper())

        return ' '.join(fixed_words)


def main():
    """Main function."""
    input_file = Path(__file__).parent / 'transformed_recipes_clean.json'
    output_file = Path(__file__).parent / 'transformed_recipes_final.json'

    print(f"Reading from: {input_file}")

    with open(input_file, 'r', encoding='utf-8') as f:
        recipes = json.load(f)

    fixer = TitleFixer()

    print(f"Polishing {len(recipes)} recipe titles...")

    for recipe in recipes:
        if 'title' in recipe:
            original = recipe['title']
            fixed = fixer.fix_title(original)
            if original != fixed:
                print(f"  ✓ '{original}' → '{fixed}'")
            recipe['title'] = fixed

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(recipes, f, indent=2, ensure_ascii=False)

    size_kb = output_file.stat().st_size / 1024

    print(f"\n✓ Polishing complete!")
    print(f"✓ Saved to: {output_file}")
    print(f"✓ File size: {size_kb:.1f} KB")


if __name__ == '__main__':
    main()
