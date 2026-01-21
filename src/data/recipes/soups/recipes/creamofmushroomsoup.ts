import { Recipe } from '../../../../types/recipe';

export const creamofmushroomsoup: Recipe = {
  name: 'Creamofmushroomsoup',
  description: 'A rich and earthy soup with deep umami flavors.',
  ingredients: [
    { name: 'Etablespoonsbutterorolive oil', amount: 1.0 },
    { name: 'o.scupslicedshanots', amount: 1.0 },
    { name: 'Tablespoonswhoie Wheatfiour', amount: 1.5, unit: 'cups' },
    { name: 'Cupsstock', amount: 4.0, unit: 'cups' },
    { name: 'Ipoundmushrooms Sliced', amount: 8.0, unit: 'oz' },
    { name: 'Itspsait', amount: 1.0 },
    { name: 'Itspsherryvinegar Ormoretotaste', amount: 1.0 },
    { name: 'Blackpeppertotaste', amount: 0.25, unit: 'tsp', notes: 'ground' },
    { name: 'Parsieysprigsforgamish', amount: 1.0 },
    { name: 'o.sini Ganonpot Heatbutterorolive oil Addshanotsandsauteuntiltransiucent Add', amount: 1.0 },
    { name: 'Flour Stira Sminutes untiltoasted.', amount: 1.0 },
  ],
  instructions: [
    'cups stock',
    'In1-gallon pot, heat butter or olive oil. Add shallots and sauté until translucent. Add',
    'Add stock 1 cup at a time, whisking to blend. Bring soup to simmer, add salt.',
    'Add mushrooms to soup. Simmer 30 minutes.',
    'Puree soup in blender. Add sherry and black pepper. Adjust seasonings. Serve garnished',
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
