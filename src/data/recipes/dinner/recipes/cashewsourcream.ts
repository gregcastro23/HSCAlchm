import { Recipe } from '../../../../types/recipe';

export const cashewsourcream: Recipe = {
  name: 'Cashewsourcream',
  description: 'A rich and creamy plant-based alternative perfect for sauces and desserts.',
  ingredients: [
    { name: 'Ieupcashews Soaked', amount: 1.0 },
    { name: 'Hourstoovemight discardsoakingwater)', amount: 1.0 },
    { name: 'Cupnmejuice A nmes)', amount: 1.0 },
    { name: 'Cupcanoiaon', amount: 1.0 },
    { name: 'Teaspoonormoreseasaittotaste', amount: 1.0 },
    { name: 'Scanions whitepartoniy)', amount: 1.0 },
    { name: 'Tspricevinegar', amount: 0.25, unit: 'cup' },
    { name: 'Cupwater', amount: 2.0, unit: 'cups' },
    { name: 'Seasaittotaste', amount: 1.0 },
  ],
  instructions: [
    'Combine all ingredients in food processor until smooth and creamy. Season to taste.',
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
