import { Recipe } from '../../../../types/recipe';

export const saltCrustedbakedbass: Recipe = {
  name: 'Salt Crustedbakedbass',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'I o.tspound Whoiebass Gnis Fins Andvisceraremoved', amount: 1.0 },
    { name: 'o.souncefreshthyme', amount: 2.0, unit: 'tsp', notes: 'chopped' },
    { name: 'egg whites', amount: 2.0 },
    { name: 'Cupskoshersait', amount: 1.0 },
    { name: 'Extra virgin olive oilfordrizzng', amount: 2.0, unit: 'tbsp' },
  ],
  instructions: [
    'Crack crust with sharp knife and carefully remove.',
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
