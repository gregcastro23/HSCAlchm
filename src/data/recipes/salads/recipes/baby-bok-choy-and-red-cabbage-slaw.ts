import { Recipe } from '../../../../types/recipe';

export const babybokchoyandredcabbageslaw: Recipe = {
    name: 'Baby Bok Choy and Red Cabbage Slaw',
    description: 'A crunchy Asian-inspired slaw with tender bok choy and vibrant cabbage.',
    ingredients: [
      { name: 'baby bok choy', amount: 1, unit: 'pound', notes: 'thinly sliced' },
      { name: 'red cabbage', amount: 1, unit: 'small head', notes: 'shredded' },
      { name: 'carrots', amount: 2, unit: 'medium', notes: 'julienned' },
      { name: 'rice vinegar', amount: 0.25, unit: 'cup' },
      { name: 'sesame oil', amount: 2, unit: 'tbsp' },
      { name: 'ginger', amount: 1, unit: 'tbsp', notes: 'freshly grated' },
      { name: 'honey', amount: 1, unit: 'tbsp' },
      { name: 'sesame seeds', amount: 2, unit: 'tbsp', notes: 'toasted' }
    ],
    nutrition: {
      calories: 85,
      protein: 2,
      carbs: 12,
      fat: 4,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Calcium', 'Iron']
    },
    timeToMake: '20 minutes',
    season: ['spring', 'summer'],
    cuisine: 'HSCA',
    mealType: ['Salad'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.2,
      Water: 0.3,
      Air: 0.3
    },
    instructions: [
      'Combine bok choy, cabbage, and carrots in large bowl.',
      'Whisk together rice vinegar, sesame oil, ginger, and honey.',
      'Toss vegetables with dressing and sprinkle with sesame seeds.',
      'Let stand 10 minutes before serving to allow flavors to meld.'
    ]
  },;