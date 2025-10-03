import { Recipe } from '../../../types/recipe';

export const watermelonjuice: Recipe = {
  "name": "Watermelon Juice",
  "description": "A refreshing and hydrating summer drink packed with natural electrolytes.",
  "ingredients": [
    {
      "name": "watermelon",
      "amount": 6.0,
      "unit": "cup",
      "notes": "cubed",
      "swaps": []
    },
    {
      "name": "lime juice",
      "amount": 1.0,
      "unit": "tbsp",
      "notes": "",
      "swaps": []
    },
    {
      "name": "mint leaves",
      "amount": 0.25,
      "unit": "cup",
      "notes": "optional, for garnish",
      "swaps": []
    },
    {
      "name": "ice cubes",
      "amount": 2.0,
      "unit": "cup",
      "notes": "for serving",
      "swaps": []
    }
  ],
  "instructions": [
    "Remove rind from watermelon and cut into chunks.",
    "Place watermelon chunks in blender or food processor.",
    "Blend until smooth and liquefied.",
    "Strain if desired, then serve chilled."
  ],
  "nutrition": {
    "calories": 200,
    "protein": 8,
    "carbs": 25,
    "fat": 12,
    "vitamins": [
      "C",
      "K"
    ],
    "minerals": [
      "Potassium",
      "Iron"
    ]
  },
  "timeToMake": "30 minutes",
  "season": [
    "all"
  ],
  "cuisine": "HSCA",
  "mealType": [
    "Health Supportive"
  ],
  "elementalBalance": {
    "Fire": 0.25,
    "Earth": 0.25,
    "Water": 0.25,
    "Air": 0.25
  }
};
