import { Recipe } from '../../../../types/recipe';

export const misoglazedsalmon: Recipe = {
    name: 'Miso Glazed Salmon',
    description: 'Wild-caught salmon with a sweet and savory miso glaze.',
    ingredients: [
      { name: 'salmon fillets', amount: 4, unit: '6 oz portions' },
      { name: 'white miso paste', amount: 0.25, unit: 'cup' },
      { name: 'mirin', amount: 2, unit: 'tbsp' },
      { name: 'sake', amount: 2, unit: 'tbsp' },
      { name: 'maple syrup', amount: 1, unit: 'tbsp' },
      { name: 'ginger, grated', amount: 1, unit: 'tbsp' },
      { name: 'sesame oil', amount: 1, unit: 'tsp' },
      { name: 'green onions, sliced', amount: 2, unit: '' }
    ],
    nutrition: {
      calories: 380,
      protein: 34,
      carbs: 8,
      fat: 24,
      vitamins: ['D', 'B12'],
      minerals: ['Omega-3', 'Selenium']
    },
    timeToMake: '30 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Dinner'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.2,
      Water: 0.4,
      Air: 0.1
    },
    instructions: [
      'In a bowl, whisk together miso, mirin, sake, maple syrup, ginger, and sesame oil.',
      'Place salmon in a dish and coat with miso mixture. Marinate for 15-30 minutes.',
      'Preheat broiler. Line a baking sheet with foil.',
      'Place salmon on prepared sheet and broil 6-8 minutes until caramelized and cooked through.',
      'Garnish with sliced green onions and serve.'
    ]
  },;