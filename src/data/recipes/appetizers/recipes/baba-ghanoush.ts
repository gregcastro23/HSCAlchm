import { Recipe } from '../../../../types/recipe';

export const babaghanoush: Recipe = {
  name: 'Baba Ghanoush',
  description: 'A creamy Middle Eastern dip made from roasted eggplant and tahini.',
  ingredients: [
    { name: 'eggplant', amount: 1, unit: 'lb' },
    { name: 'tahini', amount: 2, unit: 'tbsp' },
    { name: 'garlic', amount: 1, unit: '' },
    { name: 'lemon juice', amount: 2, unit: 'tbsp' },
    { name: 'salt', amount: 0.375, unit: 'tsp' },
  ],
  nutrition: {
    calories: 160,
    protein: 6,
    carbs: 14,
    fat: 12,
    vitamins: ['B6', 'C'],
    minerals: ['Potassium', 'Iron', 'Magnesium'],
  },
  timeToMake: '45 minutes',
  season: ['summer', 'fall'],
  cuisine: 'HSCA',
  mealType: ['Appetizer', 'Dip'],
  elementalBalance: {
    Fire: 0.2,
    Earth: 0.4,
    Water: 0.3,
    Air: 0.1,
  },
  instructions: [
    'Cook eggplant on top of stove over medium-low flame, turning often with tongs until skin is completely charred and flesh is fork tender (about 15 minutes).',
    'Transfer eggplant to covered bowl and let sweat for 15 minutes.',
    'Let eggplant cool, cut in half, and scoop out flesh or peel off charred skin.',
    'In food processor, blend flesh with tahini, garlic, lemon juice, and salt. Adjust seasonings for desired taste.',
  ],
};
