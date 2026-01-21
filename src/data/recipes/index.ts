import { Recipe } from '../../types/recipe';
import { beveragesRecipes } from './beverages';
import { breakfastRecipes } from './breakfast';
import { dessertsRecipes } from './desserts';
import { dinnerRecipes } from './dinner';
import { lunchRecipes } from './lunch';
import { saladsRecipes } from './salads';
import { saucesRecipes } from './sauces';
import { sidesRecipes } from './sides';
import { soupsRecipes } from './soups';

export const allRecipes: Recipe[] = [
  ...beveragesRecipes,
  ...breakfastRecipes,
  ...dessertsRecipes,
  ...dinnerRecipes,
  ...lunchRecipes,
  ...saladsRecipes,
  ...saucesRecipes,
  ...sidesRecipes,
  ...soupsRecipes,
];
