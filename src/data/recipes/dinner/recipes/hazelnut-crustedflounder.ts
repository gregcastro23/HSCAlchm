import { Recipe } from '../../../../types/recipe';

export const hazelnutCrustedflounder: Recipe = {
  name: 'Hazelnut Crustedflounder',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Cupshazeinuts Toasted Skinsremoved', amount: 1.0 },
    { name: 'Cuppankobreadcrumbs', amount: 0.5, unit: 'cup' },
    { name: 'Y Cupan Purposefiour', amount: 2.25, unit: 'cups' },
    { name: 'Eggs Beaten', amount: 1.0 },
    { name: 'Bfiounderfnets Seasonedwithsaitandpepper', amount: 1.0 },
    { name: 'Cupcanoiaon', amount: 1.0 },
    { name: 'Mangosaisa recipebeiow)', amount: 1.0 },
    { name: 'Preheatconventionaiovento', amount: 1.0 },
    { name: 'etsf.', amount: 1.0 },
  ],
  instructions: [
    'Combine hazelnuts and breadcrumbs in food processor. Pulse mixture until uniformly',
    'Dredge fish filet in flour, shaking off excess. Transfer filets to egg mixture, making sure to',
    'Heat canola oil in large sauté pan over medium-high heat. Add filets to pan, careful not to',
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
