import { Recipe } from '../../../../types/recipe';

export const veganmozzarella: Recipe = {
  name: 'Veganmozzarella',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Eacuprawcashews', amount: 0.5, unit: 'cup', notes: 'soaked overnight and drained' },
    { name: 'Eacupcashewmnk recipebeiow)', amount: 1.0 },
    { name: 'Iteaspoontahini', amount: 1.0 },
    { name: 'Etablespoonsiemonjuice', amount: 1.0 },
    { name: 'Iacupcoconuton', amount: 1.0 },
    { name: 'Teaspoongarliccpowder', amount: 1.0 },
    { name: 'V Bteaspoondriedbasn', amount: 1.0 },
    { name: 'Itspait', amount: 1.0, unit: 'tbsp' },
    { name: 'Icupswater Divided', amount: 1.0 },
    { name: 'Tspagarpowder', amount: 2.0, unit: 'tsp' },
  ],
  instructions: [
    'Place cashews, cashew milk, tahini, lemon juice, coconut oil, salt, garlic powder, dried',
    'Place agar in 1 % cups water and bring to simmer. Simmer until agar dissolves. Add agar',
    'Pour mixture into silicone molds and refrigerate until set.',
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
