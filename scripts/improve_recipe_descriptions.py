#!/usr/bin/env python3
"""
Improve recipe descriptions by replacing generic placeholders with meaningful descriptions
based on recipe names, categories, and ingredients.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any


def is_generic_description(description: str) -> bool:
    """Check if description is a generic placeholder."""
    if not description:
        return True
    
    generic_patterns = [
        r'delicious.*recipe.*from.*HSCA',
        r'culinary arts program',
        r'recipe from HSCA',
        r'^A delicious \w+ recipe from',
    ]
    
    desc_lower = description.lower()
    for pattern in generic_patterns:
        if re.search(pattern, desc_lower):
            return True
    
    # Check if it's too short or generic
    if len(description) < 30:
        return True
    
    return False


def create_description(recipe_name: str, category: str, ingredients: List[Dict], existing_desc: str = '') -> str:
    """Create a meaningful description based on recipe name, category, and ingredients."""
    
    # If existing description is good, keep it
    if existing_desc and not is_generic_description(existing_desc):
        return existing_desc
    
    name_lower = recipe_name.lower()
    ingredient_names = [ing.get('name', '').lower() for ing in ingredients[:5]]
    ingredient_text = ' '.join(ingredient_names)
    
    # Create specific descriptions based on recipe name and ingredients
    if 'juice' in name_lower:
        primary_ingredients = [ing['name'] for ing in ingredients[:3] if ing.get('name')]
        if primary_ingredients:
            return f"A refreshing and nutritious juice featuring {', '.join(primary_ingredients).lower()}."
        return "A refreshing and hydrating juice packed with natural goodness."
    
    elif 'smoothie' in name_lower:
        fruits = [ing['name'] for ing in ingredients if any(fruit in ing.get('name', '').lower() 
                   for fruit in ['berry', 'banana', 'mango', 'pineapple', 'apple', 'peach'])]
        if fruits:
            return f"A creamy and energizing smoothie blend with {', '.join(fruits[:2]).lower()}."
        return "A nutrient-packed smoothie blend perfect for breakfast or snack time."
    
    elif 'salad' in name_lower:
        if 'chicken' in ingredient_text or 'shrimp' in ingredient_text or 'salmon' in ingredient_text:
            return "A protein-rich salad perfect for a satisfying and nutritious meal."
        if 'kale' in ingredient_text or 'spinach' in ingredient_text:
            return "A fresh and vibrant green salad packed with nutrients and flavor."
        return "A fresh and vibrant salad featuring seasonal ingredients and crisp textures."
    
    elif 'soup' in name_lower:
        if 'mushroom' in ingredient_text:
            return "A rich and earthy soup with deep umami flavors."
        if 'chicken' in ingredient_text:
            return "A comforting and nourishing chicken soup perfect for any season."
        if 'lentil' in ingredient_text:
            return "A hearty and protein-rich soup with warming spices."
        return "A comforting and nourishing soup perfect for any season."
    
    elif 'sauce' in name_lower or 'dressing' in name_lower or 'vinaigrette' in name_lower:
        if 'tomato' in ingredient_text:
            return "A flavorful and versatile tomato-based condiment to enhance your favorite dishes."
        return "A flavorful and versatile condiment to enhance and elevate your dishes."
    
    elif 'bread' in name_lower or 'muffin' in name_lower or 'roll' in name_lower:
        return "Freshly baked goods with wholesome ingredients and amazing flavor."
    
    elif 'cookie' in name_lower or 'brownie' in name_lower or 'cake' in name_lower:
        if 'chocolate' in ingredient_text:
            return "Rich and decadent chocolate treats made with wholesome ingredients."
        return "A sweet and satisfying treat made with quality ingredients."
    
    elif 'burger' in name_lower or 'patty' in name_lower:
        return "A protein-packed plant-based patty perfect for a satisfying meal."
    
    elif 'wrap' in name_lower or 'sandwich' in name_lower:
        return "A satisfying and portable meal packed with fresh ingredients and bold flavors."
    
    elif 'stew' in name_lower:
        return "A hearty and warming stew with deep, complex flavors."
    
    elif 'roast' in name_lower or 'roasted' in name_lower:
        return "A flavorful dish with caramelized, roasted vegetables and savory notes."
    
    elif 'curry' in name_lower or 'curried' in name_lower:
        return "A fragrant and aromatic dish with warming spices and complex flavors."
    
    elif 'cream' in name_lower and ('cashew' in ingredient_text or 'coconut' in ingredient_text):
        return "A rich and creamy plant-based alternative perfect for sauces and desserts."
    
    # Category-based descriptions
    category_map = {
        'breakfast': "A nourishing morning meal to start your day with energy and flavor.",
        'lunch': "A satisfying and balanced meal perfect for midday dining.",
        'dinner': "A delicious and hearty dish ideal for evening meals.",
        'desserts': "A sweet and satisfying treat to end any meal perfectly.",
        'beverages': "A refreshing drink packed with natural goodness and flavor.",
        'salads': "A fresh and vibrant dish featuring crisp, seasonal ingredients.",
        'soups': "A comforting and warming dish perfect for any weather.",
        'sides': "A delicious accompaniment to complement your main course.",
        'sauces': "A flavorful addition to enhance and elevate your dishes.",
        'appetizers': "A delightful starter to begin your dining experience.",
        'condiments': "A flavorful condiment to add zest and character to your meals.",
    }
    
    category_key = category.lower().rstrip('s')  # Remove plural
    if category_key in category_map:
        return category_map[category_key]
    
    # Generic fallback
    return "A delicious and nutritious dish made with quality ingredients."


def improve_descriptions(data: Dict[str, Any]) -> Dict[str, Any]:
    """Improve descriptions for all recipes."""
    recipes = data.get('extracted_recipes', [])
    improved_count = 0
    kept_count = 0
    
    for item in recipes:
        if 'recipe' not in item:
            continue
        
        recipe = item['recipe']
        existing_desc = recipe.get('description', '')
        category = item.get('category', 'dinner')
        ingredients = recipe.get('ingredients', [])
        name = recipe.get('name', '')
        
        if is_generic_description(existing_desc):
            new_desc = create_description(name, category, ingredients, existing_desc)
            recipe['description'] = new_desc
            improved_count += 1
        else:
            kept_count += 1
    
    print(f"Improved {improved_count} descriptions")
    print(f"Kept {kept_count} existing good descriptions")
    
    return data


def main():
    """Main function to improve recipe descriptions."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Input: aggressively fixed database
    input_file = script_dir / 'fixed_recipes_database_aggressive.json'
    
    # Output: descriptions improved
    output_file = script_dir / 'fixed_recipes_database_improved.json'
    
    print("✨ IMPROVING RECIPE DESCRIPTIONS")
    print("=" * 60)
    print(f"Reading from: {input_file}")
    
    if not input_file.exists():
        print(f"❌ Error: {input_file} not found!")
        print("Please run fix_recipe_spacing_aggressive.py first.")
        return
    
    # Load data
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    recipes = data.get('extracted_recipes', [])
    print(f"Found {len(recipes)} recipes\n")
    
    # Improve descriptions
    data = improve_descriptions(data)
    
    # Update metadata
    data['extraction_methodology'] = data.get('extraction_methodology', '') + ' | Descriptions improved'
    
    # Save improved database
    print(f"\n💾 Saving to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    file_size = output_file.stat().st_size / 1024
    print(f"✓ File size: {file_size:.1f} KB")
    print("\n🎉 Description improvement complete!")


if __name__ == '__main__':
    main()
