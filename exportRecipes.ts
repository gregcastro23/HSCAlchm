const { allRecipes } = require('./src/data/recipes/index');
const fs = require('fs');
fs.writeFileSync('recipes.json', JSON.stringify(allRecipes, null, 2));
console.log('Recipes exported to recipes.json'); 