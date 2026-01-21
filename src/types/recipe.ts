export type Unit = string;

export interface Ingredient {
  name: string;
  amount: number;
  unit?: Unit;
  notes?: string;
  swaps?: string[];
}

export interface Nutrition {
  calories: number;
  protein: number;
  carbs: number;
  fat: number;
  vitamins: string[];
  minerals: string[];
}

export interface ElementalBalance {
  Fire: number;
  Earth: number;
  Water: number;
  Air: number;
}

export interface Recipe {
  name: string;
  description: string;
  ingredients: Ingredient[];
  nutrition: Nutrition;
  timeToMake: string;
  season: string[];
  cuisine: string;
  mealType: string[];
  elementalBalance: ElementalBalance;
  instructions: string[];
}
