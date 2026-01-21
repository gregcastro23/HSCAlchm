import { Recipe } from '../../../../types/recipe';

export const arugulaOliveoilBalsamicreduction: Recipe = {
  name: 'Arugula Oliveoil Balsamicreduction',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Servesb', amount: 1.0 },
    { name: 'Cupsbaisamicvinegar', amount: 2.0, unit: 'tbsp' },
    { name: 'Iteaspoonvania', amount: 1.0 },
    { name: 'Bouncesaruguia', amount: 1.0 },
    { name: 'Etablespoonsonvean', amount: 1.0 },
    { name: 'Iatspait', amount: 1.0 },
    { name: 'Iaapoundreggianoparmesan Gratedorshaved optionai)', amount: 1.0 },
  ],
  instructions: [
    'Combine balsamic vinegar and vanilla in medium pan. Bring mixture to simmer, and',
    'Toss arugula, oil, and salt together in bowl. Drizzle balsamic reduction to taste over',
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
