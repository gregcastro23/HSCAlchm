import { Recipe } from '../../../../types/recipe';

export const walnutteacookies: Recipe = {
  name: 'Walnutteacookies',
  description: 'A sweet and satisfying treat made with quality ingredients.',
  ingredients: [
    { name: 'o.scupcoidbutter 2sticks)', amount: 1.0 },
    { name: 'Cuppowderedmapiecrystais', amount: 1.0 },
    { name: 'Itspvaniaextract', amount: 0.5, unit: 'tsp' },
    { name: 'o.i2stspeasait', amount: 1.0 },
    { name: 'Icupunbieachedan Purposefiour', amount: 1.0 },
    { name: 'Icupwhoiewheatpastryfiour', amount: 1.5, unit: 'cups' },
    { name: 'Cupbrownricefiour', amount: 1.0, unit: 'tbsp' },
    { name: 'Eacupwainuts Finelychopped', amount: 2.0, unit: 'cups' },
    { name: 'Esof o.sine', amount: 1.0 },
    { name: 'Haif sheettrayswithparchmentpaper.', amount: 1.0 },
  ],
  instructions: [
    'Preheat oven to 350° F. Line 2 half-sheet trays with parchment.',
    'In medium bowl, sift flour, baking powder, and salt together.',
    'In stand mixer, blend peanut butter, oil, maple syrup, and vanilla.',
    'Add flour mixture to peanut butter mixture in stand mixer.',
    'Using l-ounce scoop, form cookies onto parchment-lined baking sheets and press cookies',
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
