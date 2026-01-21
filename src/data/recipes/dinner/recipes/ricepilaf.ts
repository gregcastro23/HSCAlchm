import { Recipe } from '../../../../types/recipe';

export const ricepilaf: Recipe = {
  name: 'Ricepilaf',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Ipoundonions Smandice', amount: 1.0 },
    { name: 'Tablespoonsolive oil', amount: 1.0 },
    { name: 'Cupsionggrainbrownrice', amount: 1.0 },
    { name: 'Cupsboningvegetablestock', amount: 2.0, unit: 'cups' },
    { name: 'Tspsait', amount: 1.0 },
    { name: 'Groundpepper Totaste', amount: 0.25, unit: 'tsp' },
    { name: 'Tspthyme', amount: 2.0, unit: 'tsp', notes: 'chopped' },
    { name: 'o.sbayieaves', amount: 2.0 },
    { name: 'freshherbsforgamish.', amount: 2.0, unit: 'tbsp', notes: 'chopped basil, tarragon, or dill' },
    { name: 'o.sini Ganonpot heatonandsweatonionsuntiltranshucent.', amount: 1.0 },
  ],
  instructions: [
    'In1-gallon pot, heat oil and sweat onions until translucent.',
    'Add rice and stir to coat with oil.',
    'Add stock, salt, pepper, and thyme. Bring to boil, reduce heat, cover, and simmer 45',
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
