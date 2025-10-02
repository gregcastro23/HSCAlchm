import Layout from '../components/Layout'
import { NextPage } from 'next'
import Head from 'next/head'

const Home: NextPage = () => {
  return (
    <Layout>
      <Head>
        <title>HSC Alchemy</title>
        <meta name="description" content="HSC Alchemy Recipe App" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <h1>Welcome to HSC Alchemy</h1>
      <p>Browse our collection of healthy recipes</p>
    </Layout>
  )
}

export default Home 