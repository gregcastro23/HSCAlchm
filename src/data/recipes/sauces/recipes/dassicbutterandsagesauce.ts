import { Recipe } from '../../../../types/recipe';

export const dassicbutterandsagesauce: Recipe = {
  name: 'Dassicbutterandsagesauce',
  description: 'A flavorful and versatile condiment to enhance and elevate your dishes.',
  ingredients: [
    { name: 'Istick Acup Butter', amount: 1.0 },
    { name: 'Handfuifreshsageieaves', amount: 0.25, unit: 'cup' },
  ],
  instructions: [
    'Heat butter until it browns slightly and add sage leaves.',
    'As soon as ravioli are cooked, remove them with slotted spoon, arrange on plates, pour',
    'Inblender, soak almonds in 1 cup hot water for at least 15 minutes. Process until smooth,',
    'In 2% quart sauce pan, sweat onion in oil with salt until completely soft. Add garlic and',
    'Add sweated vegetables and miso to almond milk. Process until very smooth, adding salt',
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
