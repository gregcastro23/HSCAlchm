import { Recipe } from '../../../../types/recipe';

export const freshherbmarinade: Recipe = {
  name: 'Freshherbmarinade',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'o.scupextravirginonvecn', amount: 2.0, unit: 'tbsp' },
    { name: 'Sprigsfreshrosemary Bruised', amount: 1.0 },
    { name: 'Ibunchparsiey Minced', amount: 1.0 },
    { name: 'Blackpepper Freshiyground', amount: 1.0 },
    { name: 'Ieatspait', amount: 1.0 },
    { name: 'o.sinsmanbowi combineaningredients.', amount: 1.0 },
  ],
  instructions: [
    'Insmall bowl, combine all ingredients.',
    'Let vegetables soak in marinade for 20 to 30 minutes before grilling.',
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
