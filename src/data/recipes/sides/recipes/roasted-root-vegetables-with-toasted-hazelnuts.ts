import { Recipe } from '../../../../types/recipe';

export const roastedrootvegetableswithtoastedhazelnuts: Recipe = {
    name: 'Roasted Root Vegetables with Toasted Hazelnuts',
    description: 'A medley of seasonal root vegetables roasted until caramelized, topped with toasted hazelnuts and fresh herbs.',
    ingredients: [
      { name: 'carrots', amount: 3, unit: 'medium', notes: 'cut into 2-inch pieces' },
      { name: 'parsnips', amount: 3, unit: 'medium', notes: 'cut into 2-inch pieces' },
      { name: 'sweet potatoes', amount: 2, unit: 'medium', notes: 'cut into 2-inch pieces' },
      { name: 'beets', amount: 2, unit: 'medium', notes: 'cut into 2-inch pieces' },
      { name: 'olive oil', amount: 3, unit: 'tbsp' },
      { name: 'garlic cloves', amount: 6, unit: '', notes: 'whole, peeled' },
      { name: 'hazelnuts', amount: 0.5, unit: 'cup', notes: 'toasted and roughly chopped' },
      { name: 'fresh cilantro', amount: 0.5, unit: 'cup', notes: 'chopped' },
      { name: 'sea salt', amount: 1, unit: 'tsp' },
      { name: 'black pepper', amount: 0.5, unit: 'tsp' },
      { name: 'fresh thyme', amount: 2, unit: 'tbsp', notes: 'leaves only' }
    ],
    nutrition: {
      calories: 220,
      protein: 5,
      carbs: 28,
      fat: 12,
      vitamins: ['A', 'C', 'B6'],
      minerals: ['Potassium', 'Magnesium', 'Iron']
    },
    timeToMake: '45 minutes',
    season: ['fall', 'winter'],
    cuisine: 'HSCA',
    mealType: ['Side'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.5,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'Preheat oven to 425°F.',
      'Toss all cut vegetables and whole garlic cloves with olive oil, salt, and pepper.',
      'Spread vegetables in a single layer on a large baking sheet.',
      'Roast for 35-40 minutes, stirring halfway through, until vegetables are tender and caramelized.',
      'While vegetables roast, toast hazelnuts in a dry skillet until fragrant and skins begin to peel.',
      'Rub hazelnuts in a clean kitchen towel to remove skins, then roughly chop.',
      'When vegetables are done, transfer to a serving dish.',
      'Top with toasted hazelnuts, fresh cilantro, and thyme leaves.',
      'Adjust seasoning to taste and serve hot.'
    ]
  };