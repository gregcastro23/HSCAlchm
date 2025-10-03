export * from './breakfast';
export * from './lunch';
export * from './dinner';
export * from './appetizers';
export * from './sides';
export * from './sauces';
export * from './desserts';
export * from './salads';
export * from './beverages';
export * from './condiments';
export * from './soups';

import { Recipe } from '../../types/recipe';
import { breakfastRecipes } from './breakfast';
import { lunchRecipes } from './lunch';
import { dinnerRecipes } from './dinner';
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
  ...lunchRecipes,
  ...dinnerRecipes,
  ...appetizersRecipes,
  ...sidesRecipes,
  ...saucesRecipes,
  ...dessertsRecipes,
  ...saladsRecipes,
  ...beveragesRecipes,
  ...condimentsRecipes,
  ...soupsRecipes
]; 