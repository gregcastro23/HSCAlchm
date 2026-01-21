import { Recipe } from '../../../../types/recipe';

export const sweetvegancrepes: Recipe = {
  name: 'Sweetvegancrepes',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'Makeapproximateiy', amount: 1.0 },
    { name: 'Cupscashewmnk Ormoreifneeded recipebeiow)', amount: 1.0 },
    { name: 'io.scupsan Purpesefiour', amount: 1.0 },
    { name: 'Cupcanoiaon piusmoreforpan)', amount: 1.0 },
    { name: 'Cupmapiecrystais', amount: 0.5, unit: 'cup' },
    { name: 'Iteaspoonbakingpowder', amount: 2.0, unit: 'tsp' },
    { name: 'Pinchseasait', amount: 0.125, unit: 'tsp' },
  ],
  instructions: [
    'Combine all ingredients in blender. Let batter sit for 30 minutes in refrigerator.',
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
