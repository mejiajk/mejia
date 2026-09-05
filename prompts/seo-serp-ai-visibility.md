# Prompt profesional — Rank SERP + Visibilidad IA (DataForSEO × Claude)

Prompt operativo para auditar y rastrear posicionamiento en **Google (orgánico, pack local, AI Overviews)** y en **motores de respuesta (ChatGPT, Perplexity, Claude, Gemini)**, organizado por `[WEB]` y `[LOCALIZACIÓN]`, con **rank tracking**, **log tail** incremental y detección de **frases que mejor posicionan**.

> Cómo usar: rellena el bloque `VARIABLES`, pega todo desde `=== PROMPT ===` hasta el final en Claude (con MCP DataForSEO / OpenSEO conectado) y ejecuta. Para runs recurrentes, pega solo el bloque `MODO INCREMENTAL`.

---

## VARIABLES (rellenar antes de ejecutar)

```yaml
WEB:            "example.com"                 # dominio o URL objetivo
MARCA:          "Example"                     # nombre de marca + variantes/alias
LOCALIZACION:   "Madrid, Spain"               # ciudad, región o país
IDIOMA:         "es"                          # language_code ISO
DISPOSITIVO:    ["desktop", "mobile"]         # SERP se rastrea en ambos
NEGOCIO:        "SaaS de facturación para pymes"
ES_LOCAL:       true                          # true → activa Maps, local pack y grid geográfico
COMPETIDORES:   ["competidor1.com", "competidor2.com"]   # vacío = derivar de la SERP
KEYWORDS_SEED:  ["facturación electrónica", "programa de facturación pymes"]
PROFUNDIDAD:    100                           # depth SERP
TOP_N:          50                            # keywords a rastrear en el tracker
PRESUPUESTO:    2000                          # tope de créditos por run; parar y preguntar si se supera
RUTA_LOG:       "logs/rank-log.jsonl"
```

---

=== PROMPT ===

## 1. Rol

Actúas como **analista SEO técnico senior especializado en SERP tracking y GEO/AEO (Generative Engine Optimization)**. Trabajas con datos reales de la API de DataForSEO. Tu salida es un informe accionable, no una explicación teórica.

## 2. Objetivo

Para `[WEB]` en `[LOCALIZACIÓN]`, idioma `[IDIOMA]`:

1. Medir la **posición actual** en Google orgánico, pack local y AI Overviews.
2. Medir la **visibilidad en LLMs**: ChatGPT, Perplexity, Claude y Gemini — si la marca se menciona, se cita, con qué sentimiento y qué fuentes gana la cita.
3. Mantener un **log incremental** (`[RUTA_LOG]`) con una entrada por keyword y run, y presentar un **log tail** con los deltas del último run.
4. Identificar las **frases que mejor posicionan**: qué formulaciones concretas ganan posición, snippet, AI Overview y cita en LLM — y por qué.

## 3. Reglas de ejecución (no negociables)

- **Cero invención.** Toda cifra procede de una llamada a la API. Si un dato no se pudo obtener, escribe `N/D` y la causa. Nunca estimes una posición.
- **Trazabilidad.** Cada tabla lleva al pie: `endpoint · location_code · language_code · device · fecha_UTC`.
- **Idempotencia.** Fija siempre `location_code`, `language_code`, `device` y `depth`. Sin esos parámetros los datos no son comparables entre runs.
- **Coste.** Antes de lanzar lotes, estima créditos. Si un lote supera `[PRESUPUESTO]`, para y pide confirmación indicando el coste estimado.
- **Volumen sobre latencia.** Agrupa keywords en `task_post` por lotes de hasta 100 en vez de `live` una a una, salvo cuando necesites el resultado inmediato de una sola SERP.
- **AI Overviews:** no siempre se dispara. Registra explícitamente `ai_overview_presente: true/false` — la ausencia es un dato, no un error.
- **LLMs son no deterministas.** Toda consulta a un motor de respuesta se ejecuta **3 veces** y se reporta como `citas/3` (frecuencia), nunca como un sí/no binario.
- **Distingue mención de cita.** Mención = el nombre aparece en el texto. Cita = el dominio aparece como fuente enlazada. Son métricas separadas.

## 4. Fases

### Fase 0 — Resolución de localización y contexto

1. Resuelve `[LOCALIZACIÓN]` a `location_code` real vía el endpoint de localizaciones (`/v3/serp/google/locations`) o la herramienta MCP equivalente. **No uses códigos de memoria.**
2. Fija `language_code = [IDIOMA]`.
3. Comprueba indexación de las URLs clave (`/v3/on_page/instant_pages` o inspección de URLs) antes de diagnosticar cualquier caída de ranking: una página no indexada no es un problema de contenido.
4. Devuelve un bloque `CONTEXTO` con los parámetros congelados que usarán todas las fases siguientes.

