#!/usr/bin/env python3
"""
Complete Database Cross-Reference System
Comprehensive system to locate ALL 100+ database recipes across all extraction phases
"""
import json
import re
import os
from typing import Dict, List, Tuple, Optional, Set
from difflib import SequenceMatcher
from collections import defaultdict
from dataclasses import dataclass

@dataclass
class RecipeMatch:
    """Data class for recipe matching results"""
    typescript_recipe: Dict
    extraction_recipe: Dict
    extraction_phase: str
    similarity_score: float
    match_type: str  # exact, fuzzy, ingredient, category
    confidence: float

class CompleteTypescriptDatabaseLoader:
    """Comprehensive TypeScript database loader for all recipe categories"""
    
    def __init__(self):
        self.typescript_recipes = {}
        self.recipes_by_category = defaultdict(list)
        self.total_loaded = 0
        
    def load_complete_database(self) -> Dict[str, Dict]:
        """Load complete TypeScript database from all categories"""
        print("🔍 Loading complete TypeScript database...")
        
        base_path = "src/data/recipes"
        categories = [
            'breakfast', 'lunch', 'dinner', 'appetizers', 'sides',
            'sauces', 'desserts', 'salads', 'beverages', 'condiments', 'soups'
        ]
        
        total_recipes = {}
        
        for category in categories:
            category_path = f"{base_path}/{category}/index.ts"
            if os.path.exists(category_path):
                category_recipes = self.parse_category_file(category_path, category)
                print(f"  📁 {category}: {len(category_recipes)} recipes")
                
                for recipe_name, recipe_data in category_recipes.items():
                    # Add category to recipe data
                    recipe_data['category'] = category
                    total_recipes[recipe_name] = recipe_data
                    self.recipes_by_category[category].append(recipe_data)
        
        self.typescript_recipes = total_recipes
        self.total_loaded = len(total_recipes)
        
        print(f"✅ Loaded {self.total_loaded} total TypeScript recipes across {len(categories)} categories")
        return total_recipes
    
    def parse_category_file(self, file_path: str, category: str) -> Dict[str, Dict]:
        """Parse a TypeScript category file to extract recipes"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            recipes = {}
            
            # Split content into recipe blocks
            recipe_blocks = self.split_into_recipe_blocks(content)
            
            for block in recipe_blocks:
                recipe_data = self.parse_recipe_block(block)
                if recipe_data and 'name' in recipe_data:
                    recipe_name = recipe_data['name'].lower().strip()
                    recipes[recipe_name] = recipe_data
            
            return recipes
            
        except Exception as e:
            print(f"⚠️  Error parsing {file_path}: {e}")
            return {}
    
    def split_into_recipe_blocks(self, content: str) -> List[str]:
        """Split TypeScript content into individual recipe blocks"""
        # Look for recipe objects that start with opening brace
        blocks = []
        current_block = ""
        brace_count = 0
        in_recipe = False
        
        lines = content.split('\n')
        for line in lines:
            stripped = line.strip()
            
            # Start of a recipe (has name field)
            if 'name:' in stripped and not in_recipe:
                in_recipe = True
                current_block = line + '\n'
                brace_count = line.count('{') - line.count('}')
            elif in_recipe:
                current_block += line + '\n'
                brace_count += line.count('{') - line.count('}')
                
                # End of recipe block
                if brace_count <= 0 and (stripped.endswith('},') or stripped.endswith('}')):
                    blocks.append(current_block)
                    current_block = ""
                    in_recipe = False
                    brace_count = 0
        
        # Add final block if exists
        if current_block.strip() and in_recipe:
            blocks.append(current_block)
        
        return blocks
    
    def parse_recipe_block(self, block: str) -> Optional[Dict]:
        """Parse a single recipe block to extract recipe data"""
        try:
            # Extract name
            name_match = re.search(r"name:\s*['\"]([^'\"]+)['\"]", block)
            if not name_match:
                return None
            
            recipe_name = name_match.group(1)
            
            # Extract description
            desc_match = re.search(r"description:\s*['\"]([^'\"]*)['\"]", block)
            description = desc_match.group(1) if desc_match else ""
            
            # Extract ingredients
            ingredients = self.extract_ingredients(block)
            
            # Extract instructions
            instructions = self.extract_instructions(block)
            
            # Extract other fields
            nutrition = self.extract_nutrition(block)
            time_to_make = self.extract_time_to_make(block)
            season = self.extract_season(block)
            cuisine = self.extract_cuisine(block)
            meal_type = self.extract_meal_type(block)
            
            return {
                'name': recipe_name,
                'description': description,
                'ingredients': ingredients,
                'instructions': instructions,
                'nutrition': nutrition,
                'timeToMake': time_to_make,
                'season': season,
                'cuisine': cuisine,
                'mealType': meal_type
            }
            
        except Exception as e:
            print(f"⚠️  Error parsing recipe block: {e}")
            return None
    
    def extract_ingredients(self, block: str) -> List[Dict]:
        """Extract ingredients array from recipe block"""
        ingredients = []
        
        # Find ingredients array
        ing_match = re.search(r'ingredients:\s*\[(.*?)\]', block, re.DOTALL)
        if not ing_match:
            return ingredients
        
        ingredients_text = ing_match.group(1)
        
        # Split by ingredient objects
        ing_objects = re.findall(r'\{[^}]+\}', ingredients_text)
        
        for ing_obj in ing_objects:
            # Extract ingredient fields
            name_match = re.search(r"name:\s*['\"]([^'\"]+)['\"]", ing_obj)
            amount_match = re.search(r"amount:\s*([\d.]+)", ing_obj)
            unit_match = re.search(r"unit:\s*['\"]([^'\"]*)['\"]", ing_obj)
            notes_match = re.search(r"notes:\s*['\"]([^'\"]*)['\"]", ing_obj)
            
            if name_match:
                ingredient = {
                    'name': name_match.group(1),
                    'amount': float(amount_match.group(1)) if amount_match else 1.0,
                    'unit': unit_match.group(1) if unit_match else '',
                    'notes': notes_match.group(1) if notes_match else ''
                }
                ingredients.append(ingredient)
        
        return ingredients
    
    def extract_instructions(self, block: str) -> List[str]:
        """Extract instructions array from recipe block"""
        # Find instructions array
        inst_match = re.search(r'instructions:\s*\[(.*?)\]', block, re.DOTALL)
        if not inst_match:
            return []
        
        instructions_text = inst_match.group(1)
        
        # Extract individual instruction strings
        instructions = re.findall(r"['\"]([^'\"]+)['\"]", instructions_text)
        
        return instructions
    
    def extract_nutrition(self, block: str) -> Dict:
        """Extract nutrition object from recipe block"""
        nutrition = {}
        
        nut_match = re.search(r'nutrition:\s*\{([^}]+)\}', block)
        if nut_match:
            nut_text = nut_match.group(1)
            
            # Extract numeric fields
            calories_match = re.search(r'calories:\s*(\d+)', nut_text)
            protein_match = re.search(r'protein:\s*(\d+)', nut_text)
            carbs_match = re.search(r'carbs:\s*(\d+)', nut_text)
            fat_match = re.search(r'fat:\s*(\d+)', nut_text)
            
            if calories_match:
                nutrition['calories'] = int(calories_match.group(1))
            if protein_match:
                nutrition['protein'] = int(protein_match.group(1))
            if carbs_match:
                nutrition['carbs'] = int(carbs_match.group(1))
            if fat_match:
                nutrition['fat'] = int(fat_match.group(1))
        
        return nutrition
    
    def extract_time_to_make(self, block: str) -> str:
        """Extract timeToMake from recipe block"""
        time_match = re.search(r"timeToMake:\s*['\"]([^'\"]+)['\"]", block)
        return time_match.group(1) if time_match else ""
    
    def extract_season(self, block: str) -> List[str]:
        """Extract season array from recipe block"""
        season_match = re.search(r'season:\s*\[([^\]]+)\]', block)
        if season_match:
            season_text = season_match.group(1)
            seasons = re.findall(r"['\"]([^'\"]+)['\"]", season_text)
            return seasons
        return []
    
    def extract_cuisine(self, block: str) -> str:
        """Extract cuisine from recipe block"""
        cuisine_match = re.search(r"cuisine:\s*['\"]([^'\"]+)['\"]", block)
        return cuisine_match.group(1) if cuisine_match else ""
    
    def extract_meal_type(self, block: str) -> List[str]:
        """Extract mealType array from recipe block"""
        meal_match = re.search(r'mealType:\s*\[([^\]]+)\]', block)
        if meal_match:
            meal_text = meal_match.group(1)
            meal_types = re.findall(r"['\"]([^'\"]+)['\"]", meal_text)
            return meal_types
        return []

class ComprehensiveExtractionAnalyzer:
    """Analyze ALL extraction phases comprehensively"""
    
    def __init__(self):
        self.extraction_phases = {}
        self.total_extraction_recipes = 0
        
    def load_all_extraction_phases(self) -> Dict[str, List[Dict]]:
        """Load all extraction phases"""
        print("📊 Loading all extraction phases...")
        
        phase_files = {
            'character_perfect': 'enhanced_extracted_recipes/character_perfect_hsca_recipes.json',
            'perfect': 'enhanced_extracted_recipes/perfect_hsca_recipes.json', 
            'enhanced': 'enhanced_extracted_recipes/enhanced_hsca_recipes.json',
            'improved': 'enhanced_extracted_recipes/improved_hsca_recipes.json',
            'filtered': 'enhanced_extracted_recipes/filtered_hsca_recipes.json'
        }
        
        phases = {}
        total_recipes = 0
        
        for phase_name, file_path in phase_files.items():
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    recipes = data.get('extracted_recipes', [])
                    phases[phase_name] = recipes
                    total_recipes += len(recipes)
                    
                    print(f"  📁 {phase_name}: {len(recipes)} recipes")
                    
                except Exception as e:
                    print(f"⚠️  Error loading {file_path}: {e}")
                    phases[phase_name] = []
        
        self.extraction_phases = phases
        self.total_extraction_recipes = total_recipes
        
        print(f"✅ Loaded {total_recipes} total extraction recipes across {len(phases)} phases")
        return phases

class AdvancedFuzzyMatcher:
    """Advanced fuzzy matching with multiple strategies"""
    
    def __init__(self):
        self.ocr_corruption_patterns = self.build_ocr_patterns()
        self.category_keywords = self.build_category_keywords()
        
    def build_ocr_patterns(self) -> Dict[str, str]:
        """Build comprehensive OCR corruption patterns"""
        return {
            # Number to letter corruptions
            '0': 'o', '1': 'i', '3': 'e', '5': 's', '6': 'g', '7': 't', '8': 'b',
            
            # Common OCR corruptions
            'ju1ce': 'juice', 'app1e': 'apple', 'ch1cken': 'chicken',
            'f1our': 'flour', 'sa1t': 'salt', 'oi1': 'oil', 'w1th': 'with',
            'm1lk': 'milk', 'b1ue': 'blue', 'gr33n': 'green', 'r3d': 'red',
            
            # Space removal patterns
            'andtrimmed': 'and trimmed', 'washedand': 'washed and',
            'seededand': 'seeded and', 'cutinto': 'cut into',
            
            # Complex patterns
            'rn': 'm', 'vv': 'w', 'ii': 'n', 'cl': 'd'
        }
    
    def build_category_keywords(self) -> Dict[str, List[str]]:
        """Build category-specific keywords for matching"""
        return {
            'beverages': ['juice', 'milk', 'smoothie', 'tea', 'elixir', 'agua', 'fresca'],
            'desserts': ['pudding', 'brownie', 'cookie', 'cake', 'chocolate', 'sweet'],
            'salads': ['salad', 'slaw', 'greens', 'vegetables'],
            'soups': ['soup', 'broth', 'stew', 'bisque'],
            'sauces': ['sauce', 'pesto', 'dressing', 'marinade'],
            'lunch': ['burger', 'sandwich', 'wrap', 'bowl'],
            'dinner': ['roasted', 'grilled', 'baked', 'steamed'],
            'breakfast': ['pancake', 'waffle', 'toast', 'breakfast'],
            'appetizers': ['appetizer', 'starter', 'bite'],
            'sides': ['side', 'rice', 'quinoa', 'grain'],
            'condiments': ['condiment', 'spread', 'jam', 'butter']
        }
    
    def find_all_matches(self, typescript_recipe: Dict, extraction_phases: Dict[str, List[Dict]]) -> List[RecipeMatch]:
        """Find all possible matches across all phases using multiple strategies"""
        matches = []
        
        ts_name = typescript_recipe['name'].lower().strip()
        ts_ingredients = typescript_recipe.get('ingredients', [])
        ts_category = typescript_recipe.get('category', '')
        
        for phase_name, phase_recipes in extraction_phases.items():
            for ext_recipe in phase_recipes:
                # Strategy 1: Exact name matching
                exact_match = self.exact_name_match(ts_name, ext_recipe, phase_name)
                if exact_match:
                    matches.append(exact_match)
                    continue
                
                # Strategy 2: Advanced fuzzy matching
                fuzzy_match = self.advanced_fuzzy_match(typescript_recipe, ext_recipe, phase_name)
                if fuzzy_match:
                    matches.append(fuzzy_match)
                    continue
                
                # Strategy 3: OCR corruption pattern matching
                ocr_match = self.ocr_corruption_match(typescript_recipe, ext_recipe, phase_name)
                if ocr_match:
                    matches.append(ocr_match)
                    continue
                
                # Strategy 4: Ingredient-based matching
                ingredient_match = self.ingredient_based_match(typescript_recipe, ext_recipe, phase_name)
                if ingredient_match:
                    matches.append(ingredient_match)
                    continue
                
                # Strategy 5: Category-aware matching
                category_match = self.category_aware_match(typescript_recipe, ext_recipe, phase_name)
                if category_match:
                    matches.append(category_match)
        
        return matches
    
    def exact_name_match(self, ts_name: str, ext_recipe: Dict, phase_name: str) -> Optional[RecipeMatch]:
        """Exact name matching strategy"""
        ext_name = ext_recipe.get('recipe', {}).get('name', '').lower().strip()
        
        if ts_name == ext_name:
            return RecipeMatch(
                typescript_recipe={'name': ts_name},
                extraction_recipe=ext_recipe,
                extraction_phase=phase_name,
                similarity_score=1.0,
                match_type='exact',
                confidence=1.0
            )
        return None
    
    def advanced_fuzzy_match(self, ts_recipe: Dict, ext_recipe: Dict, phase_name: str) -> Optional[RecipeMatch]:
        """Advanced fuzzy matching with enhanced algorithms"""
        ts_name = ts_recipe['name'].lower().strip()
        ext_name = ext_recipe.get('recipe', {}).get('name', '').lower().strip()
        
        if not ext_name:
            return None
        
        # Calculate similarity
        similarity = SequenceMatcher(None, ts_name, ext_name).ratio()
        
        # Enhanced similarity with partial matching
        words_ts = set(ts_name.split())
        words_ext = set(ext_name.split())
        
        if words_ts and words_ext:
            word_overlap = len(words_ts.intersection(words_ext)) / len(words_ts.union(words_ext))
            combined_similarity = (similarity + word_overlap) / 2
        else:
            combined_similarity = similarity
        
        # Accept matches with reasonable similarity
        if combined_similarity > 0.3:  # Lowered threshold for better coverage
            confidence = min(combined_similarity * 1.2, 1.0)  # Boost confidence slightly
            
            return RecipeMatch(
                typescript_recipe=ts_recipe,
                extraction_recipe=ext_recipe,
                extraction_phase=phase_name,
                similarity_score=combined_similarity,
                match_type='fuzzy',
                confidence=confidence
            )
        
        return None
    
    def ocr_corruption_match(self, ts_recipe: Dict, ext_recipe: Dict, phase_name: str) -> Optional[RecipeMatch]:
        """OCR corruption pattern matching"""
        ts_name = ts_recipe['name'].lower().strip()
        ext_name = ext_recipe.get('recipe', {}).get('name', '').lower().strip()
        
        if not ext_name:
            return None
        
        # Apply OCR corrections to extracted name
        corrected_ext_name = ext_name
        for corrupted, correct in self.ocr_corruption_patterns.items():
            corrected_ext_name = corrected_ext_name.replace(corrupted, correct)
        
        # Remove spaces for better matching
        ts_name_nospace = ts_name.replace(' ', '')
        corrected_ext_nospace = corrected_ext_name.replace(' ', '')
        
        similarity = SequenceMatcher(None, ts_name_nospace, corrected_ext_nospace).ratio()
        
        if similarity > 0.4:  # OCR corruption threshold
            return RecipeMatch(
                typescript_recipe=ts_recipe,
                extraction_recipe=ext_recipe,
                extraction_phase=phase_name,
                similarity_score=similarity,
                match_type='ocr_corruption',
                confidence=similarity * 0.8  # Lower confidence for OCR matches
            )
        
        return None
    
    def ingredient_based_match(self, ts_recipe: Dict, ext_recipe: Dict, phase_name: str) -> Optional[RecipeMatch]:
        """Ingredient-based matching for severely corrupted names"""
        ts_ingredients = ts_recipe.get('ingredients', [])
        ext_ingredients = ext_recipe.get('recipe', {}).get('ingredients', [])
        
        if not ts_ingredients or not ext_ingredients:
            return None
        
        # Extract ingredient names
        ts_ing_names = [ing['name'].lower() for ing in ts_ingredients if isinstance(ing, dict)]
        ext_ing_names = []
        
        for ing in ext_ingredients:
            if isinstance(ing, dict):
                ext_ing_names.append(ing.get('name', '').lower())
            else:
                ext_ing_names.append(str(ing).lower())
        
        # Calculate ingredient overlap
        ts_ing_set = set(ts_ing_names)
        ext_ing_set = set(ext_ing_names)
        
        if ts_ing_set and ext_ing_set:
            overlap = len(ts_ing_set.intersection(ext_ing_set))
            total = len(ts_ing_set.union(ext_ing_set))
            
            if total > 0:
                ingredient_similarity = overlap / total
                
                # Require significant ingredient overlap
                if ingredient_similarity > 0.3 and overlap >= 2:
                    return RecipeMatch(
                        typescript_recipe=ts_recipe,
                        extraction_recipe=ext_recipe,
                        extraction_phase=phase_name,
                        similarity_score=ingredient_similarity,
                        match_type='ingredient',
                        confidence=ingredient_similarity * 0.7  # Lower confidence
                    )
        
        return None
    
    def category_aware_match(self, ts_recipe: Dict, ext_recipe: Dict, phase_name: str) -> Optional[RecipeMatch]:
        """Category-aware matching using keywords"""
        ts_category = ts_recipe.get('category', '').lower()
        ts_name = ts_recipe['name'].lower()
        ext_name = ext_recipe.get('recipe', {}).get('name', '').lower()
        
        if not ext_name or ts_category not in self.category_keywords:
            return None
        
        # Check if extraction name contains category keywords
        category_words = self.category_keywords[ts_category]
        ext_has_category = any(word in ext_name for word in category_words)
        ts_has_category = any(word in ts_name for word in category_words)
        
        if ext_has_category and ts_has_category:
            # Calculate similarity within category context
            similarity = SequenceMatcher(None, ts_name, ext_name).ratio()
            
            if similarity > 0.25:  # Lower threshold for category matches
                return RecipeMatch(
                    typescript_recipe=ts_recipe,
                    extraction_recipe=ext_recipe,
                    extraction_phase=phase_name,
                    similarity_score=similarity,
                    match_type='category',
                    confidence=similarity * 0.6  # Lower confidence
                )
        
        return None

class CompleteDatabaseCrossReference:
    """Main cross-reference system for complete database coverage"""
    
    def __init__(self):
        self.database_loader = CompleteTypescriptDatabaseLoader()
        self.extraction_analyzer = ComprehensiveExtractionAnalyzer()
        self.fuzzy_matcher = AdvancedFuzzyMatcher()
        
        self.typescript_recipes = {}
        self.extraction_phases = {}
        self.all_matches = []
        self.coverage_stats = {}
        
    def run_complete_analysis(self) -> Dict:
        """Run complete cross-reference analysis"""
        print("🎯 COMPLETE DATABASE CROSS-REFERENCE ANALYSIS")
        print("=" * 60)
        
        # Step 1: Load complete TypeScript database
        self.typescript_recipes = self.database_loader.load_complete_database()
        
        # Step 2: Load all extraction phases
        self.extraction_phases = self.extraction_analyzer.load_all_extraction_phases()
        
        # Step 3: Find all matches using advanced strategies
        print(f"\n🔍 Finding matches for {len(self.typescript_recipes)} TypeScript recipes...")
        
        all_matches = []
        matched_recipes = set()
        
        for i, (ts_name, ts_recipe) in enumerate(self.typescript_recipes.items()):
            if i % 10 == 0:
                print(f"  Processing: {i}/{len(self.typescript_recipes)} recipes...")
            
            # Find all possible matches for this recipe
            recipe_matches = self.fuzzy_matcher.find_all_matches(ts_recipe, self.extraction_phases)
            
            if recipe_matches:
                # Take the best match for this recipe
                best_match = max(recipe_matches, key=lambda m: m.confidence)
                all_matches.append(best_match)
                matched_recipes.add(ts_name)
            else:
                # No match found
                print(f"    ❌ No match found for: {ts_recipe['name']}")
        
        self.all_matches = all_matches
        
        # Step 4: Calculate comprehensive coverage statistics
        self.coverage_stats = self.calculate_coverage_statistics(matched_recipes)
        
        # Step 5: Generate detailed analysis report
        analysis_report = self.generate_analysis_report()
        
        return analysis_report
    
    def calculate_coverage_statistics(self, matched_recipes: Set[str]) -> Dict:
        """Calculate comprehensive coverage statistics"""
        total_ts_recipes = len(self.typescript_recipes)
        total_matched = len(matched_recipes)
        coverage_percentage = (total_matched / total_ts_recipes) * 100 if total_ts_recipes > 0 else 0
        
        # Category-wise coverage
        category_coverage = {}
        for category, recipes in self.database_loader.recipes_by_category.items():
            category_total = len(recipes)
            category_matched = sum(1 for recipe in recipes if recipe['name'].lower() in matched_recipes)
            category_coverage[category] = {
                'total': category_total,
                'matched': category_matched,
                'percentage': (category_matched / category_total) * 100 if category_total > 0 else 0
            }
        
        # Match type distribution
        match_type_distribution = defaultdict(int)
        for match in self.all_matches:
            match_type_distribution[match.match_type] += 1
        
        # Phase distribution
        phase_distribution = defaultdict(int)
        for match in self.all_matches:
            phase_distribution[match.extraction_phase] += 1
        
        return {
            'total_typescript_recipes': total_ts_recipes,
            'total_matched_recipes': total_matched,
            'coverage_percentage': coverage_percentage,
            'unmatched_count': total_ts_recipes - total_matched,
            'category_coverage': category_coverage,
            'match_type_distribution': dict(match_type_distribution),
            'phase_distribution': dict(phase_distribution),
            'average_confidence': sum(m.confidence for m in self.all_matches) / len(self.all_matches) if self.all_matches else 0
        }
    
    def generate_analysis_report(self) -> Dict:
        """Generate comprehensive analysis report"""
        return {
            'analysis_metadata': {
                'total_typescript_recipes': len(self.typescript_recipes),
                'total_extraction_recipes': self.extraction_analyzer.total_extraction_recipes,
                'total_matches_found': len(self.all_matches),
                'analysis_timestamp': 'Phase 1 Complete Database Analysis'
            },
            'coverage_statistics': self.coverage_stats,
            'detailed_matches': [
                {
                    'typescript_name': match.typescript_recipe['name'],
                    'extraction_name': match.extraction_recipe.get('recipe', {}).get('name', ''),
                    'extraction_phase': match.extraction_phase,
                    'similarity_score': match.similarity_score,
                    'match_type': match.match_type,
                    'confidence': match.confidence,
                    'category': match.typescript_recipe.get('category', '')
                }
                for match in self.all_matches
            ],
            'unmatched_recipes': [
                {
                    'name': recipe['name'],
                    'category': recipe.get('category', ''),
                    'ingredients_count': len(recipe.get('ingredients', [])),
                    'description': recipe.get('description', '')[:100] + '...' if len(recipe.get('description', '')) > 100 else recipe.get('description', '')
                }
                for name, recipe in self.typescript_recipes.items()
                if not any(match.typescript_recipe['name'].lower() == name for match in self.all_matches)
            ]
        }
    
    def save_complete_analysis(self, analysis_report: Dict):
        """Save complete analysis results"""
        # Save detailed analysis
        with open('complete_database_cross_reference_analysis.json', 'w', encoding='utf-8') as f:
            json.dump(analysis_report, f, indent=2, ensure_ascii=False)
        
        # Generate summary report
        summary_report = self.generate_summary_report(analysis_report)
        with open('complete_database_coverage_summary.md', 'w', encoding='utf-8') as f:
            f.write(summary_report)
        
        print("✅ Complete database cross-reference analysis saved")
        
        # Print key statistics
        stats = analysis_report['coverage_statistics']
        print(f"\n📊 COMPLETE DATABASE COVERAGE SUMMARY:")
        print(f"  • Total TypeScript recipes: {stats['total_typescript_recipes']}")
        print(f"  • Total matched recipes: {stats['total_matched_recipes']}")
        print(f"  • Coverage percentage: {stats['coverage_percentage']:.1f}%")
        print(f"  • Unmatched recipes: {stats['unmatched_count']}")
        print(f"  • Average confidence: {stats['average_confidence']:.1%}")
        
        print(f"\n🎯 MATCH TYPE DISTRIBUTION:")
        for match_type, count in stats['match_type_distribution'].items():
            print(f"  • {match_type}: {count} matches")
    
    def generate_summary_report(self, analysis_report: Dict) -> str:
        """Generate summary markdown report"""
        stats = analysis_report['coverage_statistics']
        
        report = "# 🎯 COMPLETE DATABASE CROSS-REFERENCE ANALYSIS SUMMARY\n\n"
        report += "## Comprehensive Recipe Coverage Analysis\n\n"
        
        report += f"- **Total TypeScript Database Recipes**: {stats['total_typescript_recipes']}\n"
        report += f"- **Successfully Matched Recipes**: {stats['total_matched_recipes']}\n"
        report += f"- **Coverage Percentage**: {stats['coverage_percentage']:.1f}%\n"
        report += f"- **Unmatched Recipes**: {stats['unmatched_count']}\n"
        report += f"- **Average Match Confidence**: {stats['average_confidence']:.1%}\n\n"
        
        report += "## 📊 Category-wise Coverage\n\n"
        for category, coverage in stats['category_coverage'].items():
            report += f"### {category.title()}\n"
            report += f"- **Total Recipes**: {coverage['total']}\n"
            report += f"- **Matched Recipes**: {coverage['matched']}\n"
            report += f"- **Coverage**: {coverage['percentage']:.1f}%\n\n"
        
        report += "## 🔍 Match Type Distribution\n\n"
        for match_type, count in stats['match_type_distribution'].items():
            report += f"- **{match_type.title()}**: {count} matches\n"
        
        report += "\n## 📁 Extraction Phase Distribution\n\n"
        for phase, count in stats['phase_distribution'].items():
            report += f"- **{phase}**: {count} matches\n"
        
        return report

def main():
    """Run complete database cross-reference analysis"""
    analyzer = CompleteDatabaseCrossReference()
    
    # Run complete analysis
    analysis_report = analyzer.run_complete_analysis()
    
    # Save results
    analyzer.save_complete_analysis(analysis_report)
    
    print("\n🎉 COMPLETE DATABASE CROSS-REFERENCE ANALYSIS FINISHED!")

if __name__ == "__main__":
    main()