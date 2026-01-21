import { Recipe } from '../../../../types/recipe';

export const freshstrawberriesandbananas: Recipe = {
  name: 'Freshstrawberriesandbananas',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Servesb', amount: 1.0 },
    { name: 'Pintsstrawberries Trimmedandsliced', amount: 2.0, unit: 'cups' },
    { name: 'Tablespoonsmapiecrystais', amount: 1.0 },
    { name: 'Ebananas Sliced', amount: 1.0 },
    { name: 'Nemon', amount: 1.0, unit: 'whole', notes: 'juice only' },
    { name: 'Tossstrawberrieswithmapiecrystais Setasidetomaceratefor', amount: 1.0 },
    { name: 'eominutes.', amount: 1.0 },
    { name: 'Combinebananaswithiemonjuice Whenstrawberriesaredone', amount: 1.0 },
    { name: 'Macerating addbananastostrawberries.', amount: 1.0 },
  ],
  instructions: [
    'In bowl, toss strawberries with maple crystals. Set aside to macerate for 30 minutes.',
    'In separate bowl, combine bananas with lemon juice. When strawberries are done',
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
