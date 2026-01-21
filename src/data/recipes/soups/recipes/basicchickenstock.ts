import { Recipe } from '../../../../types/recipe';

export const basicchickenstock: Recipe = {
  name: 'Basicchickenstock',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Spoundschickenbones', amount: 1.0 },
    { name: 'Bouncesyenowonion imedium)', amount: 1.0 },
    { name: 'Ouncescarrot isman)', amount: 1.0 },
    { name: 'Eribscelery gounces)', amount: 1.0 },
    { name: 'Sachetof', amount: 1.0 },
    { name: 'Bayieaves Asprigsthyme 2tspblackpeppercoms Iaounceparsieystems', amount: 1.0 },
    { name: 'Squartscoidwater', amount: 1.0 },
  ],
  instructions: [
    'Combine bones, onion, carrot, celery, sachet, and water in large stock pot.',
    'Cover pot and bring to boil. Remove cover and skim any foam off top.',
    'Reduce heat and simmer uncovered for 3-4 hours.',
    'Cool stock in ice bath and refrigerate.',
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
