import { Recipe } from '../../../../types/recipe';

export const hollandaise: Recipe = {
  name: 'Hollandaise',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'Eeggyoiks', amount: 4.0 },
    { name: 'Bounces Ciarifiedbutter Meitedandwarm', amount: 1.0 },
    { name: 'o.stablespoonsiemonjuice', amount: 1.0 },
    { name: 'Saittotaste', amount: 1.0 },
    { name: 'Whiteorcayenepeppertotaste', amount: 0.1, unit: 'tsp', notes: 'or to taste' },
    { name: 'Bettomed Straight Sidedbowioverbainmarie doubieboner)', amount: 1.0 },
    { name: 'Withiemonjuice Saitandpepperuntilthickandcreamy Untilwhiskieavestracksin', amount: 1.0 },
  ],
  instructions: [
    'Using round-bottomed, straight-sided bow] over bain marie (double boiler), whisk yolks',
    'Have butter warm but not hot. Add butter slowly, drop by drop first, whisking',
    'Do not add more than egg yolks can hold. Add lemon juice, salt, and pepper to taste.',
    'Ifsauce breaks, rescue by adding 1 teaspoon of cold water and beating vigorously. If this',
    'Ifnecessary, thin with few drops of warm water.',
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
