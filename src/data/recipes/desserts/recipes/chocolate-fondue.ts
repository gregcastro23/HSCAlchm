import { Recipe } from '../../../../types/recipe';

export const chocolatefondue: Recipe = {
    name: 'Chocolate Fondue',
    description: 'A rich and creamy dairy-free chocolate fondue perfect for dipping fruits and treats.',
    ingredients: [
      { name: 'dark chocolate', amount: 12, unit: 'oz', notes: 'chopped' },
      { name: 'coconut milk', amount: 1, unit: 'cup', notes: 'full fat' },
      { name: 'maple syrup', amount: 2, unit: 'tbsp' },
      { name: 'vanilla extract', amount: 1, unit: 'tsp' },
      { name: 'sea salt', amount: 0.125, unit: 'tsp' },
      { name: 'assorted fruits', amount: 4, unit: 'cups', notes: 'for dipping' },
      { name: 'nuts', amount: 1, unit: 'cup', notes: 'toasted, for dipping' }
    ],
    nutrition: {
      calories: 280,
      protein: 3,
      carbs: 22,
      fat: 21,
      vitamins: ['E'],
      minerals: ['Iron', 'Magnesium']
    },
    timeToMake: '15 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Dessert'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.4,
      Water: 0.3,
      Air: 0.1
    },
    instructions: [
      'Chop chocolate into small pieces for even melting.',
      'Heat coconut milk in a medium saucepan until just simmering.',
      'Remove from heat and add chopped chocolate.',
      'Let stand for 1 minute, then whisk until smooth.',
      'Stir in maple syrup, vanilla extract, and salt.',
      'Transfer to a fondue pot or serving bowl.',
      'Serve with assorted fruits and toasted nuts for dipping.',
      'Keep warm while serving.'
    ]
  };