import { Recipe } from '../../../../types/recipe';

export const blueberryalmondovernightoats: Recipe = {
    name: 'Blueberry Almond Overnight Oats',
    description: 'A delicious and healthy breakfast that you can prepare the night before.',
    ingredients: [
      { name: 'old-fashioned rolled oats', amount: 1, unit: 'cup' },
      { name: 'unsweetened almond milk', amount: 1, unit: 'cup', swaps: ['oat milk', 'soy milk'] },
      { name: 'Greek yogurt', amount: 0.5, unit: 'cup', swaps: ['coconut yogurt'] },
      { name: 'honey', amount: 2, unit: 'tbsp', swaps: ['maple syrup', 'agave nectar'] },
      { name: 'chia seeds', amount: 1, unit: 'tbsp' },
      { name: 'vanilla extract', amount: 0.5, unit: 'tsp' },
      { name: 'fresh blueberries', amount: 0.5, unit: 'cup' },
      { name: 'sliced almonds', amount: 0.25, unit: 'cup' }
    ],
    nutrition: {
      calories: 400,
      protein: 18,
      carbs: 60,
      fat: 12,
      vitamins: ['C', 'E'],
      minerals: ['Calcium', 'Iron']
    },
    timeToMake: '5 minutes (plus overnight refrigeration)',
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
      'In a large bowl or mason jar, combine rolled oats, almond milk, Greek yogurt, honey, chia seeds, and vanilla extract. Mix well.',
      'Fold in fresh blueberries and sliced almonds.',
      'Cover the bowl or seal the jar and refrigerate overnight, or for at least 6 hours.',
      'In the morning, give the oats a stir. If the mixture is too thick, add a splash of almond milk to achieve desired consistency.',
      'Top with additional fresh blueberries and sliced almonds before serving, if desired.',
      'Enjoy cold or warm in the microwave for 1-2 minutes.'
    ]
};