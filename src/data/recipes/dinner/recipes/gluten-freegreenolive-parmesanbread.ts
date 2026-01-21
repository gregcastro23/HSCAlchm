import { Recipe } from '../../../../types/recipe';

export const glutenFreegreenoliveParmesanbread: Recipe = {
  name: 'Gluten Freegreenolive Parmesanbread',
  description: 'Freshly baked goods with wholesome ingredients and amazing flavor.',
  ingredients: [
    { name: 'Iacupsgiuten Freefiourbiend seepreviousrecipe)', amount: 1.0 },
    { name: 'Itspbakingpowder', amount: 2.0, unit: 'tsp' },
    { name: 'Tspait', amount: 1.0 },
    { name: 'Teaspoonbakingsoda', amount: 1.0, unit: 'tsp' },
    { name: 'Iegg Nghtiybeaten', amount: 1.0 },
    { name: 'o.seupbuttermnk', amount: 1.0 },
    { name: 'Tablespoonsbutter Meited', amount: 1.0 },
    { name: 'Iacupgreenonves Haived', amount: 1.0 },
    { name: 'Iacupgratedparmesancheese', amount: 0.5, unit: 'cup' },
  ],
  instructions: [
    'Preheat oven to 325° F.',
    'Whisk together flour, baking powder, salt, and baking soda in one bowl.',
    'In separate bowl, whisk together egg, buttermilk and melted butter.',
    'Mix wet into dry until just combined. Add olives and parmesan.',
    'Pour batter into muffin molds.',
    'Bake for 30-45 minutes, or until toothpick inserted in bread comes out clean.',
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
