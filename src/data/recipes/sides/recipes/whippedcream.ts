import { Recipe } from '../../../../types/recipe';

export const whippedcream: Recipe = {
  name: 'Whippedcream',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Servesb', amount: 1.0 },
    { name: 'Ipintheavycream', amount: 0.5, unit: 'cup' },
    { name: 'Iteaspoonvania', amount: 1.0 },
    { name: 'Iteaspoonmapieecrystais', amount: 0.5, unit: 'cup' },
  ],
  instructions: [
    'Combine all ingredients in stand mixer fitted with chilled bow] and whip until stiff peaks',
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
