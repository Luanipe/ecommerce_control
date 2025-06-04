import Head from 'next/head';
import AuthForm from '@/components/auth-form';

export default function AuthPage() {
  return (
    <>
      <Head>
        <title>E-Commerce Control</title>
        <meta name='auth'></meta>
      </Head>

      <main className='min-h-screen flex items-center justify-center'>
        <AuthForm/>
      </main>
    </>
  );
}
