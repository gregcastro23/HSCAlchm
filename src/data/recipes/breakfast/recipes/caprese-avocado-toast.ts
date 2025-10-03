import { Recipe } from '../../../../types/recipe';

export const capreseavocadotoast: Recipe = {
    name: 'Caprese Avocado Toast',
    description: 'A fresh and flavorful twist on classic avocado toast with tomatoes, mozzarella, and basil.',
    ingredients: [
      { name: 'whole grain bread', amount: 4, unit: 'slices' },
      { name: 'ripe avocados', amount: 2, unit: '' },
      { name: 'cherry tomatoes, halved', amount: 1, unit: 'cup' },
      { name: 'fresh mozzarella, torn', amount: 4, unit: 'oz' },
      { name: 'fresh basil leaves', amount: 0.25, unit: 'cup' },
      { name: 'olive oil', amount: 2, unit: 'tbsp' },
      { name: 'balsamic glaze', amount: 2, unit: 'tbsp' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' },
      { name: 'red pepper flakes', amount: 0.25, unit: 'tsp', swaps: [] }
    ],
    nutrition: {
      calories: 320,
      protein: 12,
      carbs: 28,
      fat: 20,
      vitamins: ['C', 'K', 'B6'],
      minerals: ['Potassium', 'Calcium']
    },
    timeToMake: '15 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Breakfast', 'Brunch'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.3,
      Water: 0.3,
      Air: 0.2
    },
    instructions: [
      'Toast the bread slices until golden brown.',
      'Mash the avocados in a bowl and season with salt and pepper.',
      'Spread mashed avocado evenly on each toast.',
      'Top with halved cherry tomatoes and torn mozzarella.',
      'Garnish with fresh basil leaves.',
      'Drizzle with olive oil and balsamic glaze.',
      'Sprinkle with red pepper flakes if desired.',
      'Serve immediately while toast is still warm.'
    ]
  },;