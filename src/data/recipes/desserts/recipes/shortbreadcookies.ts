import { Recipe } from '../../../../types/recipe';

export const shortbreadcookies: Recipe = {
  name: 'Shortbreadcookies',
  description: 'Freshly baked goods with wholesome ingredients and amazing flavor.',
  ingredients: [
    { name: 'Iotablespoons Iaasticks Butter Softened', amount: 1.0 },
    { name: 'Cupt', amount: 1.0 },
    { name: 'Tablespoonspowderedmapiecrystais', amount: 1.0 },
    { name: 'Teaspeonseasait', amount: 1.0 },
    { name: 'Teaspeonvaniaextract', amount: 0.5, unit: 'tsp' },
    { name: 'Iacupswhoiewheatpastryfiour', amount: 1.5, unit: 'cups' },
    { name: '0.5 Preheat oven to', amount: 1.0 },
    { name: 'eoofandnehaifsheettraywithparchmentpaper.', amount: 1.0 },
  ],
  instructions: [
    'Preheat oven to 300° F and line half sheet tray with parchment paper.',
    'Cream butter, sugar, vanilla and salt in stand mixer.',
    'Gradually sift in flour until well mixed.',
    'Firmly press dough into flattened 6-inch oval in center of sheet tray. Cut dough into 16',
    'Bake about 45-50 minutes or until entire dough is golden brown and firm to touch.',
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
