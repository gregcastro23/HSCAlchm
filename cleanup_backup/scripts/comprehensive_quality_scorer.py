#!/usr/bin/env python3
"""
Comprehensive Quality Scoring System
Multi-dimensional recipe quality assessment with weighted metrics
"""
import json
import re
from typing import Dict, List, Tuple, Optional
from collections import defaultdict
import statistics
import math

class ComprehensiveQualityScorer:
    """Advanced quality scoring with multiple dimensions and weighted metrics"""
    
    def __init__(self):
        self.gold_standard = {}
        self.extracted_recipes = {}
        self.template_matches = {}
        self.quality_weights = {
            'ingredient_accuracy': 0.60,  # Most important - recipe core
            'name_standardization': 0.15,  # Professional presentation
            'category_precision': 0.10,   # Organization accuracy
            'format_consistency': 0.10,   # Structural quality
            'completeness_score': 0.05    # Information completeness
        }
        self.load_all_data()
    
    def load_all_data(self):
        """Load all required databases and matching results"""
        try:
            # Load gold standard
            with open('enhanced_gold_standard_recipes.json', 'r', encoding='utf-8') as f:
                gold_data = json.load(f)
                self.gold_standard = gold_data['gold_standard_recipes']
            
            # Load extracted recipes
            with open('enhanced_extracted_recipes/character_perfect_hsca_recipes.json', 'r', encoding='utf-8') as f:
                extracted_data = json.load(f)
                self.extracted_recipes = {
                    i: recipe['recipe'] for i, recipe in enumerate(extracted_data['extracted_recipes'])
                }
            
            # Load template matching results
            with open('improved_template_matching_results.json', 'r', encoding='utf-8') as f:
                matching_data = json.load(f)
                self.template_matches = matching_data
            
            print(f"📊 Loaded data: {len(self.gold_standard)} gold standard, {len(self.extracted_recipes)} extracted")
            print(f"🔗 Template matches: {len(self.template_matches['detailed_matches'])}")
            
        except Exception as e:
            print(f"❌ Error loading data: {str(e)}")
    
    def calculate_ingredient_accuracy_score(self, recipe: Dict) -> Dict:
        """Calculate comprehensive ingredient accuracy score"""
        ingredients = recipe.get('ingredients', [])
        
        if not ingredients:
            return {'score': 0.0, 'details': 'No ingredients found'}
        
        scores = {
            'name_clarity': 0.0,
            'amount_precision': 0.0,
            'unit_consistency': 0.0,
            'completeness': 0.0
        }
        
        total_ingredients = len(ingredients)
        
        for ingredient in ingredients:
            name = ingredient.get('name', '')
            amount = ingredient.get('amount', 0)
            unit = ingredient.get('unit', '')
            notes = ingredient.get('notes', '')
            
            # Name clarity (readable, not corrupted)
            name_score = self.assess_ingredient_name_quality(name)
            scores['name_clarity'] += name_score
            
            # Amount precision
            amount_score = self.assess_amount_precision(amount, unit)
            scores['amount_precision'] += amount_score
            
            # Unit consistency
            unit_score = self.assess_unit_quality(unit, amount)
            scores['unit_consistency'] += unit_score
            
            # Completeness (has all necessary fields)
            completeness_score = self.assess_ingredient_completeness(name, amount, unit, notes)
            scores['completeness'] += completeness_score
        
        # Average scores
        for key in scores:
            scores[key] = scores[key] / total_ingredients if total_ingredients > 0 else 0.0
        
        # Overall ingredient accuracy
        overall_score = (
            scores['name_clarity'] * 0.4 +
            scores['amount_precision'] * 0.3 +
            scores['unit_consistency'] * 0.2 +
            scores['completeness'] * 0.1
        )
        
        return {
            'score': overall_score,
            'component_scores': scores,
            'total_ingredients': total_ingredients
        }
    
    def assess_ingredient_name_quality(self, name: str) -> float:
        """Assess ingredient name quality (clarity, no corruption)"""
        if not name:
            return 0.0
        
        score = 100.0
        
        # Check for OCR corruption patterns
        corruption_patterns = [
            r'[0-9]+[a-zA-Z]',  # Numbers mixed with letters
            r'[a-zA-Z][0-9]+',  # Letters followed by numbers
            r'\b\w*[0-9]\w*\b',  # Words with embedded numbers
            r'\b[a-z]+[A-Z][a-z]*\b',  # Incorrect camelCase
        ]
        
        for pattern in corruption_patterns:
            if re.search(pattern, name):
                score -= 15
        
        # Check for reasonable length
        if len(name) < 2:
            score -= 30
        elif len(name) > 50:  # Very long names might be concatenated
            score -= 10
        
        # Bonus for descriptive terms
        descriptive_terms = ['fresh', 'chopped', 'diced', 'minced', 'sliced', 'organic']
        if any(term in name.lower() for term in descriptive_terms):
            score += 5
        
        return max(0.0, min(100.0, score))
    
    def assess_amount_precision(self, amount: float, unit: str) -> float:
        """Assess amount precision and reasonableness"""
        if amount == 0:
            return 30.0  # Some recipes might not need amounts
        
        score = 100.0
        
        # Check for reasonable ranges
        if amount < 0:
            score -= 50  # Negative amounts are clearly wrong
        elif amount > 1000:
            score -= 20  # Very large amounts might be errors
        
        # Fractional precision bonus
        if isinstance(amount, float) and amount != int(amount):
            score += 5  # Precise measurements are good
        
        # Unit-amount consistency
        if unit in ['cups', 'tbsp', 'tsp'] and amount > 20:
            score -= 10  # Very large cup measurements might be wrong
        elif unit in ['lbs', 'oz'] and amount > 50:
            score -= 10  # Very heavy ingredients
        
        return max(0.0, min(100.0, score))
    
    def assess_unit_quality(self, unit: str, amount: float) -> float:
        """Assess unit quality and consistency"""
        if not unit:
            # No unit might be okay for some ingredients (e.g., "2 onions")
            return 80.0 if amount <= 10 else 60.0
        
        score = 100.0
        
        # Standard unit formats
        standard_units = [
            'cup', 'cups', 'tbsp', 'tsp', 'oz', 'lbs', 'lb', 'pound', 'pounds',
            'gram', 'grams', 'kg', 'ml', 'liter', 'pint', 'quart', 'gallon'
        ]
        
        if unit.lower() in standard_units:
            score += 5  # Bonus for standard units
        
        # Check for unit-amount consistency
        if unit in ['cup', 'cups'] and amount > 0 and amount < 0.01:
            score -= 15  # Very small cup measurements
        
        return max(0.0, min(100.0, score))
    
    def assess_ingredient_completeness(self, name: str, amount: float, unit: str, notes: str) -> float:
        """Assess completeness of ingredient information"""
        score = 0.0
        
        # Essential fields
        if name and len(name) > 1:
            score += 40  # Name is most important
        
        if amount > 0:
            score += 30  # Amount is important
        
        if unit:
            score += 20  # Unit is helpful
        
        if notes:
            score += 10  # Notes are bonus
        
        return score
    
    def calculate_name_standardization_score(self, recipe: Dict) -> Dict:
        """Calculate name standardization quality"""
        name = recipe.get('name', '')
        
        if not name:
            return {'score': 0.0, 'details': 'No name found'}
        
        score = 100.0
        issues = []
        
        # Check for proper capitalization
        if name != name.title():
            score -= 10
            issues.append('Capitalization inconsistent')
        
        # Check for reasonable length
        if len(name) < 5:
            score -= 20
            issues.append('Name too short')
        elif len(name) > 80:
            score -= 15
            issues.append('Name too long')
        
        # Check for special characters (should be minimal)
        special_chars = re.findall(r'[^\w\s\-\&\(\)]', name)
        if special_chars:
            score -= len(special_chars) * 5
            issues.append(f'Special characters: {special_chars}')
        
        # Bonus for descriptive names
        descriptive_words = ['with', 'and', 'in', 'roasted', 'grilled', 'fresh']
        if any(word in name.lower() for word in descriptive_words):
            score += 5
        
        return {
            'score': max(0.0, min(100.0, score)),
            'issues': issues,
            'name_length': len(name)
        }
    
    def calculate_category_precision_score(self, recipe: Dict) -> Dict:
        """Calculate category assignment precision"""
        category = recipe.get('category', '')
        
        if not category:
            return {'score': 0.0, 'details': 'No category assigned'}
        
        # Check against known categories
        valid_categories = [
            'appetizers', 'beverages', 'breakfast', 'desserts', 'dinner',
            'lunch', 'salads', 'sauces', 'sides', 'soups', 'condiments'
        ]
        
        if category.lower() in valid_categories:
            score = 100.0
            details = f'Valid category: {category}'
        else:
            score = 30.0  # Might be valid but not standard
            details = f'Non-standard category: {category}'
        
        return {
            'score': score,
            'details': details,
            'category': category
        }
    
    def calculate_format_consistency_score(self, recipe: Dict) -> Dict:
        """Calculate format consistency score"""
        scores = {
            'structure_completeness': 0.0,
            'field_consistency': 0.0,
            'data_types': 0.0
        }
        
        # Required fields
        required_fields = ['name', 'ingredients']
        optional_fields = ['description', 'instructions', 'category']
        
        # Structure completeness
        present_required = sum(1 for field in required_fields if recipe.get(field))
        scores['structure_completeness'] = (present_required / len(required_fields)) * 100
        
        present_optional = sum(1 for field in optional_fields if recipe.get(field))
        scores['structure_completeness'] += (present_optional / len(optional_fields)) * 20
        
        # Field consistency
        ingredients = recipe.get('ingredients', [])
        if ingredients:
            consistent_ingredients = sum(
                1 for ing in ingredients 
                if all(key in ing for key in ['name', 'amount', 'unit'])
            )
            scores['field_consistency'] = (consistent_ingredients / len(ingredients)) * 100
        
        # Data type correctness
        type_score = 100.0
        if 'ingredients' in recipe and not isinstance(recipe['ingredients'], list):
            type_score -= 30
        if 'name' in recipe and not isinstance(recipe['name'], str):
            type_score -= 20
        
        scores['data_types'] = type_score
        
        # Overall format score
        overall_score = statistics.mean(scores.values())
        
        return {
            'score': overall_score,
            'component_scores': scores
        }
    
    def calculate_completeness_score(self, recipe: Dict) -> Dict:
        """Calculate information completeness score"""
        completeness_areas = {
            'basic_info': ['name'],
            'ingredients': ['ingredients'],
            'instructions': ['instructions'],
            'metadata': ['description', 'category'],
        }
        
        area_scores = {}
        
        for area, fields in completeness_areas.items():
            present_fields = sum(1 for field in fields if recipe.get(field))
            area_scores[area] = (present_fields / len(fields)) * 100
        
        # Special scoring for ingredients detail
        ingredients = recipe.get('ingredients', [])
        if ingredients:
            detailed_ingredients = sum(
                1 for ing in ingredients 
                if ing.get('name') and ing.get('amount') and ing.get('unit')
            )
            area_scores['ingredient_detail'] = (detailed_ingredients / len(ingredients)) * 100
        else:
            area_scores['ingredient_detail'] = 0.0
        
        overall_completeness = statistics.mean(area_scores.values())
        
        return {
            'score': overall_completeness,
            'area_scores': area_scores
        }
    
    def calculate_comprehensive_quality_score(self, recipe_index: int, recipe: Dict) -> Dict:
        """Calculate comprehensive quality score for a recipe"""
        # Calculate component scores
        ingredient_score = self.calculate_ingredient_accuracy_score(recipe)
        name_score = self.calculate_name_standardization_score(recipe)
        category_score = self.calculate_category_precision_score(recipe)
        format_score = self.calculate_format_consistency_score(recipe)
        completeness_score = self.calculate_completeness_score(recipe)
        
        # Apply weights
        weighted_score = (
            ingredient_score['score'] * self.quality_weights['ingredient_accuracy'] +
            name_score['score'] * self.quality_weights['name_standardization'] +
            category_score['score'] * self.quality_weights['category_precision'] +
            format_score['score'] * self.quality_weights['format_consistency'] +
            completeness_score['score'] * self.quality_weights['completeness_score']
        )
        
        # Performance grade
        grade = self.assign_quality_grade(weighted_score)
        
        return {
            'recipe_index': recipe_index,
            'recipe_name': recipe.get('name', 'Unknown'),
            'weighted_quality_score': weighted_score,
            'component_scores': {
                'ingredient_accuracy': ingredient_score,
                'name_standardization': name_score,
                'category_precision': category_score,
                'format_consistency': format_score,
                'completeness': completeness_score
            },
            'performance_grade': grade,
            'quality_weights_used': self.quality_weights
        }
    
    def assign_quality_grade(self, score: float) -> Dict:
        """Assign quality grade based on score"""
        if score >= 95:
            return {'grade': 'A+', 'description': 'Excellent - Production Ready', 'production_ready': True}
        elif score >= 90:
            return {'grade': 'A', 'description': 'Very Good - Minor polish needed', 'production_ready': True}
        elif score >= 85:
            return {'grade': 'B+', 'description': 'Good - Some improvements recommended', 'production_ready': True}
        elif score >= 80:
            return {'grade': 'B', 'description': 'Acceptable - Improvements needed', 'production_ready': False}
        elif score >= 75:
            return {'grade': 'C+', 'description': 'Below expectations - Significant work needed', 'production_ready': False}
        else:
            return {'grade': 'C or below', 'description': 'Poor - Major improvements required', 'production_ready': False}
    
    def run_comprehensive_quality_assessment(self) -> Dict:
        """Run complete quality assessment on all extracted recipes"""
        print("🚀 Starting comprehensive quality assessment...")
        
        recipe_scores = []
        category_performance = defaultdict(list)
        
        for recipe_index, recipe in self.extracted_recipes.items():
            quality_result = self.calculate_comprehensive_quality_score(recipe_index, recipe)
            recipe_scores.append(quality_result)
            
            category = recipe.get('category', 'unknown')
            category_performance[category].append(quality_result['weighted_quality_score'])
        
        # Calculate overall statistics
        all_scores = [result['weighted_quality_score'] for result in recipe_scores]
        
        # Grade distribution
        grade_distribution = defaultdict(int)
        production_ready_count = 0
        
        for result in recipe_scores:
            grade = result['performance_grade']['grade']
            grade_distribution[grade] += 1
            if result['performance_grade']['production_ready']:
                production_ready_count += 1
        
        overall_results = {
            'assessment_metadata': {
                'total_recipes_assessed': len(recipe_scores),
                'quality_weights': self.quality_weights,
                'assessment_date': 'current'
            },
            'overall_statistics': {
                'mean_quality_score': statistics.mean(all_scores) if all_scores else 0.0,
                'median_quality_score': statistics.median(all_scores) if all_scores else 0.0,
                'std_deviation': statistics.stdev(all_scores) if len(all_scores) > 1 else 0.0,
                'min_score': min(all_scores) if all_scores else 0.0,
                'max_score': max(all_scores) if all_scores else 0.0
            },
            'grade_distribution': dict(grade_distribution),
            'production_readiness': {
                'production_ready_count': production_ready_count,
                'production_ready_percentage': (production_ready_count / len(recipe_scores)) * 100 if recipe_scores else 0.0
            },
            'category_performance': {
                category: {
                    'mean_score': statistics.mean(scores),
                    'recipe_count': len(scores),
                    'top_performer': max(scores) if scores else 0
                }
                for category, scores in category_performance.items()
            },
            'detailed_recipe_scores': recipe_scores
        }
        
        return overall_results
    
    def save_quality_assessment(self, results: Dict, filename: str = 'comprehensive_quality_assessment.json'):
        """Save comprehensive quality assessment results"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Quality assessment saved to {filename}")
        
        # Print executive summary
        stats = results['overall_statistics']
        production = results['production_readiness']
        
        print(f"\n📊 COMPREHENSIVE QUALITY ASSESSMENT:")
        print(f"Total Recipes Assessed: {results['assessment_metadata']['total_recipes_assessed']}")
        print(f"Mean Quality Score: {stats['mean_quality_score']:.1f}%")
        print(f"Production Ready: {production['production_ready_count']} ({production['production_ready_percentage']:.1f}%)")
        print(f"Grade Distribution: {dict(results['grade_distribution'])}")

def main():
    """Main execution function"""
    scorer = ComprehensiveQualityScorer()
    
    results = scorer.run_comprehensive_quality_assessment()
    scorer.save_quality_assessment(results)
    
    print("✨ Comprehensive quality assessment complete!")

if __name__ == "__main__":
    main()