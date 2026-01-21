import { Recipe } from '../../../../types/recipe';

export const wholewheatbread: Recipe = {
  name: 'Wholewheatbread',
  description: 'Freshly baked goods with wholesome ingredients and amazing flavor.',
  ingredients: [
    { name: 'Itablespoondryyeast', amount: 1.0 },
    { name: 'Cupswarmwater', amount: 1.0 },
    { name: 'Ieupwhoiewheatbreadfiour', amount: 1.5, unit: 'cups' },
    { name: 'Etablespoonshoneyormapiesyrup', amount: 1.0 },
    { name: 'Scupswhoiewheatpastryfiour', amount: 1.5, unit: 'cups' },
    { name: 'Cupextra virgin olive oil', amount: 2.0, unit: 'tbsp' },
    { name: 'Itablespoonseasait', amount: 1.0 },
    { name: 'forsponge:', amount: 1.0, notes: 'sliced' },
  ],
  instructions: [
    'Preheat oven to 375°. In large bowl, combine yeast, water, whole wheat bread flour, 1 cup',
    'Add olive oil, salt, and just enough of remaining pastry flour to create dough that pulls',
    'Knead dough about 10-15 minutes, adding remaining pastry flour as necessary, until',
    'Transfer dough to clean, lightly oiled bowl and cover with plastic wrap. Proof in warm',
    'While dough is proofing, prepare bread pans or sheet pans by lining with parchment',
    'Fold/turn dough. Rise one more time.',
    'Transfer bread to oven and bake approximately 30-45 minutes or until golden and firm to',
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
