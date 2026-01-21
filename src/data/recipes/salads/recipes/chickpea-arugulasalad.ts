import { Recipe } from '../../../../types/recipe';

export const chickpeaArugulasalad: Recipe = {
  name: 'Chickpea Arugulasalad',
  description: 'A fresh and vibrant salad featuring seasonal ingredients and crisp textures.',
  ingredients: [
    { name: 'o.scupchickpeas Soakedovemight', amount: 1.0 },
    { name: 'Iquartwater', amount: 2.0, unit: 'cups' },
    { name: 'Teaspooncumin', amount: 1.0 },
    { name: 'Tspeasait', amount: 0.125, unit: 'tsp' },
    { name: 'Cupsesame Garliccdressing seerecipebeiow)', amount: 1.0 },
    { name: 'Y Buncharuguia Cieanedandchoppedintebitesizedpieces scups)', amount: 1.0 },
    { name: 'o.scuponves Pittedandchopped', amount: 1.0 },
    { name: 'Tablespoonsparsiey Chopped', amount: 0.25, unit: 'cup' },
    { name: 'Tablespoonsfreshbasn Chopped', amount: 1.0 },
    { name: 'Seasaitandblackpeppertotaste', amount: 1.0 },
  ],
  instructions: [
    'Combine chickpeas, water, cumin, and salt in stockpot.',
    'Bring beans to simmer, lower heat, and cook 45-60 minutes, adding water as needed,',
    'While beans are still warm, toss with dressing. (recipe below).',
    'Let beans cool to room temperature and, right before service, add arugula, olives, parsley,',
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
