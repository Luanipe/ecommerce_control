import { useState } from 'react'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Label } from '@/components/ui/label'
import { usePush } from '@/hooks/push'
import { useRouter } from 'next/navigation'

export default function AuthForm() {
  const [mode, setMode] = useState('login')
  const [form, setForm] = useState({ email: '', password: '', name: '' });
  const { push, isLoading, error } = usePush();
  const router = useRouter();

  const isRegister = mode === 'register'

  async function handleSubmit(e) {
    e.preventDefault()
    try {
      const endpoint = isRegister ? '/auth/register' : '/auth/login';
      const payload = isRegister ? form : { email: form.email, password: form.password };

      const data = await push(endpoint, payload);
      localStorage.setItem('token', data.access_token);
      router.push('/');
    } catch (err) {
      console.error('Auth error:', err)
    }
  }

  return (
    <Card className="w-full max-w-md shadow-xl">
      <CardHeader>
        <CardTitle className="text-center">
          {isRegister ? 'Criar Conta' : 'Entrar'}
        </CardTitle>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-4">
          {isRegister && (
            <div>
              <Label htmlFor="name">Nome</Label>
              <Input
                id="name"
                value={form.name}
                onChange={(e) => setForm({ ...form, name: e.target.value })}
                required
              />
            </div>
          )}
          <div>
            <Label htmlFor="email">Email</Label>
            <Input
              id="email"
              type="email"
              value={form.email}
              onChange={(e) => setForm({ ...form, email: e.target.value })}
              required
            />
          </div>
          <div>
            <Label htmlFor="password">Senha</Label>
            <Input
              id="password"
              type="password"
              value={form.password}
              onChange={(e) => setForm({ ...form, password: e.target.value })}
              required
            />
          </div>
          <Button type="submit" className="w-full" disabled={isLoading}>
            {isLoading ? 'Processando...' : isRegister ? 'Cadastrar' : 'Entrar'}
          </Button>
          {error && <p className="text-sm text-red-500">Erro: {error.response?.data?.detail || 'Algo deu errado.'}</p>}
        </form>

        <div className="text-center mt-4 text-sm">
          {isRegister ? 'Já tem uma conta?' : 'Não tem uma conta?'}{' '}
          <button
            type="button"
            onClick={() => setMode(isRegister ? 'login' : 'register')}
            className="text-blue-600 hover:underline"
          >
            {isRegister ? 'Entrar' : 'Cadastrar'}
          </button>
        </div>
      </CardContent>
    </Card>
  )
}
