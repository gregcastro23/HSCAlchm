import { Recipe } from '../../../../types/recipe';

export const chickenunderabrick: Recipe = {
  name: 'Chickenunderabrick',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'Ipoundschicken aamedium)', amount: 1.0 },
    { name: 'Tspeasait', amount: 0.125, unit: 'tsp' },
    { name: 'Teaspeonfreshiygroundblackpepper', amount: 0.25, unit: 'tsp' },
    { name: 'Itablespoonextra Virginolive oil', amount: 3.0, unit: 'tbsp' },
    { name: 'o.sheatconvectionovento', amount: 1.0 },
    { name: 'Oof', amount: 1.0 },
    { name: 'seasonchickenwithsaitandpepper.', amount: 1.0 },
  ],
  instructions: [
    'Heat convection oven to 400° F.',
    'Season chicken with salt and pepper.',
    'Heat oil in 10-inch sauté pan over high flame. When oil is hot but not yet smoking, add',
    'Transfer pan to oven and cook for 20 minutes. Remove from oven and remove brick.',
    'Turn chicken skin side up, and carefully pour off excess fat.',
    'Transfer pan back to oven for additional 5-10 minutes, with fan turned to high.',
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
