import { Recipe } from '../../../../types/recipe';

export const grilledseitan: Recipe = {
  name: 'Grilledseitan',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'cutintosix2 Ouncesiabs reservenquidfrompackage)', amount: 1.0 },
    { name: 'Teaspoongroundcumin', amount: 1.0, unit: 'tsp' },
    { name: 'Teaspoonpaprika', amount: 1.0 },
    { name: 'Teaspoongarliccpowder', amount: 1.0 },
    { name: 'Etablespoonsextra virgin olive oil', amount: 2.0, unit: 'tbsp' },
    { name: 'Pinchseasait', amount: 0.125, unit: 'tsp' },
    { name: 'o.srecipechimichurrisauce recipefonowing)', amount: 1.0 },
    { name: 'Cumin Paprika Garliccpowder', amount: 1.0 },
    { name: 'Olive oil Andsait Marinatefor', amount: 1.0 },
    { name: 'eominutes.', amount: 1.0 },
  ],
  instructions: [
    'Combine seitan in medium bowl with liquid from package, cumin, paprika, garlic powder,',
    'Heat cast iron griddle. Grill seitan on each side until grill marks form. Return seitan to',
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
