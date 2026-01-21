import { Recipe } from '../../../../types/recipe';

export const brandade: Recipe = {
  name: 'Brandade',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'Ipoundrussetpotatoes Peeledandsliced Inchthick', amount: 1.0 },
    { name: 'o.seupmnk', amount: 1.0 },
    { name: 'Cupsheavycream', amount: 0.5, unit: 'cup' },
    { name: 'Ipoundsaitcod Soakedandrinsed', amount: 1.0 },
    { name: 'Gciovesgarlicc Roughiychopped', amount: 2.0, unit: 'medium' },
    { name: 'Cupolive oil', amount: 1.0 },
    { name: 'Juicefrom', amount: 1.0 },
    { name: 'Iemon Approximately', amount: 1.0 },
    { name: 'Tablespoons', amount: 1.0 },
    { name: 'Saitandblackpeppertotaste', amount: 1.0 },
    { name: 'Iwhoie Wheatbaguette Toasted', amount: 1.0 },
  ],
  instructions: [
    'Combine potatoes, milk, and cream in large sautoir. Bring mixture to scald, and simmer',
    'Insmall sauté pan, heat oil and garlic together. As soon as garlic begins to sizzle, remove',
    'Carefully strain potatoes and fish from milk/cream mixture and transfer to stand mixer',
    'Addin 1 cup of milk/cream mixture, garlic/oil mixture, and lemon juice. Mix until',
    'Season with salt and pepper. Serve on toasted baguette.',
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
