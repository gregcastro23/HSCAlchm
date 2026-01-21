import { Recipe } from '../../../../types/recipe';

export const sesamepressedcrust: Recipe = {
  name: 'Sesamepressedcrust',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Cupwhoiewheatpastryfiour', amount: 1.5, unit: 'cups' },
    { name: 'o.scupfood Processedronedoats', amount: 1.0 },
    { name: 'Cuptoastedsesameseeds', amount: 1.0, unit: 'tbsp' },
    { name: 'Teaspeonseasait', amount: 1.0 },
    { name: 'Cupmeitedcoconuton', amount: 1.0 },
    { name: 'Etablespoonswarmmapiesyrup', amount: 1.0 },
    { name: 'Chniedjuiceorwatertobindasneeded', amount: 1.0 },
    { name: 'o.spreheat oven to', amount: 1.0 },
    { name: 'Esof on9 inchpieortartpan.', amount: 1.0 },
  ],
  instructions: [
    'Preheat oven to 350° F. Oil 9-inch pie or tart pan.',
    'Process together whole wheat pastry flour, oatmeal, sesame seeds and salt until mixture is',
    'Whisk together oil and syrup.',
    'Add oil-syrup mixture to processor and mix until thoroughly combined. Add juice or',
    'With wet fingertips, press mixture into oiled pie plate.',
    'Bake 20 to 25 minutes, until golden.',
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
