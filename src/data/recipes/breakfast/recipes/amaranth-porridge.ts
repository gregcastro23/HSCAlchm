import { Recipe } from '../../../../types/recipe';

export const amaranthporridge: Recipe = {
    name: 'Amaranth Porridge',
    description: 'A nutrient-rich, creamy breakfast porridge made with ancient grain amaranth.',
    ingredients: [
      { name: 'amaranth', amount: 1, unit: 'cup' },
      { name: 'water', amount: 3, unit: 'cups' },
      { name: 'almond milk', amount: 1, unit: 'cup', notes: 'plus more for serving' },
      { name: 'cinnamon stick', amount: 1, unit: '' },
      { name: 'vanilla extract', amount: 1, unit: 'tsp' },
      { name: 'maple syrup', amount: 2, unit: 'tbsp' },
      { name: 'sea salt', amount: 0.25, unit: 'tsp' },
      { name: 'fresh berries', amount: 1, unit: 'cup', notes: 'for serving' },
      { name: 'toasted almonds', amount: 0.25, unit: 'cup', notes: 'sliced, for serving' }
    ],
    nutrition: {
      calories: 280,
      protein: 9,
      carbs: 48,
      fat: 6,
      vitamins: ['B6', 'E'],
      minerals: ['Iron', 'Magnesium', 'Phosphorus']
    },
    timeToMake: '30 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Breakfast'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.4,
      Water: 0.4,
      Air: 0.1
    },
    instructions: [
      'Rinse amaranth thoroughly in a fine-mesh strainer.',
      'In a medium saucepan, combine amaranth, water, and cinnamon stick.',
      'Bring to a boil, then reduce heat to low.',
      'Simmer covered for 20-25 minutes, stirring occasionally, until water is absorbed.',
      'Remove cinnamon stick and stir in almond milk, vanilla, maple syrup, and salt.',
      'Cook for an additional 5 minutes until creamy.',
      'Serve hot, topped with additional almond milk, fresh berries, and toasted almonds.'
    ]
  };