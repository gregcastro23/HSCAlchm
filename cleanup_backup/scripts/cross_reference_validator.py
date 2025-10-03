#!/usr/bin/env python3
"""
Cross-Reference Validator for Character Parsing Accuracy
Extracts and compares recipes that exist in both extraction output and TypeScript database
"""
import json
import re
from typing import Dict, List, Tuple, Optional
from difflib import SequenceMatcher
from collections import defaultdict

class CrossReferenceValidator:
    """Validates extraction accuracy against TypeScript database gold standard"""
    
    def __init__(self):
        self.typescript_recipes = {}
        self.extraction_phases = {}
        self.matched_recipes = []
        self.load_typescript_database()
        self.load_extraction_phases()
    
    def load_typescript_database(self):
        """Load all TypeScript recipes as gold standard"""
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
                self.parse_typescript_recipes(str(index_file), recipe_dir.split('/')[-1])
        
        print(f"📊 Loaded {len(self.typescript_recipes)} TypeScript recipes as gold standard")
    
    def parse_typescript_recipes(self, file_path: str, category: str):
        """Parse TypeScript recipes with detailed structure extraction"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all recipe objects in the array
            # Look for patterns like: { name: 'Recipe Name', ...
            recipes_found = 0
            
            # Split by recipe objects more carefully
            recipe_blocks = self.split_into_recipe_blocks(content)
            
            for recipe_block in recipe_blocks:
                recipe_data = self.extract_recipe_details(recipe_block)
                
                if recipe_data:
                    recipe_key = recipe_data['name'].lower().strip()
                    recipe_data['category'] = category
                    self.typescript_recipes[recipe_key] = recipe_data
                    recipes_found += 1
            
            print(f"📥 Parsed {recipes_found} recipes from {category}")
        
        except Exception as e:
            print(f"⚠️  Error parsing {file_path}: {e}")
    
    def split_into_recipe_blocks(self, content: str) -> List[str]:
        """Split TypeScript content into individual recipe blocks"""
        recipe_blocks = []
        
        # Find the recipes array
        array_start = content.find('const ')
        if array_start == -1:
            return recipe_blocks
        
        # Find the actual array content
        array_content_start = content.find('[', array_start)
        array_content_end = content.rfind('];')
        
        if array_content_start == -1 or array_content_end == -1:
            return recipe_blocks
        
        array_content = content[array_content_start+1:array_content_end]
        
        # Split by recipe objects (look for },\n  { pattern)
        current_pos = 0
        bracket_count = 0
        recipe_start = 0
        
        for i, char in enumerate(array_content):
            if char == '{':
                if bracket_count == 0:
                    recipe_start = i
                bracket_count += 1
            elif char == '}':
                bracket_count -= 1
                if bracket_count == 0:
                    # End of a recipe object
                    recipe_block = array_content[recipe_start:i+1]
                    if 'name:' in recipe_block:
                        recipe_blocks.append(recipe_block)
        
        return recipe_blocks
    
    def extract_recipe_details(self, recipe_block: str) -> Optional[Dict]:
        """Extract complete recipe details from TypeScript block"""
        try:
            # Extract name
            name_match = re.search(r'name:\s*[\'"]([^\'"]+)[\'"]', recipe_block)
            if not name_match:
                return None
            
            name = name_match.group(1)
            
            # Extract description
            desc_match = re.search(r'description:\s*[\'"]([^\'"]*)[\'"]', recipe_block)
            description = desc_match.group(1) if desc_match else ''
            
            # Extract ingredients
            ingredients = []
            ingredients_section = re.search(r'ingredients:\s*\[(.*?)\]', recipe_block, re.DOTALL)
            if ingredients_section:
                ingredients_text = ingredients_section.group(1)
                
                # Parse individual ingredients - simpler approach
                # Look for { name: 'xxx', amount: nnn, unit: 'xxx' } patterns
                ingredient_lines = ingredients_text.split('\n')
                current_ingredient = {}
                
                for line in ingredient_lines:
                    line = line.strip()
                    if line.startswith('{ name:') or line.startswith('{'):
                        # Start of new ingredient
                        current_ingredient = {}
                    
                    # Extract name
                    name_match = re.search(r'name:\s*[\'"]([^\'"]+)[\'"]', line)
                    if name_match:
                        current_ingredient['name'] = name_match.group(1)
                    
                    # Extract amount
                    amount_match = re.search(r'amount:\s*([0-9.]+)', line)
                    if amount_match:
                        current_ingredient['amount'] = float(amount_match.group(1))
                    
                    # Extract unit
                    unit_match = re.search(r'unit:\s*[\'"]([^\'"]*)[\'"]', line)
                    if unit_match:
                        current_ingredient['unit'] = unit_match.group(1)
                    
                    # Extract notes
                    notes_match = re.search(r'notes:\s*[\'"]([^\'"]*)[\'"]', line)
                    if notes_match:
                        current_ingredient['notes'] = notes_match.group(1)
                    
                    # End of ingredient
                    if line.endswith('},') or line.endswith('}'):
                        if 'name' in current_ingredient:
                            if 'notes' not in current_ingredient:
                                current_ingredient['notes'] = ''
                            ingredients.append(current_ingredient)
                        current_ingredient = {}
            
            # Extract instructions
            instructions = []
            instructions_section = re.search(r'instructions:\s*\[(.*?)\]', recipe_block, re.DOTALL)
            if instructions_section:
                instructions_text = instructions_section.group(1)
                instruction_strings = re.findall(r'[\'"]([^\'"]+)[\'"]', instructions_text)
                instructions = instruction_strings
            
            return {
                'name': name,
                'description': description,
                'ingredients': ingredients,
                'instructions': instructions
            }
        
        except Exception as e:
            print(f"⚠️  Error extracting recipe details: {e}")
            return None
    
    def load_extraction_phases(self):
        """Load extraction results from different phases"""
        extraction_files = {
            'original_ocr': 'enhanced_extracted_recipes/enhanced_hsca_recipes.json',
            'improved': 'enhanced_extracted_recipes/improved_hsca_recipes.json',
            'perfect': 'enhanced_extracted_recipes/perfect_hsca_recipes.json',
            'character_perfect': 'enhanced_extracted_recipes/character_perfect_hsca_recipes.json'
        }
        
        for phase_name, file_path in extraction_files.items():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    recipes = data.get('extracted_recipes', [])
                    self.extraction_phases[phase_name] = recipes
                    print(f"📥 Loaded {len(recipes)} recipes from {phase_name} phase")
            except FileNotFoundError:
                print(f"⚠️  {file_path} not found, skipping {phase_name} phase")
                self.extraction_phases[phase_name] = []
    
    def find_matching_recipes(self) -> List[Dict]:
        """Find recipes that exist in both TypeScript database and extraction output"""
        matches = []
        
        for ts_name, ts_recipe in self.typescript_recipes.items():
            # Look for matches in each extraction phase
            phase_matches = {}
            
            for phase_name, phase_recipes in self.extraction_phases.items():
                best_match = self.find_best_extraction_match(ts_recipe, phase_recipes)
                if best_match:
                    phase_matches[phase_name] = best_match
            
            if phase_matches:
                match_data = {
                    'typescript_recipe': ts_recipe,
                    'typescript_name': ts_name,
                    'extraction_matches': phase_matches
                }
                matches.append(match_data)
        
        self.matched_recipes = matches
        print(f"🎯 Found {len(matches)} recipes with cross-reference matches")
        return matches
    
    def find_best_extraction_match(self, ts_recipe: Dict, extraction_recipes: List[Dict]) -> Optional[Dict]:
        """Find best matching extraction recipe for a TypeScript recipe"""
        ts_name = ts_recipe['name'].lower()
        best_match = None
        best_score = 0.0
        
        for extracted_recipe_data in extraction_recipes:
            extracted_recipe = extracted_recipe_data.get('recipe', {})
            extracted_name = extracted_recipe.get('name', '').lower()
            
            # Calculate similarity score
            similarity = SequenceMatcher(None, ts_name, extracted_name).ratio()
            
            # Also try fuzzy matching with corruption patterns
            cleaned_extracted = self.clean_ocr_corruption(extracted_name)
            cleaned_similarity = SequenceMatcher(None, ts_name, cleaned_extracted).ratio()
            
            final_score = max(similarity, cleaned_similarity)
            
            if final_score > best_score and final_score > 0.5:
                best_score = final_score
                best_match = {
                    'recipe_data': extracted_recipe_data,
                    'recipe': extracted_recipe,
                    'similarity_score': final_score,
                    'cleaned_name': cleaned_extracted
                }
        
        return best_match
    
    def clean_ocr_corruption(self, text: str) -> str:
        """Clean common OCR corruption patterns"""
        if not text:
            return ""
        
        cleaned = text.lower()
        
        # Character substitutions
        char_map = {
            '0': 'o', '1': 'i', '3': 'e', '5': 's', '6': 'g', '7': 't', '8': 'b'
        }
        
        for corrupted, correct in char_map.items():
            cleaned = cleaned.replace(corrupted, correct)
        
        # Space insertion for camelCase-like patterns
        cleaned = re.sub(r'([a-z])([A-Z])', r'\\1 \\2', cleaned)
        
        # Insert spaces in known patterns
        patterns = [
            (r'cucumber\\s*agua\\s*fresca', 'cucumber agua fresca'),
            (r'beet\\s*and\\s*apple\\s*juice', 'beet and apple juice'),
            (r'pomegranate.*blueberry.*ginger.*elixir', 'pomegranate blueberry and ginger elixir')
        ]
        
        for pattern, replacement in patterns:
            cleaned = re.sub(pattern, replacement, cleaned)
        
        # Clean up multiple spaces
        cleaned = re.sub(r'\\s+', ' ', cleaned)
        
        return cleaned.strip()
    
    def analyze_character_accuracy(self, match_data: Dict) -> Dict:
        """Analyze character-level accuracy for a matched recipe"""
        ts_recipe = match_data['typescript_recipe']
        extraction_matches = match_data['extraction_matches']
        
        analysis = {
            'typescript_name': ts_recipe['name'],
            'typescript_ingredients_count': len(ts_recipe['ingredients']),
            'typescript_instructions_count': len(ts_recipe['instructions']),
            'phase_analysis': {}
        }
        
        for phase_name, extraction_match in extraction_matches.items():
            extracted_recipe = extraction_match['recipe']
            
            # Name accuracy
            name_accuracy = SequenceMatcher(
                None, 
                ts_recipe['name'].lower(), 
                extracted_recipe.get('name', '').lower()
            ).ratio()
            
            # Ingredient accuracy
            ingredient_accuracy = self.calculate_ingredient_accuracy(
                ts_recipe['ingredients'], 
                extracted_recipe.get('ingredients', [])
            )
            
            # Instruction accuracy
            instruction_accuracy = self.calculate_instruction_accuracy(
                ts_recipe['instructions'],
                extracted_recipe.get('instructions', [])
            )
            
            analysis['phase_analysis'][phase_name] = {
                'similarity_score': extraction_match['similarity_score'],
                'name_accuracy': name_accuracy,
                'ingredient_accuracy': ingredient_accuracy,
                'instruction_accuracy': instruction_accuracy,
                'overall_accuracy': (name_accuracy + ingredient_accuracy + instruction_accuracy) / 3,
                'extracted_name': extracted_recipe.get('name', ''),
                'cleaned_name': extraction_match.get('cleaned_name', ''),
                'ingredient_count': len(extracted_recipe.get('ingredients', [])),
                'instruction_count': len(extracted_recipe.get('instructions', []))
            }
        
        return analysis
    
    def calculate_ingredient_accuracy(self, ts_ingredients: List[Dict], extracted_ingredients: List) -> float:
        """Calculate ingredient parsing accuracy"""
        if not ts_ingredients or not extracted_ingredients:
            return 0.0
        
        # Count how many TypeScript ingredients have reasonable matches
        matched_count = 0
        
        for ts_ing in ts_ingredients:
            ts_name = ts_ing['name'].lower()
            
            # Look for similar ingredient in extracted list
            for ext_ing in extracted_ingredients:
                if isinstance(ext_ing, dict):
                    ext_name = ext_ing.get('name', '').lower()
                else:
                    ext_name = str(ext_ing).lower()
                
                # Clean OCR corruption from extracted ingredient
                cleaned_ext_name = self.clean_ocr_corruption(ext_name)
                
                # Check similarity
                similarity = SequenceMatcher(None, ts_name, cleaned_ext_name).ratio()
                if similarity > 0.4:  # Lower threshold for ingredient matching
                    matched_count += 1
                    break
        
        return matched_count / len(ts_ingredients)
    
    def calculate_instruction_accuracy(self, ts_instructions: List[str], extracted_instructions: List) -> float:
        """Calculate instruction parsing accuracy"""
        if not ts_instructions or not extracted_instructions:
            return 0.0
        
        # Simple count-based accuracy (more sophisticated analysis possible)
        count_similarity = min(len(extracted_instructions), len(ts_instructions)) / len(ts_instructions)
        
        # Text similarity for first few instructions
        text_similarities = []
        for i in range(min(len(ts_instructions), len(extracted_instructions), 3)):
            ts_inst = ts_instructions[i].lower()
            
            if isinstance(extracted_instructions[i], dict):
                ext_inst = extracted_instructions[i].get('text', str(extracted_instructions[i])).lower()
            else:
                ext_inst = str(extracted_instructions[i]).lower()
            
            similarity = SequenceMatcher(None, ts_inst, ext_inst).ratio()
            text_similarities.append(similarity)
        
        avg_text_similarity = sum(text_similarities) / len(text_similarities) if text_similarities else 0.0
        
        return (count_similarity + avg_text_similarity) / 2
    
    def generate_cross_reference_report(self) -> Dict:
        """Generate comprehensive cross-reference analysis report"""
        if not self.matched_recipes:
            self.find_matching_recipes()
        
        report = {
            'total_typescript_recipes': len(self.typescript_recipes),
            'total_matched_recipes': len(self.matched_recipes),
            'match_percentage': len(self.matched_recipes) / len(self.typescript_recipes) * 100,
            'phase_statistics': {},
            'detailed_analysis': [],
            'accuracy_improvements': {},
            'top_matches': [],
            'problem_recipes': []
        }
        
        # Calculate phase statistics
        for phase_name in self.extraction_phases.keys():
            phase_stats = {
                'recipes_with_matches': 0,
                'avg_name_accuracy': 0.0,
                'avg_ingredient_accuracy': 0.0,
                'avg_instruction_accuracy': 0.0,
                'avg_overall_accuracy': 0.0
            }
            
            accuracies = {
                'name': [],
                'ingredient': [],
                'instruction': [],
                'overall': []
            }
            
            for match_data in self.matched_recipes:
                analysis = self.analyze_character_accuracy(match_data)
                
                if phase_name in analysis['phase_analysis']:
                    phase_stats['recipes_with_matches'] += 1
                    phase_data = analysis['phase_analysis'][phase_name]
                    
                    accuracies['name'].append(phase_data['name_accuracy'])
                    accuracies['ingredient'].append(phase_data['ingredient_accuracy'])
                    accuracies['instruction'].append(phase_data['instruction_accuracy'])
                    accuracies['overall'].append(phase_data['overall_accuracy'])
                    
                    analysis['phase_name'] = phase_name
                    report['detailed_analysis'].append(analysis)
            
            # Calculate averages
            for metric in ['name', 'ingredient', 'instruction', 'overall']:
                if accuracies[metric]:
                    phase_stats[f'avg_{metric}_accuracy'] = sum(accuracies[metric]) / len(accuracies[metric])
            
            report['phase_statistics'][phase_name] = phase_stats
        
        # Find accuracy improvements between phases
        self.calculate_phase_improvements(report)
        
        # Identify top matches and problem cases
        self.identify_notable_cases(report)
        
        return report
    
    def calculate_phase_improvements(self, report: Dict):
        """Calculate accuracy improvements between phases"""
        phases = ['original_ocr', 'improved', 'perfect', 'character_perfect']
        improvements = {}
        
        for i in range(len(phases) - 1):
            current_phase = phases[i]
            next_phase = phases[i + 1]
            
            if current_phase in report['phase_statistics'] and next_phase in report['phase_statistics']:
                current_stats = report['phase_statistics'][current_phase]
                next_stats = report['phase_statistics'][next_phase]
                
                improvements[f'{current_phase}_to_{next_phase}'] = {
                    'name_improvement': next_stats['avg_name_accuracy'] - current_stats['avg_name_accuracy'],
                    'ingredient_improvement': next_stats['avg_ingredient_accuracy'] - current_stats['avg_ingredient_accuracy'],
                    'instruction_improvement': next_stats['avg_instruction_accuracy'] - current_stats['avg_instruction_accuracy'],
                    'overall_improvement': next_stats['avg_overall_accuracy'] - current_stats['avg_overall_accuracy']
                }
        
        report['accuracy_improvements'] = improvements
    
    def identify_notable_cases(self, report: Dict):
        """Identify top matches and problem recipes"""
        all_analyses = report['detailed_analysis']
        
        # Sort by best overall accuracy in final phase
        final_phase_analyses = []
        for analysis in all_analyses:
            if 'character_perfect' in analysis['phase_analysis']:
                final_phase_analyses.append(analysis)
        
        # Top matches
        top_matches = sorted(
            final_phase_analyses,
            key=lambda x: x['phase_analysis']['character_perfect']['overall_accuracy'],
            reverse=True
        )[:5]
        
        # Problem recipes (low accuracy)
        problem_recipes = sorted(
            final_phase_analyses,
            key=lambda x: x['phase_analysis']['character_perfect']['overall_accuracy']
        )[:5]
        
        report['top_matches'] = top_matches
        report['problem_recipes'] = problem_recipes
    
    def save_cross_reference_report(self, report: Dict):
        """Save cross-reference analysis report"""
        with open('cross_reference_analysis_report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Generate markdown report
        markdown_report = self.generate_markdown_report(report)
        with open('cross_reference_analysis_report.md', 'w', encoding='utf-8') as f:
            f.write(markdown_report)
        
        print("✅ Cross-reference analysis report saved")
        print(f"📊 Analyzed {report['total_matched_recipes']} matched recipes")
        print(f"📈 Match rate: {report['match_percentage']:.1f}%")
    
    def generate_markdown_report(self, report: Dict) -> str:
        """Generate markdown version of cross-reference report"""
        md = "# 🔍 Cross-Reference Analysis Report\\n\\n"
        md += "## TypeScript Database vs Extraction Output Comparison\\n\\n"
        
        md += f"- **Total TypeScript Recipes**: {report['total_typescript_recipes']}\\n"
        md += f"- **Matched Recipes**: {report['total_matched_recipes']}\\n"
        md += f"- **Match Rate**: {report['match_percentage']:.1f}%\\n\\n"
        
        # Phase statistics
        md += "## 📊 Phase Statistics\\n\\n"
        for phase, stats in report['phase_statistics'].items():
            md += f"### {phase.replace('_', ' ').title()}\\n"
            md += f"- **Recipes with Matches**: {stats['recipes_with_matches']}\\n"
            md += f"- **Avg Name Accuracy**: {stats['avg_name_accuracy']:.1%}\\n"
            md += f"- **Avg Ingredient Accuracy**: {stats['avg_ingredient_accuracy']:.1%}\\n"
            md += f"- **Avg Instruction Accuracy**: {stats['avg_instruction_accuracy']:.1%}\\n"
            md += f"- **Avg Overall Accuracy**: {stats['avg_overall_accuracy']:.1%}\\n\\n"
        
        # Top matches
        md += "## 🏆 Top Performing Matches\\n\\n"
        for i, match in enumerate(report['top_matches'], 1):
            if 'character_perfect' in match['phase_analysis']:
                cp_data = match['phase_analysis']['character_perfect']
                md += f"### {i}. {match['typescript_name']}\\n"
                md += f"- **Overall Accuracy**: {cp_data['overall_accuracy']:.1%}\\n"
                md += f"- **Name Accuracy**: {cp_data['name_accuracy']:.1%}\\n"
                md += f"- **Extracted Name**: `{cp_data['extracted_name']}`\\n\\n"
        
        return md

def main():
    """Run cross-reference validation analysis"""
    validator = CrossReferenceValidator()
    
    print("🔍 CROSS-REFERENCE VALIDATION ANALYSIS")
    print("=" * 50)
    
    # Find matching recipes
    matches = validator.find_matching_recipes()
    
    if matches:
        # Generate comprehensive report
        report = validator.generate_cross_reference_report()
        validator.save_cross_reference_report(report)
        
        print("\\n📋 ANALYSIS SUMMARY:")
        print(f"  • TypeScript recipes: {report['total_typescript_recipes']}")
        print(f"  • Matched recipes: {report['total_matched_recipes']}")
        print(f"  • Match rate: {report['match_percentage']:.1f}%")
        
        # Show phase improvements
        if 'original_ocr_to_character_perfect' in report['accuracy_improvements']:
            improvement = report['accuracy_improvements']['original_ocr_to_character_perfect']
            print(f"  • Overall improvement: +{improvement['overall_improvement']:.1%}")
            print(f"  • Name improvement: +{improvement['name_improvement']:.1%}")
            print(f"  • Ingredient improvement: +{improvement['ingredient_improvement']:.1%}")
        
        print("\\n🎉 CROSS-REFERENCE ANALYSIS COMPLETE!")
    else:
        print("❌ No matching recipes found")

if __name__ == "__main__":
    main()