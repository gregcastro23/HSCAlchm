import { Recipe } from '../../../../types/recipe';

export const misoGlazedwhitefish: Recipe = {
  name: 'Miso Glazedwhitefish',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'o.ggtcupsake', amount: 1.0 },
    { name: 'Y Ecupmirin', amount: 1.0, unit: 'tsp', notes: 'ground' },
    { name: 'Icupwhitemiso', amount: 0.25, unit: 'cup' },
    { name: 'Eacupricesyrup', amount: 1.25, unit: 'tbsp' },
    { name: 'o.eeecupsheyu', amount: 1.0 },
    { name: 'Bwhitefishfnets Skinon Dividedintoeighta Ounceportions', amount: 1.0 },
    { name: 'Mirin Miso Ricesyrup Andshoyuinsmanpot whisktoemuisify.', amount: 1.0 },
    { name: 'transfertoicebathtoquickiycooi.', amount: 1.0 },
  ],
  instructions: [
    'Combine sake, mirin, miso, rice syrup, and shoyu in small pot. Whisk to emulsify.',
    'Place filets in shallow hotel pan and pour marinade over them. Refrigerate for 1 hour.',
    'Heat broiler. Lightly oil half sheet tray. Arrange filets skin side down on tray. Broil 5-7',
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
