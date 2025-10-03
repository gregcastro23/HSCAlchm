import { Recipe } from '../../../../types/recipe';

export const grilledportobellomushroomsteaks: Recipe = {
    name: 'Grilled Portobello Mushroom Steaks',
    description: 'Juicy and savory grilled portobello mushrooms, perfect for a vegetarian entree.',
    ingredients: [
      { name: 'portobello mushrooms', amount: 4, unit: 'large' },
      { name: 'balsamic vinegar', amount: 0.25, unit: 'cup' },
      { name: 'soy sauce', amount: 2, unit: 'tbsp', swaps: ['tamari'] },
      { name: 'olive oil', amount: 2, unit: 'tbsp' },
      { name: 'garlic cloves, minced', amount: 3, unit: '' },
      { name: 'thyme leaves', amount: 1, unit: 'tbsp' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 120,
      protein: 4,
      carbs: 12,
      fat: 8,
      vitamins: ['D', 'B12'],
      minerals: ['Selenium', 'Copper']
    },
    timeToMake: '25 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Side', 'Entree'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.4,
      Water: 0.3,
      Air: 0.1
    },
    instructions: [
      'Clean mushrooms and remove stems. Place in a shallow dish.',
      'In a small bowl, whisk together balsamic vinegar, soy sauce, olive oil, garlic, thyme, salt, and pepper.',
      'Pour marinade over mushrooms and let marinate for 15 minutes, turning once.',
      'Preheat grill or grill pan to medium-high heat.',
      'Grill mushrooms for 4-5 minutes per side, basting with remaining marinade.',
      'Serve hot, sliced if desired.'
    ]
  },;