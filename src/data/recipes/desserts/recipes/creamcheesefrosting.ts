import { Recipe } from '../../../../types/recipe';

export const creamcheesefrosting: Recipe = {
  name: 'Creamcheesefrosting',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Seight Ouncepackagesoforganiccreamcheese Softened', amount: 1.0 },
    { name: 'Ioounces 2sticks Butter Softened', amount: 1.0, unit: 'cup' },
    { name: 'Cupsmapiecrystais', amount: 0.5, unit: 'cup' },
    { name: 'Etablespoonsvaniaextract', amount: 0.5, unit: 'tsp' },
    { name: 'Pinchseasait', amount: 0.125, unit: 'tsp' },
    { name: 'Oniowspeed beatcreamcheesewithbutteruntilsmooth.', amount: 1.0 },
  ],
  instructions: [
    'Instand mixer, on low speed, beat cream cheese with butter until smooth.',
    'Gradually beat in maple crystals, vanilla extract, and salt until well blended.',
    'Chill to set up.',
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
