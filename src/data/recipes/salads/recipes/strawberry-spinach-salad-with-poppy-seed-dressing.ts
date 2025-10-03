import { Recipe } from '../../../../types/recipe';

export const strawberryspinachsaladwithpoppyseeddressing: Recipe = {
    name: 'Strawberry Spinach Salad with Poppy Seed Dressing',
    description: 'A delightful and refreshing salad featuring sweet strawberries, tender spinach, and a creamy poppy seed dressing.',
    ingredients: [
      { name: 'baby spinach', amount: 6, unit: 'cups' },
      { name: 'strawberries, sliced', amount: 2, unit: 'cups' },
      { name: 'red onion, thinly sliced', amount: 0.5, unit: '' },
      { name: 'feta cheese, crumbled', amount: 0.5, unit: 'cup', swaps: ['goat cheese'] },
      { name: 'almonds, sliced', amount: 0.33, unit: 'cup', swaps: ['pecans', 'walnuts'] },
      { name: 'Greek yogurt', amount: 0.5, unit: 'cup' },
      { name: 'honey', amount: 2, unit: 'tbsp' },
      { name: 'apple cider vinegar', amount: 1, unit: 'tbsp' },
      { name: 'poppy seeds', amount: 1, unit: 'tsp' },
      { name: 'salt', amount: 0.25, unit: 'tsp' },
      { name: 'black pepper', amount: 0.125, unit: 'tsp' }
    ],
    nutrition: {
      calories: 280,
      protein: 10,
      carbs: 24,
      fat: 18,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Calcium', 'Iron']
    },
    timeToMake: '20 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Salad'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.4,
      Water: 0.4,
      Air: 0.1
    },
    instructions: [
      'In a large bowl, combine baby spinach, sliced strawberries, and thinly sliced red onion.',
      'In a small bowl, whisk together Greek yogurt, honey, apple cider vinegar, poppy seeds, salt, and black pepper to make the dressing.',
      'Drizzle the dressing over the salad and toss gently to coat evenly.',
      'Sprinkle crumbled feta cheese and sliced almonds over the salad.',
      'Serve immediately and enjoy the perfect balance of sweet and savory flavors!'
    ]
  },;