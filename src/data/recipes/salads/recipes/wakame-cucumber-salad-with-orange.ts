import { Recipe } from '../../../../types/recipe';

export const wakameCucumberSaladWithOrange: Recipe = {
  name: 'Wakame Cucumber Salad with Orange',
  description: 'A refreshing Japanese-inspired salad combining sea vegetables with citrus.',
  ingredients: [
    { name: 'wakame', amount: 0.25, unit: 'cup' },
    { name: 'cucumbers', amount: 2.0 },
    { name: 'sea salt', amount: 0.25, unit: 'tsp' },
    { name: 'juice oranges', amount: 2.0 },
    { name: 'cilantro', amount: 0.25, unit: 'bunch' },
    { name: 'rice vinegar', amount: 2.0, unit: 'tbsp' },
    { name: 'mirin', amount: 2.0, unit: 'tbsp' },
    { name: 'shoyu', amount: 1.0, unit: 'tbsp' },
    { name: 'maple syrup', amount: 1.5, unit: 'tbsp' },
  ],
  instructions: [
    'Instrainer set over bowl, mix cucumber with sea salt. Press with weighted plate until',
    'Chop wakame coarsely and combine with cucumbers, oranges, and cilantro in medium',
    'In separate small bow], combine dressing: rice vinegar, mirin, shoyu, and maple syrup.',
    'Toss salad with dressing. Chill 20 minutes.',
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
