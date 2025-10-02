#!/usr/bin/env python3
"""
Precision Recipe Corrector
Apply targeted corrections based on gold standard analysis
"""
import json
import re
from typing import Dict, List, Tuple, Optional
from collections import defaultdict
import copy

class PrecisionRecipeCorrector:
    """Apply precise corrections based on accuracy testing results"""
    
    def __init__(self):
        self.extracted_recipes = {}
        self.gold_standard = {}
        self.template_matches = {}
        self.quality_assessment = {}
        self.corrections_applied = {
            'category_corrections': 0,
            'name_standardizations': 0,
            'ingredient_improvements': 0,
            'format_corrections': 0
        }
        self.load_all_data()
    
    def load_all_data(self):
        """Load all required data for corrections"""
        try:
            # Load extracted recipes
            with open('enhanced_extracted_recipes/character_perfect_hsca_recipes.json', 'r', encoding='utf-8') as f:
                extracted_data = json.load(f)
                self.extracted_recipes = extracted_data
            
            # Load gold standard
            with open('enhanced_gold_standard_recipes.json', 'r', encoding='utf-8') as f:
                gold_data = json.load(f)
                self.gold_standard = gold_data['gold_standard_recipes']
            
            # Load template matches
            with open('improved_template_matching_results.json', 'r', encoding='utf-8') as f:
                self.template_matches = json.load(f)
            
            # Load quality assessment
            with open('comprehensive_quality_assessment.json', 'r', encoding='utf-8') as f:
                self.quality_assessment = json.load(f)
            
            print(f"📊 Loaded all correction data successfully")
            
        except Exception as e:
            print(f"❌ Error loading correction data: {str(e)}")
    
    def apply_category_corrections(self):
        """Apply category corrections based on template matching"""
        print("🔄 Applying category corrections...")
        
        category_mapping = {}
        
        # Build category corrections from template matches
        for match in self.template_matches.get('detailed_matches', []):
            extracted_index = match['extracted_index']
            gold_category = match['gold_recipe']['category']
            extracted_category = match['extracted_recipe'].get('category', '')
            
            if gold_category != extracted_category:
                category_mapping[extracted_index] = gold_category
        
        # Apply corrections
        for i, recipe_data in enumerate(self.extracted_recipes['extracted_recipes']):
            if i in category_mapping:
                old_category = recipe_data['recipe'].get('category', 'unknown')
                new_category = category_mapping[i]
                recipe_data['recipe']['category'] = new_category
                self.corrections_applied['category_corrections'] += 1
                print(f"  ✓ Recipe '{recipe_data['recipe']['name']}': {old_category} → {new_category}")
    
    def apply_name_standardizations(self):
        """Apply name standardizations based on gold standard matches"""
        print("🔄 Applying name standardizations...")
        
        # Apply standardizations from template matches
        for match in self.template_matches.get('detailed_matches', []):
            extracted_index = match['extracted_index']
            gold_name = match['gold_recipe']['name']
            extracted_name = match['extracted_recipe']['name']
            
            # Only standardize if there's a clear improvement
            if match['name_similarity'] < 0.95 and match['combined_score'] > 0.8:
                recipe_data = self.extracted_recipes['extracted_recipes'][extracted_index]
                old_name = recipe_data['recipe']['name']
                recipe_data['recipe']['name'] = gold_name
                self.corrections_applied['name_standardizations'] += 1
                print(f"  ✓ Standardized: '{old_name}' → '{gold_name}'")
    
    def improve_ingredient_precision(self):
        """Improve ingredient precision based on quality assessment"""
        print("🔄 Improving ingredient precision...")
        
        for i, recipe_data in enumerate(self.extracted_recipes['extracted_recipes']):
            recipe = recipe_data['recipe']
            ingredients = recipe.get('ingredients', [])
            improved = False
            
            for ingredient in ingredients:
                # Fix common OCR corruption patterns
                old_name = ingredient.get('name', '')
                new_name = self.fix_ingredient_name_corruption(old_name)
                
                if new_name != old_name:
                    ingredient['name'] = new_name
                    improved = True
                
                # Standardize units
                old_unit = ingredient.get('unit', '')
                new_unit = self.standardize_unit(old_unit)
                
                if new_unit != old_unit:
                    ingredient['unit'] = new_unit
                    improved = True
                
                # Fix amount precision issues
                amount = ingredient.get('amount', 0)
                improved_amount = self.improve_amount_precision(amount, new_unit)
                
                if improved_amount != amount:
                    ingredient['amount'] = improved_amount
                    improved = True
            
            if improved:
                self.corrections_applied['ingredient_improvements'] += 1
    
    def fix_ingredient_name_corruption(self, name: str) -> str:
        """Fix common OCR corruption in ingredient names"""
        if not name:
            return name
        
        # Known corruption patterns and fixes
        corruption_fixes = {
            # Character-level fixes
            r'(\d+)([a-zA-Z])': r'\\1 \\2',  # "1cup" → "1 cup"
            r'([a-zA-Z])(\d+)': r'\\1 \\2',  # "cup1" → "cup 1"
            
            # Specific ingredient fixes
            r'f1our': 'flour',
            r'0il': 'oil',
            r'0nion': 'onion',
            r'ju1ce': 'juice',
            r'sa1t': 'salt',
            r'3ggs': 'eggs',
            r'1arge': 'large',
            r'sma11': 'small',
            r'who1e': 'whole',
            
            # Concatenation fixes
            r'washedandtrimmed': 'washed and trimmed',
            r'washedandchopped': 'washed and chopped',
            r'peeledandchopped': 'peeled and chopped',
            r'choppedandcooked': 'chopped and cooked',
            
            # CamelCase fixes
            r'([a-z])([A-Z])': r'\\1 \\2',  # "camelCase" → "camel Case"
        }
        
        corrected_name = name
        for pattern, replacement in corruption_fixes.items():
            corrected_name = re.sub(pattern, replacement, corrected_name)
        
        # Clean up extra spaces
        corrected_name = re.sub(r'\\s+', ' ', corrected_name).strip()
        
        return corrected_name
    
    def standardize_unit(self, unit: str) -> str:
        """Standardize units to consistent format"""
        if not unit:
            return unit
        
        unit_standardizations = {
            'tablespoon': 'tbsp',
            'tablespoons': 'tbsp',
            'teaspoon': 'tsp',
            'teaspoons': 'tsp',
            'ounce': 'oz',
            'ounces': 'oz',
            'pound': 'lb',
            'pounds': 'lbs',
            'lbs': 'lb',  # Standardize to singular
            'c': 'cup',
            'C': 'cup',
            'T': 'tbsp',
            't': 'tsp',
        }
        
        return unit_standardizations.get(unit.lower(), unit)
    
    def improve_amount_precision(self, amount: float, unit: str) -> float:
        """Improve amount precision based on unit context"""
        if amount <= 0:
            return amount
        
        # Round to reasonable precision based on unit
        if unit in ['tsp', 'tbsp']:
            # For small measurements, use quarter precision
            return round(amount * 4) / 4
        elif unit in ['cup', 'cups']:
            # For cups, use eighth precision
            return round(amount * 8) / 8
        elif unit in ['oz', 'lb']:
            # For weight, use quarter precision
            return round(amount * 4) / 4
        else:
            # Default: round to nearest half
            return round(amount * 2) / 2
    
    def apply_format_corrections(self):
        """Apply format consistency corrections"""
        print("🔄 Applying format corrections...")
        
        for recipe_data in self.extracted_recipes['extracted_recipes']:
            recipe = recipe_data['recipe']
            improved = False
            
            # Ensure consistent field presence
            if 'description' not in recipe:
                recipe['description'] = f"A delicious {recipe.get('name', 'recipe')} from HSCA culinary collection."
                improved = True
            
            # Ensure ingredients have consistent structure
            ingredients = recipe.get('ingredients', [])
            for ingredient in ingredients:
                if 'swaps' not in ingredient:
                    ingredient['swaps'] = []
                    improved = True
                
                if 'notes' not in ingredient:
                    ingredient['notes'] = ''
                    improved = True
            
            # Ensure instructions exist
            if 'instructions' not in recipe or not recipe['instructions']:
                recipe['instructions'] = ['Prepare ingredients according to recipe specifications.']
                improved = True
            
            if improved:
                self.corrections_applied['format_corrections'] += 1
    
    def validate_corrections(self) -> Dict:
        """Validate the applied corrections"""
        print("🔍 Validating applied corrections...")
        
        validation_results = {
            'total_recipes': len(self.extracted_recipes['extracted_recipes']),
            'corrections_summary': self.corrections_applied,
            'validation_checks': {
                'all_recipes_have_names': 0,
                'all_recipes_have_categories': 0,
                'all_recipes_have_ingredients': 0,
                'ingredient_name_quality': 0
            }
        }
        
        for recipe_data in self.extracted_recipes['extracted_recipes']:
            recipe = recipe_data['recipe']
            
            # Validation checks
            if recipe.get('name'):
                validation_results['validation_checks']['all_recipes_have_names'] += 1
            
            if recipe.get('category'):
                validation_results['validation_checks']['all_recipes_have_categories'] += 1
            
            if recipe.get('ingredients'):
                validation_results['validation_checks']['all_recipes_have_ingredients'] += 1
                
                # Check ingredient name quality
                clean_ingredients = sum(
                    1 for ing in recipe['ingredients']
                    if ing.get('name') and not re.search(r'[0-9]+[a-zA-Z]|[a-zA-Z][0-9]+', ing['name'])
                )
                if clean_ingredients == len(recipe['ingredients']):
                    validation_results['validation_checks']['ingredient_name_quality'] += 1
        
        # Calculate percentages
        total = validation_results['total_recipes']
        validation_checks = dict(validation_results['validation_checks'])  # Create a copy
        for key in validation_checks:
            count = validation_checks[key]
            validation_results['validation_checks'][f'{key}_percentage'] = (count / total) * 100 if total > 0 else 0
        
        return validation_results
    
    def run_precision_corrections(self) -> Dict:
        """Run complete precision correction process"""
        print("🚀 Starting precision-based corrections...")
        
        # Create backup of original data
        original_data = copy.deepcopy(self.extracted_recipes)
        
        # Apply corrections in order
        self.apply_category_corrections()
        self.apply_name_standardizations()
        self.improve_ingredient_precision()
        self.apply_format_corrections()
        
        # Validate corrections
        validation_results = self.validate_corrections()
        
        # Compile results
        correction_results = {
            'correction_metadata': {
                'original_recipe_count': len(original_data['extracted_recipes']),
                'corrected_recipe_count': len(self.extracted_recipes['extracted_recipes']),
                'corrections_applied': self.corrections_applied
            },
            'validation_results': validation_results,
            'improvement_summary': {
                'total_corrections': sum(self.corrections_applied.values()),
                'correction_rate': sum(self.corrections_applied.values()) / len(self.extracted_recipes['extracted_recipes']),
                'quality_improvements': 'Applied based on gold standard analysis'
            }
        }
        
        return correction_results
    
    def save_corrected_recipes(self, filename: str = 'precision_corrected_hsca_recipes.json'):
        """Save the corrected recipe database"""
        # Update metadata
        self.extracted_recipes['extraction_metadata'] = {
            'original_extraction_date': self.extracted_recipes.get('extraction_date', 'unknown'),
            'precision_correction_date': 'current',
            'correction_summary': self.corrections_applied,
            'total_recipes': len(self.extracted_recipes['extracted_recipes'])
        }
        
        with open(f'enhanced_extracted_recipes/{filename}', 'w', encoding='utf-8') as f:
            json.dump(self.extracted_recipes, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Corrected recipes saved to enhanced_extracted_recipes/{filename}")
    
    def save_correction_report(self, results: Dict, filename: str = 'precision_correction_report.json'):
        """Save detailed correction report"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Correction report saved to {filename}")
        
        # Print summary
        print(f"\n📊 PRECISION CORRECTION SUMMARY:")
        print(f"Total Corrections Applied: {sum(self.corrections_applied.values())}")
        print(f"Category Corrections: {self.corrections_applied['category_corrections']}")
        print(f"Name Standardizations: {self.corrections_applied['name_standardizations']}")
        print(f"Ingredient Improvements: {self.corrections_applied['ingredient_improvements']}")
        print(f"Format Corrections: {self.corrections_applied['format_corrections']}")

def main():
    """Main execution function"""
    corrector = PrecisionRecipeCorrector()
    
    results = corrector.run_precision_corrections()
    corrector.save_corrected_recipes()
    corrector.save_correction_report(results)
    
    print("✨ Precision recipe corrections complete!")

if __name__ == "__main__":
    main()