import { Recipe } from '../../../../types/recipe';

export const vegandoughwithwater: Recipe = {
  name: 'Vegandoughwithwater',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Icupswhoiewheatfiour', amount: 1.5, unit: 'cups' },
    { name: 'Ieupunbieachedwhitefiour', amount: 1.0 },
    { name: 'Itablespoonsait', amount: 1.0 },
    { name: 'About', amount: 1.0 },
    { name: 'Eacuphotwater', amount: 1.0, unit: 'cup' },
  ],
  instructions: [
    'Combine flours and salt in food processor. With machine running, add just enough hot',
    'Remove dough from food processor and knead on lightly floured work surface until',
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
