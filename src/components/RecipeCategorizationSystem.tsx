import React, { useState } from 'react';
import { Card, CardHeader, CardContent } from '@/components/ui/card';
import { Recipe } from '../types/recipe';
import { allRecipes } from '../data/recipes';
import { Link } from 'react-router-dom';

const RecipeCategorizationSystem = () => {
  const [selectedCategory, setSelectedCategory] = useState<string>('all');

  const categories = [
    'Breakfast',
    'Lunch',
    'Dinner',
    'Appetizer',
    'Side Dish',
    'Sauce',
    'Dessert',
    'Salad'
  ];

  // Filter recipes based on mealType instead of category
  const filteredRecipes = selectedCategory === 'all'
    ? allRecipes
    : allRecipes.filter(recipe => recipe.mealType.includes(selectedCategory));

  return (
    <div className="w-full max-w-6xl mx-auto p-4">
      <div className="mb-6">
        <h1 className="text-3xl font-bold mb-4">HSCA Recipe Collection</h1>
        <div className="flex flex-wrap gap-2">
          <button
            className={`px-4 py-2 rounded ${
              selectedCategory === 'all' ? 'bg-blue-500 text-white' : 'bg-gray-200'
            }`}
            onClick={() => setSelectedCategory('all')}
          >
            All
          </button>
          {categories.map(category => (
            <button
              key={category}
              className={`px-4 py-2 rounded capitalize ${
                selectedCategory === category ? 'bg-blue-500 text-white' : 'bg-gray-200'
              }`}
              onClick={() => setSelectedCategory(category)}
            >
              {category}
            </button>
          ))}
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {filteredRecipes.map((recipe) => (
          <Link 
            key={recipe.name} 
            to={`/recipes/${encodeURIComponent(recipe.name)}`}
          >
            <Card className="h-full hover:shadow-lg transition-shadow">
              <CardHeader>
                <h3 className="text-xl font-semibold">{recipe.name}</h3>
                <div className="text-sm text-gray-500 capitalize">
                  {recipe.mealType.join(', ')}
                </div>
              </CardHeader>
              <CardContent>
                <div className="mb-4">
                  <h4 className="font-medium mb-2">Details:</h4>
                  <div className="text-sm">
                    <div>Time: {recipe.timeToMake}</div>
                    <div>Season: {recipe.season.join(', ')}</div>
                    <div>Cuisine: {recipe.cuisine}</div>
                  </div>
                </div>
                <div className="mb-4">
                  <h4 className="font-medium mb-2">Ingredients:</h4>
                  <ul className="list-disc list-inside text-sm">
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
                <div className="mb-4">
                  <h4 className="font-medium mb-2">Nutrition:</h4>
                  <div className="text-sm">
                    <div>Calories: {recipe.nutrition.calories}</div>
                    <div>Protein: {recipe.nutrition.protein}g</div>
                    <div>Carbs: {recipe.nutrition.carbs}g</div>
                    <div>Fat: {recipe.nutrition.fat}g</div>
                  </div>
                </div>
                <div>
                  <h4 className="font-medium mb-2">Elemental Balance:</h4>
                  <div className="text-sm">
                    <div>Fire: {recipe.elementalBalance.Fire * 100}%</div>
                    <div>Earth: {recipe.elementalBalance.Earth * 100}%</div>
                    <div>Water: {recipe.elementalBalance.Water * 100}%</div>
                    <div>Air: {recipe.elementalBalance.Air * 100}%</div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default RecipeCategorizationSystem; 