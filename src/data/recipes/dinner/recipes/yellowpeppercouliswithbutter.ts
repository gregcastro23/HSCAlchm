import { Recipe } from '../../../../types/recipe';

export const yellowpeppercouliswithbutter: Recipe = {
  name: 'Yellowpeppercouliswithbutter',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Etablespoonsunsaitedbutter', amount: 1.0 },
    { name: 'Gouncesshanots emedium)', amount: 1.0 },
    { name: 'Ioouncesyenowpepper 2medium)', amount: 1.0 },
    { name: 'Itablespoonbrownricevinegar', amount: 1.0, unit: 'tbsp' },
    { name: 'Ieacupsvegetablestock Warmed', amount: 2.0, unit: 'cups' },
    { name: 'Seasaitandfreshiygroundblackpeppertotaste', amount: 1.0 },
    { name: 'Inchsautepan Heatbutterovermedium Iowfiame Sweatshanotsuntil', amount: 1.0 },
    { name: 'transiucent.', amount: 1.0 },
  ],
  instructions: [
    'In 10-inch sauté pan, heat butter over medium-low flame. Sweat shallots until',
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
