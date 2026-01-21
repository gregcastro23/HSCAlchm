import { Recipe } from '../../../../types/recipe';

export const coleslaw: Recipe = {
  name: 'Coleslaw',
  description: 'A professional salad recipe recovered from HSCA culinary school materials.',
  ingredients: [
    { name: 'garlic, roastod, pasto extractod', amount: 1.0, unit: 'head' },
    { name: 'agave syrup', amount: 1.0, unit: 'tablespoon' },
    { name: 'apple cider vinegar', amount: 2.0, unit: 'tablespoon' },
    { name: 'lemon juice (1 lemon)', amount: 2.0, unit: 'tablespoons' },
    { name: 'canol', amount: 0.25, unit: 'cup' },
  ],
  instructions: [
    'Combine almonds in 2 1/2 quart pot with water and salt. Bring to boil, cover, and remove',
    'Inblender, combine almonds, soaking water, garlic paste, mustard, agave syrup, vinegar,',
    'In large bowl, combine cabbage (green and red) with yellow pepper and carrots.',
    'Toss dressing with vegetables. Fold in parsley and dill.',
  ],
  nutrition: {
    calories: 200,
    protein: 8,
    carbs: 25,
    fat: 12,
    vitamins: ['C', 'K'],
    minerals: ['Potassium', 'Iron'],
  },
  timeToMake: '30 minutes',
  season: ['all'],
  cuisine: 'HSCA',
  mealType: ['Health Supportive'],
  elementalBalance: {
    Fire: 0.25,
    Earth: 0.25,
    Water: 0.25,
    Air: 0.25,
  },
};
