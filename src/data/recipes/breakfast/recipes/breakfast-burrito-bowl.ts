import { Recipe } from '../../../../types/recipe';

export const breakfastburritobowl: Recipe = {
    name: 'Breakfast Burrito Bowl',
    description: 'A hearty and healthy breakfast bowl with scrambled eggs, black beans, and fresh vegetables.',
    ingredients: [
      { name: 'brown rice, cooked', amount: 2, unit: 'cups' },
      { name: 'black beans, drained and rinsed', amount: 15, unit: 'oz' },
      { name: 'eggs', amount: 4, unit: '' },
      { name: 'cherry tomatoes, halved', amount: 1, unit: 'cup' },
      { name: 'avocado, sliced', amount: 1, unit: '' },
      { name: 'red onion, diced', amount: 0.5, unit: '' },
      { name: 'cilantro, chopped', amount: 0.25, unit: 'cup' },
      { name: 'lime juice', amount: 2, unit: 'tbsp' },
      { name: 'olive oil', amount: 2, unit: 'tbsp' },
      { name: 'hot sauce', amount: 1, unit: 'tbsp', swaps: ['salsa'] }
    ],
    nutrition: {
      calories: 420,
      protein: 18,
      carbs: 52,
      fat: 16,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Iron', 'Potassium']
    },
    timeToMake: '20 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Breakfast', 'Brunch'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.4,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'Warm the cooked brown rice and black beans.',
      'Scramble the eggs in a pan with a little olive oil.',
      'Divide rice between bowls and top with scrambled eggs and black beans.',
      'Add cherry tomatoes, avocado slices, and diced red onion.',
      'Garnish with cilantro and a squeeze of lime juice.',
      'Drizzle with hot sauce if desired.',
      'Serve immediately while warm.'
    ]
  },;