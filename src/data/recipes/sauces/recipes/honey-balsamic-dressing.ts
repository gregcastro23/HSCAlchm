import { Recipe } from '../../../../types/recipe';

export const honeybalsamicdressing: Recipe = {
    name: 'Honey-Balsamic Dressing',
    description: 'A sweet and tangy dressing perfect for summer salads and grilled fruits.',
    ingredients: [
      { name: 'honey', amount: 2, unit: 'tbsp' },
      { name: 'balsamic vinegar', amount: 2, unit: 'tbsp' },
      { name: 'extra virgin olive oil', amount: 3, unit: 'tbsp' },
      { name: 'sea salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 90,
      protein: 0,
      carbs: 12,
      fat: 7,
      vitamins: [],
      minerals: []
    },
    timeToMake: '5 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Sauce', 'Dressing'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.3,
      Water: 0.3,
      Air: 0.2
    },
    instructions: [
      'In a small bowl, whisk together honey and balsamic vinegar until well combined.',
      'Slowly drizzle in olive oil while whisking continuously to emulsify.',
      'Season with salt and pepper to taste.',
      'Use immediately or store in an airtight container in the refrigerator for up to 1 week.'
    ]
  };