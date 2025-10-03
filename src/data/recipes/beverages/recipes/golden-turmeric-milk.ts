import { Recipe } from '../../../../types/recipe';

export const goldenturmericmilk: Recipe = {
    name: 'Golden Turmeric Milk',
    description: 'An anti-inflammatory almond milk infused with fresh turmeric and warming spices.',
    ingredients: [
      { name: 'blanched almonds', amount: 4, unit: 'cups' },
      { name: 'fresh turmeric', amount: 4, unit: 'oz' },
      { name: 'fresh ginger', amount: 2, unit: 'oz' },
      { name: 'water', amount: 10, unit: 'cups' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp', notes: 'ground' },
      { name: 'cinnamon', amount: 0.25, unit: 'tsp' },
      { name: 'maple syrup', amount: 1.5, unit: 'tbsp', notes: 'or to taste' }
    ],
    nutrition: {
      calories: 120,
      protein: 4,
      carbs: 7,
      fat: 9,
      vitamins: ['E', 'B2'],
      minerals: ['Calcium', 'Iron', 'Magnesium']
    },
    timeToMake: '30 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Beverage'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.3,
      Water: 0.2,
      Air: 0.2
    },
    instructions: [
      'In 2 batches, puree almonds, turmeric, and ginger with water in Vitamix until smooth. Strain milk through chinois.',
      'Transfer milk to 1-gallon pot. Bring milk mixture to simmer over medium flame (to infuse flavors). Turn off heat and add pepper, cinnamon, and maple syrup to taste.'
    ]
  },;