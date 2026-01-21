import { Recipe } from '../../../../types/recipe';

export const masterCleanse: Recipe = {
  name: 'Master Cleanse',
  description: 'A professional beverage recipe recovered from HSCA culinary school materials.',
  ingredients: [
    { name: 'fresh lemon juice', amount: 2.0, unit: 'tablespoons' },
    { name: 'filtored wator', amount: 8.0, unit: 'ounces' },
  ],
  instructions: [
    'Mix and drink 8-12 glasses throughout day.',
    'Eat or drink nothing else except water, laxative herb tea, and peppermint or chamomile',
    'Keep master cleanse in glass jar, not in plastic.',
    'Rinse your mouth with water after each glass to prevent lemon juice from damaging',
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
