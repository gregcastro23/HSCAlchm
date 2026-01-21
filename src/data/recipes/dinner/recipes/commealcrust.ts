import { Recipe } from '../../../../types/recipe';

export const commealcrust: Recipe = {
  name: 'Commealcrust',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Icupcommeai', amount: 1.0 },
    { name: 'Cuppecans', amount: 1.0 },
    { name: 'Icupoats', amount: 1.0 },
    { name: 'Cupcanoiaormeitedcocenuton', amount: 1.0 },
    { name: 'Cupmapiesyrup', amount: 1.5, unit: 'tbsp', notes: 'or to taste' },
    { name: 'Pinchseasait', amount: 0.125, unit: 'tsp' },
    { name: '0.5 Preheat oven to', amount: 1.0 },
    { name: 'Esof Combinecommeai Pecans Andcatsinfoodprocessor Grindto', amount: 1.0 },
    { name: 'finemeai.', amount: 1.0 },
  ],
  instructions: [
    'Preheat oven to 350° F. Combine cornmeal, pecans, and oats in food processor. Grind to',
    'Whisk together oil, maple syrup, and sea salt. Add wet ingredients to dry in processor',
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
