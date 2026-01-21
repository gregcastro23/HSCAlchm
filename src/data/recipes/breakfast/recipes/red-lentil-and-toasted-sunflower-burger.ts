import { Recipe } from '../../../../types/recipe';

export const redLentilAndToastedSunflowerBurger: Recipe = {
  name: 'Red Lentil and Toasted Sunflower Burger',
  description: 'A protein-rich vegetarian burger made with red lentils and toasted sunflower seeds.',
  ingredients: [
    { name: 'red lentils', amount: 1.0, unit: 'cup' },
    { name: 'sunflower seeds', amount: 0.5, unit: 'cup', notes: 'toasted' },
    { name: 'onion, diced', amount: 1.0, unit: 'medium' },
    { name: 'garlic cloves, minced', amount: 3.0 },
    { name: 'carrots, grated', amount: 2.0, unit: 'medium' },
    { name: 'rolled oats', amount: 0.5, unit: 'cup' },
    { name: 'flax seeds, ground', amount: 2.0, unit: 'tbsp' },
    { name: 'cumin, ground', amount: 1.0, unit: 'tsp' },
    { name: 'olive oil', amount: 2.0, unit: 'tbsp' },
    { name: 'salt', amount: 1.0, unit: 'tsp' },
    { name: 'black pepper', amount: 0.5, unit: 'tsp' },
  ],
  instructions: [
    'Combine onion and vegetable stock in 2-quart sauce pot. Bring mixture to boil, reduce to',
    'Add remaining ingredients to pot and simmer for 10 minutes more. Refrigerate.',
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