### Fase 1 — Universo de keywords

1. Keywords ya posicionadas de `[WEB]` (`/v3/dataforseo_labs/google/ranked_keywords/live`).
2. Expansión desde `[KEYWORDS_SEED]` (`keyword_suggestions`, `keyword_ideas`, `related_keywords`).
3. Gap competitivo frente a `[COMPETIDORES]` (`domain_intersection`, `serp_competitors`).
4. Métricas: volumen, CPC, competencia, tendencia 12 meses.
5. Clasifica cada keyword por:
   - **Intención**: informacional / comercial / transaccional / navegacional / local.
   - **Formato**: pregunta, comparativa (`X vs Y`), alternativa (`alternativas a X`), how-to, definicional, "mejor/es", `[servicio] + [ciudad]`.
   - **Prioridad** = `volumen × probabilidad_de_ganar × valor_comercial`, donde `probabilidad_de_ganar` se estima con la posición actual y la fuerza de los dominios del top 10.
6. Salida: tabla priorizada. Marca las **`[TOP_N]`** que entran al rank tracker.

### Fase 2 — SERP Google (clásico)

Para cada keyword rastreada, en `desktop` y `mobile`:

| Campo | Fuente |
|---|---|
| `posicion_organica` | `rank_absolute` del primer resultado de `[WEB]` |
| `url_posicionada` | URL exacta que rankea |
| `titulo_serp` / `descripcion_serp` | lo que Google reescribe realmente |
| `elementos_serp` | featured snippet, PAA, vídeo, imágenes, shopping, sitelinks, pack local |
| `top_3_competidores` | dominio + posición |
| `pixel_depth` | profundidad en píxeles del resultado (canibalización por SERP features) |
| `canibalizacion` | ≥2 URLs propias en el top 20 para la misma keyword |

Si `ES_LOCAL = true`, añade: posición en el **pack local** y en Maps (`/v3/serp/google/maps/live/advanced`, `local_finder`), y un **grid geográfico** alrededor de `[LOCALIZACIÓN]` (mínimo 5×5) con la posición media por punto.

### Fase 3 — AI Overviews

Solicita el AI Overview de forma explícita (`load_async_ai_overview: true` en `/v3/serp/google/organic/live/advanced`; complementa con el endpoint de AI Mode cuando aplique). Por keyword registra:

- `ai_overview_presente`: sí/no.
- `marca_citada`: ¿aparece `[WEB]` entre las fuentes?
- `posicion_cita`: orden dentro de las fuentes citadas.
- `dominios_citados`: lista completa — es tu verdadero conjunto de competidores en IA.
- `fragmento_citado`: el pasaje concreto que la IA extrajo.
- `solapamiento_top10`: % de fuentes del AI Overview que también están en el top 10 orgánico. Un solapamiento bajo significa que rankear no basta: hay que trabajar la extractabilidad.

### Fase 4 — Visibilidad en LLMs (ChatGPT · Perplexity · Claude · Gemini)

Construye **prompts de usuario reales**, no keywords. Mínimo 15, distribuidos así:

| Tipo | Plantilla |
|---|---|
| Categoría | `¿Cuál es el mejor [CATEGORÍA] para [PERFIL DE CLIENTE]?` |
| Local | `Mejor [SERVICIO] en [LOCALIZACIÓN]` |
| Comparativa | `[MARCA] vs [COMPETIDOR]: ¿cuál conviene?` |
| Alternativas | `Alternativas a [COMPETIDOR]` |
| Problema | `¿Cómo resuelvo [DOLOR DEL CLIENTE]?` |
| Marca directa | `¿Qué es [MARCA] y para quién sirve?` |
| Precio | `¿Cuánto cuesta [SERVICIO] en [LOCALIZACIÓN]?` |

Ejecuta cada prompt **3 veces por motor** (endpoints `/v3/ai_optimization/{chat_gpt|perplexity|claude|gemini}/llm_responses/live` o la herramienta MCP disponible). Verifica los nombres de endpoint contra la documentación vigente antes del primer run; si un motor no está disponible en tu plan, márcalo `N/D` en vez de omitirlo.

Registra por prompt y motor:

- `mencion` (0–3), `cita_con_enlace` (0–3), `posicion_en_respuesta` (1º, medio, último), `sentimiento` (positivo/neutro/negativo), `competidores_mencionados`, `fuentes_citadas`.
- **`Share of Model` = menciones de la marca ÷ menciones totales de marcas de la categoría.** Es la métrica cabecera de esta fase.

Si no hay acceso a la API de LLMs, ejecútalo manualmente con los mismos prompts y marca `metodo: manual` en el log. La metodología no cambia.

### Fase 5 — Frases que mejor posicionan

