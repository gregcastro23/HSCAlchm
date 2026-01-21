import { Recipe } from '../../../../types/recipe';

export const freshtomatosauce: Recipe = {
  name: 'Freshtomatosauce',
  description: 'A flavorful and versatile tomato-based condiment to enhance your favorite dishes.',
  ingredients: [
    { name: 'Etablespoonsextravirginonvean', amount: 1.0 },
    { name: 'Garlicccioves Minced', amount: 3.0 },
    { name: 'Iteaspoondriedbasn', amount: 1.0 },
    { name: 'drainedor2poundsfreshtomatoes Concass A Inchdice', amount: 1.0 },
    { name: 'Seasait', amount: 0.125, unit: 'tsp' },
    { name: 'Freshiygroundblackpepper', amount: 0.25, unit: 'tsp' },
    { name: 'I In', amount: 2.0, unit: 'tbsp' },
    { name: 'Quartsaucepancombineon Garlicc basnandtomatoes.', amount: 1.0 },
  ],
  instructions: [
    'In2% quart saucepan combine oil, garlic, basil and tomatoes.',
    'Cook over medium heat 25 to 35 minutes until tomatoes have released their juices and',
    'Add salt and black pepper to taste. You can puree sauce in blender, or serve it as is.',
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
