import { useRouter } from 'next/router'
import Layout from '@/components/Layout'
import { Recipe } from '@/types/recipe'
import { allRecipes } from '@/src/data/recipes'

export default function RecipeDetails() {
  const router = useRouter()
  const { category, recipe: recipeSlug } = router.query

  const recipeData = allRecipes.find(r => 
    r.name.toLowerCase().replace(/\s+/g, '-') === recipeSlug &&
    r.mealType.some(type => type.toLowerCase() === category)
  )

  if (!recipeData) {
    return (
      <Layout>
        <div className="container mx-auto px-4 py-8">
          <h1 className="text-2xl font-bold text-red-600">Recipe not found</h1>
          <p className="mt-4">The requested recipe could not be found.</p>
        </div>
      </Layout>
    )
  }

  return (
    <Layout>
      <div className="w-full max-w-4xl mx-auto p-4">
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h1 className="text-3xl font-bold mb-4">{recipeData.name}</h1>
          <p className="text-gray-600 mb-6">{recipeData.description}</p>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div>
              <h2 className="text-xl font-semibold mb-3">Ingredients</h2>
              <ul className="space-y-2">
                {recipeData.ingredients.map((ing, index) => (
                  <li key={index} className="flex items-start">
                    <span className="mr-2">•</span>
                    <span>
                      {ing.amount} {ing.unit} {ing.name}
                      {ing.notes && <span className="text-gray-500"> ({ing.notes})</span>}
                    </span>
                  </li>
                ))}
              </ul>
            </div>

            <div>
              <h2 className="text-xl font-semibold mb-3">Instructions</h2>
              <ol className="space-y-3">
                {recipeData.instructions.map((step, index) => (
                  <li key={index} className="pl-4">
                    <span className="font-medium mr-2">{index + 1}.</span>
                    {step}
                  </li>
                ))}
              </ol>
            </div>
          </div>

          <div className="mt-8 grid grid-cols-1 md:grid-cols-2 gap-8">
            <div>
              <h2 className="text-xl font-semibold mb-3">Details</h2>
              <div className="space-y-2 text-gray-600">
                <p>Time to Make: {recipeData.timeToMake}</p>
                <p>Season: {recipeData.season.join(', ')}</p>
                <p>Cuisine: {recipeData.cuisine}</p>
              </div>
            </div>

            <div>
              <h2 className="text-xl font-semibold mb-3">Nutrition</h2>
              <div className="grid grid-cols-2 gap-2 text-gray-600">
                <p>Calories: {recipeData.nutrition.calories}</p>
                <p>Protein: {recipeData.nutrition.protein}g</p>
                <p>Carbs: {recipeData.nutrition.carbs}g</p>
                <p>Fat: {recipeData.nutrition.fat}g</p>
              </div>
              <div className="mt-4">
                <p>Vitamins: {recipeData.nutrition.vitamins.join(', ')}</p>
                <p>Minerals: {recipeData.nutrition.minerals.join(', ')}</p>
              </div>
            </div>
          </div>

          <div className="mt-8">
            <h2 className="text-xl font-semibold mb-3">Elemental Balance</h2>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              {Object.entries(recipeData.elementalBalance).map(([element, value]) => (
                <div key={element} className="text-center p-3 bg-gray-50 rounded">
                  <p className="font-medium">{element}</p>
                  <p className="text-gray-600">{(value * 100).toFixed(0)}%</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </Layout>
  )
} 