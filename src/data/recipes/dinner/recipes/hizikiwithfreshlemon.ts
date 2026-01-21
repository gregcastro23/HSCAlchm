import { Recipe } from '../../../../types/recipe';

export const hizikiwithfreshlemon: Recipe = {
  name: 'Hizikiwithfreshlemon',
  description: 'A delicious and hearty dish ideal for evening meals.',
  ingredients: [
    { name: 'o.scupdriedhiziki Rinsedandsoakedis 2ominutes)', amount: 1.0 },
    { name: 'io.ssmantomediumonion Smandice', amount: 1.0 },
    { name: 'Tspsesameon', amount: 2.0, unit: 'tbsp' },
    { name: 'water', amount: 2.0, unit: 'cups' },
    { name: 'To', amount: 1.0 },
    { name: 'Etablespoonsshoyu', amount: 1.0 },
    { name: 'Cupfreshiemonjuice', amount: 2.0, unit: 'tbsp', notes: 'freshly squeezed' },
    { name: 'Gscanions Finelysliced', amount: 2.0, unit: 'cups' },
    { name: 'o.sdrainoffanyremainingsoakingwaterfromhizikianddiscard.', amount: 1.0 },
    { name: 'Inchpan Sauteonioninonfor', amount: 1.0 },
    { name: 'Etosminutes Addhiziki mixingwell.', amount: 1.0 },
  ],
  instructions: [
    'Drain off any remaining soaking water from hiziki and discard.',
    'In 10-inch pan, sauté onion in oil for 3 to 5 minutes. Add hiziki, mixing well.',
    'Add enough water to just barely cover hiziki. Add shoyu. Bring to boil. Cover, lower flame,',
    'Gently stir in scallions and lemon juice until well mixed. Serve.',
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
