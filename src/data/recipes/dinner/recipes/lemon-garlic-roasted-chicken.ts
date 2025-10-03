import { Recipe } from '../../../../types/recipe';

export const lemongarlicroastedchicken: Recipe = {
    name: 'Lemon Garlic Roasted Chicken',
    description: 'Juicy and flavorful roasted chicken infused with lemon, garlic, and herbs.',
    ingredients: [
      { name: 'whole chicken', amount: 4, unit: 'lbs' },
      { name: 'lemons', amount: 2, unit: '' },
      { name: 'garlic cloves, minced', amount: 6, unit: '' },
      { name: 'olive oil', amount: 0.25, unit: 'cup' },
      { name: 'dried thyme', amount: 1, unit: 'tbsp' },
      { name: 'dried rosemary', amount: 1, unit: 'tbsp' },
      { name: 'salt', amount: 1, unit: 'tsp' },
      { name: 'black pepper', amount: 0.5, unit: 'tsp' }
    ],
    nutrition: {
      calories: 420,
      protein: 42,
      carbs: 4,
      fat: 28,
      vitamins: ['B6', 'B12', 'C'],
      minerals: ['Potassium', 'Selenium']
    },
    timeToMake: '90 minutes',
    season: ['all'],
    cuisine: 'HSCA',
    mealType: ['Entree'],
    elementalBalance: {
      Fire: 0.3,
      Earth: 0.4,
      Water: 0.2,
      Air: 0.1
    },
    instructions: [
      'Preheat oven to 425°F. Rinse chicken and pat dry with paper towels.',
      'Zest one lemon and juice both lemons. In a small bowl, combine lemon zest, lemon juice, minced garlic, olive oil, thyme, rosemary, salt, and pepper.',
      'Rub the lemon-garlic mixture all over the chicken, inside and out. Place the squeezed lemon halves inside the chicken cavity.',
      'Place chicken in a roasting pan, breast-side up. Tie legs together with kitchen twine.',
      'Roast chicken for 1 to 1 1/2 hours, until the juices run clear and the internal temperature of the thigh reaches 165°F.',
      'Remove from oven, cover loosely with foil, and let rest for 15 minutes before carving.',
      'Serve hot, garnished with fresh lemon slices and herbs if desired.'
    ]
  },;