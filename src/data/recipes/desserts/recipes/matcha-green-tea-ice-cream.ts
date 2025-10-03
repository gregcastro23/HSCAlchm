import { Recipe } from '../../../../types/recipe';

export const matchagreenteaicecream: Recipe = {
    name: 'Matcha Green Tea Ice Cream',
    description: 'A dairy-free ice cream with the distinct flavor of matcha green tea.',
    ingredients: [
      { name: 'coconut milk, full fat', amount: 2, unit: 'cans' },
      { name: 'matcha powder', amount: 2, unit: 'tbsp' },
      { name: 'maple syrup', amount: 0.5, unit: 'cup' },
      { name: 'vanilla extract', amount: 1, unit: 'tsp' },
      { name: 'salt', amount: 0.125, unit: 'tsp' }
    ],
    nutrition: {
      calories: 220,
      protein: 2,
      carbs: 18,
      fat: 16,
      vitamins: ['E'],
      minerals: ['Iron', 'Magnesium']
    },
    timeToMake: '30 minutes (plus 4 hours freezing)',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Dessert'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.3,
      Water: 0.4,
      Air: 0.2
    },
    instructions: [
      'In a blender, combine all ingredients until smooth.',
      'Pour mixture into an ice cream maker and churn according to manufacturer\'s instructions.',
      'Transfer to a freezer-safe container.',
      'Freeze for at least 4 hours before serving.',
      'Let sit at room temperature for 5 minutes before scooping.'
    ]
  },;