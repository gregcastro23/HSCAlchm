import { Recipe } from '../../../../types/recipe';

export const redwinemarinade: Recipe = {
  name: 'Redwinemarinade',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'o.ggtcupredwine', amount: 1.0 },
    { name: 'Cupolive oil', amount: 1.0 },
    { name: 'Tablespoonsiemonjuice', amount: 1.0 },
    { name: 'Egarlicccioves Sliced', amount: 3.0 },
    { name: 'Itspait', amount: 1.0, unit: 'tbsp' },
    { name: 'Iteaspoonfreshiygroundblackpepper', amount: 0.25, unit: 'tsp' },
    { name: 'Sprigsfreshthyme', amount: 2.0, unit: 'tsp', notes: 'chopped' },
    { name: 'Combinewine Olive oil Iemonjuice Garlicc Salt pepperandthyme.', amount: 1.0 },
    { name: 'Instituteofcunaryeducation Coursee i9i', amount: 1.0 },
    { name: 'o.sessonao Grnng', amount: 1.0 },
  ],
  instructions: [
    'Inblender, combine wine, olive oil, lemon juice, garlic, salt, pepper and thyme.',
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
