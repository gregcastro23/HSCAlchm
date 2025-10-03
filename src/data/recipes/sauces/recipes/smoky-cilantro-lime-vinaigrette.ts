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
    mealType: ['Sauce', 'Dressing'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.2,
      Water: 0.3,
      Air: 0.2
    },
    instructions: [
      'Combine shallots, garlic, smoked paprika, cumin, lime juice, cilantro, canola oil, water, honey, salt and pepper in a blender.',
      'Blend until smooth and emulsified.'
    ]
  },;