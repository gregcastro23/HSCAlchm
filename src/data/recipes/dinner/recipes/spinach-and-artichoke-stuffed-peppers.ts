import { Recipe } from '../../../../types/recipe';

export const spinachandartichokestuffedpeppers: Recipe = {
    name: 'Spinach and Artichoke Stuffed Peppers',
    description: 'Colorful bell peppers stuffed with a creamy spinach and artichoke filling.',
    ingredients: [
      { name: 'bell peppers', amount: 4, unit: 'medium' },
      { name: 'olive oil', amount: 1, unit: 'tbsp' },
      { name: 'onion, diced', amount: 1, unit: '' },
      { name: 'garlic cloves, minced', amount: 2, unit: '' },
      { name: 'baby spinach', amount: 6, unit: 'cups' },
      { name: 'artichoke hearts, drained and chopped', amount: 14, unit: 'oz' },
      { name: 'cream cheese, softened', amount: 8, unit: 'oz' },
      { name: 'Parmesan cheese, grated', amount: 0.5, unit: 'cup' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 320,
      protein: 12,
      carbs: 20,
      fat: 22,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Calcium', 'Iron']
    },
    timeToMake: '45 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Entree'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.5,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'Preheat oven to 375°F. Cut bell peppers in half lengthwise and remove seeds and membranes. Place peppers cut-side up in a baking dish.',
      'In a large skillet, heat olive oil over medium heat. Add onion and garlic, and cook until softened, about 5 minutes.',
      'Add spinach and cook until wilted, about 3 minutes. Remove from heat and let cool slightly.',
      'In a bowl, mix cooked spinach mixture, chopped artichoke hearts, cream cheese, Parmesan cheese, salt, and pepper.',
      'Spoon the spinach and artichoke mixture into the bell pepper halves.',
      'Bake for 25-30 minutes, until peppers are tender and filling is hot and bubbly.',
      'Serve hot, garnished with additional Parmesan cheese if desired.'
    ]
  },;