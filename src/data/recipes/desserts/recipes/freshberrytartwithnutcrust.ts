import { Recipe } from '../../../../types/recipe';

export const freshberrytartwithnutcrust: Recipe = {
  name: 'Freshberrytartwithnutcrust',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Crust Fnng', amount: 1.0 },
    { name: 'Ieuppecans Roastedandcooied 2tablespoonsagarfiakes', amount: 1.0 },
    { name: 'Eacupgiuten Freefiourbiend Iaacupsappiejuice', amount: 1.0 },
    { name: 'Tablespoonsmapiecrystais 2tablespoonskuzudissoivedin', amount: 1.0 },
    { name: 'Iacupjuice', amount: 1.0, unit: 'cup', notes: 'approximately 6 limes' },
    { name: 'Iateaspoonbakingpowder 2tablespoonsmapiesyrup', amount: 1.0 },
    { name: 'Pinchseasait Seasait', amount: 1.0 },
    { name: 'itablespoonmeitedcoconutoio.scupsbiueberries Washedanddrained', amount: 1.0 },
    { name: 'Iacupmapiesyrup 2cupsraspberries Rinsedanddrained', amount: 1.0 },
  ],
  instructions: [
    'Preheat oven to 350° F. Oil 9-inch tart pan or use 5-6 four-inch, non-stick paper tart',
    'Add oil and syrup to dry ingredients in processor. Pulse lightly until dough comes',
    'Press crust mixture into tart pan(s). Refrigerate 15-20 minutes, then bake 20-25 minutes.',
    'Insmall pot, simmer agar flakes in apple juice until agar completely dissolves. Add',
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
