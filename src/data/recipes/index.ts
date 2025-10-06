import { Recipe } from '../../types/recipe';

import { breakfastRecipes } from './breakfast';
import { appetizersRecipes } from './appetizers';
import { sidesRecipes } from './sides';
import { saucesRecipes } from './sauces';
import { dessertsRecipes } from './desserts';
import { saladsRecipes } from './salads';
import { beveragesRecipes } from './beverages';
import { condimentsRecipes } from './condiments';
import { soupsRecipes } from './soups';

export const allRecipes: Recipe[] = [
  ...breakfastRecipes,
  ...appetizersRecipes,
  ...sidesRecipes,
  ...saucesRecipes,
  ...dessertsRecipes,
  ...saladsRecipes,
  ...beveragesRecipes,
  ...condimentsRecipes,
  ...soupsRecipes
]; 