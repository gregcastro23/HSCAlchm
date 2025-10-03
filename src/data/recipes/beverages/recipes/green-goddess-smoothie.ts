import { Recipe } from '../../../../types/recipe';

export const greengoddesssmoothie: Recipe = {
    name: 'Green Goddess Smoothie',
    description: 'A nutrient-packed green smoothie with spinach, avocado, and tropical fruits.',
    ingredients: [
      { name: 'baby spinach', amount: 2, unit: 'cups' },
      { name: 'ripe avocado', amount: 0.5, unit: '' },
      { name: 'frozen mango chunks', amount: 1, unit: 'cup' },
      { name: 'frozen pineapple chunks', amount: 1, unit: 'cup' },
      { name: 'coconut water', amount: 1, unit: 'cup' },
      { name: 'lime juice', amount: 1, unit: 'tbsp' },
      { name: 'ginger, grated', amount: 1, unit: 'tsp' },
      { name: 'honey', amount: 1, unit: 'tbsp', swaps: ['agave nectar'] }
    ],
    nutrition: {
      calories: 280,
      protein: 5,
      carbs: 45,
      fat: 12,
      vitamins: ['A', 'C', 'K', 'E'],
      minerals: ['Potassium', 'Magnesium']
    },
    timeToMake: '5 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Breakfast', 'Snack'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.3,
      Water: 0.4,
      Air: 0.2
    },
    instructions: [
      'Combine all ingredients in a high-speed blender.',
      'Blend until smooth and creamy.',
      'Taste and adjust sweetness if needed.',
      'Pour into glasses and serve immediately.'
    ]
  },;