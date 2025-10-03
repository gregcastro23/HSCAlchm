import { Recipe } from '../../../../types/recipe';

export const quinoabreakfastbowl: Recipe = {
    name: 'Quinoa Breakfast Bowl',
    description: 'A warm and nourishing breakfast bowl with quinoa, fresh fruits, and nuts.',
    ingredients: [
      { name: 'quinoa', amount: 1, unit: 'cup' },
      { name: 'almond milk', amount: 2, unit: 'cups', swaps: ['oat milk', 'coconut milk'] },
      { name: 'cinnamon', amount: 1, unit: 'tsp' },
      { name: 'vanilla extract', amount: 0.5, unit: 'tsp' },
      { name: 'maple syrup', amount: 2, unit: 'tbsp', swaps: ['honey'] },
      { name: 'mixed berries', amount: 1, unit: 'cup' },
      { name: 'sliced almonds', amount: 0.25, unit: 'cup' },
      { name: 'chia seeds', amount: 1, unit: 'tbsp' }
    ],
    nutrition: {
      calories: 320,
      protein: 10,
      carbs: 48,
      fat: 12,
      vitamins: ['B1', 'B2', 'E'],
      minerals: ['Iron', 'Magnesium']
    },
    timeToMake: '25 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Breakfast'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.4,
      Water: 0.3,
      Air: 0.1
    },
    instructions: [
      'Rinse quinoa thoroughly under cold water.',
      'In a medium saucepan, combine quinoa, almond milk, cinnamon, and vanilla.',
      'Bring to a boil, then reduce heat and simmer for 15-20 minutes until quinoa is tender.',
      'Stir in maple syrup.',
      'Serve warm, topped with berries, almonds, and chia seeds.'
    ]
  },;