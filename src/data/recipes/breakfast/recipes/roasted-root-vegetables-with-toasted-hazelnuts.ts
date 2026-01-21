import { Recipe } from '../../../../types/recipe';

export const roastedRootVegetablesWithToastedHazelnuts: Recipe = {
  name: 'Roasted Root Vegetables with Toasted Hazelnuts',
  description: 'A medley of seasonal root vegetables roasted until caramelized, topped with toasted hazelnuts and fresh herbs.',
  ingredients: [
    { name: 'carrots', amount: 3.0, unit: 'medium', notes: 'cut into 2-inch pieces' },
    { name: 'parsnips', amount: 3.0, unit: 'medium', notes: 'cut into 2-inch pieces' },
    { name: 'sweet potatoes', amount: 2.0, unit: 'medium', notes: 'cut into 2-inch pieces' },
    { name: 'beets', amount: 2.0, unit: 'medium', notes: 'cut into 2-inch pieces' },
    { name: 'olive oil', amount: 3.0, unit: 'tbsp' },
    { name: 'garlic cloves', amount: 6.0, notes: 'whole, peeled' },
    { name: 'hazelnuts', amount: 0.5, unit: 'cup', notes: 'toasted and roughly chopped' },
    { name: 'fresh cilantro', amount: 0.5, unit: 'cup', notes: 'chopped' },
    { name: 'sea salt', amount: 1.0, unit: 'tsp' },
    { name: 'black pepper', amount: 0.5, unit: 'tsp' },
    { name: 'fresh thyme', amount: 2.0, unit: 'tbsp', notes: 'leaves only' },
  ],
  instructions: [
    'Combinecucumbers, limejuice, mint, water, andagaveinblender andpuree until',
    'Strainpureethroughsieve andserveinglasses withsliceoflime.',
  ],
  nutrition: {
    calories: 200,
    protein: 8,
    carbs: 25,
    fat: 12,
    vitamins: ['C', 'K'],
    minerals: ['Potassium', 'Iron'],
  },
  timeToMake: '30 minutes',
  season: ['all'],
  cuisine: 'HSCA',
  mealType: ['Health Supportive'],
  elementalBalance: {
    Fire: 0.25,
    Earth: 0.25,
    Water: 0.25,
    Air: 0.25,
  },
};
