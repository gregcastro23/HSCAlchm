import { Recipe } from '../../../../types/recipe';

export const pineappleturmericsmoothie: Recipe = {
    name: 'Pineapple Turmeric Smoothie',
    description: 'A tropical and anti-inflammatory smoothie featuring pineapple, banana, and turmeric.',
    ingredients: [
      { name: 'frozen pineapple chunks', amount: 2, unit: 'cups' },
      { name: 'ripe banana', amount: 1, unit: '' },
      { name: 'almond milk', amount: 1, unit: 'cup', swaps: ['coconut milk', 'oat milk'] },
      { name: 'fresh turmeric, grated', amount: 1, unit: 'tsp', swaps: ['ground turmeric'] },
      { name: 'honey', amount: 1, unit: 'tbsp', swaps: ['maple syrup', 'agave nectar'] },
      { name: 'vanilla extract', amount: 0.5, unit: 'tsp' },
      { name: 'ice cubes', amount: 1, unit: 'cup' }
    ],
    nutrition: {
      calories: 240,
      protein: 4,
      carbs: 56,
      fat: 2,
      vitamins: ['C', 'B6', 'E'],
      minerals: ['Potassium', 'Manganese']
    },
    timeToMake: '5 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Breakfast', 'Snack'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.3,
      Water: 0.4,
      Air: 0.1
    },
    instructions: [
      'In a blender, combine frozen pineapple chunks, ripe banana, almond milk, grated turmeric, honey, and vanilla extract.',
      'Add ice cubes and blend until smooth and creamy.',
      'Pour into glasses and serve immediately, garnished with a sprinkle of ground turmeric if desired.'
    ]
  },;