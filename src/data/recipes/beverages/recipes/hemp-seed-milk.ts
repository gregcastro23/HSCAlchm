import { Recipe } from '../../../../types/recipe';

export const hempseedmilk: Recipe = {
    name: 'Hemp Seed Milk',
    description: 'A creamy plant-based milk rich in omega fatty acids.',
    ingredients: [
      { name: 'hemp seeds', amount: 1, unit: 'cup' },
      { name: 'water', amount: 4, unit: 'cups' },
      { name: 'dates', amount: 2, unit: '', notes: 'pitted' },
      { name: 'vanilla extract', amount: 0.5, unit: 'tsp' },
      { name: 'sea salt', amount: 0.125, unit: 'tsp' }
    ],
    nutrition: {
      calories: 110,
      protein: 6,
      carbs: 3,
      fat: 9,
      vitamins: ['E', 'B1'],
      minerals: ['Iron', 'Zinc', 'Magnesium']
    },
    timeToMake: '10 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Beverage'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.3,
      Water: 0.4,
      Air: 0.2
    },
    instructions: [
      'Put all ingredients into high-speed blender and blend until smooth.',
      'Served milk chilled or warmed.'
    ]
  },;