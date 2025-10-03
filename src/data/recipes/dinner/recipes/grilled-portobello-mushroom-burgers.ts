import { Recipe } from '../../../../types/recipe';

export const grilledportobellomushroomburgers: Recipe = {
    name: 'Grilled Portobello Mushroom Burgers',
    description: 'Hearty and flavorful vegetarian burgers made with marinated and grilled portobello mushrooms.',
    ingredients: [
      { name: 'portobello mushroom caps', amount: 4, unit: 'large' },
      { name: 'olive oil', amount: 0.25, unit: 'cup' },
      { name: 'balsamic vinegar', amount: 2, unit: 'tbsp' },
      { name: 'garlic cloves, minced', amount: 2, unit: '' },
      { name: 'dried thyme', amount: 1, unit: 'tsp' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' },
      { name: 'whole grain buns', amount: 4, unit: '' },
      { name: 'lettuce leaves', amount: 4, unit: '' },
      { name: 'tomato, sliced', amount: 1, unit: '' },
      { name: 'red onion, sliced', amount: 0.5, unit: '' }
    ],
    nutrition: {
      calories: 280,
      protein: 8,
      carbs: 36,
      fat: 12,
      vitamins: ['B2', 'B3', 'B5'],
      minerals: ['Potassium', 'Copper']
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
      'In a shallow dish, whisk together olive oil, balsamic vinegar, garlic, thyme, salt, and pepper.',
      'Place mushroom caps in the dish and brush the marinade over both sides. Let marinate for 10-15 minutes.',
      'Preheat grill to medium-high heat. Grill mushrooms for 4-5 minutes per side, basting with remaining marinade.',
      'Lightly toast the buns on the grill.',
      'Assemble burgers by placing a grilled mushroom on the bottom bun, topped with lettuce, tomato, and red onion. Add the top bun and serve immediately.'
    ]
  },;