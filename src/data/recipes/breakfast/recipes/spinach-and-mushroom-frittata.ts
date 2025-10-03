import { Recipe } from '../../../../types/recipe';

export const spinachandmushroomfrittata: Recipe = {
    name: 'Spinach and Mushroom Frittata',
    description: 'A fluffy and flavorful frittata packed with spinach, mushrooms, and cheese.',
    ingredients: [
      { name: 'eggs', amount: 8, unit: '' },
      { name: 'milk', amount: 0.25, unit: 'cup' },
      { name: 'olive oil', amount: 1, unit: 'tbsp' },
      { name: 'onion, diced', amount: 1, unit: '' },
      { name: 'garlic cloves, minced', amount: 2, unit: '' },
      { name: 'mushrooms, sliced', amount: 8, unit: 'oz' },
      { name: 'baby spinach', amount: 4, unit: 'cups' },
      { name: 'cheddar cheese, shredded', amount: 1, unit: 'cup', swaps: ['feta cheese', 'goat cheese'] },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 280,
      protein: 20,
      carbs: 8,
      fat: 18,
      vitamins: ['A', 'D', 'B12'],
      minerals: ['Iron', 'Calcium']
    },
    timeToMake: '35 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Breakfast', 'Brunch'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.4,
      Water: 0.3,
      Air: 0.1
    },
    instructions: [
      'Preheat oven to 375°F.',
      'In a large bowl, whisk together eggs, milk, salt, and pepper.',
      'In a large oven-safe skillet, heat olive oil over medium heat. Add onion and garlic, and cook until softened, about 5 minutes.',
      'Add mushrooms and cook until tender and liquid has evaporated, about 5 minutes.',
      'Add spinach and cook until wilted, about 2 minutes.',
      'Pour egg mixture over the vegetables in the skillet. Sprinkle shredded cheese on top.',
      'Cook on the stovetop for 2-3 minutes, until the edges start to set.',
      'Transfer the skillet to the preheated oven and bake for 15-20 minutes, until the frittata is set and lightly golden on top.',
      'Remove from oven, let cool for 5 minutes, then slice and serve hot.'
    ]
  },;