Cruza Fases 2–4 y responde con evidencia, no con intuición:

1. **Frases ganadoras propias.** Las 20 consultas donde `[WEB]` está en top 5 **o** citada en AI Overview/LLM. Extrae el patrón lingüístico común: longitud, modificadores (`mejor`, `barato`, `cerca de mí`, `para pymes`, `2026`), formato pregunta vs. nominal, presencia de la ciudad.
2. **Frases ganadoras ajenas.** Frases exactas que los dominios citados por la IA usan y `[WEB]` no. Cita el pasaje literal que fue extraído.
3. **Anatomía del pasaje citable.** De cada fragmento que la IA extrajo, mide: nº de palabras, si responde en la primera frase, si es lista o tabla, si incluye cifra o fecha, si va bajo un H2 en forma de pregunta.
4. **Entrega 15 frases reescritas listas para publicar**, cada una con: keyword objetivo, URL destino, posición exacta donde insertarla (H2 / primer párrafo / FAQ) y motivo del cambio.
5. **Quick wins**: keywords en posiciones 4–15 con volumen relevante — el mayor retorno por esfuerzo.

Fórmula de score por frase:

```
score = (0.30 × oportunidad_posicion)   # 1 - (posicion/100), 0 si no rankea
      + (0.25 × volumen_normalizado)
      + (0.20 × presencia_ai_overview)  # 1 si la marca se cita, 0.5 si el AIO existe sin cita
      + (0.15 × share_of_model)
      + (0.10 × valor_comercial)        # intención transaccional = 1
```

### Fase 6 — Log tail

Escribe **una línea JSON por keyword y run** (append-only, nunca reescribas histórico) en `[RUTA_LOG]`:

```json
{"run_id":"2026-09-05T06:00Z","web":"example.com","loc":"Madrid, Spain","location_code":1005493,"lang":"es","device":"mobile","keyword":"programa de facturación pymes","pos":7,"pos_prev":11,"delta":4,"url":"https://example.com/facturacion","volumen":2400,"serp_features":["paa","ai_overview"],"aio_presente":true,"aio_citada":false,"llm":{"chatgpt":2,"perplexity":3,"claude":1,"gemini":0},"share_of_model":0.18,"score":0.62,"fuente":"dataforseo/serp/google/organic","metodo":"api"}
```

Al final de **cada** run imprime el bloque `LOG TAIL`:

```
LOG TAIL · run 2026-09-05T06:00Z · example.com · Madrid, Spain · mobile
────────────────────────────────────────────────────────────────
SUBEN     ▲ 4  programa de facturación pymes      11 → 7
          ▲ 3  facturación electrónica autónomos  14 → 11
BAJAN     ▼ 5  software facturación               6  → 11   ⚠ salida del top 10
ENTRAN    ✚    facturación pymes madrid           —  → 18
SALEN     ✖    mejor programa facturas            22 → —
AI OVERVIEW   presente en 12/50 · marca citada en 2 (16.7%)  ▲ +1
SHARE OF MODEL  ChatGPT 0.21 ▲ · Perplexity 0.34 ▲ · Claude 0.12 ▬ · Gemini 0.05 ▼
────────────────────────────────────────────────────────────────
ALERTAS: 1 crítica · 2 medias
SIGUIENTE ACCIÓN: [una sola acción, la de mayor impacto]
```

Comandos de consulta del log:

```bash
tail -n 50 logs/rank-log.jsonl | jq -c '{k:.keyword,p:.pos,d:.delta}'
jq -s 'group_by(.run_id) | map({run:.[0].run_id, media:(map(.pos)|add/length)})' logs/rank-log.jsonl
jq 'select(.delta <= -5)' logs/rank-log.jsonl          # caídas fuertes
jq 'select(.aio_presente and (.aio_citada|not))' logs/rank-log.jsonl   # AIO sin cita = oportunidad
```

**Umbrales de alerta:**

| Nivel | Condición |
|---|---|
| 🔴 Crítica | caída ≥5 posiciones en keyword de top 10 · salida del top 10 · pérdida de cita en AI Overview · caída >20% del Share of Model |
| 🟠 Media | caída 3–4 posiciones · nuevo competidor en top 3 · canibalización detectada |
| 🟢 Info | subidas, entradas nuevas, nuevas citas ganadas |

## 5. Entregables

1. `CONTEXTO` — parámetros congelados del run.
2. `RESUMEN EJECUTIVO` — 5 líneas: estado, cambio vs. run anterior, mayor riesgo, mayor oportunidad, acción única prioritaria.
3. `TABLA SERP` — por keyword × dispositivo.
4. `TABLA AI OVERVIEW` — presencia, cita, dominios que ganan la cita.
5. `TABLA LLM` — matriz prompt × motor con menciones/3 y citas/3 + Share of Model.
6. `FRASES GANADORAS` — 15 frases reescritas con URL y ubicación exacta.
7. `LOG TAIL` — bloque anterior.
8. `PLAN 30 DÍAS` — máximo 10 acciones, ordenadas por `impacto ÷ esfuerzo`, con responsable y métrica de verificación.

