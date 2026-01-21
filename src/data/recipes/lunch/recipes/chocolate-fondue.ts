import { Recipe } from '../../../../types/recipe';

export const chocolateFondue: Recipe = {
  name: 'Chocolate Fondue',
  description: 'A rich and creamy dairy-free chocolate fondue perfect for dipping fruits and treats.',
  ingredients: [
    { name: 'dark chocolate', amount: 12.0, unit: 'oz', notes: 'chopped' },
    { name: 'coconut milk', amount: 1.0, unit: 'cup', notes: 'full fat' },
    { name: 'maple syrup', amount: 2.0, unit: 'tbsp' },
    { name: 'vanilla extract', amount: 1.0, unit: 'tsp' },
    { name: 'sea salt', amount: 0.125, unit: 'tsp' },
    { name: 'assorted fruits', amount: 4.0, unit: 'cups', notes: 'for dipping' },
    { name: 'nuts', amount: 1.0, unit: 'cup', notes: 'toasted, for dipping' },
  ],
  instructions: [
    'Insmall saucepan, combine cocoa, maple syrup, vanilla extract, and orange extract,',
    'Cover pot and gently bring to simmer. Lower heat and cook for 1-2 minutes, being careful',
    'Remove from heat and stir in soy milk until sauce has nappé.',
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
