import { Recipe } from '../../../../types/recipe';

export const kanten: Recipe = {
  name: 'Kanten',
  description: 'A professional side recipe recovered from HSCA culinary school materials.',
  ingredients: [
    { name: 'agar flakes', amount: 2.0, unit: 'tablespoons' },
    { name: 'apple juice', amount: 2.0, unit: 'cups' },
    { name: 'strawberry (sliced thin)', amount: 1.0, unit: 'pint' },
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
