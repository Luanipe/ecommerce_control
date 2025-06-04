import { useEffect } from 'react'
import { useRouter } from 'next/navigation'

export default function Home() {
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (token) {
      router.replace('/dashboard');
    } else {
      router.replace('/auth');
    }
  }, [router]);

  return null;
}