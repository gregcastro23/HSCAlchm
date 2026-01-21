import { Recipe } from '../../../../types/recipe';

export const panFriedpolentacakes: Recipe = {
  name: 'Pan Friedpolentacakes',
  description: 'A sweet and satisfying treat made with quality ingredients.',
  ingredients: [
    { name: 'o.srecipepoienta', amount: 1.0 },
    { name: 'Commeaifordredging', amount: 1.0 },
    { name: 'Notasteonforfrying', amount: 1.0 },
    { name: 'Nedhaif Sheettray Andspreadwithnghtiycned', amount: 1.0 },
    { name: 'Spatuiato', amount: 1.0 },
    { name: 'Inchthickness o.setsetuntilfirm Asminutesto', amount: 1.0 },
    { name: 'ihour.', amount: 1.0 },
  ],
  instructions: [
    'Pour hot polenta onto parchment-lined half-sheet tray, and spread with lightly oiled',
    'Cut into desired shapes using cookie cutters.',
    'Spread cornmeal on plate and dredge polenta. Prepare another plate with paper towel for',
    'Heat 4 inch oil in sauté pan, and fry polenta cakes over medium high heat until golden',
    'Drain on paper and serve hot.',
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
