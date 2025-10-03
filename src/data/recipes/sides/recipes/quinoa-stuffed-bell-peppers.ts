import { Recipe } from '../../../../types/recipe';

export const quinoastuffedbellpeppers: Recipe = {
    name: 'Quinoa Stuffed Bell Peppers',
    description: 'Colorful bell peppers stuffed with a flavorful mixture of quinoa, vegetables, and herbs.',
    ingredients: [
      { name: 'bell peppers', amount: 4, unit: 'medium' },
      { name: 'quinoa, rinsed', amount: 1, unit: 'cup' },
      { name: 'water', amount: 2, unit: 'cups' },
      { name: 'olive oil', amount: 2, unit: 'tbsp' },
      { name: 'onion, diced', amount: 1, unit: '' },
      { name: 'garlic cloves, minced', amount: 3, unit: '' },
      { name: 'zucchini, diced', amount: 1, unit: '' },
      { name: 'diced tomatoes, drained', amount: 1, unit: 'can' },
      { name: 'fresh parsley, chopped', amount: 0.25, unit: 'cup' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' },
      { name: 'crumbled feta cheese', amount: 0.5, unit: 'cup', swaps: ['goat cheese', 'shredded mozzarella'] }
    ],
    nutrition: {
      calories: 320,
      protein: 12,
      carbs: 48,
      fat: 10,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Iron', 'Magnesium']
    },
    timeToMake: '60 minutes',
    season: ['summer', 'fall'],
    cuisine: 'HSCA',
    mealType: ['Side Dish'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.5,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'Preheat oven to 375°F. Cut bell peppers in half lengthwise and remove seeds and membranes. Place peppers cut-side up in a baking dish.',
      'In a medium saucepan, bring quinoa and water to a boil. Reduce heat, cover, and simmer until quinoa is tender and water is absorbed, about 15 minutes.',
      'In a large skillet, heat olive oil over medium heat. Add onion and garlic, and cook until softened, about 5 minutes.',
      'Add zucchini and cook until tender, about 3 minutes. Stir in cooked quinoa, diced tomatoes, parsley, salt, and pepper.',
      'Spoon quinoa mixture into bell pepper halves. Top with crumbled feta cheese.',
      'Bake stuffed peppers for 25-30 minutes, until peppers are tender and filling is heated through.',
      'Serve hot, garnished with additional fresh parsley if desired.'
    ]
  },;