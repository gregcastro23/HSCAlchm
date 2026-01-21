import { Recipe, Ingredient } from '../types/recipe';
import { allRecipes } from '../data/recipes';
import { findRecipesByMealType, findRecipesBySeason } from './recipeHelpers';

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
}

type EnhancedRecipe = Recipe & {
  cookingMethods?: string[];
  numberOfServings?: number;
  prepTime?: number;
  cookTime?: number;
  elementalProperties?: { Fire: number; Earth: number; Water: number; Air: number };
};

export class RecipeGenerator {
  private generateRecipeName(_criteria: RecipeBuildingCriteria): string {
    return 'Generated Recipe';
  }

  private generateRecipeDescription(_criteria: RecipeBuildingCriteria): string {
    return 'A delicious generated recipe';
  }

  private selectIngredientsFromCriteria(_criteria: RecipeBuildingCriteria): Ingredient[] {
    return [];
  }

  private generateBaseInstructions(_ingredients: Ingredient[], _methods: string[]): string[] {
    return [];
  }

  private selectCookingMethodsFromCriteria(_criteria: RecipeBuildingCriteria): string[] {
    return [];
  }

  private estimatePrepTime(_ingredients: Ingredient[], _instructions: string[]): number {
    return 15;
  }

  private estimateCookTime(_methods: string[]): number {
    return 30;
  }

  private calculateBaseElementalProperties(_ingredients: Ingredient[]): { Fire: number; Earth: number; Water: number; Air: number } {
    return { Fire: 0.25, Earth: 0.25, Water: 0.25, Air: 0.25 };
  }

  private createBaseRecipe(criteria: RecipeBuildingCriteria): Partial<EnhancedRecipe> {
    let baseRecipe: Partial<EnhancedRecipe> = {};

    const targetCuisine = criteria.cuisine?.toLowerCase() || 'hsca';
    const targetMealType = criteria.mealType?.[0] || 'dinner';
    const targetSeason = criteria.season || criteria.currentSeason || 'all';

    let matchingRecipes = allRecipes.filter(r => r.cuisine.toLowerCase() === targetCuisine);
    matchingRecipes = findRecipesByMealType(matchingRecipes, targetMealType);
    matchingRecipes = findRecipesBySeason(matchingRecipes, targetSeason);

    if (matchingRecipes.length > 0) {
      const selectedRecipe = getRandomElement(matchingRecipes);
      baseRecipe = {
        name: selectedRecipe.name || this.generateRecipeName(criteria),
        description: selectedRecipe.description || this.generateRecipeDescription(criteria),
        cuisine: selectedRecipe.cuisine,
        ingredients: selectedRecipe.ingredients || [],
        instructions: selectedRecipe.instructions || [],
        cookingMethods: [],
        season: selectedRecipe.season || [targetSeason],
        mealType: selectedRecipe.mealType || [targetMealType],
        numberOfServings: criteria.servings || 4,
        prepTime: this.estimatePrepTime([], []),
        cookTime: this.estimateCookTime([]),
        elementalProperties: selectedRecipe.elementalBalance || this.calculateBaseElementalProperties([]),
      };

      if (criteria.requiredIngredients) {
        criteria.requiredIngredients.forEach(ing => {
          if (!baseRecipe.ingredients?.some(i => i.name === ing)) {
            baseRecipe.ingredients?.push({ name: ing, amount: 1, unit: '' });
          }
        });
      }
    } else {
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
        elementalProperties: this.calculateBaseElementalProperties([]),
      };
    }

    return baseRecipe;
  }
}
