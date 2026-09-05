# mejia

Prompts y utilidades SEO.

## Contenido

| Ruta | Descripción |
|---|---|
| [`prompts/seo-serp-ai-visibility.md`](prompts/seo-serp-ai-visibility.md) | Prompt profesional para DataForSEO + Claude: rank tracking en Google (orgánico, pack local, AI Overviews) y visibilidad en ChatGPT, Perplexity, Claude y Gemini, con log tail incremental y detección de frases ganadoras. |
| `logs/` | Destino por defecto del log append-only (`rank-log.jsonl`) que genera el prompt. |

## Uso rápido

1. Abre `prompts/seo-serp-ai-visibility.md` y rellena el bloque `VARIABLES`.
2. Pega desde `=== PROMPT ===` hasta `=== FIN DEL PROMPT ===` en Claude con el MCP de DataForSEO/OpenSEO conectado.
3. Para runs recurrentes, pega solo el bloque `MODO INCREMENTAL`.
