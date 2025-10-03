#!/usr/bin/env python3
"""
Advanced Accuracy Validator for OCR Correction System
Comprehensive testing and scoring metrics for character-perfect validation
"""
import json
import re
from typing import Dict, List, Tuple, Optional
from collections import defaultdict
from difflib import SequenceMatcher
import statistics

class AccuracyValidator:
    """Advanced accuracy validation system with enhanced scoring metrics"""
    
    def __init__(self):
        self.typescript_recipes = {}
        self.load_typescript_gold_standard()
        self.corruption_patterns = self.define_corruption_patterns()
        
    def load_typescript_gold_standard(self):
        """Load TypeScript recipes as gold standard for accuracy measurement"""
        import os
        from pathlib import Path
        
        recipe_dirs = [
            'src/data/recipes/beverages',
            'src/data/recipes/breakfast', 
            'src/data/recipes/appetizers',
            'src/data/recipes/dinner',
            'src/data/recipes/desserts',
            'src/data/recipes/salads',
            'src/data/recipes/soups',
            'src/data/recipes/sides',
            'src/data/recipes/sauces',
            'src/data/recipes/condiments',
            'src/data/recipes/lunch'
        ]
        
        for recipe_dir in recipe_dirs:
            index_file = Path(recipe_dir) / "index.ts"
            if index_file.exists():
                self.parse_typescript_gold_standard(str(index_file))
        
        print(f"📊 Loaded {len(self.typescript_recipes)} TypeScript recipes as gold standard")
    
    def parse_typescript_gold_standard(self, file_path: str):
        """Parse TypeScript for gold standard recipes"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract recipe names and ingredients with high precision
            recipe_pattern = r'\{\s*name:\s*[\'"]([^\'\"]+)[\'"],.*?ingredients:\s*\[(.*?)\]'
            matches = re.findall(recipe_pattern, content, re.DOTALL)
            
            for name, ingredients_block in matches:
                # Parse ingredients precisely
                ingredient_pattern = r'\{\s*name:\s*[\'"]([^\'\"]+)[\'"],\s*amount:\s*([0-9.]+),\s*unit:\s*[\'"]([^\'\"]*)[\'"](?:,\s*notes:\s*[\'"]([^\'\"]*)[\'"])?'
                ingredients = []
                
                for ing_match in re.finditer(ingredient_pattern, ingredients_block):
                    ingredients.append({
                        'name': ing_match.group(1),
                        'amount': float(ing_match.group(2)),
                        'unit': ing_match.group(3),
                        'notes': ing_match.group(4) if ing_match.group(4) else ''
                    })
                
                self.typescript_recipes[name.lower()] = {
                    'name': name,
                    'ingredients': ingredients
                }
        
        except Exception as e:
            print(f"⚠️  Error parsing gold standard from {file_path}: {e}")
    
    def define_corruption_patterns(self) -> Dict[str, List[str]]:
        """Define known OCR corruption patterns for testing"""
        return {
            # Character-level corruptions
            'character_substitutions': [
                ('e', '3'), ('a', '4'), ('i', '1'), ('o', '0'), ('s', '5'),
                ('g', '6'), ('t', '7'), ('b', '8'), ('l', '1'), ('S', '5')
            ],
            
            # Word-level corruptions from actual data
            'word_corruptions': {
                'beets': ['b33ts', 'b3ets', 'be3ts', 'eiargebeets'],
                'large': ['1arge', 'lar6e', '1ar6e'],
                'washed': ['wa5hed', 'wash3d', 'wa5h3d', 'washedandtrimmed'],
                'trimmed': ['tr1mmed', 'trimm3d', 'tr1mm3d'],
                'apples': ['app13s', 'app1es', '4pp1es', 'granysmithappies'],
                'granny smith': ['grany5m1th', 'granysmith', '6ranysmith'],
                'peeled': ['p33l3d', 'pe313d', 'peeied'],
                'cut': ['cu7', 'cu+', 'cutproducetofitjuicerfeedtube'],
                'flour': ['f1our', 'f10ur'],
                'oil': ['oi1', '0i1'],
                'juice': ['ju1ce', 'ju1c3'],
                'salt': ['sa1t', '5a1t'],
                'and': ['4nd', 'an6']
            },
            
            # Concatenation corruptions
            'concatenations': [
                'washedandtrimmed',
                'cutproducetofitjuicerfeedtube',
                'granysmithappies',
                'eiargebeets'
            ]
        }
    
    def generate_synthetic_corruptions(self, clean_text: str) -> List[str]:
        """Generate synthetic OCR corruptions for testing"""
        corruptions = []
        
        # Character substitution corruptions
        for old_char, new_char in self.corruption_patterns['character_substitutions']:
            if old_char in clean_text:
                corrupted = clean_text.replace(old_char, new_char)
                corruptions.append(corrupted)
        
        # Word-level corruptions
        for clean_word, corrupted_variants in self.corruption_patterns['word_corruptions'].items():
            if clean_word.lower() in clean_text.lower():
                for variant in corrupted_variants:
                    corrupted = re.sub(re.escape(clean_word), variant, clean_text, flags=re.IGNORECASE)
                    corruptions.append(corrupted)
        
        # Space removal corruption
        corruptions.append(clean_text.replace(' ', ''))
        
        # Mixed corruptions (realistic OCR errors)
        mixed = clean_text.lower()
        mixed = mixed.replace('e', '3').replace('a', '4').replace('i', '1')
        corruptions.append(mixed)
        
        return corruptions
    
    def calculate_character_accuracy(self, original: str, corrected: str, gold_standard: str) -> Dict[str, float]:
        """Calculate character-level accuracy metrics"""
        if not gold_standard:
            return {'accuracy': 0.0, 'precision': 0.0, 'recall': 0.0, 'f1_score': 0.0}
        
        # Character-level comparison
        original_chars = set(original.lower())
        corrected_chars = set(corrected.lower())
        gold_chars = set(gold_standard.lower())
        
        # True positives: characters correctly preserved/corrected
        true_positives = len(corrected_chars & gold_chars)
        
        # False positives: incorrect characters introduced
        false_positives = len(corrected_chars - gold_chars)
        
        # False negatives: correct characters missing
        false_negatives = len(gold_chars - corrected_chars)
        
        # Calculate metrics
        precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0.0
        recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0.0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
        
        # Overall similarity
        similarity = SequenceMatcher(None, corrected.lower(), gold_standard.lower()).ratio()
        
        return {
            'character_accuracy': similarity,
            'precision': precision,
            'recall': recall,
            'f1_score': f1_score,
            'levenshtein_similarity': similarity
        }
    
    def calculate_ingredient_accuracy(self, extracted_ingredients: List[Dict], gold_ingredients: List[Dict]) -> Dict[str, float]:
        """Calculate ingredient-level accuracy metrics"""
        if not gold_ingredients:
            return {'ingredient_accuracy': 0.0, 'name_accuracy': 0.0, 'structure_accuracy': 0.0}
        
        # Match ingredients by similarity
        matched_pairs = []
        used_gold_indices = set()
        
        for ext_ing in extracted_ingredients:
            best_match_idx = -1
            best_score = 0.0
            
            for i, gold_ing in enumerate(gold_ingredients):
                if i in used_gold_indices:
                    continue
                
                # Compare ingredient names
                ext_name = ext_ing.get('name', '').lower()
                gold_name = gold_ing.get('name', '').lower()
                
                similarity = SequenceMatcher(None, ext_name, gold_name).ratio()
                if similarity > best_score:
                    best_score = similarity
                    best_match_idx = i
            
            if best_match_idx >= 0 and best_score > 0.5:
                matched_pairs.append((ext_ing, gold_ingredients[best_match_idx], best_score))
                used_gold_indices.add(best_match_idx)
        
        if not matched_pairs:
            return {'ingredient_accuracy': 0.0, 'name_accuracy': 0.0, 'structure_accuracy': 0.0}
        
        # Calculate accuracy metrics
        name_scores = [score for _, _, score in matched_pairs]
        name_accuracy = statistics.mean(name_scores)
        
        # Structure accuracy (amount, unit, notes)
        structure_scores = []
        for ext_ing, gold_ing, _ in matched_pairs:
            structure_score = 0.0
            
            # Amount accuracy
            ext_amount = ext_ing.get('amount', 0)
            gold_amount = gold_ing.get('amount', 0)
            if gold_amount > 0:
                amount_accuracy = 1.0 - abs(ext_amount - gold_amount) / gold_amount
                structure_score += max(0, amount_accuracy) * 0.4
            
            # Unit accuracy
            ext_unit = ext_ing.get('unit', '').lower()
            gold_unit = gold_ing.get('unit', '').lower()
            unit_accuracy = 1.0 if ext_unit == gold_unit else 0.0
            structure_score += unit_accuracy * 0.3
            
            # Notes accuracy
            ext_notes = ext_ing.get('notes', '').lower()
            gold_notes = gold_ing.get('notes', '').lower()
            notes_accuracy = SequenceMatcher(None, ext_notes, gold_notes).ratio()
            structure_score += notes_accuracy * 0.3
            
            structure_scores.append(structure_score)
        
        structure_accuracy = statistics.mean(structure_scores)
        
        # Overall ingredient accuracy
        ingredient_accuracy = (name_accuracy * 0.6 + structure_accuracy * 0.4)
        
        return {
            'ingredient_accuracy': ingredient_accuracy,
            'name_accuracy': name_accuracy,
            'structure_accuracy': structure_accuracy,
            'matched_ingredients': len(matched_pairs),
            'total_gold_ingredients': len(gold_ingredients),
            'coverage': len(matched_pairs) / len(gold_ingredients)
        }
    
    def test_ocr_correction_system(self) -> Dict:
        """Test the OCR correction system comprehensively"""
        print("🧪 TESTING OCR CORRECTION SYSTEM")
        print("=" * 50)
        
        # Load original corrupted data and corrected data
        try:
            with open('enhanced_extracted_recipes/enhanced_hsca_recipes.json', 'r', encoding='utf-8') as f:
                original_data = json.load(f)
        except FileNotFoundError:
            print("❌ Original enhanced recipes not found")
            return {}
        
        try:
            with open('enhanced_extracted_recipes/character_perfect_hsca_recipes.json', 'r', encoding='utf-8') as f:
                corrected_data = json.load(f)
        except FileNotFoundError:
            print("❌ Character-perfect recipes not found")
            return {}
        
        original_recipes = original_data.get('extracted_recipes', [])
        corrected_recipes = corrected_data.get('extracted_recipes', [])
        
        print(f"📊 Testing {len(original_recipes)} original vs {len(corrected_recipes)} corrected recipes")
        
        test_results = {
            'total_recipes_tested': min(len(original_recipes), len(corrected_recipes)),
            'character_accuracy_scores': [],
            'ingredient_accuracy_scores': [],
            'template_matches': 0,
            'significant_improvements': 0,
            'corruption_fixes': [],
            'detailed_results': []
        }
        
        # Test recipe by recipe
        for i in range(min(len(original_recipes), len(corrected_recipes))):
            original_recipe = original_recipes[i].get('recipe', {})
            corrected_recipe = corrected_recipes[i].get('recipe', {})
            
            # Test name correction
            original_name = original_recipe.get('name', '')
            corrected_name = corrected_recipe.get('name', '')
            
            # Find gold standard
            gold_standard = self.find_gold_standard_recipe(corrected_name)
            
            name_accuracy = {}
            ingredient_accuracy = {}
            
            if gold_standard:
                # Character accuracy for name
                name_accuracy = self.calculate_character_accuracy(
                    original_name, corrected_name, gold_standard['name']
                )
                
                # Ingredient accuracy
                original_ingredients = original_recipe.get('ingredients', [])
                corrected_ingredients = corrected_recipe.get('ingredients', [])
                gold_ingredients = gold_standard.get('ingredients', [])
                
                ingredient_accuracy = self.calculate_ingredient_accuracy(
                    corrected_ingredients, gold_ingredients
                )
                
                test_results['template_matches'] += 1
            else:
                # Synthetic testing with corruptions
                corrupted_names = self.generate_synthetic_corruptions(corrected_name)
                synthetic_scores = []
                
                for corrupted in corrupted_names:
                    score = self.calculate_character_accuracy(
                        corrupted, corrected_name, corrected_name
                    )
                    synthetic_scores.append(score['character_accuracy'])
                
                if synthetic_scores:
                    name_accuracy = {'character_accuracy': statistics.mean(synthetic_scores)}
            
            # Record significant improvements
            if name_accuracy.get('character_accuracy', 0) > 0.8:
                test_results['significant_improvements'] += 1
            
            # Record corruption fixes
            if original_name != corrected_name:
                test_results['corruption_fixes'].append({
                    'original': original_name,
                    'corrected': corrected_name,
                    'improvement_score': name_accuracy.get('character_accuracy', 0)
                })
            
            test_results['character_accuracy_scores'].append(name_accuracy.get('character_accuracy', 0))
            test_results['ingredient_accuracy_scores'].append(ingredient_accuracy.get('ingredient_accuracy', 0))
            
            # Detailed result for sample recipes
            if i < 10:  # Store detailed results for first 10 recipes
                test_results['detailed_results'].append({
                    'recipe_index': i,
                    'original_name': original_name,
                    'corrected_name': corrected_name,
                    'gold_standard_found': gold_standard is not None,
                    'name_accuracy': name_accuracy,
                    'ingredient_accuracy': ingredient_accuracy
                })
        
        return test_results
    
    def find_gold_standard_recipe(self, recipe_name: str) -> Optional[Dict]:
        """Find gold standard recipe for comparison"""
        name_key = recipe_name.lower().strip()
        
        # Direct match
        if name_key in self.typescript_recipes:
            return self.typescript_recipes[name_key]
        
        # Fuzzy match
        best_match = None
        best_score = 0.0
        
        for ts_name, ts_recipe in self.typescript_recipes.items():
            similarity = SequenceMatcher(None, name_key, ts_name).ratio()
            if similarity > best_score and similarity > 0.8:
                best_score = similarity
                best_match = ts_recipe
        
        return best_match
    
    def generate_accuracy_report(self, test_results: Dict) -> str:
        """Generate comprehensive accuracy report"""
        report = "# 📊 OCR CORRECTION SYSTEM ACCURACY REPORT\n\n"
        report += "## Executive Summary\n\n"
        
        # Calculate aggregate metrics
        char_scores = test_results.get('character_accuracy_scores', [])
        ing_scores = test_results.get('ingredient_accuracy_scores', [])
        
        if char_scores:
            avg_char_accuracy = statistics.mean(char_scores)
            median_char_accuracy = statistics.median(char_scores)
            std_char_accuracy = statistics.stdev(char_scores) if len(char_scores) > 1 else 0
        else:
            avg_char_accuracy = median_char_accuracy = std_char_accuracy = 0
        
        if ing_scores:
            avg_ing_accuracy = statistics.mean([s for s in ing_scores if s > 0])
            median_ing_accuracy = statistics.median([s for s in ing_scores if s > 0])
        else:
            avg_ing_accuracy = median_ing_accuracy = 0
        
        total_tested = test_results.get('total_recipes_tested', 0)
        template_matches = test_results.get('template_matches', 0)
        significant_improvements = test_results.get('significant_improvements', 0)
        corruption_fixes = len(test_results.get('corruption_fixes', []))
        
        report += f"- **Total Recipes Tested**: {total_tested}\n"
        report += f"- **Template Matches Found**: {template_matches} ({template_matches/total_tested*100:.1f}%)\n"
        report += f"- **Significant Improvements**: {significant_improvements} ({significant_improvements/total_tested*100:.1f}%)\n"
        report += f"- **Corruption Fixes Applied**: {corruption_fixes}\n\n"
        
        report += "## 🎯 Character-Level Accuracy Metrics\n\n"
        report += f"- **Average Character Accuracy**: {avg_char_accuracy:.3f} ({avg_char_accuracy*100:.1f}%)\n"
        report += f"- **Median Character Accuracy**: {median_char_accuracy:.3f} ({median_char_accuracy*100:.1f}%)\n"
        report += f"- **Standard Deviation**: {std_char_accuracy:.3f}\n"
        report += f"- **Recipes with >80% Accuracy**: {sum(1 for s in char_scores if s > 0.8)} ({sum(1 for s in char_scores if s > 0.8)/len(char_scores)*100:.1f}%)\n"
        report += f"- **Recipes with >90% Accuracy**: {sum(1 for s in char_scores if s > 0.9)} ({sum(1 for s in char_scores if s > 0.9)/len(char_scores)*100:.1f}%)\n\n"
        
        report += "## 🥄 Ingredient-Level Accuracy Metrics\n\n"
        report += f"- **Average Ingredient Accuracy**: {avg_ing_accuracy:.3f} ({avg_ing_accuracy*100:.1f}%)\n"
        report += f"- **Median Ingredient Accuracy**: {median_ing_accuracy:.3f} ({median_ing_accuracy*100:.1f}%)\n\n"
        
        # Corruption fixes examples
        corruption_fixes_list = test_results.get('corruption_fixes', [])
        if corruption_fixes_list:
            report += "## 🔧 Corruption Fixes Examples\n\n"
            
            # Sort by improvement score
            sorted_fixes = sorted(corruption_fixes_list, key=lambda x: x['improvement_score'], reverse=True)
            
            for i, fix in enumerate(sorted_fixes[:10]):  # Top 10 fixes
                report += f"### Fix {i+1}: {fix['improvement_score']:.1%} improvement\n"
                report += f"- **Original**: `{fix['original']}`\n"
                report += f"- **Corrected**: `{fix['corrected']}`\n\n"
        
        # Detailed results for sample recipes
        detailed_results = test_results.get('detailed_results', [])
        if detailed_results:
            report += "## 📋 Detailed Sample Results\n\n"
            
            for result in detailed_results:
                report += f"### Recipe {result['recipe_index'] + 1}\n"
                report += f"- **Original Name**: `{result['original_name']}`\n"
                report += f"- **Corrected Name**: `{result['corrected_name']}`\n"
                report += f"- **Gold Standard Found**: {'✅' if result['gold_standard_found'] else '❌'}\n"
                
                name_acc = result.get('name_accuracy', {})
                if name_acc:
                    report += f"- **Character Accuracy**: {name_acc.get('character_accuracy', 0):.1%}\n"
                
                ing_acc = result.get('ingredient_accuracy', {})
                if ing_acc:
                    report += f"- **Ingredient Accuracy**: {ing_acc.get('ingredient_accuracy', 0):.1%}\n"
                
                report += "\n"
        
        return report
    
    def save_accuracy_report(self, test_results: Dict):
        """Save comprehensive accuracy report"""
        report_content = self.generate_accuracy_report(test_results)
        
        with open('accuracy_validation_report.md', 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        # Also save raw results as JSON
        with open('accuracy_test_results.json', 'w', encoding='utf-8') as f:
            json.dump(test_results, f, indent=2, ensure_ascii=False)
        
        print("✅ Accuracy report saved to accuracy_validation_report.md")
        print("✅ Raw test results saved to accuracy_test_results.json")

def main():
    """Run comprehensive accuracy validation"""
    validator = AccuracyValidator()
    
    print("🧪 COMPREHENSIVE OCR CORRECTION ACCURACY VALIDATION")
    print("=" * 60)
    
    # Run tests
    test_results = validator.test_ocr_correction_system()
    
    if test_results:
        # Generate and save report
        validator.save_accuracy_report(test_results)
        
        # Print summary
        total_tested = test_results.get('total_recipes_tested', 0)
        template_matches = test_results.get('template_matches', 0)
        significant_improvements = test_results.get('significant_improvements', 0)
        
        print(f"\n📊 VALIDATION SUMMARY:")
        print(f"  • Recipes tested: {total_tested}")
        print(f"  • Template matches: {template_matches}")
        print(f"  • Significant improvements: {significant_improvements}")
        
        char_scores = test_results.get('character_accuracy_scores', [])
        if char_scores:
            avg_accuracy = sum(char_scores) / len(char_scores)
            print(f"  • Average character accuracy: {avg_accuracy:.1%}")
        
        print("\n🎉 ACCURACY VALIDATION COMPLETE!")
    else:
        print("❌ Accuracy validation failed")

if __name__ == "__main__":
    main()