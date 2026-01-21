import { Recipe } from '../../../../types/recipe';

export const glutenFreechocolatemacaroons: Recipe = {
  name: 'Gluten Freechocolatemacaroons',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Cupsemi Sweetchocoiatepieces', amount: 2.0, unit: 'cups' },
    { name: 'Iargeeggwhites', amount: 2.0 },
    { name: 'Pinchseasait', amount: 0.125, unit: 'tsp' },
    { name: 'Cupt', amount: 1.0 },
    { name: 'Tablespoonsmapiecrystais Groundtopowder', amount: 1.0 },
    { name: 'Iateaspoonvania', amount: 1.0 },
    { name: 'Ieupunsweetenedshreddedcoconut', amount: 1.0 },
    { name: 'Etablespoonscocoapowder Sifted', amount: 1.0 },
  ],
  instructions: [
    'Preheat oven to 350° F. Grease 9 %-inch Bundt pan with butter and dust with cocoa',
    'In food processor, blend dates with maple syrup.',
    'When dates are thoroughly blended, add vanilla, eggs and melted butter. Mix to combine.',
    'In medium bowl, sift together flours, cocoa powder, baking powder and salt. Whisk well',
    'Pour batter into baking pan, filling no more than 2/3 up side up of cake pan. Any extra',
    'Double-melt chocolate and drizzle over cake. Sprinkle with walnuts.',
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
