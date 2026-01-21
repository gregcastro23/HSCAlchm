import { Recipe } from '../../../../types/recipe';

export const threeCitrusmarinade: Recipe = {
  name: 'Three Citrusmarinade',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Cupfreshnmejuice', amount: 4.0, unit: 'oz' },
    { name: 'Cupfreshiemonjuice', amount: 2.0, unit: 'tbsp', notes: 'freshly squeezed' },
    { name: 'Y Cupfreshorangejuice', amount: 2.0, unit: 'tbsp' },
    { name: 'Cupolive oil', amount: 1.0 },
    { name: 'Ciovesgarlicc Sliced', amount: 0.25, unit: 'cup' },
    { name: 'Tspcoarseiygroundblackpepper', amount: 0.25, unit: 'tsp' },
    { name: 'Sbayieaves Crushed', amount: 0.5, unit: 'cup' },
    { name: 'Stablespoonschoppedcnantro', amount: 1.0 },
    { name: 'Iemonjuice Orangejuice Enveon Garlicc Blackpepper Bayieaves', amount: 1.0 },
    { name: 'andcnantroinbiender.', amount: 1.0 },
  ],
  instructions: [
    'Combine lime juice, lemon juice, orange juice, olive oil, garlic, black pepper, bay leaves',
    'Let stand 30 minutes to allow flavors to develop before using.',
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
