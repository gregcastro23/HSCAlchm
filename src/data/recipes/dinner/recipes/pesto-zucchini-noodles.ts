import { Recipe } from '../../../../types/recipe';

export const pestozucchininoodles: Recipe = {
    name: 'Pesto Zucchini Noodles',
    description: 'A light and refreshing dish featuring spiralized zucchini noodles tossed in homemade pesto sauce.',
    ingredients: [
      { name: 'zucchini, spiralized', amount: 4, unit: 'medium' },
      { name: 'basil leaves', amount: 2, unit: 'cups' },
      { name: 'pine nuts', amount: 0.25, unit: 'cup', swaps: ['walnuts', 'almonds'] },
      { name: 'Parmesan cheese, grated', amount: 0.5, unit: 'cup' },
      { name: 'garlic cloves', amount: 2, unit: '' },
      { name: 'lemon juice', amount: 2, unit: 'tbsp' },
      { name: 'olive oil', amount: 0.33, unit: 'cup' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' },
      { name: 'cherry tomatoes, halved', amount: 1, unit: 'cup' }
    ],
    nutrition: {
      calories: 280,
      protein: 8,
      carbs: 12,
      fat: 24,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Potassium', 'Manganese']
    },
    timeToMake: '20 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Entree'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.3,
      Water: 0.4,
      Air: 0.1
    },
    instructions: [
      'In a food processor, combine basil leaves, pine nuts, Parmesan cheese, garlic, lemon juice, olive oil, salt, and pepper. Process until smooth, scraping down the sides as needed.',
      'In a large bowl, toss spiralized zucchini noodles with the pesto sauce until evenly coated.',
      'Divide zucchini noodles among serving plates and top with halved cherry tomatoes.',
      'Serve immediately, garnished with additional Parmesan cheese and fresh basil leaves, if desired.'
    ]
  },;