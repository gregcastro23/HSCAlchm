import { Recipe } from '../../../../types/recipe';

export const herbmarinade: Recipe = {
  name: 'Herbmarinade',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'o.eeecupextra virgin olive oil', amount: 2.0, unit: 'tbsp' },
    { name: 'Itablespoondriedthyme', amount: 1.0, unit: 'tbsp' },
    { name: 'Iteaspoondriedbasn', amount: 1.0 },
    { name: 'Iteaspoondriedoregano', amount: 1.0, unit: 'tsp' },
    { name: 'o.tsciovesgarlicc Sliced', amount: 1.0 },
    { name: 'Freshiygroundblackpepper', amount: 0.25, unit: 'tsp' },
    { name: 'Atspait', amount: 1.0 },
    { name: 'Warmaningredientsinonandremovefromheat Cooimarinade', amount: 1.0 },
    { name: 'beforeuse.', amount: 1.0 },
    { name: 'Instituteofcunaryeducation Coursee i9o', amount: 1.0 },
    { name: 'o.sessonao Grnng', amount: 1.0 },
  ],
  instructions: [
    'Insmall saucepan, warm all ingredients in oil and remove from heat. Cool marinade',
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
