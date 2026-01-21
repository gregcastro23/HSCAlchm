import { Recipe } from '../../../../types/recipe';

export const gingermarinade: Recipe = {
  name: 'Gingermarinade',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Cupolive oil', amount: 1.0 },
    { name: 'Cupredwinevinegar', amount: 0.25, unit: 'cup' },
    { name: 'Cupshoyu', amount: 2.0, unit: 'tbsp' },
    { name: 'Iacuptomatopaste', amount: 1.0 },
    { name: 'Juiceofiemon', amount: 1.0 },
    { name: 'Ciovesgarlicc Peeledandsliced', amount: 1.0 },
    { name: 'Teaspeondryoregano', amount: 1.0 },
    { name: 'Etablespoonpeeledandslicedginger', amount: 1.0 },
  ],
  instructions: [
    'Combine ingredients in blender and puree.',
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
