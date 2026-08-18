import { describe, expect, it, vi } from 'vitest';
import { OllamaAdapter } from '../OllamaAdapter';

describe('OllamaAdapter', () => {
  it('lists models from the configured tags endpoint', async () => {
    const fetcher = vi.fn().mockResolvedValue(new Response(JSON.stringify({ models: [{ name: 'llama3.2' }] }), { status: 200 }));
    const adapter = new OllamaAdapter('/api/ollama', fetcher as typeof fetch);

    await expect(adapter.listModels()).resolves.toEqual([{ name: 'llama3.2' }]);
    expect(fetcher).toHaveBeenCalledWith('/api/ollama/api/tags', expect.objectContaining({ method: 'GET' }));
  });

  it('sends chat messages and returns the generated message', async () => {
    const fetcher = vi.fn().mockResolvedValue(new Response(JSON.stringify({ message: { role: 'assistant', content: 'Hello' } }), { status: 200 }));
    const adapter = new OllamaAdapter('/api/ollama', fetcher as typeof fetch);

    await expect(adapter.chat({ model: 'llama3.2', messages: [{ role: 'user', content: 'Hi' }] })).resolves.toEqual({ role: 'assistant', content: 'Hello' });
    expect(fetcher).toHaveBeenCalledWith('/api/ollama/api/chat', expect.objectContaining({ method: 'POST' }));
  });

  it('fails closed on non-OK responses', async () => {
    const fetcher = vi.fn().mockResolvedValue(new Response('upstream failure', { status: 502 }));
    const adapter = new OllamaAdapter('/api/ollama', fetcher as typeof fetch);

    await expect(adapter.listModels()).rejects.toThrow('Ollama request failed: 502');
  });
});
