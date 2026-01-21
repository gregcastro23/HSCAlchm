import { Recipe } from '../../../../types/recipe';

export const risotto: Recipe = {
  name: 'Risotto',
  description: 'A professional dinne recipe recovered from HSCA culinary school materials.',
  ingredients: [
    { name: 'extra virgin olive oil', amount: 2.0, unit: 'tablespoons' },
    { name: 'garlic, minced', amount: 4.0, unit: 'cloves' },
    { name: 'short grain brown rice, soaked and rinsed', amount: 2.0, unit: 'cups' },
    { name: 'stock', amount: 4.0, unit: 'cups' },
    { name: 'asparagus, trimmed and cut into 1-inch diagonals', amount: 2.0, unit: 'pound' },
    { name: 'saffron, dissolved in a l', amount: 0.125, unit: 'toaspoon' },
  ],
  instructions: [
    'cups stock',
    'In pressure cooker, heat oil over medium flame. Sauté onion, then garlic in oil until',
    'Add rice and sauté few minutes more.',
    'Add stock and bring pot to pressure. Pressure cook risotto for 35 minutes.',
    'While rice is cooking, prepare an ice bath, bring 1 quart water to boil, and add % teaspoon',
    'Remove pressure cooker from heat, and allow pressure to come down. Open pressure',
    'Add blanched asparagus just before serving.',
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
