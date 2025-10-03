import { Recipe } from '../../../../types/recipe';

export const applepearcrisp: Recipe = {
    name: 'Apple-Pear Crisp',
    description: 'A warm and comforting fruit crisp with a crunchy oat topping.',
    ingredients: [
      { name: 'apples, sliced', amount: 3, unit: 'large' },
      { name: 'pears, sliced', amount: 3, unit: 'large' },
      { name: 'lemon juice', amount: 2, unit: 'tbsp' },
      { name: 'maple syrup', amount: 0.25, unit: 'cup' },
      { name: 'cinnamon', amount: 1, unit: 'tsp' },
      { name: 'rolled oats', amount: 1, unit: 'cup' },
      { name: 'almond flour', amount: 0.5, unit: 'cup' },
      { name: 'chopped nuts', amount: 0.5, unit: 'cup' },
      { name: 'coconut oil, melted', amount: 0.25, unit: 'cup' },
      { name: 'salt', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 280,
      protein: 5,
      carbs: 42,
      fat: 12,
      vitamins: ['C', 'E'],
      minerals: ['Iron', 'Magnesium']
    },
    timeToMake: '1 hour',
    season: ['fall', 'winter'],
    cuisine: 'HSCA',
    mealType: ['Dessert'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.4,
      Water: 0.3,
      Air: 0.1
    },
    instructions: [
      'Preheat oven to 350°F.',
      'In a large bowl, toss sliced fruit with lemon juice, maple syrup, and cinnamon.',
      'In another bowl, combine oats, almond flour, nuts, melted coconut oil, and salt.',
      'Transfer fruit mixture to a baking dish.',
      'Sprinkle oat mixture evenly over the fruit.',
      'Bake for 45-50 minutes until fruit is tender and topping is golden brown.',
      'Let cool slightly before serving.'
    ]
  },;