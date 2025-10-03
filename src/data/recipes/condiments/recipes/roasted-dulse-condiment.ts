import { Recipe } from '../../../../types/recipe';

export const roasteddulsecondiment: Recipe = {
    name: 'Roasted Dulse Condiment',
    description: 'A savory seaweed-based condiment perfect for adding umami flavor to dishes.',
    ingredients: [
      { name: 'dulse', amount: 0.5, unit: 'cup', swaps: ['nori'] },
      { name: 'sesame seeds, toasted', amount: 0.5, unit: 'cup' }
    ],
    nutrition: {
      calories: 140,
      protein: 5,
      carbs: 8,
      fat: 11,
      vitamins: ['B12', 'A'],
      minerals: ['Iodine', 'Iron', 'Magnesium']
    },
    timeToMake: '15 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Condiment'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.4,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'Preheat oven to 350° F. Place dulse on half sheet pan with parchment and bake for 10 minutes.',
      'Combine toasted sesame seeds with roasted dulse in suribachi and grind until most of seeds are broken.',
      'Serve as a condiment over cooked millet.',
      'Store excess in air-tight glass container.'
    ]
  },;