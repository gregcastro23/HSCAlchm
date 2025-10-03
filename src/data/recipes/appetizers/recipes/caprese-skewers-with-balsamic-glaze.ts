import { Recipe } from '../../../../types/recipe';

export const capreseskewerswithbalsamicglaze: Recipe = {
    name: 'Caprese Skewers with Balsamic Glaze',
    description: 'A simple and elegant appetizer featuring fresh mozzarella, cherry tomatoes, and basil leaves.',
    ingredients: [
      { name: 'cherry tomatoes', amount: 1, unit: 'pint' },
      { name: 'fresh mozzarella balls', amount: 8, unit: 'oz' },
      { name: 'fresh basil leaves', amount: 24, unit: '' },
      { name: 'olive oil', amount: 2, unit: 'tbsp' },
      { name: 'balsamic glaze', amount: 0.25, unit: 'cup' },
      { name: 'salt', amount: 0.25, unit: 'tsp' },
      { name: 'black pepper', amount: 0.125, unit: 'tsp' }
    ],
    nutrition: {
      calories: 200,
      protein: 12,
      carbs: 8,
      fat: 14,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Calcium', 'Potassium']
    },
    timeToMake: '20 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Appetizer'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.4,
      Water: 0.4,
      Air: 0.1
    },
    instructions: [
      'Thread cherry tomatoes, mozzarella balls, and basil leaves onto skewers, alternating the ingredients.',
      'Arrange the skewers on a serving platter.',
      'Drizzle olive oil and balsamic glaze over the skewers.',
      'Sprinkle with salt and black pepper.',
      'Serve immediately as a fresh and flavorful appetizer.'
    ]
  },;