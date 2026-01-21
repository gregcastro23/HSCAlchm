import { Recipe } from '../../../../types/recipe';

export const sweetbrewwithcitrusfruit: Recipe = {
  name: 'Sweetbrewwithcitrusfruit',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'Quartsfnteredwater', amount: 1.0, unit: 'cup' },
    { name: 'Gkukichateabags o.scupioosekukicha)', amount: 1.0 },
    { name: 'Mintteabags', amount: 4.0 },
    { name: 'Iemon Thiniysliced', amount: 0.5 },
    { name: 'Orange Thiniysliced', amount: 2.0, unit: 'tbsp' },
    { name: 'Quartsorganicappiejuice', amount: 1.0 },
    { name: 'o.sint Ganonpot bringwatertobon.', amount: 1.0 },
  ],
  instructions: [
    'In1-gallon pot, bring water to boil.',
    'Turn off flame. Steep tea bags and fruit in water, covered, for 5 minutes.',
    'Add apple juice to pot, stir and serve.',
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
