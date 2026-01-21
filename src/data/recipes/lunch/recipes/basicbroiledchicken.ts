import { Recipe } from '../../../../types/recipe';

export const basicbroiledchicken: Recipe = {
  name: 'Basicbroiledchicken',
  description: 'A satisfying and balanced meal perfect for midday dining.',
  ingredients: [
    { name: 'Mediumchicken napounds)', amount: 1.0 },
    { name: 'Etablespoonsextra virgin olive oil', amount: 2.0, unit: 'tbsp' },
    { name: 'Teaspeonseasaitormoretotaste', amount: 1.0 },
    { name: 'Pinchfreshiygroundblackpepper', amount: 0.25, unit: 'tsp' },
    { name: '0.5 Preheatbroner', amount: 1.0 },
    { name: 'Ominutespriortousing adjustracktoiowestsetting.', amount: 1.0 },
  ],
  instructions: [
    'Preheat broiler 20 minutes prior to using. Adjust rack to lowest setting.',
    'Rub both skin side and inside of chicken with olive oil, salt, and fresh ground black',
    'Heat 10-inch sauté pan over medium flame and place chicken, skin side down, in pan. Do',
    'Broil chicken skin side down for 15 minutes. Carefully flip chicken skin side up, and',
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
