import { Recipe } from '../../../../types/recipe';

export const bruschettawithfreshtomatoes: Recipe = {
    name: 'Bruschetta with Fresh Tomatoes',
    description: 'Classic Italian appetizer featuring toasted bread topped with seasoned fresh tomatoes and basil.',
    ingredients: [
      { name: 'baguette, sliced', amount: 1, unit: '' },
      { name: 'ripe tomatoes, diced', amount: 4, unit: 'medium' },
      { name: 'fresh basil leaves, chopped', amount: 0.5, unit: 'cup' },
      { name: 'garlic cloves, minced', amount: 3, unit: '' },
      { name: 'olive oil', amount: 0.25, unit: 'cup' },
      { name: 'balsamic vinegar', amount: 2, unit: 'tbsp' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 180,
      protein: 4,
      carbs: 24,
      fat: 8,
      vitamins: ['A', 'C', 'K'],
      minerals: ['Potassium', 'Iron']
    },
    timeToMake: '25 minutes',
    season: ['summer'],
    cuisine: 'HSCA',
    mealType: ['Appetizer'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.4,
      Water: 0.2,
      Air: 0.2
    },
    instructions: [
      'Preheat oven to 375°F.',
      'In a bowl, combine diced tomatoes, basil, garlic, 2 tablespoons olive oil, balsamic vinegar, salt, and pepper.',
      'Let the mixture sit at room temperature for 15 minutes to marinate.',
      'Brush baguette slices with remaining olive oil and arrange on a baking sheet.',
      'Toast in the oven for 5-7 minutes until golden brown.',
      'Top each slice with the tomato mixture and serve immediately.'
    ]
  },;