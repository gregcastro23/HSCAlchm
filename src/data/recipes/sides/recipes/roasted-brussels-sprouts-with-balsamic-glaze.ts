import { Recipe } from '../../../../types/recipe';

export const roastedbrusselssproutswithbalsamicglaze: Recipe = {
    name: 'Roasted Brussels Sprouts with Balsamic Glaze',
    description: 'Crispy and caramelized Brussels sprouts drizzled with a sweet and tangy balsamic glaze.',
    ingredients: [
      { name: 'Brussels sprouts, trimmed and halved', amount: 1.5, unit: 'lbs' },
      { name: 'olive oil', amount: 2, unit: 'tbsp' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' },
      { name: 'balsamic vinegar', amount: 0.25, unit: 'cup' },
      { name: 'honey', amount: 1, unit: 'tbsp' }
    ],
    nutrition: {
      calories: 160,
      protein: 6,
      carbs: 20,
      fat: 8,
      vitamins: ['C', 'K', 'B6'],
      minerals: ['Potassium', 'Iron']
    },
    timeToMake: '40 minutes',
    season: ['fall', 'winter'],
    cuisine: 'HSCA',
    mealType: ['Side Dish'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.6,
      Water: 0.1,
      Air: 0.1
    },
    instructions: [
      'Preheat oven to 425°F. Line a baking sheet with parchment paper.',
      'In a large bowl, toss Brussels sprouts with olive oil, salt, and pepper until evenly coated.',
      'Spread the Brussels sprouts in a single layer on the prepared baking sheet.',
      'Roast for 25-30 minutes, stirring halfway through, until the Brussels sprouts are tender and caramelized.',
      'In a small saucepan, combine balsamic vinegar and honey. Bring to a boil, then reduce heat and simmer until the mixture thickens and coats the back of a spoon, about 5-7 minutes.',
      'Drizzle the balsamic glaze over the roasted Brussels sprouts and toss to coat evenly.',
      'Serve hot as a delicious and healthy side dish.'
    ]
  },;