import { Recipe } from '../../../../types/recipe';

export const tempehSausage: Recipe = {
  name: 'Tempeh Sausage',
  description: 'A professional sauce recipe recovered from HSCA culinary school materials.',
  ingredients: [
    { name: 'tompeh', amount: 8.0, unit: 'ounces' },
    { name: 'garlic, minced', amount: 1.0, unit: 'clove' },
    { name: 'wator', amount: 2.0, unit: 'tablespoons' },
    { name: 'olive oil', amount: 1.0, unit: 'tablespoon' },
    { name: 'tamari', amount: 2.0, unit: 'tablespoons' },
    { name: 'sage', amount: 4.0, unit: 'toaspoon' },
    { name: 'dried marjoram', amount: 4.0, unit: 'toaspoon' },
    { name: 'dried thyme', amount: 0.25, unit: 'toaspoon' },
    { name: 'paprika', amount: 0.25, unit: 'toaspoon' },
    { name: 'fennel seeds, l', amount: 0.25, unit: 'toaspoon' },
  ],
  instructions: [
    'Cut tempeh into 2-inch pieces and steam for 20 minutes in steamer basket over',
    'Grate tempeh on large holes on box grater. Combine grated tempeh with garlic, water,',
    'Form mixture into walnut-sized balls using 1-ounce ice cream scoop and press into',
    'Prepare plate with paper towel for draining. In sauté pan, heat oil and fry patties until',
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
