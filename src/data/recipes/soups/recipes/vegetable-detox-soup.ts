import { Recipe } from '../../../../types/recipe';

export const vegetableDetoxSoup: Recipe = {
  name: 'Vegetable Detox Soup',
  description: 'A cleansing soup packed with detoxifying vegetables and healing herbs.',
  ingredients: [
    { name: 'olive oil', amount: 2, unit: 'tbsp' },
    { name: 'onion', amount: 1, unit: 'large', notes: 'diced' },
    { name: 'garlic cloves', amount: 4, unit: '', notes: 'minced' },
    { name: 'ginger', amount: 2, unit: 'tbsp', notes: 'fresh, minced' },
    { name: 'celery stalks', amount: 4, unit: '', notes: 'chopped' },
    { name: 'carrots', amount: 3, unit: 'medium', notes: 'chopped' },
    { name: 'broccoli', amount: 2, unit: 'cups', notes: 'florets' },
    { name: 'kale', amount: 4, unit: 'cups', notes: 'chopped' },
    { name: 'parsley', amount: 1, unit: 'cup', notes: 'fresh' },
    { name: 'turmeric', amount: 1, unit: 'tsp', notes: 'ground' },
    { name: 'vegetable broth', amount: 8, unit: 'cups' },
    { name: 'lemon', amount: 1, unit: 'whole', notes: 'juice only' },
    { name: 'sea salt', amount: 1, unit: 'tsp' },
    { name: 'black pepper', amount: 0.5, unit: 'tsp' }
  ],
  nutrition: {
    calories: 120,
    protein: 4,
    carbs: 18,
    fat: 5,
    vitamins: ['A', 'C', 'K'],
    minerals: ['Iron', 'Potassium', 'Magnesium']
  },
  timeToMake: '40 minutes',
  season: ['all'],
  cuisine: 'HSCA',
  mealType: ['Soup'],
  elementalBalance: {
    Fire: 0.2,
    Earth: 0.2,
    Water: 0.4,
    Air: 0.2
  },
  instructions: [
    'Heat olive oil in a large pot over medium heat.',
    'Add onion, garlic, and ginger. Sauté until onion is translucent, about 5 minutes.',
    'Add celery and carrots. Cook for another 5 minutes.',
    'Stir in turmeric and cook for 1 minute until fragrant.',
    'Add vegetable broth and bring to a boil.',
    'Reduce heat and simmer for 10 minutes.',
    'Add broccoli and continue cooking for 5 minutes.',
    'Add kale and cook until just wilted, about 3 minutes.',
    'Stir in parsley and lemon juice.',
    'Season with salt and pepper to taste.',
    'Serve hot, garnished with additional fresh parsley if desired.'
  ]
};
