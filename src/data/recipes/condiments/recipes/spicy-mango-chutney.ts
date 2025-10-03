import { Recipe } from '../../../../types/recipe';

export const spicymangochutney: Recipe = {
    name: 'Spicy Mango Chutney',
    description: 'A sweet and spicy condiment perfect for curries, sandwiches, or as a dipping sauce.',
    ingredients: [
      { name: 'ripe mangoes, diced', amount: 4, unit: 'cups' },
      { name: 'red onion, finely chopped', amount: 1, unit: '' },
      { name: 'ginger, minced', amount: 2, unit: 'tbsp' },
      { name: 'garlic cloves, minced', amount: 3, unit: '' },
      { name: 'red chili peppers, seeded and minced', amount: 2, unit: '' },
      { name: 'apple cider vinegar', amount: 0.5, unit: 'cup' },
      { name: 'brown sugar', amount: 0.5, unit: 'cup' },
      { name: 'mustard seeds', amount: 1, unit: 'tsp' },
      { name: 'ground cumin', amount: 1, unit: 'tsp' },
      { name: 'salt', amount: 1, unit: 'tsp' }
    ],
    nutrition: {
      calories: 80,
      protein: 1,
      carbs: 20,
      fat: 0,
      vitamins: ['A', 'C'],
      minerals: ['Potassium']
    },
    timeToMake: '45 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Condiment'],
    elementalBalance: {
      Fire: 0.4,
      Earth: 0.2,
      Water: 0.3,
      Air: 0.1
    },
    instructions: [
      'In a large saucepan, combine all ingredients.',
      'Bring to a boil over medium-high heat, stirring occasionally.',
      'Reduce heat and simmer for 30-35 minutes, until mangoes are soft and mixture has thickened.',
      'Let cool completely.',
      'Store in airtight containers in the refrigerator for up to 2 weeks.'
    ]
  },;