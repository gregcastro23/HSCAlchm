import { Recipe } from '../../../../types/recipe';

export const roastedbutternutsquashsalad: Recipe = {
    name: 'Roasted Butternut Squash Salad',
    description: 'A hearty and flavorful salad featuring roasted butternut squash, greens, and a tangy dressing.',
    ingredients: [
      { name: 'butternut squash, cubed', amount: 4, unit: 'cups' },
      { name: 'olive oil', amount: 2, unit: 'tbsp' },
      { name: 'mixed greens', amount: 6, unit: 'cups' },
      { name: 'dried cranberries', amount: 0.5, unit: 'cup' },
      { name: 'pumpkin seeds', amount: 0.25, unit: 'cup' },
      { name: 'goat cheese, crumbled', amount: 4, unit: 'oz', swaps: ['feta cheese'] },
      { name: 'apple cider vinegar', amount: 2, unit: 'tbsp' },
      { name: 'Dijon mustard', amount: 1, unit: 'tsp' },
      { name: 'honey', amount: 1, unit: 'tbsp' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 320,
      protein: 8,
      carbs: 36,
      fat: 18,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Potassium', 'Magnesium']
    },
    timeToMake: '40 minutes',
    season: ['fall', 'winter'],
    cuisine: 'HSCA',
    mealType: ['Side Dish'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.6,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'Preheat oven to 400°F. Toss cubed butternut squash with olive oil, salt, and pepper. Spread on a baking sheet and roast for 25-30 minutes, until tender and lightly caramelized.',
      'In a large bowl, combine mixed greens, roasted butternut squash, dried cranberries, pumpkin seeds, and crumbled goat cheese.',
      'In a small bowl, whisk together apple cider vinegar, Dijon mustard, honey, salt, and pepper to make the dressing.',
      'Drizzle dressing over salad and toss to coat evenly.',
      'Serve immediately and enjoy!'
    ]
  },;