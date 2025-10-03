import { Recipe } from '../../../../types/recipe';

export const mangoavocadosalsa: Recipe = {
    name: 'Mango Avocado Salsa',
    description: 'A fresh and zesty salsa perfect for topping grilled fish, chicken, or enjoying with chips.',
    ingredients: [
      { name: 'ripe mango, diced', amount: 2, unit: '' },
      { name: 'avocado, diced', amount: 1, unit: '' },
      { name: 'red onion, finely chopped', amount: 0.5, unit: '' },
      { name: 'jalapeño pepper, seeded and minced', amount: 1, unit: '' },
      { name: 'fresh cilantro, chopped', amount: 0.25, unit: 'cup' },
      { name: 'lime juice', amount: 2, unit: 'tbsp' },
      { name: 'salt', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 160,
      protein: 2,
      carbs: 20,
      fat: 10,
      vitamins: ['A', 'C', 'E'],
      minerals: ['Potassium', 'Magnesium']
    },
    timeToMake: '15 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Appetizer', 'Snack'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.3,
      Water: 0.4,
      Air: 0.1
    },
    instructions: [
      'In a medium bowl, combine diced mango, avocado, red onion, jalapeño pepper, and cilantro.',
      'Add lime juice and salt, and gently toss to combine.',
      'Taste and adjust seasoning if needed.',
      'Serve immediately with grilled meats, fish, or tortilla chips.'
    ]
  },;