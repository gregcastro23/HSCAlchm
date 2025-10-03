import { Recipe } from '../../../../types/recipe';

export const mushroomConsomme: Recipe = {
  name: 'Mushroom Consommé',
  description: 'A clear, flavorful mushroom broth with deep umami notes.',
  ingredients: [
    { name: 'dried shiitake mushrooms', amount: 2, unit: 'oz' },
    { name: 'dried porcini mushrooms', amount: 1, unit: 'oz' },
    { name: 'kombu', amount: 2, unit: 'pieces' },
    { name: 'water', amount: 5, unit: 'quarts' },
    { name: 'onion', amount: 0.5, unit: 'pound', notes: '½ large, peeled and chopped' },
    { name: 'carrot', amount: 0.5, unit: 'pound', notes: '1 large, peeled and chopped' },
    { name: 'fennel bulb', amount: 1, unit: 'pound', notes: 'chopped' },
    { name: 'olive oil', amount: 1.25, unit: 'tbsp' },
    { name: 'tomatoes', amount: 1.5, unit: 'pounds', notes: 'seeded and chopped' },
    { name: 'garlic', amount: 8, unit: 'cloves', notes: 'sliced' },
    { name: 'button mushrooms', amount: 2, unit: 'pounds', notes: 'sliced' },
    { name: 'parsley stems', amount: 0.5, unit: 'oz' },
    { name: 'bay leaves', amount: 2, unit: '' }
  ],
  nutrition: {
    calories: 45,
    protein: 3,
    carbs: 7,
    fat: 1,
    vitamins: ['D', 'B'],
    minerals: ['Selenium', 'Copper']
  },
  timeToMake: '90 minutes',
  season: ['fall', 'winter'],
  cuisine: 'HSCA',
  mealType: ['Soup'],
  elementalBalance: {
    Fire: 0.2,
    Earth: 0.4,
    Water: 0.3,
    Air: 0.1
  },
  instructions: [
    'Combine dried mushrooms, kombu, and water in stockpot. Bring to simmer.',
    'Meanwhile, in separate pan, sauté onion, carrot, and fennel in olive oil until tender.',
    'Add tomatoes and garlic to vegetables and cook until tomatoes break down.',
    'Add button mushrooms and cook until they release their liquid.',
    'Add sautéed vegetables to stockpot with bouquet garni.',
    'Simmer for 45 minutes, strain, and serve hot.'
  ]
};
