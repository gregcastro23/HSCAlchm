import { Recipe } from '../../../../types/recipe';

export const gingerscallionsauce: Recipe = {
    name: 'Ginger-Scallion Sauce',
    description: 'A vibrant and aromatic sauce perfect for noodles, rice, or grilled proteins.',
    ingredients: [
      { name: 'scallions, finely chopped', amount: 2, unit: 'cups' },
      { name: 'fresh ginger, minced', amount: 0.25, unit: 'cup' },
      { name: 'neutral oil', amount: 0.5, unit: 'cup' },
      { name: 'soy sauce', amount: 2, unit: 'tbsp' },
      { name: 'rice vinegar', amount: 1, unit: 'tbsp' },
      { name: 'sesame oil', amount: 1, unit: 'tsp' },
      { name: 'salt', amount: 0.5, unit: 'tsp' }
    ],
    nutrition: {
      calories: 90,
      protein: 1,
      carbs: 2,
      fat: 9,
      vitamins: ['K', 'C'],
      minerals: ['Iron']
    },
    timeToMake: '15 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Condiment'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.2,
      Water: 0.3,
      Air: 0.2
    },
    instructions: [
      'Heat neutral oil in a small saucepan until just smoking.',
      'Place scallions and ginger in a heat-proof bowl.',
      'Carefully pour hot oil over the scallions and ginger (it will sizzle).',
      'Stir in soy sauce, rice vinegar, sesame oil, and salt.',
      'Let cool to room temperature.',
      'Store in an airtight container in the refrigerator for up to 1 week.'
    ]
  },;