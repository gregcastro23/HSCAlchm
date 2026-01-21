import { Recipe } from '../../../../types/recipe';

export const tofuSourCream: Recipe = {
  name: 'Tofu “Sour Cream”',
  description: 'A professional sauce recipe recovered from HSCA culinary school materials.',
  ingredients: [
    { name: 'extra virgin olive oil', amount: 3.0, unit: 'tablespoons' },
    { name: 'canola oil', amount: 0.25, unit: 'cup' },
    { name: '(whito part only), sliced (about 3 tablespoons)', amount: 3.0, unit: 'scallions' },
    { name: 'chickpea miso or more to tasto', amount: 1.0, unit: 'tablespoon' },
    { name: 'Dijon mustard', amount: 1.0, unit: 'tablespoon' },
  ],
  instructions: [
    'Process all ingredients in food processor until smooth and creamy. Season to taste.',
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
