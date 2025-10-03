import { Recipe } from '../../../../types/recipe';

export const celerycarrotgingerjuice: Recipe = {
    name: 'Celery-Carrot-Ginger Juice',
    description: 'A cleansing and anti-inflammatory juice blend rich in minerals and antioxidants.',
    ingredients: [
      { name: 'celery stalks', amount: 8, unit: '', notes: 'washed' },
      { name: 'carrots', amount: 4, unit: 'large', notes: 'peeled' },
      { name: 'ginger', amount: 2, unit: 'inch', notes: 'peeled' },
      { name: 'lemon', amount: 0.5, unit: '', notes: 'peeled' },
      { name: 'green apple', amount: 1, unit: '', notes: 'cored and quartered' }
    ],
    nutrition: {
      calories: 95,
      protein: 2,
      carbs: 22,
      fat: 0,
      vitamins: ['A', 'K', 'C'],
      minerals: ['Potassium', 'Sodium', 'Folate']
    },
    timeToMake: '15 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Beverage'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.3,
      Water: 0.3,
      Air: 0.2
    },
    instructions: [
      'Wash all produce thoroughly.',
      'Cut ingredients into juicer-friendly pieces.',
      'Process through juicer, alternating between celery and carrots.',
      'Add ginger and lemon last.',
      'Stir well before serving.'
    ]
  },;