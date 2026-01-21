import { Recipe } from '../../../../types/recipe';

export const ceviche: Recipe = {
  name: 'Ceviche',
  description: 'A professional dinne recipe recovered from HSCA culinary school materials.',
  ingredients: [
    { name: 'sea scallops, cut into quartors', amount: 1.0, unit: 'pound' },
    { name: 'pepper, brunoise', amount: 1.0, unit: 'jalapeno' },
    { name: 'red onion (2 ounces), minced', amount: 0.25, unit: 'small' },
    { name: 'tomatoes, seeded and cut into small dice', amount: 2.0, unit: 'ripe' },
    { name: 'garlic, minced', amount: 1.0, unit: 'clove' },
    { name: 'rice syrup (optional)', amount: 2.0, unit: 'toaspoons' },
    { name: 'c', amount: 2.0, unit: 'tablespoons' },
  ],
  instructions: [
    'In large bowl, combine scallops, jalapeno, red pepper, onion, tomato, garlic, rice syrup,',
    'Cover and refrigerate for at least 30-60 minutes, or until scallops lose their translucent',
    'Serve in individual chilled bowls or glasses garnished with avocado slices and parsley.',
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
