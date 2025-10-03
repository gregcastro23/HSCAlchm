import { Recipe } from '../../../../types/recipe';

export const hizikiwithcarrotsandagtofu: Recipe = {
    name: 'Hiziki with Carrots and Agé Tofu',
    description: 'A traditional Japanese side dish combining sea vegetables with fried tofu.',
    ingredients: [
      { name: 'canola oil', amount: 2, unit: 'cups' },
      { name: 'firm tofu', amount: 7, unit: 'oz' },
      { name: 'hiziki', amount: 0.5, unit: 'cup' },
      { name: 'apple juice', amount: 1, unit: 'cup' },
      { name: 'water', amount: 0.75, unit: 'cup' },
      { name: 'carrot', amount: 6, unit: 'oz' },
      { name: 'onion', amount: 10, unit: 'oz' },
      { name: 'toasted sesame oil', amount: 1, unit: 'tbsp' },
      { name: 'shoyu', amount: 2, unit: 'tbsp' },
      { name: 'white sesame seeds', amount: 1, unit: 'tbsp' }
    ],
    nutrition: {
      calories: 180,
      protein: 8,
      carbs: 16,
      fat: 11,
      vitamins: ['A', 'K'],
      minerals: ['Calcium', 'Iron', 'Iodine']
    },
    timeToMake: '50 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Side'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.4,
      Water: 0.3,
      Air: 0.1
    },
    instructions: [
      'Heat oil to 375° F in 2 ½ quart pot. Line plate with paper towel.',
      'Fry tofu in batches until golden. Drain on paper towel.',
      'Combine hiziki in separate 2 ½ quart pot with apple juice and water. Bring to boil.',
      'Add carrots, onion, fried tofu, toasted sesame oil, and shoyu.',
      'Simmer 30 minutes or until all liquid is absorbed.',
      'Garnish with sesame seeds before serving.'
    ]
  },;