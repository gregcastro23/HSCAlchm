import { Recipe } from '../../../../types/recipe';

export const seafoodsausage: Recipe = {
    name: 'Seafood Sausage',
    description: 'A delicate seafood sausage made with fresh fish and shellfish.',
    ingredients: [
      { name: 'white fish fillet', amount: 0.5, unit: 'lb', notes: 'such as cod or halibut' },
      { name: 'scallops', amount: 0.5, unit: 'lb' },
      { name: 'shrimp, peeled', amount: 0.5, unit: 'lb' },
      { name: 'egg whites', amount: 2, unit: '' },
      { name: 'heavy cream', amount: 0.5, unit: 'cup' },
      { name: 'chives, minced', amount: 0.25, unit: 'cup' },
      { name: 'tarragon, chopped', amount: 2, unit: 'tbsp' },
      { name: 'salt', amount: 1, unit: 'tsp' },
      { name: 'white pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 180,
      protein: 28,
      carbs: 2,
      fat: 8,
      vitamins: ['B12', 'D'],
      minerals: ['Selenium', 'Iodine']
    },
    timeToMake: '1 hour',
    season: ['spring', 'summer'],
    cuisine: 'HSCA',
    mealType: ['Entree'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.1,
      Water: 0.6,
      Air: 0.1
    },
    instructions: [
      'Chill all seafood thoroughly. Cut into small pieces.',
      'In a food processor, blend seafood until smooth.',
      'Add egg whites, cream, herbs, salt, and pepper. Process until well combined.',
      'Form mixture into sausage shapes using plastic wrap.',
      'Poach in simmering water until firm, about 10-12 minutes.',
      'Let cool slightly before serving.'
    ]
  },;