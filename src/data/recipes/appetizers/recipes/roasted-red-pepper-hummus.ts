import { Recipe } from '../../../../types/recipe';

export const roastedredpepperhummus: Recipe = {
    name: 'Roasted Red Pepper Hummus',
    description: 'Creamy hummus with sweet roasted red peppers and tahini.',
    ingredients: [
      { name: 'chickpeas, drained and rinsed', amount: 15, unit: 'oz' },
      { name: 'roasted red peppers', amount: 12, unit: 'oz' },
      { name: 'tahini', amount: 0.333, unit: 'cup' },
      { name: 'garlic cloves', amount: 3, unit: '' },
      { name: 'lemon juice', amount: 0.25, unit: 'cup' },
      { name: 'olive oil', amount: 0.25, unit: 'cup' },
      { name: 'ground cumin', amount: 1, unit: 'tsp' },
      { name: 'smoked paprika', amount: 0.5, unit: 'tsp' },
      { name: 'salt', amount: 1, unit: 'tsp' }
    ],
    nutrition: {
      calories: 180,
      protein: 6,
      carbs: 16,
      fat: 12,
      vitamins: ['A', 'C', 'E'],
      minerals: ['Iron', 'Calcium']
    },
    timeToMake: '15 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Appetizer', 'Snack'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.4,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'In a food processor, combine chickpeas, roasted red peppers, tahini, and garlic.',
      'Process until smooth, scraping down sides as needed.',
      'With machine running, add lemon juice and olive oil in a steady stream.',
      'Add cumin, paprika, and salt. Process until well combined.',
      'Taste and adjust seasonings as needed.',
      'Serve with pita chips, vegetables, or use as a spread.'
    ]
  },;