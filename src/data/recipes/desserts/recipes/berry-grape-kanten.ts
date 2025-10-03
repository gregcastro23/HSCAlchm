import { Recipe } from '../../../../types/recipe';

export const berrygrapekanten: Recipe = {
    name: 'Berry-Grape Kanten',
    description: 'A refreshing Japanese-inspired dessert made with agar and fresh fruits.',
    ingredients: [
      { name: 'white grape juice', amount: 2, unit: 'cups' },
      { name: 'agar flakes', amount: 2.5, unit: 'tbsp' },
      { name: 'ginger juice', amount: 1.5, unit: 'tsp' },
      { name: 'lemon zest', amount: 1.5, unit: 'tsp' },
      { name: 'agave syrup', amount: 0.25, unit: 'cup' },
      { name: 'green grapes', amount: 9, unit: 'oz' },
      { name: 'strawberries', amount: 4, unit: 'oz' }
    ],
    nutrition: {
      calories: 120,
      protein: 1,
      carbs: 28,
      fat: 0,
      vitamins: ['C', 'K'],
      minerals: ['Manganese', 'Potassium']
    },
    timeToMake: '45 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Dessert'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.2,
      Water: 0.6,
      Air: 0.1
    },
    instructions: [
      'In 2 ½ quart pot, combine grape juice and agar flakes. Soak agar for 5 minutes.',
      'Bring agar-juice mixture to boil over medium heat, whisking frequently. Lower flame and simmer 5 minutes or until agar is completely dissolved.',
      'Add ginger juice, lemon zest, and agave syrup to juice mixture. Simmer 2 minutes more.',
      'Divide and arrange grapes and strawberries equally among individual ramekins.',
      'Slowly pour juice mixture over grapes and strawberries in ramekins. Let mixture stand until no more steam rises.',
      'Transfer kanten to refrigerator until firmed up, about 30 minutes.',
      'Serve kanten as is from ramekins.'
    ]
  },;