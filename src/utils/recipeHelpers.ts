import { Recipe } from '../types/recipe';

export const calculateTotalCalories = (recipe: Recipe): number => {
  return recipe.nutrition.calories;
};

export const findRecipesByIngredient = (recipes: Recipe[], ingredient: string): Recipe[] => {
  return recipes.filter(recipe => 
    recipe.ingredients.some(ing => 
      ing.name.toLowerCase().includes(ingredient.toLowerCase())
    )
  );
};

export const findRecipesByMealType = (recipes: Recipe[], mealType: string): Recipe[] => {
  return recipes.filter(recipe => 
    recipe.mealType.some(type => 
      type.toLowerCase() === mealType.toLowerCase()
    )
  );
};

export const findRecipesBySeason = (recipes: Recipe[], season: string): Recipe[] => {
  return recipes.filter(recipe => 
    recipe.season.some(s => 
      s.toLowerCase() === season.toLowerCase()
    )
  );
};
