import { Recipe } from '../../../../types/recipe';

export const whitebeanwithgarlicRosemaryAndtomatoes: Recipe = {
  name: 'Whitebeanwithgarlic Rosemary Andtomatoes',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Servesb', amount: 1.0 },
    { name: 'Ipintgrapetomatoes Haived', amount: 4.0, unit: 'medium' },
    { name: 'Stablespoonsolive oil Divided', amount: 1.0 },
    { name: 'Sciovesgarlicc Sliced', amount: 0.25, unit: 'cup' },
    { name: 'Iteaspoondryrosemary', amount: 1.0, unit: 'tbsp' },
    { name: 'Teaspoondryoregano', amount: 1.0 },
    { name: 'Ieupwhitebeans Soakedovemightanddrained', amount: 1.0 },
    { name: 'Tspait', amount: 1.0 },
    { name: 'Ecupswater', amount: 2.0, unit: 'cups' },
    { name: 'Saitandpeppertotaste', amount: 1.0 },
  ],
  instructions: [
    'Preheat oven to 200° F. Toss grape tomatoes in bowl with 2 tablespoons olive oil. Spread',
    'While tomatoes are roasting, heat remaining 3 tablespoons olive oil over medium flame in',
    'Secure lid to pressure cooker, bring cooker up to pressure, lower heat, and cook beans for',
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
