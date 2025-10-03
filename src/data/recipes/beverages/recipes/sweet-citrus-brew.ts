import { Recipe } from '../../../../types/recipe';

export const sweetcitrusbrew: Recipe = {
    name: 'Sweet Citrus Brew',
    description: 'A refreshing citrus-infused tea blend with subtle sweetness.',
    ingredients: [
      { name: 'green tea bags', amount: 4, unit: '' },
      { name: 'orange', amount: 1, unit: '', notes: 'sliced' },
      { name: 'lemon', amount: 1, unit: '', notes: 'sliced' },
      { name: 'honey', amount: 2, unit: 'tbsp', swaps: ['agave nectar'] },
      { name: 'fresh mint leaves', amount: 0.25, unit: 'cup' },
      { name: 'filtered water', amount: 4, unit: 'cups' }
    ],
    nutrition: {
      calories: 40,
      protein: 0,
      carbs: 10,
      fat: 0,
      vitamins: ['C', 'A'],
      minerals: ['Potassium']
    },
    timeToMake: '20 minutes',
    season: ['spring', 'summer'],
    cuisine: 'HSCA',
    mealType: ['Beverage'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.1,
      Water: 0.4,
      Air: 0.3
    },
    instructions: [
      'Bring water to just below boiling.',
      'Add tea bags and steep for 3-4 minutes.',
      'Remove tea bags and add honey, stirring until dissolved.',
      'Add citrus slices and mint leaves.',
      'Let cool to room temperature.',
      'Serve over ice and garnish with additional citrus slices if desired.'
    ]
  };