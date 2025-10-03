import { Recipe } from '../../../../types/recipe';

export const smokycilantrolimevinaigrette: Recipe = {
    name: 'Smoky Cilantro-Lime Vinaigrette',
    description: 'A zesty and smoky vinaigrette perfect for salads or as a marinade.',
    ingredients: [
      { name: 'shallots, chopped', amount: 0.333, unit: 'cup' },
      { name: 'garlic cloves', amount: 2, unit: '' },
      { name: 'smoked paprika', amount: 1, unit: 'tsp' },
      { name: 'ground cumin', amount: 0.5, unit: 'tsp' },
      { name: 'lime juice', amount: 0.25, unit: 'cup' },
      { name: 'cilantro leaves', amount: 0.333, unit: 'cup' },
      { name: 'canola oil', amount: 0.333, unit: 'cup' },
      { name: 'water', amount: 2, unit: 'tbsp' },
      { name: 'honey', amount: 2, unit: 'tsp' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'ground black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 120,
      protein: 0,
      carbs: 6,
      fat: 12,
      vitamins: ['C'],
      minerals: ['Potassium']
    },
    timeToMake: '10 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Dressing'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.2,
      Water: 0.3,
      Air: 0.2
    },
    instructions: [
      'Combine all ingredients in a blender or food processor.',
      'Blend until smooth and well combined.',
      'Taste and adjust seasoning if needed.',
      'Store in an airtight container in the refrigerator for up to 1 week.'
    ]
  },;