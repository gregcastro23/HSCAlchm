import { Recipe } from '../../../../types/recipe';

export const grilledpeachandburratasalad: Recipe = {
    name: 'Grilled Peach and Burrata Salad',
    description: 'A sophisticated summer salad featuring grilled peaches, creamy burrata, and peppery arugula.',
    ingredients: [
      { name: 'ripe peaches, halved', amount: 4, unit: '' },
      { name: 'burrata cheese', amount: 8, unit: 'oz', swaps: ['fresh mozzarella'] },
      { name: 'baby arugula', amount: 6, unit: 'cups' },
      { name: 'prosciutto (optional)', amount: 4, unit: 'slices' },
      { name: 'honey', amount: 2, unit: 'tbsp' },
      { name: 'balsamic vinegar', amount: 2, unit: 'tbsp' },
      { name: 'extra virgin olive oil', amount: 3, unit: 'tbsp' },
      { name: 'sea salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' },
      { name: 'fresh basil leaves', amount: 0.25, unit: 'cup' }
    ],
    nutrition: {
      calories: 320,
      protein: 15,
      carbs: 25,
      fat: 20,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Calcium', 'Iron']
    },
    timeToMake: '25 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Salad'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.3,
      Water: 0.3,
      Air: 0.2
    },
    instructions: [
      'Preheat grill to medium-high heat.',
      'Brush peach halves with 1 tablespoon olive oil.',
      'Grill peaches cut-side down until lightly charred and softened, about 4-5 minutes.',
      'In a small bowl, whisk together honey, balsamic vinegar, remaining olive oil, salt, and pepper.',
      'Arrange arugula on a serving platter.',
      'Top with grilled peaches and torn burrata cheese.',
      'If using, add prosciutto slices.',
      'Drizzle with the honey-balsamic dressing.',
      'Garnish with fresh basil leaves.',
      'Serve immediately while peaches are still warm.'
    ]
  },;