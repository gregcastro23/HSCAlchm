import { Recipe } from '../../../../types/recipe';

export const freshherbdressing: Recipe = {
    name: 'Fresh Herb Dressing',
    description: 'A light, herb-infused dressing perfect for salads or vegetables.',
    ingredients: [
      { name: 'vegetable stock', amount: 2, unit: 'cups' },
      { name: 'shallots', amount: 2, unit: 'tbsp', notes: 'minced' },
      { name: 'extra-virgin olive oil', amount: 1, unit: 'tbsp' },
      { name: 'prepared mustard', amount: 2, unit: 'tsp' },
      { name: 'orange juice', amount: 2, unit: 'tbsp' },
      { name: 'rice syrup', amount: 1.25, unit: 'tbsp' },
      { name: 'fresh herbs', amount: 2, unit: 'tbsp', notes: 'chopped basil, tarragon, or dill' }
    ],
    nutrition: {
      calories: 45,
      protein: 1,
      carbs: 6,
      fat: 3,
      vitamins: ['C', 'K'],
      minerals: ['Iron']
    },
    timeToMake: '20 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Sauce'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.2,
      Water: 0.3,
      Air: 0.3
    },
    instructions: [
      'In small sauce pan, reduce stock to 6 tablespoons and set aside to cool.',
      'Combine stock with shallots, olive oil, mustard, orange juice, rice syrup and herbs in blender and puree until emulsified.'
    ]
  },;