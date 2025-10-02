#!/usr/bin/env python3
"""
Recipe Accuracy Validator - Cross-checks pending recipes against approved database
"""

import json
import os
from typing import Dict, List, Set, Tuple
from collections import defaultdict
import difflib

class RecipeAccuracyValidator:
    def __init__(self):
        self.pending_dir = "staging/pending_recipes"
        self.approved_dir = "staging/approved_recipes"
        self.reports_dir = "reports"

    def load_json_file(self, filepath: str) -> Dict:
        """Load JSON file safely"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Error loading {filepath}: {e}")
            return {}

    def extract_recipe_names(self, data: Dict) -> Set[str]:
        """Extract recipe names from various JSON structures"""
        names = set()

        # Handle different JSON structures
        if 'lesson_summary' in data:
            # New extraction format
            for lesson_data in data['lesson_summary'].values():
                for recipe_name in lesson_data.get('recipe_names', []):
                    names.add(recipe_name)
        elif 'gold_standard_recipes' in data:
            # Gold standard format - recipes nested under IDs
            for recipe_id, recipe_data in data['gold_standard_recipes'].items():
                if isinstance(recipe_data, dict) and 'name' in recipe_data:
                    names.add(recipe_data['name'])
        elif 'extracted_recipes' in data:
            # Character perfect format
            for recipe_item in data['extracted_recipes']:
                if isinstance(recipe_item, dict) and 'recipe' in recipe_item and 'name' in recipe_item['recipe']:
                    name = recipe_item['recipe']['name']
                    names.add(name)
                else:
                    print(f"DEBUG: Skipping recipe_item with keys: {recipe_item.keys() if isinstance(recipe_item, dict) else type(recipe_item)}")
        elif 'recipes' in data:
            # Legacy format
            for recipe in data['recipes']:
                if isinstance(recipe, dict) and 'name' in recipe:
                    names.add(recipe['name'])
                elif isinstance(recipe, dict) and 'recipe' in recipe and 'name' in recipe['recipe']:
                    names.add(recipe['recipe']['name'])

        return names

    def normalize_recipe_name(self, name: str) -> str:
        """Normalize recipe name for better comparison"""
        # Remove OCR artifacts and normalize
        normalized = name.lower()
        # Replace common OCR errors
        ocr_fixes = {
            '0': 'o',
            '1': 'i',
            '5': 's',
            '8': 'b',
            '3': 'e'
        }
        for ocr_char, real_char in ocr_fixes.items():
            normalized = normalized.replace(ocr_char, real_char)

        # Remove extra spaces and special chars
        import re
        normalized = re.sub(r'[^\w\s]', '', normalized)
        normalized = ' '.join(normalized.split())

        return normalized

    def find_similar_recipes(self, pending_recipes: Set[str], approved_recipes: Set[str]) -> Dict:
        """Find similar recipes using fuzzy matching"""
        from difflib import SequenceMatcher

        similar_pairs = []
        matched_pending = set()
        matched_approved = set()

        # Normalize all names
        pending_normalized = {name: self.normalize_recipe_name(name) for name in pending_recipes}
        approved_normalized = {name: self.normalize_recipe_name(name) for name in approved_recipes}

        # Find matches with similarity > 0.8
        for pending_name, pending_norm in pending_normalized.items():
            best_match = None
            best_score = 0

            for approved_name, approved_norm in approved_normalized.items():
                if approved_name in matched_approved:
                    continue

                # Try exact match first
                if pending_norm == approved_norm:
                    best_match = approved_name
                    best_score = 1.0
                    break

                # Try fuzzy match
                score = SequenceMatcher(None, pending_norm, approved_norm).ratio()
                if score > best_score and score > 0.8:
                    best_match = approved_name
                    best_score = score

            if best_match and best_score > 0.7:  # Lower threshold for potential matches
                similar_pairs.append({
                    'pending': pending_name,
                    'approved': best_match,
                    'similarity': best_score,
                    'pending_normalized': pending_norm,
                    'approved_normalized': approved_normalized[best_match]
                })
                matched_pending.add(pending_name)
                matched_approved.add(best_match)

        return {
            'similar_pairs': similar_pairs,
            'matched_pending': matched_pending,
            'matched_approved': matched_approved,
            'similarity_count': len(similar_pairs)
        }

    def compare_recipe_sets(self, pending_recipes: Set[str], approved_recipes: Set[str]) -> Dict:
        """Compare two sets of recipes with fuzzy matching"""
        # Find similar recipes
        similarity_data = self.find_similar_recipes(pending_recipes, approved_recipes)

        # Calculate differences excluding similar matches
        unmatched_pending = pending_recipes - similarity_data['matched_pending']
        unmatched_approved = approved_recipes - similarity_data['matched_approved']

        new_recipes = unmatched_pending - unmatched_approved
        missing_recipes = unmatched_approved - unmatched_pending

        return {
            'new_recipes': sorted(list(new_recipes)),
            'existing_recipes': sorted(list(similarity_data['matched_pending'])),
            'missing_recipes': sorted(list(missing_recipes)),
            'pending_count': len(pending_recipes),
            'approved_count': len(approved_recipes),
            'new_count': len(new_recipes),
            'existing_count': len(similarity_data['matched_pending']),
            'missing_count': len(missing_recipes),
            'similar_pairs': similarity_data['similar_pairs'],
            'similarity_count': similarity_data['similarity_count']
        }

    def validate_pending_recipes(self) -> Dict:
        """Main validation function"""
        print("🔍 Starting Recipe Accuracy Validation")
        print("=" * 50)

        # Load approved recipes (character_perfect as baseline)
        approved_file = "enhanced_extracted_recipes/character_perfect_hsca_recipes.json"
        print(f"🔍 Loading approved recipes from: {approved_file}")
        approved_data = self.load_json_file(approved_file)

        if not approved_data:
            print("❌ No approved recipes found")
            return {}

        print(f"   Approved data keys: {list(approved_data.keys()) if isinstance(approved_data, dict) else type(approved_data)}")
        if 'extracted_recipes' in approved_data:
            print(f"   Number of extracted_recipes: {len(approved_data['extracted_recipes'])}")

        approved_names = self.extract_recipe_names(approved_data)
        print(f"✅ Loaded {len(approved_names)} approved recipes")
        print(f"   First few approved names: {sorted(list(approved_names))[:3]}")

        # Check for pending recipes
        pending_files = []
        if os.path.exists(self.pending_dir):
            pending_files = [f for f in os.listdir(self.pending_dir) if f.endswith('.json')]

        if not pending_files:
            print("❌ No pending recipes found")
            return {}

        results = {}

        for pending_file in pending_files:
            print(f"\n🔍 Validating: {pending_file}")
            pending_path = os.path.join(self.pending_dir, pending_file)
            pending_data = self.load_json_file(pending_path)

            if not pending_data:
                continue

            pending_names = self.extract_recipe_names(pending_data)
            print(f"📊 Found {len(pending_names)} recipes in pending file")
            print(f"   First few pending names: {sorted(list(pending_names))[:3]}")

            # Compare recipe sets
            comparison = self.compare_recipe_sets(pending_names, approved_names)

            # Detailed analysis
            analysis = self.analyze_recipe_differences(pending_data, approved_data, comparison)

            results[pending_file] = {
                'comparison': comparison,
                'analysis': analysis,
                'pending_data': pending_data,
                'approved_data': approved_data
            }

            # Print summary
            print(f"📈 Summary for {pending_file}:")
            print(f"   • New recipes: {comparison['new_count']}")
            print(f"   • Existing recipes: {comparison['existing_count']}")
            print(f"   • Missing recipes: {comparison['missing_count']}")

            if comparison['new_count'] > 0:
                print(f"   • Sample new recipes: {comparison['new_recipes'][:3]}")

            if comparison['missing_count'] > 0:
                print(f"   • Sample missing recipes: {comparison['missing_recipes'][:3]}")

        return results

    def analyze_recipe_differences(self, pending_data: Dict, approved_data: Dict, comparison: Dict) -> Dict:
        """Detailed analysis of recipe differences"""
        analysis = {
            'quality_improvements': [],
            'potential_issues': [],
            'recommendations': []
        }

        # Check for quality improvements in new recipes
        if 'lesson_summary' in pending_data:
            total_ingredients = 0
            total_instructions = 0
            recipe_count = 0

            for lesson_data in pending_data['lesson_summary'].values():
                recipe_count += lesson_data.get('recipes_found', 0)
                total_ingredients += lesson_data.get('avg_ingredients_per_recipe', 0) * lesson_data.get('recipes_found', 0)
                total_instructions += lesson_data.get('avg_instructions_per_recipe', 0) * lesson_data.get('recipes_found', 0)

            if recipe_count > 0:
                avg_ingredients = total_ingredients / recipe_count
                avg_instructions = total_instructions / recipe_count

                analysis['quality_improvements'].append({
                    'metric': 'ingredient_completeness',
                    'value': avg_ingredients,
                    'description': f"Average {avg_ingredients:.1f} ingredients per recipe"
                })

                analysis['quality_improvements'].append({
                    'metric': 'instruction_completeness',
                    'value': avg_instructions,
                    'description': f"Average {avg_instructions:.1f} instructions per recipe"
                })

        # Check for potential issues
        if comparison['missing_count'] > 0:
            analysis['potential_issues'].append({
                'issue': 'missing_recipes',
                'count': comparison['missing_count'],
                'description': f"{comparison['missing_count']} previously approved recipes not found in new extraction"
            })

        # Generate recommendations
        if comparison['new_count'] > 0 and comparison['missing_count'] == 0:
            analysis['recommendations'].append({
                'action': 'approve_new_recipes',
                'description': f"Approve {comparison['new_count']} new recipes - no existing recipes lost"
            })
        elif comparison['missing_count'] > 0:
            analysis['recommendations'].append({
                'action': 'investigate_missing',
                'description': f"Investigate {comparison['missing_count']} missing recipes before approval"
            })

        return analysis

    def generate_validation_report(self, results: Dict) -> str:
        """Generate comprehensive validation report"""
        report = []
        report.append("# Recipe Accuracy Validation Report")
        report.append("=" * 50)
        import datetime
        report.append(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")

        for filename, result in results.items():
            report.append(f"## Validation Results: {filename}")
            report.append("")

            comp = result['comparison']
            analysis = result['analysis']

            # Use corrected counts that account for similarity matching
            total_pending = comp['pending_count']
            total_approved = comp['approved_count']
            truly_new = comp['new_count']
            matched_existing = comp['existing_count']
            truly_missing = comp['missing_count']
            similar_count = comp['similarity_count']

            report.append("### Summary Statistics")
            report.append(f"- **Pending recipes**: {total_pending}")
            report.append(f"- **Approved recipes**: {total_approved}")
            report.append(f"- **Truly new recipes**: {truly_new}")
            report.append(f"- **Matched existing recipes**: {matched_existing} (via similarity)")
            report.append(f"- **Missing recipes**: {truly_missing}")
            report.append(f"- **Similar matches found**: {similar_count}")
            report.append(f"- **Total coverage**: {matched_existing + truly_new}/{total_pending} ({(matched_existing + truly_new)/total_pending*100:.1f}%)")
            report.append("")

            if comp['similarity_count'] > 0:
                report.append("### Similar Recipe Matches")
                report.append("These recipes appear to be the same but with different naming/OCR:")
                for match in comp['similar_matches'][:10]:  # Show first 10
                    report.append(f"- **{match['pending']}** → *{match['approved']}* (similarity: {match['similarity']:.2f})")
                if comp['similarity_count'] > 10:
                    report.append(f"- ... and {comp['similarity_count'] - 10} more similar matches")
                report.append("")

            if comp['new_count'] > 0:
                report.append("### Truly New Recipes Found")
                for recipe in comp['new_recipes'][:10]:  # Show first 10
                    report.append(f"- {recipe}")
                if comp['new_count'] > 10:
                    report.append(f"- ... and {comp['new_count'] - 10} more")
                report.append("")

            if comp['missing_count'] > 0:
                report.append("### Missing Recipes (Previously Approved)")
                for recipe in comp['missing_recipes'][:10]:  # Show first 10
                    report.append(f"- {recipe}")
                if comp['missing_count'] > 10:
                    report.append(f"- ... and {comp['missing_count'] - 10} more")
                report.append("")

            if analysis['quality_improvements']:
                report.append("### Quality Improvements")
                for improvement in analysis['quality_improvements']:
                    report.append(f"- {improvement['description']}")
                report.append("")

            if analysis['potential_issues']:
                report.append("### Potential Issues")
                for issue in analysis['potential_issues']:
                    report.append(f"- ⚠️ {issue['description']}")
                report.append("")

            if analysis['recommendations']:
                report.append("### Recommendations")
                for rec in analysis['recommendations']:
                    report.append(f"- ✅ {rec['description']}")
                report.append("")

        return "\n".join(report)

def main():
    validator = RecipeAccuracyValidator()
    results = validator.validate_pending_recipes()

    if results:
        # Generate and save report
        report = validator.generate_validation_report(results)

        os.makedirs(validator.reports_dir, exist_ok=True)
        report_file = os.path.join(validator.reports_dir, "recipe_accuracy_validation_report.md")

        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)

        print("\n📄 Validation report saved to:")
        print(f"   {report_file}")

        # Summary
        total_new = sum(r['comparison']['new_count'] for r in results.values())
        total_missing = sum(r['comparison']['missing_count'] for r in results.values())

        print("\n🎯 Overall Summary:")
        print(f"   • New recipes to review: {total_new}")
        print(f"   • Missing recipes to investigate: {total_missing}")

        if total_missing == 0 and total_new > 0:
            print("   ✅ Ready for approval - no regressions detected!")
        elif total_missing > 0:
            print("   ⚠️ Requires investigation - some approved recipes missing")

    else:
        print("❌ No validation results generated")

if __name__ == "__main__":
    main()
