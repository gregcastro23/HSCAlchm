import Link from 'next/link'
import { Recipe } from '../types/recipe'

interface RecipeCardProps {
  recipe: Recipe
}

export default function RecipeCard({ recipe }: RecipeCardProps) {
  const totalIngredients = recipe.ingredients.length
  const primaryMealType = recipe.mealType[0] || 'General'

  return (
    <Link href={`/recipes/${encodeURIComponent(recipe.name.toLowerCase().replace(/\s+/g, '-'))}`}>
      <div className="card p-6 cursor-pointer group">
        {/* Header */}
        <div className="mb-4">
          <div className="flex items-start justify-between mb-2">
            <span className="elemental-badge bg-primary-100 text-primary-800">
              {primaryMealType}
            </span>
            <span className="text-sm text-gray-500">{recipe.timeToMake}</span>
          </div>
          <h3 className="text-xl font-serif font-semibold text-gray-900 group-hover:text-orange-700 transition-colors line-clamp-2">
            {recipe.name}
          </h3>
        </div>

        {/* Description */}
        <p className="text-gray-600 text-sm mb-4 line-clamp-3">
          {recipe.description}
        </p>

        {/* Key Details */}
        <div className="space-y-2 mb-4">
          <div className="flex items-center text-sm text-gray-500">
            <span className="font-medium">Cuisine:</span>
            <span className="ml-2">{recipe.cuisine}</span>
          </div>
          <div className="flex items-center text-sm text-gray-500">
            <span className="font-medium">Ingredients:</span>
            <span className="ml-2">{totalIngredients} items</span>
          </div>
        </div>

        {/* Elemental Balance Preview */}
        <div className="mb-4">
          <div className="text-xs font-medium text-gray-700 mb-2">Elemental Balance</div>
          <div className="flex space-x-1">
            {Object.entries(recipe.elementalBalance).map(([element, percentage]) => {
              const colors = {
                Fire: 'bg-red-400',
                Earth: 'bg-amber-400',
                Water: 'bg-blue-400',
                Air: 'bg-green-400'
              }
              return (
                <div
                  key={element}
                  className={`h-2 rounded-full ${colors[element as keyof typeof colors]}`}
                  style={{ width: `${percentage * 100}%` }}
                  title={`${element}: ${(percentage * 100).toFixed(0)}%`}
                />
              )
            })}
          </div>
        </div>

        {/* Nutrition Preview */}
        <div className="pt-4 border-t border-gray-100">
          <div className="grid grid-cols-4 gap-2 text-center">
            <div>
              <div className="text-lg font-semibold text-gray-900">{recipe.nutrition.calories}</div>
              <div className="text-xs text-gray-500">cal</div>
            </div>
            <div>
              <div className="text-lg font-semibold text-gray-900">{recipe.nutrition.protein}g</div>
              <div className="text-xs text-gray-500">protein</div>
            </div>
            <div>
              <div className="text-lg font-semibold text-gray-900">{recipe.nutrition.carbs}g</div>
              <div className="text-xs text-gray-500">carbs</div>
            </div>
            <div>
              <div className="text-lg font-semibold text-gray-900">{recipe.nutrition.fat}g</div>
              <div className="text-xs text-gray-500">fat</div>
            </div>
          </div>
        </div>
      </div>
    </Link>
  )
}
