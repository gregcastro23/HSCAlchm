import { Recipe } from '../../../../types/recipe';

export const richalmondmilkForalmondfruittart: Recipe = {
  name: 'Richalmondmilk foralmondfruittart)',
  description: 'A delicious and nutritious dish made with quality ingredients.',
  ingredients: [
    { name: 'Icupsbianchedaimonds', amount: 4.0, unit: 'cups' },
    { name: 'Ecupsboningwater', amount: 1.0 },
    { name: 'Ea Teaspeonvaniaextract', amount: 0.5, unit: 'tsp' },
  ],
  instructions: [
    'Combine almonds and water in blender or Vitamix. Process for a few minutes until well-',
    'Rinse piece of cheesecloth (double thickness) with cold water and wring thoroughly.',
    'Pour small amount of almond mixture through sieve or chinois lined with prepared',
    'Strain almond milk through sieve. Add vanilla.',
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
