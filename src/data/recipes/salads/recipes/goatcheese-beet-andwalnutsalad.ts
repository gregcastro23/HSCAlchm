import { Recipe } from '../../../../types/recipe';

export const goatcheeseBeetAndwalnutsalad: Recipe = {
  name: 'Goatcheese Beet Andwalnutsalad',
  description: 'A fresh and vibrant salad featuring seasonal ingredients and crisp textures.',
  ingredients: [
    { name: 'Headsromaineiettuce', amount: 1.0 },
    { name: 'Buncheswatercress Stemmed', amount: 1.0 },
    { name: 'Headsredoakieafiettuce', amount: 1.0 },
    { name: 'Headsfrisee', amount: 1.0 },
    { name: 'Endive', amount: 1.0 },
    { name: 'o.sredonion Thiniysliced', amount: 0.5 },
    { name: 'Osmanbeets Roasted Peeledandcutintobitesizepieces', amount: 1.0 },
    { name: 'Cupstoastedwainuts', amount: 0.25, unit: 'cup', notes: 'sliced, for serving' },
    { name: 'Poundssoftgoatcheese', amount: 1.0 },
    { name: 'Baguettes Cutinto', amount: 1.0 },
    { name: 'Sncesandtoasted', amount: 0.5, unit: 'cup' },
    { name: 'Irecipecreamyfreshhorseradishdressing recipebeiow)', amount: 1.0 },
    { name: 'tossangreenstogetherandputonindividuaipiates.', amount: 1.0 },
  ],
  instructions: [
    'Inlarge bowl, toss all greens together and put on individual plates.',
    'Assemble each plate with endive, onion, beets, walnuts, goat cheese, and baguettes.',
    'Dress each salad immediately prior to service.',
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
