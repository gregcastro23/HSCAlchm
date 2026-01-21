import { Recipe } from '../../../../types/recipe';

export const watermelonJuice: Recipe = {
  name: 'Watermelon Juice',
  description: 'A refreshing and hydrating summer drink packed with natural electrolytes.',
  ingredients: [
    { name: 'watermelon', amount: 6.0, unit: 'cups', notes: 'cubed' },
    { name: 'lime juice', amount: 1.0, unit: 'tbsp' },
    { name: 'mint leaves', amount: 0.25, unit: 'cup', notes: 'optional, for garlicish' },
    { name: 'ice cubes', amount: 2.0, unit: 'cups', notes: 'for serving' },
  ],
  instructions: [
    'Cut watermelon into approximately 2 inch x 4 inch pieces.',
    'Ina high-speed blender puree watermelon pieces in batches.',
    'Using a mesh strainer set over a large bowl strain watermelon juice. Discard solids.',
    'Stir in lemon juice and refrigerate until ready to serve.',
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
