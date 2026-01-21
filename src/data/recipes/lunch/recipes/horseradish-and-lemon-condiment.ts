import { Recipe } from '../../../../types/recipe';

export const horseradishAndLemonCondiment: Recipe = {
  name: 'Horseradish and Lemon Condiment',
  description: 'A zesty, bright condiment that combines the heat of fresh horseradish with citrus notes.',
  ingredients: [
    { name: 'fresh horseradish root', amount: 8.0, unit: 'oz', notes: 'peeled and finely grated' },
    { name: 'lemons', amount: 2.0, notes: 'juice and zest' },
    { name: 'apple cider vinegar', amount: 2.0, unit: 'tbsp' },
    { name: 'olive oil', amount: 1.0, unit: 'tbsp' },
    { name: 'sea salt', amount: 0.5, unit: 'tsp' },
    { name: 'honey', amount: 1.0, unit: 'tsp', notes: 'optional' },
  ],
  instructions: [
    'Grate horseradish on box grater using fine holes.',
    'Combine horseradish with lemon juice and set aside for ten minutes at room temperature.',
    'Serve cold or room temperature mixed into water, stock or soup.',
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
