import { Recipe } from '../../../../types/recipe';

export const handmadegarlicmayonaise: Recipe = {
  name: 'Handmadegarlicmayonaise',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Iteaspoonmincedgarlicc 2cioves)', amount: 1.0 },
    { name: 'Tspeasait', amount: 0.125, unit: 'tsp' },
    { name: 'Eggyoiks Roomtemperature', amount: 1.0 },
    { name: 'Optionai Iateaspoondijon Typemustard', amount: 1.0 },
    { name: 'Troybrandturkisholive oilorspectrumbrandcanfomian', amount: 1.0 },
    { name: 'olive oil)', amount: 10.0, unit: 'oz' },
    { name: 'Ia 2tspiemonjuice', amount: 2.0, unit: 'tbsp', notes: 'freshly squeezed' },
    { name: 'o.ssmashgarliccwithsaittopasteoncuttingboard.', amount: 1.0 },
  ],
  instructions: [
    'Smash garlic with salt to paste on cutting board.',
    'Put garlic paste in bow] together with egg yolks and mustard; whisk until smooth.',
    'Slowly add oil (no more than one teaspoon at a time) to egg yolk mixture, whisking until',
    'As mixture begins to thicken, oil can be added somewhat more rapidly (no more than one',
    'When all oil has been incorporated, whisk in lemon juice.',
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
