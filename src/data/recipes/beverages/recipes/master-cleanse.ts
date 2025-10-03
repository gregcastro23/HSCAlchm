import { Recipe } from '../../../../types/recipe';

export const mastercleanse: Recipe = {
    name: 'Master Cleanse',
    description: 'A traditional cleansing drink combining citrus, maple syrup, and cayenne.',
    ingredients: [
      { name: 'filtered water', amount: 10, unit: 'oz', notes: 'room temperature or warm' },
      { name: 'lemon juice', amount: 2, unit: 'tbsp', notes: 'freshly squeezed' },
      { name: 'maple syrup', amount: 2, unit: 'tbsp', notes: 'grade B or dark' },
      { name: 'cayenne pepper', amount: 0.1, unit: 'tsp', notes: 'or to taste' }
    ],
    nutrition: {
      calories: 110,
      protein: 0,
      carbs: 28,
      fat: 0,
      vitamins: ['C', 'B6'],
      minerals: ['Potassium', 'Manganese']
    },
    timeToMake: '5 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Beverage'],
    elementalBalance: {
      Fire: 0.4,
      Earth: 0.1,
      Water: 0.3,
      Air: 0.2
    },
    instructions: [
      'In a glass, combine filtered water with fresh lemon juice.',
      'Stir in maple syrup until fully dissolved.',
      'Add cayenne pepper and stir well.',
      'Adjust ingredients to taste if needed.',
      'Serve immediately.'
    ]
  },;