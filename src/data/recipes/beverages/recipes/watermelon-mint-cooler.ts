import { Recipe } from '../../../../types/recipe';

export const watermelonmintcooler: Recipe = {
    name: 'Watermelon Mint Cooler',
    description: 'A refreshing and hydrating drink made with juicy watermelon and fresh mint.',
    ingredients: [
      { name: 'watermelon, cubed', amount: 4, unit: 'cups' },
      { name: 'fresh mint leaves', amount: 0.5, unit: 'cup' },
      { name: 'lime, juiced', amount: 1, unit: '' },
      { name: 'honey', amount: 2, unit: 'tbsp', swaps: ['agave nectar'] },
      { name: 'water', amount: 1, unit: 'cup' },
      { name: 'ice cubes', amount: 2, unit: 'cups' }
    ],
    nutrition: {
      calories: 120,
      protein: 2,
      carbs: 32,
      fat: 0,
      vitamins: ['A', 'C'],
      minerals: ['Potassium', 'Magnesium']
    },
    timeToMake: '10 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Beverage'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.2,
      Water: 0.6,
      Air: 0.1
    },
    instructions: [
      'In a blender, combine watermelon, mint leaves, lime juice, honey, and water.',
      'Blend until smooth.',
      'Pour the mixture over ice cubes in serving glasses.',
      'Garnish with additional mint leaves, if desired.',
      'Serve chilled and enjoy!'
    ]
  },;