import { Recipe } from '../../../../types/recipe';

export const ichibandashi: Recipe = {
  name: 'Ichibandashi',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'S Inchpiecekombu', amount: 1.0 },
    { name: 'Cupswater', amount: 2.0, unit: 'cups' },
    { name: 'o.eeecupbonitofiakes optionai)', amount: 1.0 },
    { name: 'Ifithassaityresidue piaceitinpotandcoverwithcoidwater.', amount: 1.0 },
    { name: 'o.setstand', amount: 1.0 },
    { name: 'eominutes.', amount: 1.0 },
  ],
  instructions: [
    'Wipe kombu with towel, if it has salty residue. Place it in pot and cover with cold water.',
    'Bring to boil, add bonito flakes and remove from heat.',
    'Wait till bonito flakes sink to bottom of pot and strain through cheesecloth.',
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
