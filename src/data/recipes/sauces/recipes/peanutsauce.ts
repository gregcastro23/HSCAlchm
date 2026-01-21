import { Recipe } from '../../../../types/recipe';

export const peanutsauce: Recipe = {
  name: 'Peanutsauce',
  description: 'A flavorful and versatile condiment to enhance and elevate your dishes.',
  ingredients: [
    { name: 'o.scuppeanuts Roasted 2tablespoonsnmejuice nime)', amount: 1.0 },
    { name: 'Cupwater Aateaspeoncayene', amount: 1.0 },
    { name: 'Itablespoonchoppedgarlicc nargeciove) Ea Cupcoconutmnk', amount: 1.0 },
    { name: 'Teaspoontamari Itablespoonmapiesyrup', amount: 1.0 },
    { name: 'Tsptoastedsesameon Seasaittotaste', amount: 1.0, unit: 'tbsp' },
    { name: 'Tspcoconutsugar', amount: 1.0, unit: 'cup' },
    { name: 'o.spureepeanutsandwaterinvitamixtopasteconsistency Add Garlicc Tamari Oil Sugar', amount: 1.0 },
    { name: 'Nmejuice Cayene Coconutmnk Andmapiesyrup Pureeuntilsmooth addsaittotaste.', amount: 1.0 },
    { name: 'Instituteofcunaryeducation Coursee 9b', amount: 1.0 },
    { name: 'o.sessonea Pouitry', amount: 1.0 },
  ],
  instructions: [
    'Combinecucumbers, limejuice, mint, water, andagaveinblender andpuree until',
    'Strainpureethroughsieve andserveinglasses withsliceoflime.',
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
