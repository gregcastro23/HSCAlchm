import { Recipe } from '../../../../types/recipe';

export const redlentilandtoastedsunflowerburger: Recipe = {
    name: 'Red Lentil and Toasted Sunflower Burger',
    description: 'A protein-rich vegetarian burger made with red lentils and toasted sunflower seeds.',
    ingredients: [
      { name: 'red lentils', amount: 1, unit: 'cup' },
      { name: 'sunflower seeds', amount: 0.5, unit: 'cup', notes: 'toasted' },
      { name: 'onion, diced', amount: 1, unit: 'medium' },
      { name: 'garlic cloves, minced', amount: 3, unit: '' },
      { name: 'carrots, grated', amount: 2, unit: 'medium' },
      { name: 'rolled oats', amount: 0.5, unit: 'cup' },
      { name: 'flax seeds, ground', amount: 2, unit: 'tbsp' },
      { name: 'cumin, ground', amount: 1, unit: 'tsp' },
      { name: 'olive oil', amount: 2, unit: 'tbsp' },
      { name: 'salt', amount: 1, unit: 'tsp' },
      { name: 'black pepper', amount: 0.5, unit: 'tsp' }
    ],
    nutrition: {
      calories: 260,
      protein: 12,
      carbs: 28,
      fat: 14,
      vitamins: ['B1', 'B6', 'E'],
      minerals: ['Iron', 'Zinc', 'Magnesium']
    },
    timeToMake: '45 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Entree'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.4,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'Cook red lentils until tender, about 15 minutes. Drain well.',
      'Toast sunflower seeds in a dry skillet until fragrant.',
      'Sauté onion and garlic in 1 tbsp olive oil until softened.',
      'In a food processor, combine lentils, sunflower seeds, onion mixture, carrots, oats, and spices.',
      'Form into 6 patties and refrigerate for 30 minutes.',
      'Heat remaining oil in a skillet and cook patties until golden brown, about 4-5 minutes per side.'
    ]
  },;