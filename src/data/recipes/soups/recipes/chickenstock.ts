import { Recipe } from '../../../../types/recipe';

export const chickenstock: Recipe = {
  name: 'Chickenstock',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Bpoundsbones Necks Backs wingtips)', amount: 1.0 },
    { name: 'Gquartswater', amount: 1.0 },
    { name: 'Ipoundmirepeix', amount: 1.0 },
    { name: 'Beuquetgami', amount: 1.0 },
    { name: 'Tablespoonsbrownricevinegarorcidervinegar', amount: 1.0 },
    { name: 'Simmier', amount: 1.0 },
    { name: 'Natoahours', amount: 1.0 },
    { name: 'anmeatstocksshouidbesimmeredhaifcovered.', amount: 1.0 },
    { name: 'Instituteofcunaryeducation course2 i2a', amount: 1.0 },
  ],
  instructions: [
    'Combine bones, onion, carrot, celery, sachet, and water in large stock pot.',
    'Cover pot and bring to boil. Remove cover and skim any foam off top.',
    'Reduce heat and simmer uncovered for 3-4 hours.',
    'Cool stock in ice bath and refrigerate.',
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
