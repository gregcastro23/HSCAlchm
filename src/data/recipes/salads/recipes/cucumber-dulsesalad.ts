import { Recipe } from '../../../../types/recipe';

export const cucumberDulsesalad: Recipe = {
  name: 'Cucumber Dulsesalad',
  description: 'A fresh and vibrant salad featuring seasonal ingredients and crisp textures.',
  ingredients: [
    { name: 'Saiad', amount: 1.0 },
    { name: 'Ipoundkirbycucumbers', amount: 2.0 },
    { name: 'Tspeasait', amount: 0.125, unit: 'tsp' },
    { name: 'Ieoseiypacked', amount: 1.0 },
    { name: 'Dressing', amount: 2.0, unit: 'oz' },
    { name: 'Itablespoonricevinegar', amount: 1.0, unit: 'tbsp' },
    { name: 'Itablespoonmincedgarlicc nargeciove)', amount: 1.0 },
    { name: 'Itsptone Groundmustard', amount: 1.0, unit: 'tsp' },
    { name: 'Etablespoonsextra virgin olive oil', amount: 2.0, unit: 'tbsp' },
    { name: '0.5 Scoreskinofcucumbersaiongiengthwithpeeierorzester Sncethiniyintoroundsand', amount: 1.0 },
    { name: 'Sprinkiewithsait Setasidefor', amount: 1.0 },
    { name: 'Eominutes Rinse iftoosaity.', amount: 1.0 },
  ],
  instructions: [
    'Score skin of cucumbers along length with peeler or zester. Slice thinly into rounds and',
    'Quickly rinse dulse in bowl of cold water, until softened. Squeeze excess liquid out. Finely',
    'Combine dulse and cucumbers in medium bowl. Mix well.',
    'In small bowl, whisk, rice vinegar, garlic, and mustard. Slowly drizzle in olive oil and',
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
