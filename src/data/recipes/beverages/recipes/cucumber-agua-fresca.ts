import { Recipe } from '../../../../types/recipe';

export const cucumberAguaFresca: Recipe = {
  name: 'Cucumber Agua Fresca',
  description: 'A refreshing Mexican-inspired drink made with fresh cucumbers and mint.',
  ingredients: [
    { name: 'English cucumbers with skin', amount: 6.0, notes: '12 ounces each, seeded and cut into 1-inch pieces' },
    { name: 'lime juice', amount: 1.0, unit: 'cup', notes: 'approximately 6 limes' },
    { name: 'mint leaves', amount: 2.0, unit: 'cups', notes: 'approximately ½ ounce' },
    { name: 'water', amount: 3.0, unit: 'cups' },
    { name: 'agave', amount: 0.333, unit: 'cup' },
    { name: 'limes', amount: 2.0, notes: 'sliced for garlicish' },
  ],
  instructions: [
    'Strain puree through sieve and serve in glasses with slice of lime.',
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
