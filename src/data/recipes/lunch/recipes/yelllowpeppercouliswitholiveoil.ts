import { Recipe } from '../../../../types/recipe';

export const yelllowpeppercouliswitholiveoil: Recipe = {
  name: 'Yelllowpeppercouliswitholiveoil',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'Tablespoonsextra virgin olive oil', amount: 2.0, unit: 'tbsp' },
    { name: 'gouncesshanots', amount: 1.0 },
    { name: 'Ioouncesyenowpepper 2medium)', amount: 1.0 },
    { name: 'Itablespoonbrownricevinegar', amount: 1.0, unit: 'tbsp' },
    { name: 'Ieacupsvegetablestock Warmed', amount: 2.0, unit: 'cups' },
    { name: 'Seasaitandfreshiygroundblackpeppertotaste', amount: 1.0 },
    { name: 'Inchsautepan Heatonovermediumfiame sweatshanotsuntitransiucent.', amount: 1.0 },
  ],
  instructions: [
    'In 10-inch sauté pan, heat oil over medium flame. Sweat shallots until translucent.',
    'Add peppers and sweat until softened.',
    'Add vinegar and reduce until almost dry (au sec).',
    'Add stock and simmer uncovered for 15 minutes.',
    'Puree in blender until creamy and return to pan. Season to taste with salt and pepper.',
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
