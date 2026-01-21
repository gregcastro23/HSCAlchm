import { Recipe } from '../../../../types/recipe';

export const basicmarinade: Recipe = {
  name: 'Basicmarinade',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Cupextra virgin olive oil', amount: 2.0, unit: 'tbsp' },
    { name: 'Itablespoondijonmustard', amount: 1.0, unit: 'tsp' },
    { name: 'Ciovesgarlicc Peeledandcrushed', amount: 1.0 },
    { name: 'Tablespoonsshoyu', amount: 1.0 },
    { name: 'Itablespoonbaisamicvinegar', amount: 2.0, unit: 'tbsp' },
    { name: 'Itablespooniemonjuice', amount: 1.0 },
    { name: 'Freshgroundblackpepper', amount: 0.25, unit: 'tsp' },
    { name: 'Dashhotsauce', amount: 2.0, unit: 'tbsp' },
    { name: 'io.s whisktogetheraningredients.', amount: 1.0 },
  ],
  instructions: [
    'Whisk together all ingredients.',
    'Marinate vegetables and grill.',
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
