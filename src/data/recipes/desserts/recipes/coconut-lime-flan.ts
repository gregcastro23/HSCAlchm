import { Recipe } from '../../../../types/recipe';

export const coconutlimeflan: Recipe = {
    name: 'Coconut-Lime Flan',
    description: 'A tropical dairy-free flan with coconut milk and lime.',
    ingredients: [
      { name: 'coconut milk', amount: 3.5, unit: 'cups' },
      { name: 'agar flakes', amount: 2, unit: 'tbsp' },
      { name: 'maple syrup', amount: 0.5, unit: 'cup' },
      { name: 'kuzu', amount: 1, unit: 'tbsp' },
      { name: 'lime juice', amount: 3, unit: 'tbsp' },
      { name: 'water', amount: 0.5, unit: 'cup' },
      { name: 'maple crystals', amount: 0.5, unit: 'cup' },
      { name: 'toasted dried coconut', amount: 0.5, unit: 'cup' }
    ],
    nutrition: {
      calories: 220,
      protein: 2,
      carbs: 26,
      fat: 14,
      vitamins: ['C'],
      minerals: ['Iron', 'Manganese']
    },
    timeToMake: '30 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Dessert'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.3,
      Water: 0.5,
      Air: 0.1
    },
    instructions: [
      'In 2 ½ quart pot, combine coconut milk and agar. Soak agar for 5 minutes.',
      'Bring mixture to boil. Reduce heat and simmer uncovered until agar is completely dissolved.',
      'Add maple syrup and stir until combined.',
      'Dissolve kuzu in lime juice and water until there are no lumps. Add to milk mixture and simmer until thickened.',
      'Lightly oil ramekins and sprinkle maple crystals in bottom of each ramekin.',
      'Pour custard into ramekins. Refrigerate to set.',
      'When set, run paring knife around the side of each ramekin to separate custard.',
      'Invert custard onto plate. Garnish with coconut.'
    ]
  },;