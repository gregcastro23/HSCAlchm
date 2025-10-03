import { Recipe } from '../../../../types/recipe';

export const spinachAndArtichokeDip: Recipe = {
  name: 'Spinach and Artichoke Dip',
  description: 'A warm and creamy dip loaded with spinach, artichokes, and melted cheese.',
  ingredients: [
    { name: 'frozen spinach, thawed and squeezed dry', amount: 10, unit: 'oz' },
    { name: 'marinated artichoke hearts, drained and chopped', amount: 14, unit: 'oz' },
    { name: 'cream cheese, softened', amount: 8, unit: 'oz' },
    { name: 'sour cream', amount: 0.5, unit: 'cup' },
    { name: 'mayonnaise', amount: 0.25, unit: 'cup' },
    { name: 'Parmesan cheese, grated', amount: 0.5, unit: 'cup' },
    { name: 'garlic cloves, minced', amount: 3, unit: '' },
    { name: 'red pepper flakes', amount: 0.25, unit: 'tsp' },
    { name: 'salt', amount: 0.5, unit: 'tsp' },
    { name: 'black pepper', amount: 0.25, unit: 'tsp' }
  ],
  nutrition: {
    calories: 220,
    protein: 8,
    carbs: 8,
    fat: 18,
    vitamins: ['A', 'C', 'K'],
    minerals: ['Calcium', 'Iron']
  },
  timeToMake: '30 minutes',
  season: ['all'],
  cuisine: 'HSCA',
  mealType: ['Appetizer'],
  elementalBalance: {
    Fire: 0.2,
    Earth: 0.4,
    Water: 0.3,
    Air: 0.1
  },
  instructions: [
    'Preheat oven to 375°F.',
    'In a large bowl, mix together spinach, artichoke hearts, cream cheese, sour cream, mayonnaise, Parmesan cheese, garlic, red pepper flakes, salt, and pepper until well combined.',
    'Transfer mixture to a baking dish and spread evenly.',
    'Bake for 20-25 minutes, until hot and bubbly and lightly browned on top.',
    'Serve warm with pita chips, sliced baguette, or fresh vegetables for dipping.'
  ]
};