Formato: tablas markdown, cifras con su fecha, sin adjetivos vacíos. Si un dato falta, dilo.

## 6. Cadencia

| Frecuencia | Qué |
|---|---|
| Diaria | Rank tracking `[TOP_N]` + log tail |
| Semanal | AI Overviews + Share of Model en LLMs |
| Mensual | Universo de keywords, gap competitivo, auditoría técnica |
| Trimestral | Revisión de arquitectura de contenidos y clusters |

=== FIN DEL PROMPT ===

---

## MODO INCREMENTAL (runs recurrentes — pegar solo esto)

```
Ejecuta el run de tracking de [WEB] en [LOCALIZACIÓN] con los parámetros congelados del bloque CONTEXTO.
No repitas las fases 0, 1 ni 5 completas.
1. Refresca la SERP de las [TOP_N] keywords (desktop + mobile).
2. Refresca presencia y citas en AI Overview.
3. Refresca Share of Model si han pasado ≥7 días desde la última medición; si no, arrastra el valor anterior marcándolo como "sin refrescar".
4. Añade las líneas nuevas a [RUTA_LOG] — no reescribas histórico.
5. Imprime únicamente: LOG TAIL + ALERTAS + la acción prioritaria.
Si no hay cambios materiales (ningún delta ≥3 y ninguna alerta), responde solo: "Sin cambios materiales" + la media de posición.
```

---

## Mapa de endpoints DataForSEO ↔ herramientas MCP

Verifica rutas y disponibilidad contra la documentación vigente antes del primer run; los nombres de endpoint cambian entre versiones y no todos entran en todos los planes.

| Necesidad | Endpoint DataForSEO | Herramienta MCP equivalente |
|---|---|---|
| Resolver localización | `/v3/serp/google/locations` | — (parámetro de las demás) |
| SERP orgánica + AI Overview | `/v3/serp/google/organic/live/advanced` (`load_async_ai_overview: true`) | `get_serp_results` |
| SERP local / pack | `/v3/serp/google/maps/live/advanced`, `/local_finder/` | `get_local_serp_results` |
| Grid geográfico | (composición de SERP local por coordenadas) | `get_local_rank_grid` |
| Keywords posicionadas | `/v3/dataforseo_labs/google/ranked_keywords/live` | `get_ranked_keywords` |
| Investigación de keywords | `/v3/dataforseo_labs/google/keyword_suggestions/live`, `/keyword_ideas/` | `research_keywords`, `get_domain_keyword_suggestions` |
| Volumen y CPC | `/v3/keywords_data/google_ads/search_volume/live` | `get_keyword_metrics` |
| Competidores SERP | `/v3/dataforseo_labs/google/serp_competitors/live` | `find_serp_competitors` |
| Rank tracker persistente | (tareas SERP programadas) | `create_rank_tracker`, `add_rank_tracking_keywords`, `run_rank_tracker`, `get_rank_tracker` |
| Respuestas de LLM | `/v3/ai_optimization/{chat_gpt\|claude\|perplexity\|gemini}/llm_responses/live` | — (ejecutar manual si no disponible) |
| Volumen de búsqueda en IA | `/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live` | — |
| Auditoría técnica | `/v3/on_page/task_post`, `/v3/on_page/instant_pages` | `run_site_audit`, `get_audit_issues`, `get_audit_pages` |
| Indexación | Google Search Console URL Inspection | `inspect_urls` |
| Rendimiento real | GSC / GA4 | `get_search_console_performance`, `get_google_analytics_organic_overview` |
| Backlinks | `/v3/backlinks/summary/live` | `get_backlinks_overview`, `get_backlinks_profile` |
| Ficha de Google Business | — | `get_business_profile`, `get_business_reviews` |

## Notas de método

- **AI Overview ≠ top 10.** La cita en AIO depende de la extractabilidad del pasaje (respuesta directa en ≤60 palabras bajo un H2 en forma de pregunta), no solo de la posición. Mide siempre el `solapamiento_top10`.
- **Los LLMs no se rastrean, se muestrean.** Tres ejecuciones es el mínimo estadístico útil; con presupuesto, sube a cinco y reporta la desviación.
- **Un `location_code` distinto invalida la serie histórica.** Congélalo en el bloque `CONTEXTO` y no lo cambies sin abrir un log nuevo.
- **La ausencia de datos es un dato.** `N/D` con causa siempre gana a una estimación plausible.
