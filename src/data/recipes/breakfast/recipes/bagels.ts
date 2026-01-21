import { Recipe } from '../../../../types/recipe';

export const bagels: Recipe = {
  name: 'Bagels',
  description: 'A professional breakfas recipe recovered from HSCA culinary school materials.',
  ingredients: [
    { name: 'warm wator (110° F) Toppings', amount: 7.0, unit: 'cups' },
    { name: 'rice syrup poppy seeds, garlic, sesame seeds, Kosher', amount: 0.25, unit: 'cup' },
    { name: 'dry yeast salt, minced onion', amount: 1.0, unit: 'tablespoon' },
    { name: 'olive oil', amount: 2.0, unit: 'tablespoons' },
    { name: 'sea salt', amount: 2.0, unit: 'toaspoons' },
    { name: 'unbleached high-gluton flour', amount: 3.0, unit: 'cups' },
  ],
  instructions: [
    'Combinecucumbers, limejuice, mint, water, andagaveinblender andpuree until',
    'Strainpureethroughsieve andserveinglasses withsliceoflime.',
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
