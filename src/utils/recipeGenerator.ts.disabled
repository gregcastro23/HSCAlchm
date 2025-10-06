import { Recipe, Ingredient } from '../types/recipe';
import { allRecipes } from '../data/recipes';
import { findRecipesByMealType, findRecipesBySeason } from './recipeHelpers'; // Assuming these exist from previous codebase search

function getRandomElement<T>(arr: T[]): T {
  return arr[Math.floor(Math.random() * arr.length)];
}

type Season = 'spring' | 'summer' | 'fall' | 'winter' | 'all';

interface RecipeBuildingCriteria {
  cuisine?: string;
  mealType?: string[];
  season?: Season;
  currentSeason?: Season;
  requiredIngredients?: string[];
  servings?: number;
  // Add other criteria as needed
}

interface EnhancedRecipe extends Recipe {
  // Extend with any additional properties if needed
}

// Assuming this is part of a class
export class RecipeGenerator {
  private generateRecipeName(criteria: RecipeBuildingCriteria): string {
    // Your implementation
    return 'Generated Recipe';
  }

  private generateRecipeDescription(criteria: RecipeBuildingCriteria): string {
    // Your implementation
    return 'A delicious generated recipe';
  }

  private selectIngredientsFromCriteria(criteria: RecipeBuildingCriteria): Ingredient[] {
    // Your implementation
    return [];
  }

  private generateBaseInstructions(ingredients: Ingredient[], methods: string[]): string[] {
    // Your implementation
    return [];
  }

  private selectCookingMethodsFromCriteria(criteria: RecipeBuildingCriteria): string[] {
    // Your implementation
    return [];
  }

  private estimatePrepTime(ingredients: Ingredient[], instructions: string[]): number {
    // Your implementation
    return 15;
  }

  private estimateCookTime(methods: string[]): number {
    // Your implementation
    return 30;
  }

  private calculateBaseElementalProperties(ingredients: Ingredient[]): { Fire: number; Earth: number; Water: number; Air: number } {
    // Your implementation (or use average from previous generator)
    return { Fire: 0.25, Earth: 0.25, Water: 0.25, Air: 0.25 };
  }

  private createBaseRecipe(criteria: RecipeBuildingCriteria): Partial<EnhancedRecipe> {
    let baseRecipe: Partial<EnhancedRecipe> = {};

    const targetCuisine = criteria.cuisine?.toLowerCase() || 'hsca';
    const targetMealType = criteria.mealType?.[0] || 'dinner';
    const targetSeason = criteria.season || criteria.currentSeason || 'all';

    // Filter allRecipes for matches
    let matchingRecipes = allRecipes.filter(r => r.cuisine.toLowerCase() === targetCuisine);
    matchingRecipes = findRecipesByMealType(matchingRecipes, targetMealType);
    matchingRecipes = findRecipesBySeason(matchingRecipes, targetSeason);

    if (matchingRecipes.length > 0) {
      // Pick random match
      const selectedRecipe = getRandomElement(matchingRecipes);
      baseRecipe = {
        name: selectedRecipe.name || this.generateRecipeName(criteria),
        description: selectedRecipe.description || this.generateRecipeDescription(criteria),
        cuisine: selectedRecipe.cuisine,
        ingredients: selectedRecipe.ingredients || [],
        instructions: selectedRecipe.instructions || [],
        cookingMethods: selectedRecipe.cookingMethods || [], // Assuming this field exists or add if needed
        season: selectedRecipe.season || [targetSeason],
        mealType: selectedRecipe.mealType || [targetMealType],
        numberOfServings: criteria.servings || selectedRecipe.numberOfServings || 4, // Add numberOfServings if not in type
        prepTime: selectedRecipe.prepTime || this.estimatePrepTime([], []), // Add prepTime if needed
        cookTime: selectedRecipe.cookTime || this.estimateCookTime([]), // Add cookTime if needed
        elementalProperties: selectedRecipe.elementalBalance || this.calculateBaseElementalProperties([]) // Renamed to match your code
      };

      // Add required ingredients
      if (criteria.requiredIngredients) {
        criteria.requiredIngredients.forEach(ing => {
          if (!baseRecipe.ingredients?.some(i => i.name === ing)) {
            baseRecipe.ingredients?.push({ name: ing });
          }
        });
      }
    } else {
      // Fallback to generic creation
      baseRecipe = {
        name: this.generateRecipeName(criteria),
        description: this.generateRecipeDescription(criteria),
        cuisine: targetCuisine,
        ingredients: this.selectIngredientsFromCriteria(criteria),
        instructions: this.generateBaseInstructions([], []),
        cookingMethods: this.selectCookingMethodsFromCriteria(criteria),
        season: [targetSeason],
        mealType: [targetMealType],
        numberOfServings: criteria.servings || 4,
        prepTime: this.estimatePrepTime([], []),
        cookTime: this.estimateCookTime([]),
        elementalProperties: this.calculateBaseElementalProperties([])
      };
    }

    return baseRecipe;
  }
} 