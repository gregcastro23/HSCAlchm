import { Recipe } from '../../../../types/recipe';

export const monkfishwithlemonCaperbutter: Recipe = {
  name: 'Monkfishwithlemon Caperbutter',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Monkfishfnets Seasonedwithsaitandpepper', amount: 1.0 },
    { name: 'Saitandpeppertoseasonfish', amount: 1.0 },
    { name: 'Y Cupan Purposefiour Fordredging', amount: 1.0 },
    { name: 'Etablespoonsolive oil', amount: 1.0 },
    { name: 'Tablespoonsbutter', amount: 1.0 },
    { name: 'Tablespoonscapers', amount: 1.0 },
    { name: 'Tablespoonsiemonjuice Approximately', amount: 1.0 },
    { name: 'Iaiemon', amount: 1.0, unit: 'whole', notes: 'juice only' },
    { name: '0.5 Heatconventionaiovento', amount: 1.0 },
    { name: 'etsf.', amount: 1.0 },
  ],
  instructions: [
    'Heat conventional oven to 375° F.',
    'Dredge filets in flour. Shake off excess.',
    'Heat olive oil in 10-inch sauté pan over medium heat.',
    'Brown filets on both sides.',
    'Transfer fish to sizzle platter, and complete cooking in oven, approximately 10 minutes.',
    'Transfer fish from oven to plate and garnish with browned butter. Serve immediately.',
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
