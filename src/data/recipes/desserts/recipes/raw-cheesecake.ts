import { Recipe } from '../../../../types/recipe';

export const rawCheesecake: Recipe = {
  name: 'Raw “Cheesecake”',
  description: 'A professional dessert recipe recovered from HSCA culinary school materials.',
  ingredients: [
    { name: 'datos, pittod Blueberry', amount: 5.0 },
    { name: 'coconut oil, meltod Mango', amount: 2.0, unit: 'tablespoons' },
  ],
  instructions: [
    'Combinecucumbers, limejuice, mint, water, andagaveinblender andpuree until',
    'Strainpureethroughsieve andserveinglasses withsliceoflime.',
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
