import { Recipe } from '../../../../types/recipe';

export const horseradishcashewsauce: Recipe = {
    name: 'Horseradish Cashew Sauce',
    description: 'A creamy, dairy-free sauce with a spicy kick from fresh horseradish.',
    ingredients: [
      { name: 'cashews', amount: 0.5, unit: 'cup', notes: 'soaked overnight and drained' },
      { name: 'horseradish', amount: 0.25, unit: 'cup', notes: 'peeled and roughly chopped' },
      { name: 'white miso', amount: 0.25, unit: 'cup' },
      { name: 'water', amount: 0.75, unit: 'cup' },
      { name: 'garlic', amount: 2, unit: 'cloves' },
      { name: 'lemon juice', amount: 0.25, unit: 'cup' },
      { name: 'brown rice vinegar', amount: 1, unit: 'tbsp' },
      { name: 'umeboshi paste', amount: 1, unit: 'tbsp' },
      { name: 'Dijon mustard', amount: 1, unit: 'tsp' }
    ],
    nutrition: {
      calories: 90,
      protein: 3,
      carbs: 8,
      fat: 6,
      vitamins: ['C', 'B6'],
      minerals: ['Magnesium', 'Zinc']
    },
    timeToMake: '15 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Sauce'],
    elementalBalance: {
      Fire: 0.4,
      Earth: 0.3,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'Combine all ingredients in a high-speed blender.',
      'Blend until completely smooth and creamy, about 2-3 minutes.',
      'If needed, add more water tablespoon by tablespoon to reach desired consistency.',
      'Taste and adjust seasoning if needed.',
      'Store in an airtight container in the refrigerator for up to 1 week.'
    ]
  },;