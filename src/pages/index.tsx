import { useRouter } from 'next/router'
import Layout from '@/components/Layout'
import Link from 'next/link'
import { allRecipes } from '@/data/recipes'

export default function CategoryPage() {
  const router = useRouter()
  const { category } = router.query
  
  // Filter recipes by category
  const recipes = allRecipes.filter(recipe => 
    recipe.mealType.some(type => 
      type.toLowerCase() === category?.toString().toLowerCase()
    )
  )

  return (
    <Layout>
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-8 capitalize">
          {category?.toString().replace('-', ' ')} Recipes
        </h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {recipes.map((recipe) => {
            const urlFriendlyName = recipe.name.toLowerCase()
              .replace(/é/g, 'e')
              .replace(/\s+/g, '-')
              .replace(/[^a-z0-9-]/g, '')

            return (
              <Link 
                key={recipe.name}
                href={`/recipes/${category}/${urlFriendlyName}`}
                className="block hover:shadow-lg transition-shadow"
              >
                <div className="border rounded-lg p-6 h-full bg-white">
                  <h2 className="text-xl font-semibold mb-2">{recipe.name}</h2>
                  <p className="text-gray-600 mb-4">{recipe.description}</p>
                  <div className="text-sm text-gray-500">
                    <p>Time: {recipe.timeToMake}</p>
                    <p>Cuisine: {recipe.cuisine}</p>
                  </div>
                </div>
              </Link>
            )
          })}
        </div>
      </div>
    </Layout>
  )
} 