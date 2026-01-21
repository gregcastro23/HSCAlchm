import { Recipe } from '../../../../types/recipe';

export const bakedmeringueshells: Recipe = {
  name: 'Bakedmeringueshells',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'Aounces Eggwhites', amount: 2.0 },
    { name: 'Bounces Mapiecrystais', amount: 0.5, unit: 'cup' },
    { name: '0.5 Preheat oven to', amount: 1.0 },
    { name: 'sfandnesheettraywithparchmentpaper.', amount: 1.0 },
  ],
  instructions: [
    'Preheat oven to 225° F and line sheet tray with parchment paper.',
    'Beat egg whites to soft peaks, then add sweetener one tablespoon at a time until',
    'Using pastry bag or spoon, pipe or spoon meringue on sheet tray. Bake until crisp',
    'Cool shells completely and remove from parchment.',
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
