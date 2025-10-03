import { Recipe } from '../../../../types/recipe';

export const berrysorbet: Recipe = {
    name: 'Berry Sorbet',
    description: 'A refreshing dairy-free sorbet made with mixed berries and natural sweeteners.',
    ingredients: [
      { name: 'mixed berries', amount: 4, unit: 'cups', notes: 'fresh or frozen' },
      { name: 'maple syrup', amount: 0.333, unit: 'cup' },
      { name: 'lemon juice', amount: 2, unit: 'tbsp' },
      { name: 'water', amount: 0.5, unit: 'cup' },
      { name: 'mint leaves', amount: 0.25, unit: 'cup', notes: 'for garnish' }
    ],
    nutrition: {
      calories: 120,
      protein: 1,
      carbs: 30,
      fat: 0,
      vitamins: ['C', 'K'],
      minerals: ['Manganese', 'Potassium']
    },
    timeToMake: '20 minutes (plus 4 hours freezing)',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Dessert'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.1,
      Water: 0.6,
      Air: 0.2
    },
    instructions: [
      'Combine berries, maple syrup, lemon juice, and water in a blender.',
      'Blend until completely smooth.',
      'Strain mixture through a fine-mesh sieve to remove seeds.',
      'Pour into ice cream maker and churn according to manufacturer\'s instructions.',
      'Transfer to a freezer-safe container.',
      'Freeze for at least 4 hours until firm.',
      'Let sit at room temperature for 5 minutes before scooping.',
      'Garnish with fresh mint leaves before serving.'
    ]
  },;