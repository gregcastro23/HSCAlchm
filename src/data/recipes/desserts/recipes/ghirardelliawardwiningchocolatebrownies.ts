import { Recipe } from '../../../../types/recipe';

export const ghirardelliawardwiningchocolatebrownies: Recipe = {
  name: 'Ghirardelliawardwiningchocolatebrownies',
  description: 'A sweet and satisfying treat made with quality ingredients.',
  ingredients: [
    { name: 'eggs', amount: 4.0 },
  ],
  instructions: [
    'Preheat oven to 375° F (325° F in convection oven). Grease and flour 8 x 8-inch square',
    'Whisk eggs with sugar and vanilla; add melted butter.',
    'Whisk together dry ingredients (cocoa, flour, baking powder, and salt) and fold into egg',
    'Bake for 20 minutes or until toothpick inserted in middle of brownie comes out clean.',
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
