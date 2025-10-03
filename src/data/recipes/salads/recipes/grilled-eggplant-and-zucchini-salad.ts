import { Recipe } from '../../../../types/recipe';

export const grilledeggplantandzucchinisalad: Recipe = {
    name: 'Grilled Eggplant and Zucchini Salad',
    description: 'A smoky and savory salad made with grilled eggplant, zucchini, and a tangy lemon vinaigrette.',
    ingredients: [
      { name: 'eggplant, sliced into rounds', amount: 1, unit: 'large' },
      { name: 'zucchini, sliced lengthwise', amount: 2, unit: 'medium' },
      { name: 'olive oil', amount: 3, unit: 'tbsp' },
      { name: 'mixed greens', amount: 4, unit: 'cups' },
      { name: 'cherry tomatoes, halved', amount: 1, unit: 'cup' },
      { name: 'red onion, thinly sliced', amount: 0.5, unit: '' },
      { name: 'lemon, juiced', amount: 1, unit: '' },
      { name: 'Dijon mustard', amount: 1, unit: 'tsp' },
      { name: 'garlic clove, minced', amount: 1, unit: '' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 240,
      protein: 4,
      carbs: 16,
      fat: 18,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Potassium', 'Manganese']
    },
    timeToMake: '30 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Salad'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.5,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'Preheat grill to medium-high heat.',
      'Brush eggplant and zucchini slices with 2 tablespoons of olive oil, salt, and pepper.',
      'Grill eggplant and zucchini for 3-4 minutes per side, until tender and lightly charred. Remove from heat and let cool slightly.',
      'In a large bowl, combine mixed greens, cherry tomatoes, and sliced red onion.',
      'In a small bowl, whisk together lemon juice, remaining olive oil, Dijon mustard, minced garlic, salt, and pepper to make the vinaigrette.',
      'Cut grilled eggplant and zucchini into bite-sized pieces and add to the salad bowl.',
      'Drizzle the vinaigrette over the salad and toss gently to coat evenly.',
      'Serve immediately as a refreshing and healthy salad.'
    ]
  },;