# mejia

Herramienta de SEO para Claude Code: rastreo de posición en Google (orgánico, pack local, AI Overviews) y de visibilidad en motores de respuesta, con log incremental.

## Contenido

| Ruta | Descripción |
|---|---|
| [`prompts/seo-serp-ai-visibility.md`](prompts/seo-serp-ai-visibility.md) | Prompt largo, para pegar en cualquier Claude. Es la especificación del método. |
| `.claude/commands/seo-setup.md` | `/seo-setup` — da de alta un proyecto: resuelve `location_code`, investiga el sitio, escribe su config. |
| `.claude/commands/seo-run.md` | `/seo-run` — ejecuta el run, escribe al log e imprime el LOG TAIL. |
| `.claude/commands/seo-frases.md` | `/seo-frases` — analiza el log y devuelve las frases que mejor posicionan. |
| `scripts/dfs.sh` | Cliente mínimo de la API de DataForSEO (GET/POST con auth básica). |
| `scripts/saldo.sh` | Créditos restantes. Se ejecuta solo al abrir cada comando. |
| `configs/` | Una config YAML por proyecto. |
| `logs/` | Log append-only en JSONL, uno por serie. Fuera de git. |

## Puesta en marcha

```bash
export DATAFORSEO_LOGIN="tu@email"
export DATAFORSEO_PASSWORD="tu_password_de_api"   # el de la API, no el del panel
./scripts/saldo.sh                                # comprueba que responde
```

Luego, dentro de Claude Code en este repo:

```
/seo-setup glp.com.pa "Panama" es
/seo-run glp.com.pa
/seo-frases glp.com.pa
```

`/seo-run` es el que se repite a diario; los otros dos son puntuales.

## Notas

- Las credenciales van solo por entorno. `.env`, `logs/*.jsonl` y `raw/` están fuera de git.
- Cada comando comprueba el saldo antes de empezar y para si no llega.
- El primer run no tiene deltas: sin línea base no hay comparación. El log empieza a decir algo en el segundo.
