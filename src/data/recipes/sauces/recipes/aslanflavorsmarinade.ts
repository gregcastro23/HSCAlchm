import { Recipe } from '../../../../types/recipe';

export const aslanflavorsmarinade: Recipe = {
  name: 'Aslanflavorsmarinade',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Y Cupfreshiysqueezedorangejuice', amount: 1.0 },
    { name: 'Tablespoonsricevinegar', amount: 1.0, unit: 'tbsp' },
    { name: 'Etablespoonsshoyu', amount: 1.0 },
    { name: 'Etablespoonscanoiaorcoconuton', amount: 1.0 },
    { name: 'Iteaspoondarksesameon', amount: 1.0 },
    { name: 'Iargegarlicccioves Sliced', amount: 3.0 },
    { name: 'Itablespoonchoppedfreshginger', amount: 1.0 },
    { name: 'Iscanion Chopped', amount: 1.0, unit: 'large' },
    { name: 'Severaisprigsfreshcnantro', amount: 1.0 },
    { name: 'combineaningredients.', amount: 1.0 },
    { name: 'Instituteofcunaryeducation Coursee i9t', amount: 1.0 },
  ],
  instructions: [
    'Inblender, combine all ingredients.',
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
