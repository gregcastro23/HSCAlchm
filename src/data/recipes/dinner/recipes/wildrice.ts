import { Recipe } from '../../../../types/recipe';

export const wildrice: Recipe = {
  name: 'Wildrice',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'o.scupwndrice Soakedin', amount: 1.0 },
    { name: 'cupswaterforbhoursanddrained)', amount: 1.0 },
    { name: 'Cupswater', amount: 2.0, unit: 'cups' },
    { name: 'Tspait', amount: 1.0 },
    { name: '.washanddrainrice.', amount: 1.0 },
    { name: 'Addricetowater Addsait Bringtoabon Covered Iowerheatand', amount: 1.0 },
    { name: 'Simmerabout', amount: 1.0 },
    { name: 'Stosominutesoruntilriceistender riceshouidbutterfiysnghtiy).', amount: 1.0 },
  ],
  instructions: [
    'Wash and drain rice.',
    'In small saucepot, add rice to water. Add salt. Bring to a boil, covered, lower heat and',
    'Place rice in colander and drain excess water.',
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
