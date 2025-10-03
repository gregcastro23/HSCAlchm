import { Recipe } from '../../../../types/recipe';

export const wakamecucumbersaladwithorange: Recipe = {
    name: 'Wakame Cucumber Salad with Orange',
    description: 'A refreshing Japanese-inspired salad combining sea vegetables with citrus.',
    ingredients: [
      { name: 'wakame', amount: 0.25, unit: 'cup' },
      { name: 'cucumbers', amount: 2, unit: '' },
      { name: 'sea salt', amount: 0.25, unit: 'tsp' },
      { name: 'juice oranges', amount: 2, unit: '' },
      { name: 'cilantro', amount: 0.25, unit: 'bunch' },
      { name: 'rice vinegar', amount: 2, unit: 'tbsp' },
      { name: 'mirin', amount: 2, unit: 'tbsp' },
      { name: 'shoyu', amount: 1, unit: 'tbsp' },
      { name: 'maple syrup', amount: 1.5, unit: 'tbsp' }
    ],
    nutrition: {
      calories: 85,
      protein: 2,
      carbs: 18,
      fat: 0,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Iodine', 'Potassium']
    },
    timeToMake: '35 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Salad'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.2,
      Water: 0.5,
      Air: 0.2
    },
    instructions: [
      'Soak wakame in cold water for 5 minutes until reconstituted. Drain and chop into bite-size pieces.',
      'Cut cucumbers in half lengthwise, scoop out seeds, and slice thinly.',
      'Toss cucumbers with salt and let drain in colander for 20 minutes.',
      'Supreme oranges (cut segments from membrane) and reserve juice.',
      'Chop cilantro leaves.',
      'Combine rice vinegar, mirin, shoyu, and maple syrup with reserved orange juice.',
      'Toss wakame and cucumbers with dressing.',
      'Garnish with orange segments and cilantro before serving.'
    ]
  },;