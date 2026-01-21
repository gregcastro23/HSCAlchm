import { Recipe } from '../../../../types/recipe';

export const sunDriedtomatoandpesto: Recipe = {
  name: 'Sun Driedtomatoandpesto',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Nargebunchfreshbasn Washedandstemsremoved', amount: 1.0 },
    { name: 'Icupswainuts Toasted', amount: 1.0 },
    { name: 'Iosun Driedtomatoes Reconstituted', amount: 1.0 },
    { name: 'Ciovesgarlice', amount: 1.0 },
    { name: 'o.ggttablespoonsonvean', amount: 1.0 },
    { name: 'Iteaspoonwhitemiso', amount: 0.25, unit: 'cup' },
    { name: 'Seasaittotaste', amount: 1.0 },
  ],
  instructions: [
    'Combine all ingredients in food processor until puréed. Taste and adjust seasoning.',
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
