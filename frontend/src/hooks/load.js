import { useState } from 'react'
import api from '@/lib/api'

export function useLoad(url, config = {}) {
  const [data, setData] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)

  async function load() {
    setIsLoading(true)
    setError(null)
    try {
      const response = await api.get(url, config)
      setData(response.data)
      return response.data
    } catch (err) {
      setError(err)
      throw err
    } finally {
      setIsLoading(false)
    }
  }

  return {
    data,
    error,
    isLoading,
    load
  }
}