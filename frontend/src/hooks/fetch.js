import useSWR from 'swr'
import api from '@/lib/api';

const fetcher = (url) => api.get(url).then(res => res.data);

export function useFetch(url, options = {}) {
  const { data, error, isLoading, mutate } = useSWR(url, fetcher, options)

  return {
    data,
    error,
    isLoading,
    mutate
  }
}
