import { useState } from 'react'
import api from '@/lib/api'

export function usePush(url, defaultMethod = 'post') {
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  async function push(payload, method = defaultMethod, config = {}) {
    setIsLoading(true);
    setError(null);
    try {
      const response = await api[method](url, payload, config);
      setData(response.data);
      return response.data;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }

  return {
    push,
    data,
    isLoading,
    error
  }
}