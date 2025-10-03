import { Recipe } from '../../../../types/recipe';

export const horseradishandlemoncondiment: Recipe = {
    name: 'Horseradish and Lemon Condiment',
    description: 'A zesty, bright condiment that combines the heat of fresh horseradish with citrus notes.',
    ingredients: [
      { name: 'fresh horseradish root', amount: 8, unit: 'oz', notes: 'peeled and finely grated' },
      { name: 'lemons', amount: 2, unit: '', notes: 'juice and zest' },
      { name: 'apple cider vinegar', amount: 2, unit: 'tbsp' },
      { name: 'olive oil', amount: 1, unit: 'tbsp' },
      { name: 'sea salt', amount: 0.5, unit: 'tsp' },
      { name: 'honey', amount: 1, unit: 'tsp', notes: 'optional' }
    ],
    nutrition: {
      calories: 25,
      protein: 1,
      carbs: 5,
      fat: 1,
      vitamins: ['C'],
      minerals: ['Potassium', 'Calcium']
    },
    timeToMake: '15 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Condiment'],
    elementalBalance: {
      Fire: 0.6,
      Earth: 0.1,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'Peel and finely grate the fresh horseradish root.',
      'Zest the lemons, then juice them.',
      'In a bowl, combine grated horseradish, lemon zest, and lemon juice.',
      'Add apple cider vinegar and olive oil.',
      'Season with sea salt.',
      'If desired, add honey to balance the heat.',
      'Mix well and let stand for 10 minutes to allow flavors to meld.',
      'Store in an airtight container in the refrigerator for up to 2 weeks.'
    ]
  };