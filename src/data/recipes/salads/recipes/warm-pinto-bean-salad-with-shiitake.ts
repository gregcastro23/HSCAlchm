import { Recipe } from '../../../../types/recipe';

export const warmpintobeansaladwithshiitake: Recipe = {
    name: 'Warm Pinto Bean Salad with Shiitake',
    description: 'A hearty warm salad combining tender pinto beans with umami-rich shiitake mushrooms.',
    ingredients: [
      { name: 'pinto beans, cooked', amount: 3, unit: 'cups' },
      { name: 'shiitake mushrooms', amount: 8, unit: 'oz', notes: 'sliced' },
      { name: 'olive oil', amount: 3, unit: 'tbsp' },
      { name: 'shallots', amount: 2, unit: 'medium', notes: 'finely diced' },
      { name: 'garlic cloves', amount: 3, unit: '', notes: 'minced' },
      { name: 'fresh thyme', amount: 2, unit: 'tsp', notes: 'chopped' },
      { name: 'apple cider vinegar', amount: 2, unit: 'tbsp' },
      { name: 'tamari', amount: 1, unit: 'tbsp' },
      { name: 'fresh parsley', amount: 0.5, unit: 'cup', notes: 'chopped' },
      { name: 'sea salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 280,
      protein: 14,
      carbs: 38,
      fat: 9,
      vitamins: ['B6', 'C', 'K'],
      minerals: ['Iron', 'Potassium', 'Magnesium']
    },
    timeToMake: '25 minutes',
    season: ['fall', 'winter'],
    cuisine: 'HSCA',
    mealType: ['Salad'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.5,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'Heat 2 tablespoons olive oil in a large skillet over medium heat.',
      'Add shallots and cook until softened, about 3 minutes.',
      'Add shiitake mushrooms and cook until they release their moisture and begin to brown, about 5-7 minutes.',
      'Add garlic and thyme, cook for another minute until fragrant.',
      'Add cooked pinto beans and gently heat through.',
      'In a small bowl, whisk together remaining olive oil, apple cider vinegar, and tamari.',
      'Pour dressing over the warm bean mixture and toss gently.',
      'Season with salt and pepper to taste.',
      'Stir in fresh parsley just before serving.',
      'Serve warm or at room temperature.'
    ]
  };