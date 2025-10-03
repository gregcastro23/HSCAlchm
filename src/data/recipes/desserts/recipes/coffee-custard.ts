import { Recipe } from '../../../../types/recipe';

export const coffeecustard: Recipe = {
    name: 'Coffee Custard',
    description: 'A dairy-free coffee custard with maple and pecan garnish.',
    ingredients: [
      { name: 'almond milk', amount: 3.5, unit: 'cups' },
      { name: 'agar flakes', amount: 2, unit: 'tbsp' },
      { name: 'maple syrup', amount: 0.5, unit: 'cup' },
      { name: 'kuzu', amount: 1, unit: 'tbsp' },
      { name: 'instant coffee', amount: 0.25, unit: 'cup' },
      { name: 'water', amount: 0.5, unit: 'cup' },
      { name: 'maple crystals', amount: 0.5, unit: 'cup' },
      { name: 'pecans, toasted', amount: 0.5, unit: 'cup' }
    ],
    nutrition: {
      calories: 180,
      protein: 3,
      carbs: 32,
      fat: 6,
      vitamins: ['E'],
      minerals: ['Manganese', 'Magnesium']
    },
    timeToMake: '30 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Dessert'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.3,
      Water: 0.4,
      Air: 0.1
    },
    instructions: [
      'In 2 ½ quart pot, combine milk and agar. Soak agar 5 minutes.',
      'Bring mixture to boil, lower heat, and simmer uncovered for about 5 minutes or more, until agar is completely dissolved.',
      'Add maple syrup and stir until combined.',
      'Dissolve kuzu and coffee in water until there are no lumps. Add to milk mixture and simmer until slightly thickened.',
      'Lightly oil ramekins and sprinkle 2 teaspoons maple crystals in bottom of each ramekin.',
      'Pour custard into ramekins. Refrigerate to set.',
      'When custard is set, run paring knife around side of each ramekin to separate custard.',
      'Invert custard onto plate. Garnish with pecans.'
    ]
  },;