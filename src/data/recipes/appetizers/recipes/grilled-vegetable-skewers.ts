import { Recipe } from '../../../../types/recipe';

export const grilledvegetableskewers: Recipe = {
    name: 'Grilled Vegetable Skewers',
    description: 'Colorful and flavorful skewers loaded with marinated and grilled vegetables.',
    ingredients: [
      { name: 'zucchini, sliced', amount: 2, unit: '' },
      { name: 'yellow squash, sliced', amount: 2, unit: '' },
      { name: 'red bell pepper, cut into chunks', amount: 1, unit: '' },
      { name: 'red onion, cut into chunks', amount: 1, unit: '' },
      { name: 'cherry tomatoes', amount: 1, unit: 'pint' },
      { name: 'olive oil', amount: 0.25, unit: 'cup' },
      { name: 'balsamic vinegar', amount: 2, unit: 'tbsp' },
      { name: 'garlic cloves, minced', amount: 2, unit: '' },
      { name: 'dried oregano', amount: 1, unit: 'tsp' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 120,
      protein: 2,
      carbs: 12,
      fat: 8,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Potassium', 'Manganese']
    },
    timeToMake: '30 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Appetizer', 'Side Dish'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.5,
      Water: 0.1,
      Air: 0.1
    },
    instructions: [
      'In a large bowl, whisk together olive oil, balsamic vinegar, garlic, oregano, salt, and pepper.',
      'Add zucchini, yellow squash, bell pepper, onion, and cherry tomatoes to the bowl and toss to coat evenly with the marinade.',
      'Thread the vegetables onto skewers, alternating colors and shapes for visual appeal.',
      'Preheat grill to medium-high heat. Grill skewers for 8-10 minutes, turning occasionally, until vegetables are tender and lightly charred.',
      'Serve hot as a side dish or appetizer.'
    ]
  },;