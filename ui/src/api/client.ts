const BASE = '';  // proxied by Vite to http://localhost:8000

export type ApiRecord = Record<string, unknown>;

async function request<T>(url: string, options?: RequestInit): Promise<T> {
  const res = await fetch(url, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  });
  if (!res.ok) {
    const text = await res.text().catch(() => res.statusText);
    throw new Error(`${res.status}: ${text}`);
  }
  if (res.status === 204) return undefined as T;
  return res.json();
}

export const api = {
  list(path: string, params?: Record<string, string>): Promise<ApiRecord[]> {
    const url = params
      ? `${BASE}${path}?${new URLSearchParams(params)}`
      : `${BASE}${path}`;
    return request<ApiRecord[]>(url);
  },

  getOne(path: string, id: string): Promise<ApiRecord> {
    return request<ApiRecord>(`${BASE}${path}/${id}`);
  },

  create(path: string, data: ApiRecord): Promise<ApiRecord> {
    return request<ApiRecord>(`${BASE}${path}`, {
      method: 'POST',
      body: JSON.stringify(data),
    });
  },

  update(path: string, id: string, data: ApiRecord): Promise<ApiRecord> {
    return request<ApiRecord>(`${BASE}${path}/${id}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  },

  remove(path: string, id: string): Promise<void> {
    return request<void>(`${BASE}${path}/${id}`, { method: 'DELETE' });
  },
};
