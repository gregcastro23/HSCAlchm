import { Recipe } from '../../../../types/recipe';

export const vegancashewcream: Recipe = {
  name: 'Vegancashewcream',
  description: 'A rich and creamy plant-based alternative perfect for sauces and desserts.',
  ingredients: [
    { name: 'Servesb', amount: 1.0 },
    { name: 'Cupscashews Soakedovemight', amount: 1.0 },
    { name: 'Iteaspoonvania', amount: 1.0 },
    { name: 'brown rice vinegar', amount: 1.0, unit: 'tbsp' },
    { name: 'Cupmapiesyrup', amount: 1.5, unit: 'tbsp', notes: 'or to taste' },
    { name: 'Iacupwater ormoreifnecessary)', amount: 1.0 },
  ],
  instructions: [
    'Combine cashews, vanilla, brown rice vinegar, salt, and maple syrup in Vitamix with wand',
    'When mixture is starting to smooth, add water, and continue processing. When mixture is',
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
