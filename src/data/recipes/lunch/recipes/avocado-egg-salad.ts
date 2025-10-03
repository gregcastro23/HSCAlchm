import { Recipe } from '../../../../types/recipe';

export const avocadoeggsalad: Recipe = {
    name: 'Avocado Egg Salad',
    description: 'A creamy and nutritious twist on classic egg salad, made with mashed avocado.',
    ingredients: [
      { name: 'hard-boiled eggs, chopped', amount: 6, unit: '' },
      { name: 'ripe avocado, mashed', amount: 1, unit: '' },
      { name: 'red onion, finely diced', amount: 0.25, unit: 'cup' },
      { name: 'celery stalk, finely diced', amount: 1, unit: '' },
      { name: 'fresh dill, chopped', amount: 2, unit: 'tbsp', swaps: ['parsley', 'chives'] },
      { name: 'lemon juice', amount: 1, unit: 'tbsp' },
      { name: 'Dijon mustard', amount: 1, unit: 'tsp' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 200,
      protein: 12,
      carbs: 6,
      fat: 14,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Potassium', 'Folate']
    },
    timeToMake: '20 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Lunch'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.4,
      Water: 0.4,
      Air: 0.1
    },
    instructions: [
      'In a large bowl, combine chopped hard-boiled eggs, mashed avocado, red onion, celery, and fresh dill.',
      'Add lemon juice, Dijon mustard, salt, and pepper to the bowl. Mix well until all ingredients are evenly combined.',
      'Taste and adjust seasoning as needed.',
      'Serve on toasted bread, crackers, or lettuce wraps for a low-carb option.',
      'Store any leftovers in an airtight container in the refrigerator for up to 3 days.'
    ]
  };