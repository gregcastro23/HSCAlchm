import { Recipe } from '../../../../types/recipe';

export const berrychiapudding: Recipe = {
    name: 'Berry Chia Pudding',
    description: 'A healthy and delicious dessert made with chia seeds and fresh berries.',
    ingredients: [
      { name: 'chia seeds', amount: 0.5, unit: 'cup' },
      { name: 'almond milk', amount: 2, unit: 'cups', swaps: ['coconut milk', 'oat milk'] },
      { name: 'maple syrup', amount: 3, unit: 'tbsp', swaps: ['honey'] },
      { name: 'vanilla extract', amount: 1, unit: 'tsp' },
      { name: 'mixed berries', amount: 2, unit: 'cups' },
      { name: 'sliced almonds', amount: 0.25, unit: 'cup' }
    ],
    nutrition: {
      calories: 220,
      protein: 8,
      carbs: 28,
      fat: 12,
      vitamins: ['C', 'E'],
      minerals: ['Calcium', 'Omega-3']
    },
    timeToMake: '10 minutes (plus 4 hours chilling)',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Dessert', 'Breakfast'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.3,
      Water: 0.4,
      Air: 0.2
    },
    instructions: [
      'In a medium bowl, whisk together chia seeds, almond milk, maple syrup, and vanilla extract.',
      'Cover and refrigerate for at least 4 hours or overnight.',
      'Stir pudding to break up any clumps.',
      'Layer pudding with fresh berries in serving glasses.',
      'Top with sliced almonds and serve chilled.'
    ]
  },;