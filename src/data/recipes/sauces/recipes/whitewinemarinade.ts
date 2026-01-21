import { Recipe } from '../../../../types/recipe';

export const whitewinemarinade: Recipe = {
  name: 'Whitewinemarinade',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Ea Cupwhitewine', amount: 1.0 },
    { name: 'Y Ecupolive oil', amount: 1.0 },
    { name: 'Ifreshiemonslicedorzestof', amount: 1.0 },
    { name: 'orange', amount: 1.0, notes: 'sliced' },
    { name: 'o.sheapingtablespoonchoppedfreshherbsoriteaspoondriedherbs', amount: 1.0 },
    { name: 'Severaiparsieysprigs', amount: 1.0 },
    { name: 'Freshblackpepper', amount: 0.25, unit: 'tsp', notes: 'ground' },
  ],
  instructions: [
    'Combine ingredients. This marinade can be used for most vegetables (use half amount of',
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
