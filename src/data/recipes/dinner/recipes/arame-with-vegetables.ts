import { Recipe } from '../../../../types/recipe';

export const arameWithVegetables: Recipe = {
  name: 'Arame with Vegetables',
  description: 'A nourishing side dish combining sea vegetables with land vegetables.',
  ingredients: [
    { name: 'sesame oil', amount: 1.0, unit: 'tbsp' },
    { name: 'onion', amount: 10.0, unit: 'oz' },
    { name: 'carrot', amount: 6.0, unit: 'oz' },
    { name: 'arame', amount: 1.5, unit: 'cups' },
    { name: 'shoyu', amount: 2.0, unit: 'tbsp' },
    { name: 'brown rice syrup', amount: 2.0, unit: 'tbsp' },
    { name: 'mirin', amount: 2.0, unit: 'tbsp' },
    { name: 'bok choy', amount: 8.0, unit: 'oz' },
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
