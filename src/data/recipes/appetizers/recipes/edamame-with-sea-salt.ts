import { Recipe } from '../../../../types/recipe';

export const edamamewithseasalt: Recipe = {
    name: 'Edamame with Sea Salt',
    description: 'Simple and nutritious steamed edamame pods with sea salt.',
    ingredients: [
      { name: 'frozen edamame pods', amount: 1, unit: 'lb' },
      { name: 'sea salt', amount: 1, unit: 'tsp' },
      { name: 'water', amount: 4, unit: 'cups' }
    ],
    nutrition: {
      calories: 120,
      protein: 11,
      carbs: 10,
      fat: 5,
      vitamins: ['K', 'C', 'B6'],
      minerals: ['Iron', 'Magnesium']
    },
    timeToMake: '10 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Appetizer', 'Snack'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.4,
      Water: 0.4,
      Air: 0.1
    },
    instructions: [
      'Bring water to a boil in a medium saucepan.',
      'Add frozen edamame pods and cook for 5 minutes.',
      'Drain well and transfer to a serving bowl.',
      'Sprinkle with sea salt while still hot.',
      'Serve warm or at room temperature.'
    ]
  };