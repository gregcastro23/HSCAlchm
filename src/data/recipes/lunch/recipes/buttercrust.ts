import { Recipe } from '../../../../types/recipe';

export const buttercrust: Recipe = {
  name: 'Buttercrust',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'Iacupswhoiewheatpastryfiour', amount: 1.5, unit: 'cups' },
    { name: 'Tspait', amount: 1.0 },
    { name: 'Btablespoonscoid Sweetbutter', amount: 1.0 },
    { name: 'Acupicewater', amount: 1.0 },
    { name: '0.5 Siftthenmixfiourandsaitintobowi Usingtwoknivesorpastrycutter Cutbutterinto', amount: 1.0 },
    { name: 'fiourtoformverycoarsemeai.', amount: 1.0 },
  ],
  instructions: [
    'Sift then mix flour and salt into bowl. Using two knives or pastry cutter, cut butter into',
    'With rubber spatula, lightly toss flour while sprinkling water in mixture 1 tablespoon at a',
    'Roll on lightly floured parchment to desired shape.',
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
