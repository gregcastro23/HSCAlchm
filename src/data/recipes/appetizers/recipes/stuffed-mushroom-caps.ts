import { Recipe } from '../../../../types/recipe';

export const stuffedmushroomcaps: Recipe = {
    name: 'Stuffed Mushroom Caps',
    description: 'Tender mushrooms filled with a savory herb and cheese mixture.',
    ingredients: [
      { name: 'cremini mushrooms', amount: 24, unit: 'medium' },
      { name: 'cream cheese, softened', amount: 8, unit: 'oz' },
      { name: 'Parmesan cheese, grated', amount: 0.5, unit: 'cup' },
      { name: 'garlic cloves, minced', amount: 2, unit: '' },
      { name: 'fresh parsley, chopped', amount: 0.25, unit: 'cup' },
      { name: 'fresh thyme leaves', amount: 1, unit: 'tbsp' },
      { name: 'breadcrumbs', amount: 0.5, unit: 'cup' },
      { name: 'olive oil', amount: 2, unit: 'tbsp' },
      { name: 'salt', amount: 0.5, unit: 'tsp' },
      { name: 'black pepper', amount: 0.25, unit: 'tsp' }
    ],
    nutrition: {
      calories: 160,
      protein: 8,
      carbs: 6,
      fat: 12,
      vitamins: ['D', 'B12'],
      minerals: ['Selenium', 'Copper']
    },
    timeToMake: '35 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Appetizer'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.5,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'Preheat oven to 400°F. Remove stems from mushrooms and finely chop them.',
      'In a bowl, mix chopped stems, cream cheese, Parmesan, garlic, herbs, and breadcrumbs.',
      'Season with salt and pepper.',
      'Fill each mushroom cap with the mixture.',
      'Place on a baking sheet and drizzle with olive oil.',
      'Bake for 20-25 minutes until golden brown and mushrooms are tender.'
    ]
  },;