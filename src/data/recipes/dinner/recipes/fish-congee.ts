import { Recipe } from '../../../../types/recipe';

export const fishcongee: Recipe = {
    name: 'Fish Congee',
    description: 'A comforting rice porridge with delicate white fish and ginger.',
    ingredients: [
      { name: 'white rice', amount: 1, unit: 'cup' },
      { name: 'water', amount: 8, unit: 'cups' },
      { name: 'white fish fillets', amount: 12, unit: 'oz' },
      { name: 'ginger', amount: 2, unit: 'inches', notes: 'julienned' },
      { name: 'green onions', amount: 4, unit: '', notes: 'sliced' },
      { name: 'tamari', amount: 2, unit: 'tbsp' },
      { name: 'sesame oil', amount: 1, unit: 'tbsp' }
    ],
    nutrition: {
      calories: 250,
      protein: 20,
      carbs: 35,
      fat: 4,
      vitamins: ['B12', 'D'],
      minerals: ['Selenium', 'Iron']
    },
    timeToMake: '1 hour',
    season: ['winter'],
    cuisine: 'HSCA',
    mealType: ['Dinner', 'Breakfast'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.3,
      Water: 0.5,
      Air: 0.1
    },
    instructions: [
      'Rinse rice until water runs clear.',
      'Combine rice and water in large pot. Bring to boil, then reduce to simmer.',
      'Cook for 45 minutes, stirring occasionally, until rice breaks down and becomes creamy.',
      'Add fish and ginger. Simmer for 5 minutes until fish is cooked.',
      'Season with tamari and sesame oil.',
      'Garnish with green onions before serving.'
    ]
  },;