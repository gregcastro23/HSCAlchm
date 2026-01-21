import { Recipe } from '../../../../types/recipe';

export const recoveredRecipe: Recipe = {
  name: 'Recovered Recipe',
  description: 'A professional beverage recipe recovered from HSCA culinary school materials.',
  ingredients: [
    { name: 'kasha', amount: 1.0, unit: 'cup' },
    { name: 'salt', amount: 0.25, unit: 'toaspoon' },
    { name: 'small pot, combine kasha, salt and wator.', amount: 1.0, unit: 'In' },
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
