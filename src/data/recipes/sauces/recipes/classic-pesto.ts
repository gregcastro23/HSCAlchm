import { Recipe } from '../../../../types/recipe';

export const classicpesto: Recipe = {
    name: 'Classic Pesto',
    description: 'Fresh and vibrant basil pesto perfect for pasta, sandwiches, or as a dip.',
    ingredients: [
      { name: 'fresh basil leaves', amount: 2, unit: 'cups' },
      { name: 'pine nuts', amount: 0.333, unit: 'cup', swaps: ['walnuts', 'almonds'] },
      { name: 'garlic cloves', amount: 2, unit: '' },
      { name: 'Parmesan cheese, grated', amount: 0.5, unit: 'cup' },
      { name: 'extra virgin olive oil', amount: 0.5, unit: 'cup' },
      { name: 'lemon juice', amount: 1, unit: 'tbsp' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 150,
      protein: 3,
      carbs: 2,
      fat: 15,
      vitamins: ['K', 'A'],
      minerals: ['Iron', 'Calcium']
    },
    timeToMake: '15 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Sauce'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.3,
      Water: 0.2,
      Air: 0.3
    },
    instructions: [
      'Toast pine nuts in a dry skillet over medium heat until lightly golden and fragrant, about 3-5 minutes. Let cool.',
      'In a food processor, combine basil, cooled pine nuts, and garlic. Pulse until coarsely chopped.',
      'Add Parmesan cheese, olive oil, lemon juice, salt, and pepper.',
      'Process until smooth, scraping down the sides as needed.',
      'Taste and adjust seasoning if needed.',
      'Store in an airtight container in the refrigerator for up to 1 week, or freeze for up to 3 months.'
    ]
  },;