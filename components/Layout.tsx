import Link from 'next/link'

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="container">
      <nav className="navigation">
        <Link href="/">Home</Link>
        <Link href="/recipes/appetizers">Appetizers</Link>
        <Link href="/recipes/main">Main Dishes</Link>
        <Link href="/recipes/sides">Sides</Link>
        <Link href="/recipes/soups">Soups</Link>
        <Link href="/recipes/salads">Salads</Link>
        <Link href="/recipes/desserts">Desserts</Link>
        <Link href="/recipes/beverages">Beverages</Link>
        <Link href="/recipes/condiments">Condiments</Link>
      </nav>
      <main className="main-content">
        {children}
      </main>
      <style jsx>{`
        .container {
          display: flex;
          min-height: 100vh;
        }
        .navigation {
          width: 200px;
          padding: 20px;
          background: #f5f5f5;
          display: flex;
          flex-direction: column;
          gap: 10px;
        }
        .main-content {
          flex: 1;
          padding: 20px;
        }
      `}</style>
    </div>
  )
} 