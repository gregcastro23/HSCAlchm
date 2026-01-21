import { Recipe } from '../../../../types/recipe';

export const frittata: Recipe = {
  name: 'Frittata',
  description: 'A professional dinne recipe recovered from HSCA culinary school materials.',
  ingredients: [
    { name: 'eggs', amount: 2.0 },
    { name: 'medium bowl whisk together filling(s), salt, and pepper with eggs.', amount: 1.0, unit: 'In' },
  ],
  instructions: [
    'In medium bowl whisk together filling(s), salt, and pepper with eggs.',
    'Heat oil in sauté pan.',
    'Pour in egg mixture.',
    'Cook over medium-low heat until bottom is set.',
    'Slide pan under preheated broiler for 1 or 2 minutes until lightly browned and set or, in',
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
