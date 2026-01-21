import { Recipe } from '../../../../types/recipe';

export const tomatopasta: Recipe = {
  name: 'Tomatopasta',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Cupsunbieachedfiour', amount: 1.0 },
    { name: 'Tablespoonstomatopaste', amount: 1.0 },
    { name: 'Eiargeeggs Beaten', amount: 2.0, unit: 'medium', notes: 'peeled and quartered' },
    { name: 'I stirtomatopasteintoeggs.', amount: 1.0 },
  ],
  instructions: [
    'Stir tomato paste into eggs.',
    'Follow one of the below methods.',
    'Pulse flour in food processor to evenly distribute and aerate. Add tomato-egg mixture,',
    'Turn dough onto work surface; knead until dough is smooth, 1 to 2 minutes. Cover with',
    'Sift flour onto work surface (or bowl) in mound and make hollow in middle. Pour tomato-',
    'Work in water with both thumbs, then press dough into ball and work in rest of flour.',
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
