import { Recipe } from '../../../../types/recipe';

export const aramewithvegetables: Recipe = {
    name: 'Arame with Vegetables',
    description: 'A nourishing side dish combining sea vegetables with land vegetables.',
    ingredients: [
      { name: 'sesame oil', amount: 1, unit: 'tbsp' },
      { name: 'onion', amount: 10, unit: 'oz' },
      { name: 'carrot', amount: 6, unit: 'oz' },
      { name: 'arame', amount: 1.5, unit: 'cups' },
      { name: 'shoyu', amount: 2, unit: 'tbsp' },
      { name: 'brown rice syrup', amount: 2, unit: 'tbsp' },
      { name: 'mirin', amount: 2, unit: 'tbsp' },
      { name: 'bok choy', amount: 8, unit: 'oz' }
    ],
    nutrition: {
      calories: 140,
      protein: 4,
      carbs: 24,
      fat: 5,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Iodine', 'Iron', 'Calcium']
    },
    timeToMake: '45 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Side'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.3,
      Water: 0.4,
      Air: 0.1
    },
    instructions: [
      'In 10-inch sauté pan, heat oil over medium flame. Sweat onion for 5 minutes or until translucent.',
      'Add carrot and sweat another 5 minutes.',
      'Add arame to onions and carrots. Stir well. Sweat for another minute until arame is heated through.',
      'Add water to cover arame halfway. Bring water to boil. Add shoyu, brown rice syrup, and mirin.',
      'Simmer for 20-30 minutes or until all liquid has evaporated.',
      'Add bok choy stems and sweat until stems just become tender. Add leaves and sweat until leaves wilt.'
    ]
  },;