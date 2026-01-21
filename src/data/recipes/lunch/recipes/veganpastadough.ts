import { Recipe } from '../../../../types/recipe';

export const veganpastadough: Recipe = {
  name: 'Veganpastadough',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'Iaapoundsnkentofu', amount: 1.0 },
    { name: 'Tablespoonsextravirginonvean', amount: 1.0 },
    { name: 'Iacupwater', amount: 2.0, unit: 'cups' },
    { name: 'Pinchseasait', amount: 0.125, unit: 'tsp' },
    { name: 'Cupsunbieachedan Purposefiouroricupunbieachedan Purposefiourand', amount: 1.0 },
    { name: 'Icupwhoie', amount: 1.0 },
    { name: 'Wheatbreadfiour', amount: 1.0 },
  ],
  instructions: [
    'Blend tofu, olive oil, water, and salt in blender under smooth.',
    'In food processor, pulse flour for few seconds to aerate it. Add tofu mixture and process',
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
