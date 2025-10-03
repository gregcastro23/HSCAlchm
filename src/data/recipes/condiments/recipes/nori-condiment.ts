import { Recipe } from '../../../../types/recipe';

export const noricondiment: Recipe = {
    name: 'Nori Condiment',
    description: 'A flavorful seaweed condiment with a sweet and savory profile.',
    ingredients: [
      { name: 'toasted nori sheets', amount: 7, unit: 'sheets' },
      { name: 'water', amount: 1, unit: 'cup' },
      { name: 'shoyu', amount: 2, unit: 'tbsp' },
      { name: 'brown rice syrup', amount: 2, unit: 'tbsp' }
    ],
    nutrition: {
      calories: 45,
      protein: 2,
      carbs: 9,
      fat: 0,
      vitamins: ['B12', 'A'],
      minerals: ['Iodine', 'Iron']
    },
    timeToMake: '20 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Condiment'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.3,
      Water: 0.5,
      Air: 0.1
    },
    instructions: [
      'In 2-quart saucepan, add nori, water, shoyu, and rice syrup.',
      'Bring to boil, reduce to simmer, and stir often. Let simmer until all the liquid is absorbed.',
      'Serve as condiment on grains or beans.'
    ]
  },;