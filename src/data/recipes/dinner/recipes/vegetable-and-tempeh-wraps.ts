import { Recipe } from '../../../../types/recipe';

export const vegetableandtempehwraps: Recipe = {
    name: 'Vegetable and Tempeh Wraps',
    description: 'Hearty vegetable and tempeh wraps with seasonal vegetables.',
    ingredients: [
      { name: 'tempeh', amount: 16, unit: 'oz', notes: 'sliced' },
      { name: 'tamari', amount: 0.25, unit: 'cup' },
      { name: 'mirin', amount: 2, unit: 'tbsp' },
      { name: 'sesame oil', amount: 2, unit: 'tbsp' },
      { name: 'mixed vegetables', amount: 4, unit: 'cups', notes: 'seasonal, julienned' },
      { name: 'ginger', amount: 2, unit: 'tbsp', notes: 'minced' },
      { name: 'garlic', amount: 3, unit: 'cloves', notes: 'minced' },
      { name: 'whole grain wraps', amount: 8, unit: 'large' },
      { name: 'sprouts', amount: 2, unit: 'cups' }
    ],
    nutrition: {
      calories: 320,
      protein: 18,
      carbs: 38,
      fat: 12,
      vitamins: ['B12', 'K'],
      minerals: ['Iron', 'Calcium']
    },
    timeToMake: '40 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Dinner', 'Lunch'],
    elementalBalance: {
      Fire: 0.2,
      Earth: 0.3,
      Water: 0.2,
      Air: 0.3
    },
    instructions: [
      'Marinate tempeh in tamari and mirin for 20 minutes.',
      'Heat sesame oil in large skillet. Cook tempeh until golden brown on both sides.',
      'In same pan, sauté vegetables with ginger and garlic until tender-crisp.',
      'Warm wraps according to package instructions.',
      'Assemble wraps with tempeh, vegetables, and sprouts.'
    ]
  },;