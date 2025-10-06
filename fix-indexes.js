const fs = require('fs');
const path = require('path');

// Function to extract export name from a recipe file
function getExportName(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    const match = content.match(/export const (\w+): Recipe =/);
    return match ? match[1] : null;
  } catch (error) {
    console.error(`Error reading ${filePath}:`, error.message);
    return null;
  }
}

// Function to generate index file for a category
function generateIndexFile(categoryPath) {
  const recipesDir = path.join(categoryPath, 'recipes');

  if (!fs.existsSync(recipesDir)) {
    console.log(`No recipes directory found for ${categoryPath}`);
    return;
  }

  const recipeFiles = fs.readdirSync(recipesDir)
    .filter(file => file.endsWith('.ts'))
    .sort();

  const imports = [];
  const exports = [];

  recipeFiles.forEach(file => {
    const filePath = path.join(recipesDir, file);
    const exportName = getExportName(filePath);

    if (exportName) {
      imports.push(`import { ${exportName} } from './recipes/${file}';`);
      exports.push(`  ${exportName},`);
    } else {
      console.log(`Could not find export name for ${file}`);
    }
  });

  const indexContent = `import { Recipe } from '../../../types/recipe';
${imports.join('\n')}

export const ${path.basename(categoryPath)}Recipes: Recipe[] = [
${exports.join('\n')}
];
`;

  const indexPath = path.join(categoryPath, 'index.ts');
  fs.writeFileSync(indexPath, indexContent);
  console.log(`Generated ${indexPath}`);
}

// Generate index files for all categories
const categories = [
  'appetizers', 'beverages', 'breakfast', 'condiments', 'desserts',
  'dinner', 'lunch', 'salads', 'sauces', 'sides', 'soups',
];

categories.forEach(category => {
  const categoryPath = path.join(__dirname, 'src/data/recipes', category);
  if (fs.existsSync(categoryPath)) {
    generateIndexFile(categoryPath);
  } else {
    console.log(`Category path not found: ${categoryPath}`);
  }
});

console.log('Done generating index files');
