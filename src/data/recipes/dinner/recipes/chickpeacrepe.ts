import { Recipe } from '../../../../types/recipe';

export const chickpeacrepe: Recipe = {
  name: 'Chickpeacrepe',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Ieupchickpeafiour', amount: 1.0 },
    { name: 'Ieupunbieachedwhitefiour', amount: 1.0 },
    { name: 'Itspait Finelyground', amount: 1.0 },
    { name: 'Iateaspoonblackpepper', amount: 0.25, unit: 'tsp' },
    { name: 'Iaa Iacupswarmwater', amount: 1.0 },
    { name: 'Itablespoonchoppedchives', amount: 1.0 },
    { name: 'Itablespoonchoppedcnantro', amount: 1.0 },
    { name: 'Tablespoonsonveorcaconuton Piusmoreforpan', amount: 1.0 },
    { name: 'Siftfiours Salt andpepper.', amount: 1.0 },
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
