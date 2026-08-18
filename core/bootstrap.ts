import { OllamaAdapter } from '../OllamaAdapter';

export interface AppDependencies {
  ollama: OllamaAdapter;
  productName: 'ScholarEgine';
  systemName: 'GODSPEED';
}

export function bootstrap(): AppDependencies {
  return {
    ollama: new OllamaAdapter(),
    productName: 'ScholarEgine',
    systemName: 'GODSPEED',
  };
}
