import { Recipe } from '../../../../types/recipe';

export const mangochiapudding: Recipe = {
    name: 'Mango Chia Pudding',
    description: 'A creamy and refreshing pudding made with chia seeds and sweet mango.',
    ingredients: [
      { name: 'chia seeds', amount: 0.5, unit: 'cup' },
      { name: 'almond milk', amount: 2, unit: 'cups', swaps: ['coconut milk', 'oat milk'] },
      { name: 'honey', amount: 2, unit: 'tbsp', swaps: ['maple syrup', 'agave nectar'] },
      { name: 'vanilla extract', amount: 1, unit: 'tsp' },
      { name: 'ripe mango, diced', amount: 1, unit: '' },
      { name: 'coconut flakes', amount: 0.25, unit: 'cup' }
    ],
    nutrition: {
      calories: 280,
      protein: 8,
      carbs: 40,
      fat: 12,
      vitamins: ['C', 'E'],
      minerals: ['Calcium', 'Magnesium']
    },
    timeToMake: '4 hours',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Breakfast', 'Dessert'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.3,
      Water: 0.5,
      Air: 0.1
    },
    instructions: [
      'In a large bowl, whisk together chia seeds, almond milk, honey, and vanilla extract.',
      'Cover and refrigerate for at least 4 hours, or overnight, until the mixture thickens and the chia seeds have absorbed the liquid.',
      'Layer the chia pudding and diced mango in glasses or bowls.',
      'Top with coconut flakes and additional diced mango, if desired.',
      'Serve chilled and enjoy!'
    ]
  },;