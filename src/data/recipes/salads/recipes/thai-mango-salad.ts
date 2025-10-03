import { Recipe } from '../../../../types/recipe';

export const thaimangosalad: Recipe = {
    name: 'Thai Mango Salad',
    description: 'A refreshing and zesty salad with ripe mango, fresh herbs, and a spicy lime dressing.',
    ingredients: [
      { name: 'ripe mangoes, julienned', amount: 2, unit: 'large' },
      { name: 'red bell pepper, julienned', amount: 1, unit: '' },
      { name: 'red onion, thinly sliced', amount: 0.5, unit: '' },
      { name: 'fresh cilantro, chopped', amount: 0.5, unit: 'cup' },
      { name: 'fresh mint leaves, chopped', amount: 0.25, unit: 'cup' },
      { name: 'lime juice', amount: 3, unit: 'tbsp' },
      { name: 'fish sauce', amount: 1, unit: 'tbsp' },
      { name: 'honey', amount: 1, unit: 'tbsp' },
      { name: 'bird\'s eye chili, finely chopped (optional)', amount: 1, unit: '' },
      { name: 'roasted peanuts, chopped', amount: 0.25, unit: 'cup' }
    ],
    nutrition: {
      calories: 160,
      protein: 4,
      carbs: 28,
      fat: 6,
      vitamins: ['A', 'C'],
      minerals: ['Potassium', 'Magnesium']
    },
    timeToMake: '20 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Salad'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.3,
      Water: 0.3,
      Air: 0.1
    },
    instructions: [
      'In a large bowl, combine julienned mangoes, bell pepper, red onion, cilantro, and mint.',
      'In a small bowl, whisk together lime juice, fish sauce, honey, and bird\'s eye chili (if using) to make the dressing.',
      'Pour the dressing over the mango mixture and toss gently to coat evenly.',
      'Transfer the salad to a serving plate and sprinkle chopped peanuts on top.',
      'Serve immediately as a refreshing and flavorful side dish or light meal.'
    ]
  },;