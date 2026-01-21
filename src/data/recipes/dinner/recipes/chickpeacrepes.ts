import { Recipe } from '../../../../types/recipe';

export const chickpeacrepes: Recipe = {
  name: 'Chickpeacrepes',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Ieupchickpeafiour', amount: 1.0 },
    { name: 'Ieupunbieachedwhitefiour', amount: 1.0 },
    { name: 'itspait.', amount: 1.0 },
    { name: 'Iateaspoonblackpepper', amount: 0.25, unit: 'tsp' },
    { name: 'Cupswarmwater', amount: 1.0 },
    { name: 'Itablespoonfinelychoppedchives', amount: 1.0 },
    { name: 'Tablespoonsonveorcoconuton orinfusedon)', amount: 1.0 },
    { name: 'whisktogetherfiourswithsaitandpepper.', amount: 1.0 },
  ],
  instructions: [
    'In large bowl, sift flours, salt, and pepper.',
    'Add water, herbs and oil to flour mixture and blend with whisk until smooth. (May also',
    'Let batter rest at room temperature at least 30 minutes. If necessary, thin batter with',
    'Prepare crépe pan by oiling lightly. Pour approximately \\ cup of batter into pan, tipping',
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
