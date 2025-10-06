import React, { useState } from 'react';
// import { generateRecipe } from '../utils/recipeGenerator';
import { Recipe } from '../types/recipe';

export default function RecipeBuilder() {
  const [mealType, setMealType] = useState('Appetizer');
  const [generatedRecipe] = useState<Recipe | null>(null);

  const handleGenerate = () => {
    // Temporarily disabled - recipe generation not implemented
    alert('Recipe generation is not currently available.');
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Recipe Builder</h1>
      <select
        value={mealType}
        onChange={(e) => setMealType(e.target.value)}
        className="mb-4 p-2 border rounded"
      >
        <option>Appetizer</option>
        <option>Breakfast</option>
        <option>Lunch</option>
        <option>Dinner</option>
        <option>Dessert</option>
        {/* Add more options as needed */}
      </select>
      <button
        onClick={handleGenerate}
        className="bg-blue-500 text-white p-2 rounded"
      >
        Generate Recipe
      </button>
      {generatedRecipe && (
        <div className="mt-4 border p-4 rounded">
          <h2 className="text-xl font-semibold">{generatedRecipe.name}</h2>
          <p>{generatedRecipe.description}</p>
          <h3>Ingredients:</h3>
          <ul>
            {generatedRecipe.ingredients.map((ing, idx) => (
              <li key={idx}>{ing.amount.toFixed(1)} {ing.unit} {ing.name}</li>
            ))}
          </ul>
          {/* Add more display fields as needed */}
        </div>
      )}
    </div>
  );
}
