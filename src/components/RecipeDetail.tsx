import { ArrowLeft, Clock, ChefHat, Flame, Leaf, Droplets, Wind } from 'lucide-react';
import Link from 'next/link';
import { Recipe } from '../types/recipe';
import ElementalBalanceChart from './ElementalBalanceChart';

interface RecipeDetailProps {
  recipe: Recipe
}

export default function RecipeDetail({ recipe }: RecipeDetailProps) {
  const elementalIcons = {
    Fire: Flame,
    Earth: Leaf,
    Water: Droplets,
    Air: Wind,
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header with Back Button */}
      <div className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <Link
            href="/"
            className="inline-flex items-center text-gray-600 hover:text-gray-900 transition-colors mb-4"
          >
            <ArrowLeft className="h-4 w-4 mr-2" />
            Back to Recipes
          </Link>

          {/* Recipe Header */}
          <div className="mb-6">
            <div className="flex flex-wrap items-center gap-3 mb-4">
              {recipe.mealType.map(type => (
                <span key={type} className="elemental-badge bg-primary-100 text-primary-800">
                  {type}
                </span>
              ))}
              <span className="elemental-badge bg-secondary-100 text-secondary-800">
                {recipe.cuisine}
              </span>
              {recipe.season.map(season => (
                <span key={season} className="elemental-badge bg-accent-100 text-accent-800">
                  {season}
                </span>
              ))}
            </div>

            <h1 className="text-4xl font-serif font-bold text-gray-900 mb-4">
              {recipe.name}
            </h1>

            <p className="text-xl text-gray-600 mb-6">
              {recipe.description}
            </p>

            <div className="flex items-center text-gray-500">
              <Clock className="h-5 w-5 mr-2" />
              <span>{recipe.timeToMake}</span>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Main Content */}
          <div className="lg:col-span-2 space-y-8">
            {/* Ingredients */}
            <div className="card p-6">
              <h2 className="text-2xl font-serif font-semibold text-gray-900 mb-6 flex items-center">
                <ChefHat className="h-6 w-6 mr-3 text-orange-600" />
                Ingredients
              </h2>
              <div className="space-y-3">
                {recipe.ingredients.map((ingredient, index) => (
                  <div key={index} className="flex items-start">
                    <div className="w-16 flex-shrink-0 text-right mr-4">
                      <span className="text-gray-600 font-medium">
                        {ingredient.amount === Math.floor(ingredient.amount)
                          ? ingredient.amount
                          : ingredient.amount.toFixed(2).replace(/\.?0+$/, '')
                        } {ingredient.unit}
                      </span>
                    </div>
                    <div className="flex-1">
                      <span className="text-gray-900">{ingredient.name}</span>
                      {ingredient.notes && (
                        <span className="text-gray-500 text-sm ml-2">
                          ({ingredient.notes})
                        </span>
                      )}
                      {ingredient.swaps && ingredient.swaps.length > 0 && (
                        <div className="text-sm text-gray-500 mt-1">
                          <span className="font-medium">Alternatives:</span> {ingredient.swaps.join(', ')}
                        </div>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Instructions */}
            <div className="card p-6">
              <h2 className="text-2xl font-serif font-semibold text-gray-900 mb-6">
                Instructions
              </h2>
              <ol className="space-y-4">
                {recipe.instructions.map((instruction, index) => (
                  <li key={index} className="flex">
                    <span className="flex-shrink-0 w-8 h-8 bg-orange-100 text-orange-800 rounded-full flex items-center justify-center text-sm font-medium mr-4 mt-0.5">
                      {index + 1}
                    </span>
                    <span className="text-gray-700 leading-relaxed">
                      {instruction}
                    </span>
                  </li>
                ))}
              </ol>
            </div>
          </div>

          {/* Sidebar */}
          <div className="space-y-8">
            {/* Elemental Balance */}
            <div className="card p-6">
              <h3 className="text-xl font-serif font-semibold text-gray-900 mb-4">
                Elemental Balance
              </h3>
              <ElementalBalanceChart balance={recipe.elementalBalance} />
              <div className="mt-4 space-y-2">
                {Object.entries(recipe.elementalBalance).map(([element, percentage]) => {
                  const IconComponent = elementalIcons[element as keyof typeof elementalIcons];
                  return (
                    <div key={element} className="flex items-center justify-between">
                      <div className="flex items-center">
                        <IconComponent className="h-4 w-4 mr-2 text-gray-500" />
                        <span className="text-gray-700">{element}</span>
                      </div>
                      <span className="text-gray-900 font-medium">
                        {(percentage * 100).toFixed(0)}%
                      </span>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Nutrition */}
            <div className="card p-6">
              <h3 className="text-xl font-serif font-semibold text-gray-900 mb-4">
                Nutritional Information
              </h3>
              <div className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <div className="text-center">
                    <div className="text-2xl font-bold text-gray-900">{recipe.nutrition.calories}</div>
                    <div className="text-sm text-gray-500">Calories</div>
                  </div>
                  <div className="text-center">
                    <div className="text-2xl font-bold text-gray-900">{recipe.nutrition.protein}g</div>
                    <div className="text-sm text-gray-500">Protein</div>
                  </div>
                  <div className="text-center">
                    <div className="text-2xl font-bold text-gray-900">{recipe.nutrition.carbs}g</div>
                    <div className="text-sm text-gray-500">Carbohydrates</div>
                  </div>
                  <div className="text-center">
                    <div className="text-2xl font-bold text-gray-900">{recipe.nutrition.fat}g</div>
                    <div className="text-sm text-gray-500">Fat</div>
                  </div>
                </div>

                {recipe.nutrition.vitamins.length > 0 && (
                  <div>
                    <div className="text-sm font-medium text-gray-700 mb-2">Vitamins</div>
                    <div className="flex flex-wrap gap-1">
                      {recipe.nutrition.vitamins.map(vitamin => (
                        <span key={vitamin} className="elemental-badge bg-green-100 text-green-800">
                          {vitamin}
                        </span>
                      ))}
                    </div>
                  </div>
                )}

                {recipe.nutrition.minerals.length > 0 && (
                  <div>
                    <div className="text-sm font-medium text-gray-700 mb-2">Minerals</div>
                    <div className="flex flex-wrap gap-1">
                      {recipe.nutrition.minerals.map(mineral => (
                        <span key={mineral} className="elemental-badge bg-blue-100 text-blue-800">
                          {mineral}
                        </span>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
