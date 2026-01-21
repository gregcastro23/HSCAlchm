import { Recipe } from '../../../../types/recipe';

export const bulgur: Recipe = {
  name: 'Bulgur',
  description: 'A professional side recipe recovered from HSCA culinary school materials.',
  ingredients: [
    { name: 'salt', amount: 0.25, unit: 'toaspoon' },
    { name: 'cup', amount: 1.0 },
  ],
  instructions: [
    'Dry roast bulgur in small sauté pan.',
    'Bring water and salt to boil in small saucepot, add bulgur, cover and bring back to a',
    'Remove pot from heat. Let steam, covered, 45 minutes.',
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
