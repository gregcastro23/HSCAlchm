import { Recipe } from '../../../../types/recipe';

export const greenpowersmoothiebowl: Recipe = {
    name: 'Green Power Smoothie Bowl',
    description: 'A nutrient-rich smoothie bowl packed with greens, fruits, and superfood toppings.',
    ingredients: [
      { name: 'frozen banana', amount: 1, unit: 'large' },
      { name: 'spinach', amount: 2, unit: 'cups' },
      { name: 'frozen mango chunks', amount: 1, unit: 'cup' },
      { name: 'coconut water', amount: 1, unit: 'cup' },
      { name: 'protein powder', amount: 1, unit: 'scoop', swaps: ['hemp seeds'] },
      { name: 'ginger, grated', amount: 1, unit: 'tsp' },
      { name: 'granola', amount: 0.25, unit: 'cup' },
      { name: 'coconut flakes', amount: 2, unit: 'tbsp' },
      { name: 'fresh berries', amount: 0.5, unit: 'cup' }
    ],
    nutrition: {
      calories: 380,
      protein: 15,
      carbs: 62,
      fat: 8,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Iron', 'Potassium']
    },
    timeToMake: '10 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Breakfast'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.3,
      Water: 0.4,
      Air: 0.2
    },
    instructions: [
      'In a high-speed blender, combine banana, spinach, mango, coconut water, protein powder, and ginger.',
      'Blend until smooth and creamy. The mixture should be thicker than a regular smoothie.',
      'Pour into a bowl.',
      'Top with granola, coconut flakes, and fresh berries.',
      'Serve immediately.'
    ]
  },;