import { Recipe } from '../../../../types/recipe';

export const broiledarcticcharwithblackquinoa: Recipe = {
    name: 'Broiled Arctic Char with Black Quinoa',
    description: 'Broiled arctic char served over black quinoa with rapini and capers.',
    ingredients: [
      { name: 'arctic char fillets', amount: 24, unit: 'oz', notes: '6 oz portions' },
      { name: 'black quinoa', amount: 1.5, unit: 'cups' },
      { name: 'rapini', amount: 2, unit: 'bunches' },
      { name: 'capers', amount: 3, unit: 'tbsp' },
      { name: 'lemon', amount: 2, unit: '', notes: '1 juiced, 1 for serving' },
      { name: 'olive oil', amount: 3, unit: 'tbsp' },
      { name: 'garlic cloves, minced', amount: 4, unit: '' },
      { name: 'red pepper flakes', amount: 0.5, unit: 'tsp' },
      { name: 'salt', amount: 1, unit: 'tsp' },
      { name: 'black pepper', amount: 0.5, unit: 'tsp' }
    ],
    nutrition: {
      calories: 420,
      protein: 38,
      carbs: 32,
      fat: 18,
      vitamins: ['B12', 'D', 'K'],
      minerals: ['Omega-3', 'Iron']
    },
    timeToMake: '40 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Dinner'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.2,
      Water: 0.3,
      Air: 0.2
    },
    instructions: [
      'Cook black quinoa according to package instructions.',
      'Blanch rapini in boiling water for 2 minutes, then shock in ice water.',
      'Season arctic char with salt, pepper, and olive oil.',
      'Broil char for 8-10 minutes until cooked through.',
      'Sauté blanched rapini with garlic and red pepper flakes.',
      'Toss quinoa with capers, lemon juice, and remaining olive oil.',
      'Serve char over quinoa and rapini, garnished with lemon wedges.'
    ]
  };