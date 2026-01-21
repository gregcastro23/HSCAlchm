import { Recipe } from '../../../../types/recipe';

export const roastedRedPepperHummus: Recipe = {
  name: 'Roasted Red Pepper Hummus',
  description: 'Creamy hummus with sweet roasted red peppers and tahini.',
  ingredients: [
    { name: 'chickpeas, drained and rinsed', amount: 15.0, unit: 'oz' },
    { name: 'roasted red peppers', amount: 12.0, unit: 'oz' },
    { name: 'tahini', amount: 0.333, unit: 'cup' },
    { name: 'garlic cloves', amount: 3.0 },
    { name: 'lemon juice', amount: 0.25, unit: 'cup' },
    { name: 'olive oil', amount: 0.25, unit: 'cup' },
    { name: 'ground cumin', amount: 1.0, unit: 'tsp' },
    { name: 'smoked paprika', amount: 0.5, unit: 'tsp' },
    { name: 'salt', amount: 1.0, unit: 'tsp' },
  ],
  instructions: [
    'Preheat oven to 375° F-400° F.',
    'Combine vegetables, garlic, and olive oil in large roasting pan.',
    'Roast for 30 minutes. Drain and cool.',
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
