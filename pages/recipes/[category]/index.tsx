import { useRouter } from 'next/router'
import Layout from '../../../components/Layout'
import Link from 'next/link'
import { appetizerRecipes } from '../../../src/data/recipes/appetizers/index'
import { dinnerRecipes } from '../../../src/data/recipes/dinner/index'
import { sideRecipes } from '../../../src/data/recipes/sides/index'
import { soupRecipes } from '../../../src/data/recipes/soups/index'
import { saladRecipes } from '../../../src/data/recipes/salads/index'
import { dessertRecipes } from '../../../src/data/recipes/desserts/index'
import { beverageRecipes } from '../../../src/data/recipes/beverages/index'
import { condimentRecipes } from '../../../src/data/recipes/condiments/index'

const recipeCategories = {
  appetizers: appetizerRecipes,
  main: dinnerRecipes,
  sides: sideRecipes,
  soups: soupRecipes,
  salads: saladRecipes,
  desserts: dessertRecipes,
  beverages: beverageRecipes,
  condiments: condimentRecipes,
}

export default function CategoryPage() {
  const router = useRouter()
  const { category } = router.query
  
  const recipes = category ? recipeCategories[category as keyof typeof recipeCategories] : []

  return (
    <Layout>
      <h1>{category ? `${category.charAt(0).toUpperCase()}${category.slice(1)}` : 'Loading...'}</h1>
      <div className="recipe-grid">
        {recipes?.map((recipe) => (
          <Link 
            href={`/recipes/${category}/${recipe.name.toLowerCase().replace(/\s+/g, '-')}`}
            key={recipe.name}
          >
            <div className="recipe-card">
              <h2>{recipe.name}</h2>
              <p>{recipe.description}</p>
              <p>Time: {recipe.timeToMake}</p>
            </div>
          </Link>
        ))}
      </div>
      <style jsx>{`
        .recipe-grid {
          display: grid;
          grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
          gap: 20px;
          padding: 20px 0;
        }
        .recipe-card {
          border: 1px solid #eee;
          padding: 15px;
          border-radius: 8px;
          cursor: pointer;
          transition: transform 0.2s;
        }
        .recipe-card:hover {
          transform: translateY(-3px);
          box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
      `}</style>
    </Layout>
  )
} 