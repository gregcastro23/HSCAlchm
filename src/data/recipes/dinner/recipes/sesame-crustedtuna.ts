import { Recipe } from '../../../../types/recipe';

export const sesameCrustedtuna: Recipe = {
  name: 'Sesame Crustedtuna',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Ipoundtuna Skinremoved', amount: 1.0 },
    { name: 'Saitandpeppertotaste', amount: 1.0 },
    { name: 'white sesame seeds', amount: 1.0, unit: 'tbsp' },
    { name: 'Cupblacksesameseeds', amount: 0.25, unit: 'cup', notes: 'toasted, for garlicish' },
    { name: 'Tablespoonscanoiaon', amount: 1.0 },
    { name: 'Tablespoonswasabipowder Mixedwithwatertoformsmoothpaste', amount: 1.0 },
    { name: 'Dippingsauce recipebeiow)', amount: 1.0 },
    { name: '0.5 seasontunawithsaitandpepper.', amount: 1.0 },
  ],
  instructions: [
    'Season tuna with salt and pepper.',
    'Combine sesame seeds and completely crust tuna.',
    'Heat canola oil in sauté pan over medium heat.',
    'Sear tuna on all sides, approximately 1 - 2 minutes each side.',
    'Lettuna rest for 5 minutes before slicing.',
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
