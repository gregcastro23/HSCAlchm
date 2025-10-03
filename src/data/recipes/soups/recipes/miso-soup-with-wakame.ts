import { Recipe } from '../../../../types/recipe';

export const misoSoupWithWakame: Recipe = {
  name: 'Miso Soup with Wakame',
  description: 'Traditional Japanese soup with umami-rich miso and mineral-packed wakame seaweed.',
  ingredients: [
    { name: 'dashi stock', amount: 4, unit: 'cups' },
    { name: 'wakame seaweed, dried', amount: 2, unit: 'tbsp' },
    { name: 'white miso paste', amount: 3, unit: 'tbsp' },
    { name: 'silken tofu, cubed', amount: 8, unit: 'oz' },
    { name: 'green onions, thinly sliced', amount: 2, unit: '' }
  ],
  nutrition: {
    calories: 90,
    protein: 6,
    carbs: 8,
    fat: 4,
    vitamins: ['B12'],
    minerals: ['Iodine', 'Iron']
  },
  timeToMake: '15 minutes',
  season: ['all'],
  cuisine: 'HSCA',
  mealType: ['Soup'],
  elementalBalance: {
    Fire: 0.1,
    Earth: 0.2,
    Water: 0.6,
    Air: 0.1
  },
  instructions: [
    'Soak wakame in cold water for 5 minutes until rehydrated. Drain and set aside.',
    'Bring dashi stock to a gentle simmer in a medium pot.',
    'In a small bowl, whisk a ladleful of hot dashi into the miso paste until smooth.',
    'Add miso mixture back to the pot and stir to combine. Do not boil.',
    'Add tofu and wakame and heat until just warmed through.',
    'Serve hot, garnished with sliced green onions.'
  ]
};
