import { Recipe } from '../../../../types/recipe';

export const quinoabuddhabowl: Recipe = {
    name: 'Quinoa Buddha Bowl',
    description: 'A nourishing bowl of quinoa, roasted vegetables, and tahini dressing.',
    ingredients: [
      { name: 'quinoa', amount: 1, unit: 'cup' },
      { name: 'sweet potato, cubed', amount: 2, unit: 'medium' },
      { name: 'chickpeas, drained', amount: 15, unit: 'oz' },
      { name: 'kale, chopped', amount: 4, unit: 'cups' },
      { name: 'red onion, sliced', amount: 1, unit: 'medium' },
      { name: 'olive oil', amount: 3, unit: 'tbsp' },
      { name: 'tahini', amount: 0.25, unit: 'cup' },
      { name: 'lemon juice', amount: 2, unit: 'tbsp' },
      { name: 'garlic clove, minced', amount: 1, unit: '' },
      { name: 'salt', amount: 1, unit: 'tsp' },
      { name: 'black pepper', amount: 0.5, unit: 'tsp' }
    ],
    nutrition: {
      calories: 420,
      protein: 14,
      carbs: 58,
      fat: 18,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Iron', 'Magnesium']
    },
    timeToMake: '45 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Dinner'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.4,
      Water: 0.3,
      Air: 0.1
    },
    instructions: [
      'Preheat oven to 400°F.',
      'Cook quinoa according to package instructions.',
      'Toss sweet potato and chickpeas with 2 tbsp olive oil, salt, and pepper. Roast for 25-30 minutes.',
      'Make dressing by whisking together tahini, lemon juice, garlic, and 2-4 tbsp water.',
      'Massage kale with remaining olive oil.',
      'Assemble bowls with quinoa, roasted vegetables, kale, and drizzle with tahini dressing.'
    ]
  },;