import { Recipe } from '../../../../types/recipe';

export const wholegrainpancakes: Recipe = {
    name: 'Whole Grain Pancakes',
    description: 'Fluffy and nutritious pancakes made with whole grain flour and topped with fresh berries.',
    ingredients: [
      { name: 'whole wheat flour', amount: 1.5, unit: 'cups' },
      { name: 'baking powder', amount: 2, unit: 'tsp' },
      { name: 'cinnamon', amount: 1, unit: 'tsp' },
      { name: 'salt', amount: 0.25, unit: 'tsp' },
      { name: 'almond milk', amount: 1.5, unit: 'cups', swaps: ['oat milk', 'soy milk'] },
      { name: 'eggs', amount: 2, unit: '' },
      { name: 'maple syrup', amount: 2, unit: 'tbsp', swaps: ['honey'] },
      { name: 'vanilla extract', amount: 1, unit: 'tsp' },
      { name: 'coconut oil, melted', amount: 3, unit: 'tbsp' },
      { name: 'mixed berries', amount: 2, unit: 'cups' }
    ],
    nutrition: {
      calories: 280,
      protein: 8,
      carbs: 42,
      fat: 10,
      vitamins: ['B1', 'B2', 'C'],
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
      'In a large bowl, whisk together whole wheat flour, baking powder, cinnamon, and salt.',
      'In another bowl, combine almond milk, eggs, maple syrup, and vanilla extract.',
      'Pour wet ingredients into dry ingredients and mix until just combined.',
      'Stir in melted coconut oil.',
      'Heat a griddle or non-stick pan over medium heat.',
      'Pour 1/4 cup batter for each pancake.',
      'Cook until bubbles form on surface, then flip and cook other side.',
      'Serve warm with fresh berries and additional maple syrup.'
    ]
  },;