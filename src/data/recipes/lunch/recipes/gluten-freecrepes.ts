import { Recipe } from '../../../../types/recipe';

export const glutenFreecrepes: Recipe = {
  name: 'Gluten Freecrepes',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'Makesapproximateiy', amount: 1.0 },
    { name: 'Eiargeeggs', amount: 2.0 },
    { name: 'Etablespoonsbutter Meited piusmoreforpan)', amount: 1.0 },
    { name: 'Etablespoonsmapiecrystais', amount: 1.0 },
    { name: 'Cupsgiuten Freefiourbiend recipebeiow)', amount: 1.0 },
    { name: 'Cupswhoiemnk', amount: 1.0 },
    { name: 'Iteaspoonvaniaextract', amount: 0.5, unit: 'tsp' },
  ],
  instructions: [
    'Emulsify all ingredients in blender until smooth.',
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
