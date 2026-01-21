import { Recipe } from '../../../../types/recipe';

export const brownbeefstock: Recipe = {
  name: 'Brownbeefstock',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Bpoundsbeeforveaibones', amount: 1.0 },
    { name: 'Ipoundmirepeix', amount: 1.0 },
    { name: 'Gquartswaterorenoughtocoverby', amount: 1.0 },
    { name: 'Inches', amount: 2.0, unit: 'cups' },
    { name: 'o.ggttomatoes Chopped', amount: 2.0, unit: 'medium' },
    { name: 'Icupwhiteorredwineor', amount: 1.0 },
    { name: 'Tablespoonsbaisamicvinegar', amount: 2.0, unit: 'tbsp' },
    { name: 'Brownbonesandvegetablesbyroastingfirstin', amount: 1.0 },
    { name: 'Sofoven Simmer', amount: 1.0 },
    { name: 'Gtobhours', amount: 1.0 },
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
