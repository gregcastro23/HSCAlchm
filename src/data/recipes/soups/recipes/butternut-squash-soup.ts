import { Recipe } from '../../../../types/recipe';

export const butternutSquashSoup: Recipe = {
  name: 'Butternut Squash Soup',
  description: 'A creamy, warming soup perfect for fall and winter months.',
  ingredients: [
    { name: 'butternut squash, peeled and cubed', amount: 2, unit: 'lbs' },
    { name: 'olive oil', amount: 2, unit: 'tbsp' },
    { name: 'onion, chopped', amount: 1, unit: 'large' },
    { name: 'garlic cloves, minced', amount: 3, unit: '' },
    { name: 'fresh ginger, minced', amount: 1, unit: 'tbsp' },
    { name: 'vegetable broth', amount: 4, unit: 'cups' },
    { name: 'coconut milk', amount: 1, unit: 'can' },
    { name: 'maple syrup', amount: 1, unit: 'tbsp' },
    { name: 'ground cinnamon', amount: 0.5, unit: 'tsp' },
    { name: 'ground nutmeg', amount: 0.25, unit: 'tsp' },
    { name: 'salt', amount: 1, unit: 'tsp' },
    { name: 'black pepper', amount: 0.5, unit: 'tsp' }
  ],
  nutrition: {
    calories: 220,
    protein: 3,
    carbs: 28,
    fat: 12,
    vitamins: ['A', 'C'],
    minerals: ['Potassium', 'Magnesium']
  },
  timeToMake: '45 minutes',
  season: ['fall', 'winter'],
  cuisine: 'HSCA',
  mealType: ['Soup'],
  elementalBalance: {
    Fire: 0.2,
    Earth: 0.5,
    Water: 0.2,
    Air: 0.1
  },
  instructions: [
    'Heat olive oil in a large pot over medium heat. Add onion and cook until softened, about 5 minutes.',
    'Add garlic and ginger, cook for another minute until fragrant.',
    'Add butternut squash, vegetable broth, cinnamon, nutmeg, salt, and pepper. Bring to a boil.',
    'Reduce heat, cover, and simmer for 20-25 minutes until squash is very tender.',
    'Add coconut milk and maple syrup.',
    'Using an immersion blender, blend until smooth. Alternatively, carefully transfer to a blender in batches.',
    'Taste and adjust seasoning if needed.',
    'Serve hot, garnished with a drizzle of coconut milk and pumpkin seeds if desired.'
  ]
};
