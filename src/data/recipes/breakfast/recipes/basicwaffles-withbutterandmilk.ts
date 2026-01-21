import { Recipe } from '../../../../types/recipe';

export const basicwafflesWithbutterandmilk: Recipe = {
  name: 'Basicwaffles withbutterandmilk)',
  description: 'A nourishing morning meal to start your day with energy and flavor.',
  ingredients: [
    { name: 'Icupswhoiewheat Pastryfiour Sifted', amount: 1.0 },
    { name: 'Tspbakingpowder', amount: 2.0, unit: 'tsp' },
    { name: 'Itablespoonmapiecrystais', amount: 1.0 },
    { name: 'Eeggs Separated', amount: 1.0 },
    { name: 'Iacupmeitedbutter', amount: 1.0 },
    { name: 'Icupsorganicmnk', amount: 1.0 },
    { name: 'Iatspait Finelyground', amount: 1.0 },
    { name: 'Biueberrysyrup Forgamish recipebeiow)', amount: 1.0 },
    { name: 'Whisktogetherfiour Bakingpowder andmapiecrystais.', amount: 1.0 },
    { name: 'Beateggyoikswell Addbutter Mnk andsait.', amount: 1.0 },
  ],
  instructions: [
    'In large bowl, whisk together flour, baking powder, and maple crystals.',
    'In separate bowl, beat egg yolks well; add butter, milk, and salt.',
    'Make well in center of dry ingredients. Pour in liquid ingredients and combine with a few',
    'Beat egg whites until stiff, but not dry, fold into batter with rubber spatula just to',
    'Heat waffle iron. Ladle in 34 cups batter.',
    'Cook each waffle 4 minutes or until indicator light on machine goes on.',
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
