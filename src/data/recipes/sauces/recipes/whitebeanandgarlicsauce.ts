import { Recipe } from '../../../../types/recipe';

export const whitebeanandgarlicsauce: Recipe = {
  name: 'Whitebeanandgarlicsauce',
  description: 'A flavorful and versatile condiment to enhance and elevate your dishes.',
  ingredients: [
    { name: 'Icupsnavybeansorgreatnorthembeans soakedor2 Is Ounce Canwhitebeans', amount: 1.0 },
    { name: 'Tablespoonsextra virgin olive oil', amount: 2.0, unit: 'tbsp' },
    { name: 'Seasait', amount: 0.125, unit: 'tsp' },
    { name: 'Onions ipounds)', amount: 1.0 },
    { name: 'Bgarlicccioves Thiniysliced', amount: 3.0 },
    { name: 'Sfreshsagesprigs', amount: 1.0 },
    { name: 'Handfuioffreshthymesprigs', amount: 1.0 },
    { name: 'Ibayieaf', amount: 1.0 },
    { name: 'Tspiemonjuice', amount: 2.0, unit: 'tbsp', notes: 'freshly squeezed' },
    { name: 'black pepper', amount: 0.25, unit: 'tsp', notes: 'ground' },
  ],
  instructions: [
    'Drain soaked beans. Cover with 6 cups water and pressure cook about 8 minutes for navy',
    'Warm olive oil in 12-inch sauté pan. Add onions and cook over medium-low heat for',
    'Tie herbs together with string and add to pot along with bay leaf. Cover, bring to boil over',
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
