import { Recipe } from '../../../../types/recipe';

export const caesarsaladwithshrimp: Recipe = {
    name: 'Caesar Salad with Shrimp',
    description: 'Classic Caesar salad topped with grilled shrimp.',
    ingredients: [
      { name: 'romaine lettuce', amount: 2, unit: 'heads', swaps: ['kale', 'spinach'] },
      { name: 'shrimp, peeled and deveined', amount: 1, unit: 'lb' },
      { name: 'olive oil', amount: 2, unit: 'tbsp' },
      { name: 'garlic cloves, minced', amount: 2, unit: '' },
      { name: 'lemon juice', amount: 2, unit: 'tbsp' },
      { name: 'Dijon mustard', amount: 1, unit: 'tsp' },
      { name: 'anchovy fillets, minced', amount: 4, unit: '', swaps: ['capers'] },
      { name: 'Parmesan cheese, grated', amount: 0.5, unit: 'cup' },
      { name: 'croutons', amount: 1, unit: 'cup', swaps: ['toasted nuts'] },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 380,
      protein: 36,
      carbs: 12,
      fat: 22,
      vitamins: ['A', 'C', 'B12'],
      minerals: ['Iron', 'Calcium']
    },
    timeToMake: '30 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Salad'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.3,
      Water: 0.4,
      Air: 0.1
    },
    instructions: [
      'In a large bowl, tear romaine lettuce into bite-size pieces.',
      'In a skillet, heat olive oil over medium-high heat. Add shrimp and cook until pink and opaque, about 3 minutes per side. Set aside to cool.',
      'In a small bowl, whisk together garlic, lemon juice, Dijon mustard, anchovies, Parmesan cheese, salt, and pepper to make the dressing.',
      'Add cooled shrimp to the bowl with the lettuce. Pour dressing over the salad and toss to coat.',
      'Top with croutons and additional Parmesan cheese, if desired. Serve immediately.'
    ]
  },;