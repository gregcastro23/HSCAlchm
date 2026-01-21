import { Recipe } from '../../../../types/recipe';

export const ravioliwithbeetstuffing: Recipe = {
  name: 'Ravioliwithbeetstuffing',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Ipoundfreshbeets', amount: 1.0, unit: 'cup', notes: 'for serving' },
    { name: 'Iteaspoonfeneiseeds', amount: 1.0 },
    { name: 'Iacupbutter', amount: 1.0 },
    { name: 'Iaacupmincedshanots', amount: 1.0 },
    { name: 'Eacupbreadcrumbs', amount: 0.5, unit: 'cup' },
    { name: 'o.i2steaspoongroundginger', amount: 1.0 },
    { name: 'Tspait Ormoretotaste', amount: 1.0 },
    { name: 'Freshiygroundblackpepper', amount: 0.25, unit: 'tsp' },
    { name: 'Ieggyoik', amount: 1.0 },
    { name: 'Eggwhiteforbrushing', amount: 2.0 },
  ],
  instructions: [
    'Cover beets with water and simmer until tender. Peel and puree in food processor.',
    'Toast fennel seeds in sauté pan. Remove to spice grinder or mortar and pestle and grind.',
    'Heat butter in 8-inch sauté pan, and sauté shallots until translucent. Add breaderumbs',
    'In food processor, combine tofu, olive oil, lemon juice, salt, garlic and miso. Process,',
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
