import { Recipe } from '../../../../types/recipe';

export const greenvitalityjuice: Recipe = {
    name: 'Green Vitality Juice',
    description: 'A nutrient-rich green juice blend that supports detoxification and energy.',
    ingredients: [
      { name: 'green apples', amount: 2, unit: '', notes: 'cored and cut into chunks' },
      { name: 'celery stalks', amount: 4, unit: '' },
      { name: 'cucumber', amount: 1, unit: '', notes: 'large' },
      { name: 'spinach', amount: 2, unit: 'cups' },
      { name: 'lemon', amount: 1, unit: '', notes: 'peeled' },
      { name: 'ginger', amount: 1, unit: 'inch' },
      { name: 'parsley', amount: 0.5, unit: 'cup' }
    ],
    nutrition: {
      calories: 120,
      protein: 3,
      carbs: 29,
      fat: 0,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Iron', 'Potassium']
    },
    timeToMake: '15 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Beverage'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.2,
      Water: 0.4,
      Air: 0.2
    },
    instructions: [
      'Wash all produce thoroughly.',
      'Cut produce into pieces that will fit through your juicer.',
      'Feed ingredients through the juicer, alternating leafy greens with harder vegetables.',
      'Stir juice and serve immediately.',
      'Can be stored in an airtight container for up to 24 hours.'
    ]
  },;