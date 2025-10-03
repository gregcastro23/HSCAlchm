import { Recipe } from '../../../../types/recipe';

export const quinoaandblackbeansalad: Recipe = {
    name: 'Quinoa and Black Bean Salad',
    description: 'A protein-packed salad with fluffy quinoa, black beans, and fresh vegetables.',
    ingredients: [
      { name: 'quinoa, rinsed', amount: 1, unit: 'cup' },
      { name: 'water', amount: 2, unit: 'cups' },
      { name: 'black beans, drained and rinsed', amount: 1, unit: 'can' },
      { name: 'cherry tomatoes, halved', amount: 1, unit: 'cup' },
      { name: 'cucumber, diced', amount: 1, unit: '' },
      { name: 'red bell pepper, diced', amount: 1, unit: '' },
      { name: 'red onion, diced', amount: 0.5, unit: '' },
      { name: 'cilantro, chopped', amount: 0.5, unit: 'cup' },
      { name: 'lime juice', amount: 2, unit: 'tbsp' },
      { name: 'olive oil', amount: 2, unit: 'tbsp' },
      { name: 'ground cumin', amount: 1, unit: 'tsp' },
      { name: 'salt', amount: 0.5, unit: 'tsp' }
    ],
    nutrition: {
      calories: 280,
      protein: 12,
      carbs: 48,
      fat: 8,
      vitamins: ['A', 'C', 'E'],
      minerals: ['Iron', 'Magnesium']
    },
    timeToMake: '30 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Salad'],
    elementalBalance: {
      Fire: 0.1,
      Earth: 0.5,
      Water: 0.3,
      Air: 0.1
    },
    instructions: [
      'In a medium saucepan, bring quinoa and water to a boil. Reduce heat, cover, and simmer until quinoa is tender and water is absorbed, about 15 minutes.',
      'Remove from heat and let stand, covered, for 5 minutes. Fluff with a fork and let cool.',
      'In a large bowl, combine cooled quinoa, black beans, tomatoes, cucumber, bell pepper, onion, and cilantro.',
      'In a small bowl, whisk together lime juice, olive oil, cumin, and salt. Pour over quinoa mixture and toss to coat.',
      'Chill in the refrigerator for at least 30 minutes before serving to allow flavors to meld.'
    ]
  },;