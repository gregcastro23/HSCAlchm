import { Recipe } from '../../../../types/recipe';

export const mediterraneanblackcod: Recipe = {
    name: 'Mediterranean Black Cod',
    description: 'A delicate fish dish with Mediterranean flavors and muhammara sauce.',
    ingredients: [
      { name: 'black cod fillets', amount: 24, unit: 'oz', notes: '6 oz portions' },
      { name: 'olive oil', amount: 2, unit: 'tbsp' },
      { name: 'lemon juice', amount: 2, unit: 'tbsp' },
      { name: 'garlic', amount: 2, unit: 'cloves', notes: 'minced' },
      { name: 'fresh oregano', amount: 1, unit: 'tbsp', notes: 'chopped' },
      { name: 'salt', amount: 1, unit: 'tsp' },
      { name: 'black pepper', amount: 0.5, unit: 'tsp' },
      // Muhammara sauce ingredients
      { name: 'red peppers', amount: 2, unit: 'large', notes: 'roasted, peeled, seeded' },
      { name: 'walnuts', amount: 1, unit: 'cup', notes: 'toasted' },
      { name: 'pomegranate molasses', amount: 2, unit: 'tbsp' },
      { name: 'breadcrumbs', amount: 0.5, unit: 'cup' },
      { name: 'cumin', amount: 1, unit: 'tsp', notes: 'ground' },
      { name: 'Aleppo pepper', amount: 1, unit: 'tsp' }
    ],
    nutrition: {
      calories: 380,
      protein: 34,
      carbs: 12,
      fat: 22,
      vitamins: ['B12', 'D'],
      minerals: ['Selenium', 'Omega-3']
    },
    timeToMake: '45 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Dinner'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.2,
      Water: 0.3,
      Air: 0.2
    },
    instructions: [
      'Marinate cod in olive oil, lemon juice, garlic, oregano, salt, and pepper for 30 minutes.',
      'For muhammara: Blend roasted peppers, walnuts, pomegranate molasses, breadcrumbs, cumin, and Aleppo pepper until smooth.',
      'Preheat oven to 400°F.',
      'Place cod on parchment-lined baking sheet and roast for 12-15 minutes until just cooked through.',
      'Serve cod with muhammara sauce.'
    ]
  },;