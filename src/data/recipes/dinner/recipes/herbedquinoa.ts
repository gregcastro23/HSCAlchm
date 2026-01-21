import { Recipe } from '../../../../types/recipe';

export const herbedquinoa: Recipe = {
  name: 'Herbedquinoa',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'o.scupquinoa Rinsed', amount: 1.0, unit: 'cup' },
    { name: 'Icupsboningwater', amount: 1.0 },
    { name: 'To', amount: 1.0 },
    { name: 'Teaspoonofsait', amount: 1.0 },
    { name: 'Itablespoonfreshtarragon Chopped', amount: 2.0, unit: 'tbsp' },
    { name: 'o.stoastquinoain', amount: 1.0 },
    { name: 'Quartsaucepanoverhighheat Stirringconstantiyuntilitsmens', amount: 1.0 },
    { name: 'Nuttyandbrownsnghtiy S tminutes).', amount: 1.0 },
  ],
  instructions: [
    'Toast quinoa in 2 4% quart saucepan over high heat, stirring constantly until it smells',
    'Remove quinoa from heat. Add boiling water and salt. Lower heat and simmer, covered,',
    'Fluff with fork and add tarragon before serving.',
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
