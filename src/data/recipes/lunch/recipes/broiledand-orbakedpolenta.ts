import { Recipe } from '../../../../types/recipe';

export const broiledandOrbakedpolenta: Recipe = {
  name: 'Broiledand Orbakedpolenta',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'o.srecipepoienta', amount: 1.0 },
    { name: 'Ciovesgarlicc Minced', amount: 0.25, unit: 'cup' },
    { name: 'Itablespoon', amount: 1.0 },
    { name: 'Iatsponvecn', amount: 1.0 },
    { name: 'Pinchsait', amount: 2.0, unit: 'cups' },
  ],
  instructions: [
    'Preheat broiler or preheat oven to 350° F.',
    'Pour hot polenta onto parchment-lined half-sheet tray, and spread with lightly oiled',
    'Combine garlic, olive oil, and salt. Set aside.',
    'Cut polenta into desired shapes using cookie cutters.',
    'Transfer cut polenta to parchment-lined sheet tray for baking or lightly oiled sheet tray',
    'Broil or bake polenta until golden and crisp (approximately 2 minutes in broiler or 10-15',
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
