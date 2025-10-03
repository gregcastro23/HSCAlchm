import { Recipe } from '../../../../types/recipe';

export const hibiscusicedtea: Recipe = {
    name: 'Hibiscus Iced Tea',
    description: 'A tart and refreshing herbal tea made with hibiscus flowers and subtle spices.',
    ingredients: [
      { name: 'dried hibiscus flowers', amount: 0.5, unit: 'cup' },
      { name: 'cinnamon stick', amount: 1, unit: '' },
      { name: 'fresh ginger, sliced', amount: 1, unit: 'inch' },
      { name: 'water', amount: 8, unit: 'cups' },
      { name: 'honey', amount: 0.25, unit: 'cup', swaps: ['agave nectar'] },
      { name: 'lime juice', amount: 2, unit: 'tbsp' }
    ],
    nutrition: {
      calories: 45,
      protein: 0,
      carbs: 12,
      fat: 0,
      vitamins: ['C'],
      minerals: ['Iron', 'Magnesium']
    },
    timeToMake: '25 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Beverage'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.1,
      Water: 0.4,
      Air: 0.2
    },
    instructions: [
      'In a large pot, bring water to a boil.',
      'Add hibiscus flowers, cinnamon stick, and ginger. Turn off heat and let steep for 20 minutes.',
      'Strain the tea into a pitcher and discard the solids.',
      'Stir in honey and lime juice until honey dissolves.',
      'Refrigerate until chilled.',
      'Serve over ice, garnished with lime slices if desired.'
    ]
  },;