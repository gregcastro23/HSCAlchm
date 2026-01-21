import { Recipe } from '../../../../types/recipe';

export const lemonandmapleFlavoredyogurt: Recipe = {
  name: 'Lemonandmaple Flavoredyogurt',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'o.scupgreek yogurt', amount: 1.0 },
    { name: 'Zestof', amount: 1.0 },
    { name: 'Nemon', amount: 1.0, unit: 'whole', notes: 'juice only' },
    { name: 'Itablespoonpius', amount: 1.0 },
    { name: 'Iatspmapiesyrup', amount: 1.5, unit: 'tbsp', notes: 'or to taste' },
  ],
  instructions: [
    'Whisk together all ingredients in small bowl.',
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
