#!/usr/bin/env python3
"""
Recipe Validation Review - Lexical and Semantic Analysis of Pending Recipes
Determines which pending recipes can be safely incorporated into the legacy database
"""

import json
import os
import re
from typing import Dict, List, Set, Tuple
from collections import defaultdict

class RecipeValidator:
    def __init__(self):
        self.pending_file = "staging/pending_recipes/pending_2025-10-02_extraction.json"
        self.approved_file = "enhanced_extracted_recipes/character_perfect_hsca_recipes.json"
        self.pending_recipes = set()
        self.approved_recipes = set()
        self.truly_new_recipes = []

    def load_data(self):
        """Load pending and approved recipe data"""
        print("🔍 Loading recipe data for validation...")

        # Load pending recipes
        with open(self.pending_file, 'r') as f:
            pending_data = json.load(f)

        # Extract all recipe names from pending data
        for lesson_data in pending_data.get('lesson_summary', {}).values():
            for recipe_name in lesson_data.get('recipe_names', []):
                self.pending_recipes.add(recipe_name)

        print(f"✅ Loaded {len(self.pending_recipes)} pending recipes")

        # Load approved recipes
        with open(self.approved_file, 'r') as f:
            approved_data = json.load(f)

        # Extract recipe names from approved data
        for recipe in approved_data.get('extracted_recipes', []):
            recipe_obj = recipe.get('recipe', {})
            name = recipe_obj.get('name', '')
            if name:
                self.approved_recipes.add(name)

        print(f"✅ Loaded {len(self.approved_recipes)} approved recipes")

    def identify_truly_new_recipes(self):
        """Identify recipes that are truly new (not in approved baseline)"""
        # Use fuzzy matching to avoid false positives
        from difflib import SequenceMatcher

        def normalize_name(name: str) -> str:
            """Normalize recipe name for better matching"""
            # Clean OCR artifacts
            name = name.replace('0', 'o').replace('1', 'i').replace('5', 's').replace('8', 'b').replace('3', 'e')
            # Remove common words and punctuation
            name = re.sub(r'\b(the|a|and|or|with|for|in|on|of)\b', '', name, flags=re.IGNORECASE)
            name = re.sub(r'[^\w\s]', '', name)
            return ' '.join(name.split()).lower()

        approved_normalized = {name: normalize_name(name) for name in self.approved_recipes}

        for pending_name in self.pending_recipes:
            pending_norm = normalize_name(pending_name)

            # Check for exact or close matches
            is_new = True
            for approved_orig, approved_norm in approved_normalized.items():
                similarity = SequenceMatcher(None, pending_norm, approved_norm).ratio()
                if similarity > 0.85:  # Very close match
                    is_new = False
                    break

            if is_new:
                self.truly_new_recipes.append(pending_name)

        print(f"🎯 Identified {len(self.truly_new_recipes)} truly new recipes")
        return self.truly_new_recipes

    def lexical_validation(self, recipe_name: str) -> Dict:
        """Perform lexical validation on recipe name"""
        # Clean OCR artifacts for proper validation
        import sys
        sys.path.append('extraction')
        from enhanced_recipe_extractor import clean_ocr_text
        cleaned_name = clean_ocr_text(recipe_name)

        validation = {
            'original': recipe_name,
            'cleaned': cleaned_name,
            'issues': [],
            'quality_score': 0,
            'recommendation': 'review'
        }

        # Check for excessive OCR corruption
        ocr_chars = ['0', '1', '5', '8', '3']
        corruption_ratio = sum(1 for char in recipe_name if char in ocr_chars) / len(recipe_name) if recipe_name else 0

        if corruption_ratio > 0.1:  # More than 10% OCR corruption
            validation['issues'].append(f"High OCR corruption ({corruption_ratio:.1%})")
            validation['quality_score'] -= 20

        # Check for reasonable length
        if len(cleaned_name.split()) < 2:
            validation['issues'].append("Too short (less than 2 words)")
            validation['quality_score'] -= 30

        if len(cleaned_name.split()) > 8:
            validation['issues'].append("Too long (more than 8 words)")
            validation['quality_score'] -= 10

        # Check for food-related keywords
        food_keywords = [
            'soup', 'salad', 'sauce', 'chicken', 'beef', 'fish', 'pasta', 'rice', 'bread',
            'cake', 'pie', 'tart', 'mousse', 'custard', 'fondue', 'crepe', 'brownie',
            'crust', 'juice', 'smoothie', 'cucumber', 'tomato', 'mushroom', 'spinach',
            'artichoke', 'broccoli', 'cauliflower', 'zucchini', 'eggplant', 'onion',
            'garlic', 'roasted', 'grilled', 'baked', 'cream', 'chocolate', 'quinoa',
            'lentil', 'burger', 'roll', 'pudding', 'curry', 'stew', 'puree', 'pesto',
            'hummus', 'guacamole', 'salsa', 'relish', 'chutney', 'milk', 'yogurt'
        ]

        has_food_words = any(word in cleaned_name.lower() for word in food_keywords)
        if not has_food_words:
            validation['issues'].append("No recognizable food keywords")
            validation['quality_score'] -= 40

        # Check for non-recipe content
        non_recipe_indicators = ['lesson', 'institute', 'course', 'page', 'assembly']
        has_non_recipe = any(word in cleaned_name.lower() for word in non_recipe_indicators)
        if has_non_recipe:
            validation['issues'].append("Contains non-recipe content")
            validation['quality_score'] -= 50

        # Final scoring
        if validation['quality_score'] >= -10 and not validation['issues']:
            validation['recommendation'] = 'approve'
        elif validation['quality_score'] >= -30:
            validation['recommendation'] = 'review'
        else:
            validation['recommendation'] = 'reject'

        return validation

    def semantic_validation(self, recipe_name: str) -> Dict:
        """Perform semantic validation - check if recipe makes sense"""
        import sys
        sys.path.append('extraction')
        from enhanced_recipe_extractor import suggest_category, clean_ocr_text

        cleaned_name = clean_ocr_text(recipe_name)
        category = suggest_category(recipe_name)

        validation = {
            'category': category,
            'makes_sense': True,
            'issues': [],
            'confidence': 'high'
        }

        # Check for contradictory elements
        name_lower = cleaned_name.lower()

        # Beverages shouldn't have cooking methods
        if category == 'beverages':
            cooking_methods = ['roasted', 'grilled', 'baked', 'fried', 'broiled', 'sautéed']
            if any(method in name_lower for method in cooking_methods):
                validation['issues'].append("Beverage with cooking method")
                validation['makes_sense'] = False
                validation['confidence'] = 'low'

        # Check for ingredient coherence
        if 'burger' in name_lower and 'lentil' in name_lower:
            validation['issues'].append("Plant-based burger - check if intentional")
            validation['confidence'] = 'medium'

        # Check for incomplete phrases
        if name_lower.endswith(('for', 'with', 'and', 'or')):
            validation['issues'].append("Ends with conjunction - may be incomplete")
            validation['confidence'] = 'low'

        return validation

    def comprehensive_validation(self):
        """Perform comprehensive validation of truly new recipes"""
        print("\n🔬 Starting Comprehensive Recipe Validation")
        print("=" * 60)

        self.load_data()
        new_recipes = self.identify_truly_new_recipes()

        results = []
        approved = []
        rejected = []
        needs_review = []

        for recipe_name in new_recipes:
            lexical = self.lexical_validation(recipe_name)
            semantic = self.semantic_validation(recipe_name)

            result = {
                'name': recipe_name,
                'lexical': lexical,
                'semantic': semantic,
                'overall_score': lexical['quality_score'],
                'final_decision': 'review'
            }

            # Determine final decision
            if lexical['recommendation'] == 'approve' and semantic['makes_sense']:
                result['final_decision'] = 'approve'
                approved.append(result)
            elif lexical['recommendation'] == 'reject' or not semantic['makes_sense']:
                result['final_decision'] = 'reject'
                rejected.append(result)
            else:
                needs_review.append(result)

            results.append(result)

        return {
            'total_new': len(new_recipes),
            'approved': approved,
            'rejected': rejected,
            'needs_review': needs_review,
            'all_results': results
        }

    def generate_report(self, validation_results: Dict) -> str:
        """Generate comprehensive validation report"""
        report = []
        report.append("# Recipe Validation Review Report")
        report.append("=" * 50)
        report.append("")

        total = validation_results['total_new']
        approved = len(validation_results['approved'])
        rejected = len(validation_results['rejected'])
        review = len(validation_results['needs_review'])

        report.append("## Summary")
        report.append(f"- **Total new recipes**: {total}")
        report.append(f"- **Approved for inclusion**: {approved} ({approved/total*100:.1f}%)" if total > 0 else "- **Approved for inclusion**: 0")
        report.append(f"- **Rejected**: {rejected} ({rejected/total*100:.1f}%)" if total > 0 else "- **Rejected**: 0")
        report.append(f"- **Needs manual review**: {review} ({review/total*100:.1f}%)" if total > 0 else "- **Needs manual review**: 0")
        report.append("")

        if validation_results['approved']:
            report.append("## ✅ Approved Recipes")
            report.append("These recipes passed validation and can be safely added to the legacy database:")
            report.append("")
            for recipe in validation_results['approved']:
                report.append(f"### {recipe['lexical']['cleaned']}")
                report.append(f"- **Original**: {recipe['name']}")
                report.append(f"- **Category**: {recipe['semantic']['category']}")
                if recipe['semantic']['issues']:
                    report.append(f"- **Notes**: {', '.join(recipe['semantic']['issues'])}")
                report.append("")

        if validation_results['needs_review']:
            report.append("## 🤔 Needs Manual Review")
            report.append("These recipes require human review before inclusion:")
            report.append("")
            for recipe in validation_results['needs_review']:
                report.append(f"### {recipe['lexical']['cleaned']}")
                report.append(f"- **Original**: {recipe['name']}")
                report.append(f"- **Issues**: {', '.join(recipe['lexical']['issues'])}")
                if recipe['semantic']['issues']:
                    report.append(f"- **Semantic notes**: {', '.join(recipe['semantic']['issues'])}")
                report.append("")

        if validation_results['rejected']:
            report.append("## ❌ Rejected Recipes")
            report.append("These recipes failed validation and should not be included:")
            report.append("")
            for recipe in validation_results['rejected']:
                report.append(f"### {recipe['name']}")
                report.append(f"- **Issues**: {', '.join(recipe['lexical']['issues'])}")
                if recipe['semantic']['issues']:
                    report.append(f"- **Semantic issues**: {', '.join(recipe['semantic']['issues'])}")
                report.append("")

        return "\n".join(report)

def main():
    validator = RecipeValidator()
    results = validator.comprehensive_validation()
    report = validator.generate_report(results)

    # Save report
    os.makedirs("reports", exist_ok=True)
    with open("reports/recipe_validation_review.md", 'w') as f:
        f.write(report)

    print("\n📄 Validation report saved to: reports/recipe_validation_review.md")

    # Summary
    approved = len(results['approved'])
    total = results['total_new']

    print(f"\n🎯 Validation Summary:")
    print(f"   • Approved: {approved}/{total} ({approved/total*100:.1f}%)" if total > 0 else "   • Approved: 0/0")
    print(f"   • Can be safely added to legacy database: {approved} recipes")

if __name__ == "__main__":
    main()
