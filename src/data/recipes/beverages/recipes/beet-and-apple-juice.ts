import { Recipe } from '../../../../types/recipe';

export const beetAndAppleJuice: Recipe = {
  name: 'Beet and Apple Juice',
  description: 'A vibrant, earthy juice that supports liver function and blood building.',
  ingredients: [
    { name: 'beets', amount: 2.0, unit: 'medium', notes: 'peeled and quartered' },
    { name: 'apples', amount: 2.0, notes: 'cored and quartered' },
    { name: 'carrots', amount: 2.0, unit: 'large' },
    { name: 'ginger', amount: 1.0, unit: 'inch' },
    { name: 'lemon', amount: 0.5, notes: 'peeled' },
  ],
  instructions: [
    'Cut produce to fit juicer feed tube.',
    'Alternate juicing beets and apples, finishing with beets. Refrigerate juice 5-10 minutes for',
    'Scrape off any excess foam and serve immediately.',
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
