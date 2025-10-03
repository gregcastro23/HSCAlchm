import { Recipe } from '../../../../types/recipe';

export const carrotgingerdressing: Recipe = {
    name: 'Carrot-Ginger Dressing',
    description: 'A light and refreshing Japanese-inspired dressing perfect for salads.',
    ingredients: [
      { name: 'carrots, roughly chopped', amount: 2, unit: 'medium' },
      { name: 'fresh ginger, peeled', amount: 2, unit: 'inches' },
      { name: 'yellow onion, chopped', amount: 0.25, unit: 'cup' },
      { name: 'rice vinegar', amount: 0.25, unit: 'cup' },
      { name: 'sesame oil', amount: 2, unit: 'tbsp' },
      { name: 'neutral oil', amount: 0.25, unit: 'cup' },
      { name: 'miso paste', amount: 1, unit: 'tbsp' },
      { name: 'honey', amount: 1, unit: 'tbsp' },
      { name: 'water', amount: 2, unit: 'tbsp' }
    ],
    nutrition: {
      calories: 70,
      protein: 1,
      carbs: 5,
      fat: 6,
      vitamins: ['A', 'C'],
      minerals: ['Potassium']
    },
    timeToMake: '15 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Dressing'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.3,
      Water: 0.3,
      Air: 0.2
    },
    instructions: [
      'Combine carrots, ginger, and onion in a food processor. Process until finely chopped.',
      'Add remaining ingredients and process until smooth.',
      'If needed, thin with additional water to reach desired consistency.',
      'Store in an airtight container in the refrigerator for up to 1 week.'
    ]
  },;