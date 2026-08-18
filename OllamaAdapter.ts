export type ChatRole = 'system' | 'user' | 'assistant';

export interface ModelInfo {
  name: string;
  modified_at?: string;
  size?: number;
}

export interface ChatMessage {
  role: ChatRole;
  content: string;
}

export interface ChatRequest {
  model: string;
  messages: ChatMessage[];
  stream?: boolean;
}

export interface ChatResponse {
  role: 'assistant';
  content: string;
}

type FetchLike = typeof fetch;

interface TagsResponse {
  models?: ModelInfo[];
}

interface ChatApiResponse {
  message?: ChatResponse;
}

export class OllamaAdapter {
  constructor(private readonly baseUrl = '/api/ollama', private readonly fetcher: FetchLike = fetch) {}

  async listModels(): Promise<ModelInfo[]> {
    const response = await this.fetcher(`${this.baseUrl}/api/tags`, { method: 'GET' });
    return this.readJson<TagsResponse>(response).then((data) => data.models ?? []);
  }

  async chat(request: ChatRequest): Promise<ChatResponse> {
    const response = await this.fetcher(`${this.baseUrl}/api/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...request, stream: false }),
    });
    const data = await this.readJson<ChatApiResponse>(response);
    if (!data.message) {
      throw new Error('Ollama response did not contain a message');
    }
    return data.message;
  }

  private async readJson<T>(response: Response): Promise<T> {
    if (!response.ok) {
      throw new Error(`Ollama request failed: ${response.status}`);
    }
    return response.json() as Promise<T>;
  }
}
