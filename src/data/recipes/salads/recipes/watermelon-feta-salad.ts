import { Recipe } from '../../../../types/recipe';

export const watermelonfetasalad: Recipe = {
    name: 'Watermelon Feta Salad',
    description: 'A refreshing summer salad combining sweet watermelon with salty feta and fresh mint.',
    ingredients: [
      { name: 'watermelon, cubed', amount: 6, unit: 'cups' },
      { name: 'feta cheese, crumbled', amount: 1, unit: 'cup' },
      { name: 'fresh mint leaves', amount: 0.5, unit: 'cup' },
      { name: 'red onion, thinly sliced', amount: 0.5, unit: '' },
      { name: 'extra virgin olive oil', amount: 2, unit: 'tbsp' },
      { name: 'balsamic glaze', amount: 2, unit: 'tbsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 180,
      protein: 5,
      carbs: 20,
      fat: 11,
      vitamins: ['A', 'C'],
      minerals: ['Calcium', 'Potassium']
    },
    timeToMake: '15 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Salad'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.2,
      Water: 0.6,
      Air: 0.1
    },
    instructions: [
      'In a large bowl, combine watermelon cubes and thinly sliced red onion.',
      'Sprinkle crumbled feta cheese over the watermelon.',
      'Tear fresh mint leaves and scatter over the salad.',
      'Drizzle with olive oil and balsamic glaze.',
      'Season with fresh black pepper.',
      'Toss gently to combine just before serving.',
      'Serve immediately while fresh and crisp.'
    ]
  },;