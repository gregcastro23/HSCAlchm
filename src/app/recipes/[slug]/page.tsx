import { notFound } from 'next/navigation';
import { allRecipes } from '../../../data/recipes/index';
import { Metadata } from 'next';
import RecipeDetail from '../../../components/RecipeDetail';

interface PageProps {
  params: Promise<{ slug: string }>
}

export async function generateStaticParams() {
  return allRecipes.map((recipe) => ({
    slug: recipe.name.toLowerCase().replace(/\s+/g, '-'),
  }));
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { slug } = await params;
  const recipe = allRecipes.find(
    r => r.name.toLowerCase().replace(/\s+/g, '-') === slug,
  );

  if (!recipe) {
    return {
      title: 'Recipe Not Found',
    };
  }

  return {
    title: `${recipe.name} | HSCAlchm Recipe Collection`,
    description: recipe.description,
  };
}

export default async function RecipePage({ params }: PageProps) {
  const { slug } = await params;
  const recipe = allRecipes.find(
    r => r.name.toLowerCase().replace(/\s+/g, '-') === slug,
  );

  if (!recipe) {
    notFound();
  }

  return <RecipeDetail recipe={recipe} />;
}
