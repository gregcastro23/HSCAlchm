import { Recipe } from '../../../../types/recipe';

export const capresestuffedportobellomushrooms: Recipe = {
    name: 'Caprese Stuffed Portobello Mushrooms',
    description: 'Juicy portobello mushrooms stuffed with fresh mozzarella, tomatoes, and basil, then baked to perfection.',
    ingredients: [
      { name: 'portobello mushrooms, stems removed', amount: 4, unit: 'large' },
      { name: 'olive oil', amount: 2, unit: 'tbsp' },
      { name: 'fresh mozzarella, sliced', amount: 8, unit: 'oz' },
      { name: 'tomatoes, sliced', amount: 2, unit: 'medium' },
      { name: 'fresh basil leaves', amount: 1, unit: 'cup' },
      { name: 'balsamic vinegar', amount: 2, unit: 'tbsp' },
      { name: 'garlic cloves, minced', amount: 2, unit: '' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 280,
      protein: 14,
      carbs: 12,
      fat: 20,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Potassium', 'Calcium']
    },
    timeToMake: '30 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Entree'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.5,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'Preheat oven to 400°F. Brush portobello mushrooms with olive oil and place on a baking sheet, gill-side up.',
      'In a small bowl, whisk together balsamic vinegar, minced garlic, salt, and pepper.',
      'Arrange sliced mozzarella, tomatoes, and basil leaves inside each mushroom cap. Drizzle with the balsamic mixture.',
      'Bake for 15-20 minutes, until the mushrooms are tender and the cheese is melted and bubbly.',
      'Serve hot, garnished with additional fresh basil leaves if desired.'
    ]
  },;