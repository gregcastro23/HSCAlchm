import { Recipe } from '../../../types/recipe';

export const beetandapplejuice: Recipe = {
  "name": "Beet and Apple Juice",
  "description": "A vibrant, earthy juice that supports liver function and blood building.",
  "ingredients": [
    {
      "name": "beets",
      "amount": 2.0,
      "unit": "medium",
      "notes": "peeled and quartered",
      "swaps": []
    },
    {
      "name": "apples",
      "amount": 2.0,
      "unit": "unit",
      "notes": "cored and quartered",
      "swaps": []
    },
    {
      "name": "carrots",
      "amount": 2.0,
      "unit": "large",
      "notes": "",
      "swaps": []
    },
    {
      "name": "ginger",
      "amount": 1.0,
      "unit": "inch",
      "notes": "",
      "swaps": []
    },
    {
      "name": "lemon",
      "amount": 0.5,
      "unit": "unit",
      "notes": "peeled",
      "swaps": []
    }
  ],
  "instructions": [
    "Wash beets and apples thoroughly.",
    "Cut ingredients into pieces suitable for juicer.",
    "Process through juicer, alternating between beets and apples.",
    "Serve immediately or chill for later consumption."
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
