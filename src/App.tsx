import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import RecipesPage from './pages/recipes';
import RecipeDetails from './components/RecipeDetails';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/recipes" element={<RecipesPage />} />
        <Route path="/recipes/:recipeName" element={<RecipeDetails />} />
      </Routes>
    </Router>
  );
}

export default App; 