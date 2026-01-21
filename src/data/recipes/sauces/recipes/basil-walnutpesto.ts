import { Recipe } from '../../../../types/recipe';

export const basilWalnutpesto: Recipe = {
  name: 'Basil Walnutpesto',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Eacupwainutsforpestopiuseupforgamish', amount: 1.0 },
    { name: 'Cupsbasnieaves Firmiypacked', amount: 1.0 },
    { name: 'Igarliccciove', amount: 3.0 },
    { name: 'Tablespoonsfreshiemonjuice', amount: 1.0 },
    { name: 'o.eeecupextra virgin olive oil', amount: 2.0, unit: 'tbsp' },
    { name: 'Iteaspoonmenowbarieymiso', amount: 1.0 },
    { name: 'Tspait', amount: 1.0 },
    { name: 'Iateaspoonblackpepper', amount: 0.25, unit: 'tsp' },
  ],
  instructions: [
    'Preheat oven to 350°F. Toast walnuts on sheet tray for 10 minutes. Remove from oven',
    'Transfer walnuts from strainer and add 3% cup to food processor. Add remaining',
    'Process everything until smooth. Chop by hand remaining % cup of walnuts into pieces.',
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
