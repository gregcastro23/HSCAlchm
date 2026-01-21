import { Recipe } from '../../../../types/recipe';

export const mangosalsaforcrustedflounder: Recipe = {
  name: 'Mangosalsaforcrustedflounder',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'o.sripemango Skined Pittedandmediumdice', amount: 1.0 },
    { name: 'Redonion Smandice', amount: 0.5 },
    { name: 'Ouncescucumber Seededandsmandice', amount: 1.0 },
    { name: 'Ijaiapenopepper Seededandminced', amount: 1.0 },
    { name: 'Y Ouncecnantro Chopped', amount: 0.5, unit: 'cup' },
    { name: 'Chopped', amount: 0.5, unit: 'cup' },
    { name: 'Itablespoonolive oil', amount: 1.0 },
    { name: 'Saitandpeppertotaste', amount: 1.0 },
  ],
  instructions: [
    'Combine all ingredients and serve atop crusted flounder.',
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
