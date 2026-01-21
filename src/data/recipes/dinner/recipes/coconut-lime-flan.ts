import { Recipe } from '../../../../types/recipe';

export const coconutLimeFlan: Recipe = {
  name: 'Coconut-Lime Flan',
  description: 'A tropical dairy-free flan with coconut milk and lime.',
  ingredients: [
    { name: 'coconut milk', amount: 3.5, unit: 'cups' },
    { name: 'agar flakes', amount: 2.0, unit: 'tbsp' },
    { name: 'maple syrup', amount: 0.5, unit: 'cup' },
    { name: 'kuzu', amount: 1.0, unit: 'tbsp' },
    { name: 'lime juice', amount: 3.0, unit: 'tbsp' },
    { name: 'water', amount: 0.5, unit: 'cup' },
    { name: 'maple crystals', amount: 0.5, unit: 'cup' },
    { name: 'toasted dried coconut', amount: 0.5, unit: 'cup' },
  ],
  instructions: [
    'In21/2 quart pot, combine coconut milk and agar. Soak agar for 5 minutes.',
    'Bring mixture to boil. Reduce heat and simmer uncovered for about 5 minutes or more, until',
    'Add maple syrup and stir until combined.',
    'Dissolve kuzu in lime juice and water until there are no lumps. Add to milk mixture and',
    'Lightly oil ramekins and sprinkle 2 teaspoons maple crystals in bottom of each ramekin.',
    'Pour custard into ramekins. Refrigerate to set.',
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
