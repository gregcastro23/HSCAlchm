import { Recipe } from '../../../../types/recipe';

export const tempehreubensandwich: Recipe = {
  name: 'Tempehreubensandwich',
  description: 'A satisfying and portable meal packed with fresh ingredients and bold flavors.',
  ingredients: [
    { name: 'o.srecipefriedtempeh recipefonows)', amount: 1.0 },
    { name: 'Irecipespeitbread recipefonows)', amount: 1.0 },
    { name: 'condiments:', amount: 1.0 },
    { name: 'Eslicedtomato', amount: 1.0 },
    { name: 'Eavocadospreadomayonaise', amount: 1.0 },
    { name: 'Mustard', amount: 1.0, unit: 'tsp' },
    { name: 'Eketchup recipebeiow)', amount: 1.0 },
    { name: 'Esauerkraut', amount: 1.0 },
    { name: 'Epickies', amount: 1.0 },
  ],
  instructions: [
    'In blender, combine raisins (with soaking liquid), tomato puree, garlic, water, paprika,',
    'In 2% quart saucepan, on high heat, heat oil. Slowly add tomato mixture. Lower heat and',
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
