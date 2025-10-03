import { Recipe } from '../../../../types/recipe';

export const chocolatechipcookies: Recipe = {
    name: 'Chocolate Chip Cookies',
    description: 'Classic homemade chocolate chip cookies.',
    ingredients: [
      { name: 'all-purpose flour', amount: 2.25, unit: 'cups' },
      { name: 'baking soda', amount: 1, unit: 'tsp' },
      { name: 'salt', amount: 1, unit: 'tsp' },
      { name: 'butter, softened', amount: 1, unit: 'cup' },
      { name: 'granulated sugar', amount: 0.75, unit: 'cup' },
      { name: 'packed brown sugar', amount: 0.75, unit: 'cup' },
      { name: 'vanilla extract', amount: 1, unit: 'tsp' },
      { name: 'large eggs', amount: 2, unit: '' },
      { name: 'semisweet chocolate chips', amount: 2, unit: 'cups' },
      { name: 'chopped nuts (optional)', amount: 1, unit: 'cup', swaps: ['dried fruit'] }
    ],
    nutrition: {
      calories: 450,
      protein: 6,
      carbs: 62,
      fat: 24,
      vitamins: ['A', 'D'],
      minerals: ['Iron', 'Calcium']
    },
    timeToMake: '30 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Dessert'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.5,
      Water: 0.2,
      Air: 0.2
    },
    instructions: [
      'Preheat oven to 375° F. Line half sheet tray with parchment paper.',
      'In a small bowl, whisk together flour, baking soda and salt.',
      'In a large bowl, beat butter and sugars until light and fluffy, about 2 minutes.',
      'Beat in vanilla and then eggs one at a time until combined.',
      'Gradually stir flour mixture into butter mixture. Mix in chocolate chips and nuts (if using).',
      'Drop rounded tablespoons of dough onto prepared sheet tray about 2 inches apart.',
      'Bake until edges are lightly browned, 8 to 10 minutes. Cool on sheet tray 5 minutes before transferring to wire rack.'
    ]
  },;