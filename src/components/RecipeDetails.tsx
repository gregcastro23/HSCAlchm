import React from 'react';
import { useParams } from 'react-router-dom';
import { Card, CardHeader, CardContent } from '@/components/ui/card';
import { allRecipes } from '../data/recipes';

const RecipeDetails = () => {
  const { recipeName } = useParams();
  const recipe = allRecipes.find(r => r.name === decodeURIComponent(recipeName || ''));

  if (!recipe) {
    return <div>Recipe not found</div>;
  }

  return (
    <div className="w-full max-w-4xl mx-auto p-4">
      <Card>
        <CardHeader>
          <h2 className="text-2xl font-bold">{recipe.name}</h2>
          <p className="text-gray-600">{recipe.description}</p>
          <div className="mt-2 text-sm">
            <span className="mr-4">Time: {recipe.timeToMake}</span>
            <span>Cuisine: {recipe.cuisine}</span>
          </div>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h3 className="text-xl font-semibold mb-3">Ingredients</h3>
              <ul className="list-disc list-inside space-y-2">
                {recipe.ingredients.map((ingredient, index) => (
                  <li key={index}>
                    {ingredient.amount} {ingredient.unit} {ingredient.name}
                    {ingredient.swaps && (
                      <span className="text-gray-500">
                        {' '}
                        (or {ingredient.swaps.join(', ')})
                      </span>
                    )}
                  </li>
                ))}
              </ul>
            </div>
            <div>
              <h3 className="text-xl font-semibold mb-3">Instructions</h3>
              <ol className="list-decimal list-inside space-y-2">
                {recipe.instructions.map((instruction, index) => (
                  <li key={index} className="pl-2">{instruction}</li>
                ))}
              </ol>
            </div>
          </div>
          <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h3 className="text-xl font-semibold mb-3">Nutrition</h3>
              <div className="grid grid-cols-2 gap-2">
                <div>Calories: {recipe.nutrition.calories}</div>
                <div>Protein: {recipe.nutrition.protein}g</div>
                <div>Carbs: {recipe.nutrition.carbs}g</div>
                <div>Fat: {recipe.nutrition.fat}g</div>
              </div>
            </div>
            <div>
              <h3 className="text-xl font-semibold mb-3">Elemental Balance</h3>
              <div className="grid grid-cols-2 gap-2">
                <div>Fire: {recipe.elementalBalance.Fire * 100}%</div>
                <div>Earth: {recipe.elementalBalance.Earth * 100}%</div>
                <div>Water: {recipe.elementalBalance.Water * 100}%</div>
                <div>Air: {recipe.elementalBalance.Air * 100}%</div>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default RecipeDetails; 