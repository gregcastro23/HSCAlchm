import { Recipe } from '../../../../types/recipe';

export const applephylloroll: Recipe = {
    name: 'Apple Phyllo Roll',
    description: 'A delicate and crispy pastry filled with spiced apples and wrapped in flaky phyllo dough.',
    ingredients: [
      { name: 'phyllo dough sheets', amount: 8, unit: '' },
      { name: 'apples', amount: 4, unit: 'large', notes: 'peeled and thinly sliced' },
      { name: 'lemon juice', amount: 1, unit: 'tbsp' },
      { name: 'maple syrup', amount: 0.25, unit: 'cup' },
      { name: 'cinnamon', amount: 1, unit: 'tsp' },
      { name: 'nutmeg', amount: 0.25, unit: 'tsp' },
      { name: 'coconut oil, melted', amount: 0.333, unit: 'cup' },
      { name: 'almonds', amount: 0.5, unit: 'cup', notes: 'finely chopped' }
    ],
    nutrition: {
      calories: 260,
      protein: 4,
      carbs: 38,
      fat: 12,
      vitamins: ['C', 'E'],
      minerals: ['Iron', 'Magnesium']
    },
    timeToMake: '45 minutes',
    season: ['fall', 'winter'],
    cuisine: 'HSCA',
    mealType: ['Dessert'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.3,
      Water: 0.2,
      Air: 0.3
    },
    instructions: [
      'Preheat oven to 375°F.',
      'In a bowl, combine sliced apples, lemon juice, maple syrup, cinnamon, and nutmeg.',
      'Lay out one phyllo sheet and brush with melted coconut oil.',
      'Layer another sheet on top and repeat until all sheets are used.',
      'Spread apple mixture along one long edge of the phyllo stack.',
      'Sprinkle with chopped almonds.',
      'Roll up carefully, tucking in edges.',
      'Brush top with remaining coconut oil.',
      'Bake for 25-30 minutes until golden brown and crispy.'
    ]
  };