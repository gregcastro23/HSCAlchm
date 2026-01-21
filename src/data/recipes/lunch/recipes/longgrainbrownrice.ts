import { Recipe } from '../../../../types/recipe';

export const longgrainbrownrice: Recipe = {
  name: 'Longgrainbrownrice',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'Icupionggrainbrownrice Washed', amount: 1.0 },
    { name: 'Ieacupsboningwater', amount: 1.0 },
    { name: 'Tspait', amount: 1.0 },
    { name: '0.5 Dryroastuntilriceinsmanpotuntildryandsnghtiyaromatic', amount: 1.0 },
  ],
  instructions: [
    'Dry roast until rice in small pot until dry and slightly aromatic',
    'Add boiling water and salt to rice. Cover. Bring back to a boil. Reduce heat, and simmer',
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
