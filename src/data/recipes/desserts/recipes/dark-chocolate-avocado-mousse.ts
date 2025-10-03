import { Recipe } from '../../../../types/recipe';

export const darkchocolateavocadomousse: Recipe = {
    name: 'Dark Chocolate Avocado Mousse',
    description: 'A rich and creamy chocolate mousse made with ripe avocados and dark chocolate.',
    ingredients: [
      { name: 'ripe avocados', amount: 2, unit: 'large' },
      { name: 'dark chocolate, melted', amount: 8, unit: 'oz' },
      { name: 'cocoa powder', amount: 0.25, unit: 'cup' },
      { name: 'maple syrup', amount: 0.333, unit: 'cup', swaps: ['honey'] },
      { name: 'vanilla extract', amount: 1, unit: 'tsp' },
      { name: 'almond milk', amount: 0.25, unit: 'cup' },
      { name: 'salt', amount: 0.125, unit: 'tsp' },
      { name: 'fresh raspberries', amount: 1, unit: 'cup' }
    ],
    nutrition: {
      calories: 280,
      protein: 4,
      carbs: 26,
      fat: 20,
      vitamins: ['E', 'K'],
      minerals: ['Magnesium', 'Potassium']
    },
    timeToMake: '15 minutes (plus 2 hours chilling)',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Dessert'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.4,
      Water: 0.4,
      Air: 0.1
    },
    instructions: [
      'In a food processor, blend avocados until smooth.',
      'Add melted chocolate, cocoa powder, maple syrup, vanilla, almond milk, and salt.',
      'Process until completely smooth and creamy.',
      'Divide into serving dishes.',
      'Refrigerate for at least 2 hours or until chilled.',
      'Top with fresh raspberries before serving.'
    ]
  },;