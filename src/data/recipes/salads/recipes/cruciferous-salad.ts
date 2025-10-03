import { Recipe } from '../../../../types/recipe';

export const cruciferoussalad: Recipe = {
    name: 'Cruciferous Salad',
    description: 'A hearty salad featuring various cruciferous vegetables with horseradish dressing.',
    ingredients: [
      { name: 'broccoli', amount: 2, unit: 'heads', notes: 'bite-size florets and stems' },
      { name: 'cauliflower', amount: 1, unit: 'head', notes: 'bite-size florets' },
      { name: 'Brussels sprouts', amount: 1, unit: 'pound', notes: 'finely shredded' },
      { name: 'horseradish', amount: 0.25, unit: 'cup', notes: 'peeled and roughly chopped' },
      { name: 'cashews', amount: 0.5, unit: 'cup', notes: 'soaked overnight and drained' },
      { name: 'extra virgin olive oil', amount: 0.25, unit: 'cup' },
      { name: 'white miso', amount: 0.25, unit: 'cup' },
      { name: 'water', amount: 0.75, unit: 'cup' },
      { name: 'garlic', amount: 2, unit: 'cloves' },
      { name: 'lemon juice', amount: 0.25, unit: 'cup' },
      { name: 'brown rice vinegar', amount: 1, unit: 'tbsp' },
      { name: 'umeboshi paste', amount: 1, unit: 'tbsp' },
      { name: 'Dijon mustard', amount: 1, unit: 'tsp' },
      { name: 'sesame seeds', amount: 0.25, unit: 'cup', notes: 'toasted, for garnish' }
    ],
    nutrition: {
      calories: 150,
      protein: 6,
      carbs: 15,
      fat: 9,
      vitamins: ['C', 'K', 'B6'],
      minerals: ['Folate', 'Potassium']
    },
    timeToMake: '45 minutes',
    season: ['fall', 'winter'],
    cuisine: 'HSCA',
    mealType: ['Salad'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.4,
      Water: 0.2,
      Air: 0.2
    },
    instructions: [
      'Bring 1-gallon water to boil with 1 tablespoon salt. Prepare an ice bath.',
      'Blanch broccoli, broccoli stems, and cauliflower separately – broccoli for 30 seconds, cauliflower for 1 minute. Shock blanched vegetables in ice water.',
      'Drain and transfer broccoli, broccoli stems, and cauliflower to bowl and add Brussels sprouts.',
      'In Vitamix, combine dressing ingredients. Process until creamy and smooth, and more water if needed.',
      'Toss vegetables in dressing and serve garnished with sesame seeds.'
    ]
  },;