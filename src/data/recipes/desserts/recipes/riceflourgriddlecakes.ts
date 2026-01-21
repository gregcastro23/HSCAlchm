import { Recipe } from '../../../../types/recipe';

export const riceflourgriddlecakes: Recipe = {
  name: 'Riceflourgriddlecakes',
  description: 'A sweet and satisfying treat made with quality ingredients.',
  ingredients: [
    { name: 'Eupsbrownricefiour', amount: 1.0, unit: 'tbsp' },
    { name: 'Itablespoon', amount: 1.0 },
    { name: 'Iatspbakingpowder', amount: 2.0, unit: 'tsp' },
    { name: 'Iaacupmapiecrystais', amount: 0.5, unit: 'cup' },
    { name: 'Iatspcinamon', amount: 1.0, unit: 'tsp' },
    { name: 'Teaspoonutmeg', amount: 0.25, unit: 'tsp' },
    { name: 'itspait.', amount: 1.0 },
    { name: 'Itablespoonfiaxseed Groundtofinemeai', amount: 1.0 },
    { name: 'Cupsaimondmnk', amount: 1.0, unit: 'cup', notes: 'plus more for serving' },
    { name: 'Tspcoconuton Meited', amount: 0.333, unit: 'cup' },
  ],
  instructions: [
    'Whisk together flour, baking powder, maple crystals, cinnamon, nutmeg, salt and ground',
    'Inblender combine almond milk, and butter or oil.',
    'Combine liquid ingredients and dry ingredients.',
    'Using 1-ounce ladle, pour batter onto griddle. Cook cakes until bubbles in batter break on',
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
