import { Recipe } from '../../../../types/recipe';

export const glutenFreeandveganwaffles: Recipe = {
  name: 'Gluten Freeandveganwaffles',
  description: 'A nourishing morning meal to start your day with energy and flavor.',
  ingredients: [
    { name: 'Icupshigh Proteimgiuten Freefiourmix recipebeiow)', amount: 1.0 },
    { name: 'Tspbakingpowder', amount: 2.0, unit: 'tsp' },
    { name: 'Iatspeasait', amount: 0.125, unit: 'tsp' },
    { name: 'Tablespoonsmapiecrystais', amount: 1.0 },
    { name: 'Iateaspoongroundcinamen', amount: 0.5, unit: 'tsp' },
    { name: 'Tablespoonsmeitedon', amount: 1.0 },
    { name: 'Iateaspoonvaniaextract', amount: 0.5, unit: 'tsp' },
    { name: 'Ieupaimondmnk', amount: 1.0, unit: 'cup', notes: 'plus more for serving' },
    { name: 'Eacupaquafaba fromcanedchickpeas)', amount: 1.0 },
    { name: 'Smanamountofontobrushorsprayontowaftieiron', amount: 1.0 },
  ],
  instructions: [
    'Pre-heat waffle iron.',
    'In large bow] whisk together flours, baking powder, salt, maple crystals, and cinnamon.',
    'In separate bowl, whisk oil, vanilla extract, and almond milk.',
    'In stand mixer, beat aqua faba until stiff peaks are achieved; fold into batter until barely',
    'Lightly grease waffle iron. For each waffle pour about 4-% cup batter onto griddle.',
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
