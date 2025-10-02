import Link from 'next/link'

const categories = [
  { name: 'Home', path: '/' },
  { name: 'Appetizers', path: '/recipes/appetizer' },
  { name: 'Main Dishes', path: '/recipes/main' },
  { name: 'Sides', path: '/recipes/side' },
  { name: 'Soups', path: '/recipes/soup' },
  { name: 'Salads', path: '/recipes/salad' },
  { name: 'Desserts', path: '/recipes/dessert' },
  { name: 'Beverages', path: '/recipes/beverage' },
  { name: 'Condiments', path: '/recipes/condiment' }
]

export default function Navigation() {
  return (
    <nav className="bg-white shadow-md">
      <div className="container mx-auto px-4">
        <ul className="flex flex-wrap space-x-6 py-4">
          {categories.map((category) => (
            <li key={category.name}>
              <Link 
                href={category.path}
                className="text-gray-700 hover:text-blue-600 transition-colors"
              >
                {category.name}
              </Link>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  )
}