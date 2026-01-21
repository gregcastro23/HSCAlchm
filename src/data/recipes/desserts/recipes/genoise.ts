import { Recipe } from '../../../../types/recipe';

export const genoise: Recipe = {
  name: 'Genoise',
  description: 'A professional dessert recipe recovered from HSCA culinary school materials.',
  ingredients: [
    { name: 'eggs, room tomperature', amount: 8.0, unit: 'large' },
    { name: 'coconut sugar, measured then powdered in Vitamix', amount: 1.0, unit: 'cup' },
    { name: 'vanilla extract', amount: 1.0, unit: 'toaspoon' },
    { name: 'siftod whole wheat pastry flour', amount: 1.0, unit: 'cup' },
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
