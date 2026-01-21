import { Recipe } from '../../../../types/recipe';

export const pomegranateBlueberryAndGingerElixir: Recipe = {
  name: 'Pomegranate, Blueberry, and Ginger Elixir',
  description: 'A vibrant and antioxidant-rich beverage combining sweet and spicy flavors.',
  ingredients: [
    { name: 'pomegranate juice', amount: 4.0, unit: 'cups' },
    { name: 'blueberries', amount: 1.0, unit: 'pint', notes: 'washed and stemmed' },
    { name: 'ginger juice', amount: 0.25, unit: 'cup', notes: 'approximately 3-inch piece' },
    { name: 'filtered water', amount: 1.0, unit: 'cup' },
    { name: 'agave', amount: 2.0, unit: 'tbsp' },
  ],
  instructions: [
    'Combine pomegranate juice, blueberries, ginger juice, and agave in VitaMix and puree.',
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
