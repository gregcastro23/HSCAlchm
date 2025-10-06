import { ChevronDown } from 'lucide-react'
import { useState } from 'react'

interface CategoryFilterProps {
  categories: string[]
  selectedCategory: string
  onCategoryChange: (category: string) => void
}

export default function CategoryFilter({
  categories,
  selectedCategory,
  onCategoryChange
}: CategoryFilterProps) {
  const [isOpen, setIsOpen] = useState(false)

  const allCategories = ['all', ...categories]

  return (
    <div className="relative">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full bg-white border border-gray-300 rounded-lg px-4 py-3 text-left shadow-sm focus:ring-2 focus:ring-orange-500 focus:border-orange-500 flex items-center justify-between"
      >
        <span className="text-gray-700">
          {selectedCategory === 'all' ? 'All Categories' : selectedCategory}
        </span>
        <ChevronDown className={`h-5 w-5 text-gray-400 transition-transform ${isOpen ? 'rotate-180' : ''}`} />
      </button>

      {isOpen && (
        <>
          {/* Backdrop */}
          <div
            className="fixed inset-0 z-10"
            onClick={() => setIsOpen(false)}
          />

          {/* Dropdown */}
          <div className="absolute z-20 w-full mt-1 bg-white border border-gray-300 rounded-lg shadow-lg max-h-60 overflow-y-auto">
            {allCategories.map((category) => (
              <button
                key={category}
                onClick={() => {
                  onCategoryChange(category)
                  setIsOpen(false)
                }}
                className={`w-full px-4 py-3 text-left hover:bg-gray-50 transition-colors ${
                  selectedCategory === category
                    ? 'bg-orange-50 text-orange-700 font-medium'
                    : 'text-gray-700'
                }`}
              >
                {category === 'all' ? 'All Categories' : category}
              </button>
            ))}
          </div>
        </>
      )}
    </div>
  )
}
