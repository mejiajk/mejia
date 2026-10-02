# Sistema de citaciones diarias para grounding

## Qué es (y qué no es)

Un pipeline que cada día recolecta fuentes públicas, **verifica** que la URL responde y que el fragmento aparece
literalmente en la página, y publica un dataset de ejemplos de grounding (afirmación + evidencia + fuente).

No "entrena" a ChatGPT, AI Overviews ni Perplexity: esos sistemas no aceptan citaciones enviadas desde fuera.
Lo que sí se obtiene: (1) un set de evaluación/ajuste para tus propios modelos y prompts RAG, y (2) un
banco de fuentes con fragmento citable, útil como referencia de qué formato de contenido se cita bien (ver GEO/AEO).

## Decisiones

| Pregunta | Elección | Por qué |
|---|---|---|
| Plataforma | Script Python (stdlib) + GitHub Actions | Sin costo por tarea (Zapier/Make cobran por operación), versionado, sin servidor, encaja con el repo |
| Fuentes | arXiv API (académico), RSS de medios (noticias), blogs de ingeniería (técnico), agencias/organismos (industria) | APIs/feeds abiertos, estables, sin scraping de buscadores ni Scholar (no tiene API y bloquea) |
| Frecuencia | 1×/día, 11:17 UTC | Los feeds no cambian lo bastante para más; evita la hora en punto |
| Destino | `citations/data/YYYY-MM-DD.jsonl` en git + digest `.md` + Slack opcional | JSONL = dataset; git = historial y auditoría; Slack = revisión humana |

## Flujo

```
configs/citations.json ─► 1 COLECTAR (arXiv / RSS por categoría)
                          2 FILTRAR  (antigüedad ≤ 14 d, no visto antes: dedupe por id de URL)
                          3 VERIFICAR(GET de la URL, HTTP 200, hash del contenido)
                          4 EXTRAER  (1-2 oraciones literales con cifras/entidades; sin boilerplate)
                          5 COMPROBAR(snippet ∈ texto descargado; si no, se descarta)
                          6 EMITIR   (JSONL + MD + Slack)
```

Garantía clave: el fragmento **nunca lo escribe un LLM**; se extrae del texto descargado. Así no hay citas inventadas.

## Esquema de cada citación

```json
{
  "id": "5d3442bca8ad",
  "url": "...", "title": "...", "domain": "...", "published": "2026-10-01",
  "snippet": "1-2 oraciones literales",
  "category": "academic|news|technical|industry",
  "citation": "Título. dominio, fecha. url",
  "verification": {"http_status": 200, "snippet_verbatim_in_page": true,
                   "content_sha256": "...", "retrieved_at": "..."},
  "grounding": {"evidence": "...", "source_id": "5d3442bca8ad",
                "answer_template": "Según {dominio} ({fecha}): {evidencia} [fuente: {url}]"}
}
```

Cómo usarlo como ejemplo de grounding: dale `evidence` al modelo como contexto, pídele una respuesta con cita,
y evalúa (a) que cite `url`, (b) que la afirmación esté soportada por `evidence`, (c) que no añada hechos ausentes.
`content_sha256` + `retrieved_at` permiten detectar cuándo la fuente cambió y el ejemplo caducó.

## Puesta en marcha

```bash
python3 scripts/citations.py --dry-run     # prueba local, no escribe
python3 scripts/citations.py               # escribe citations/data/<hoy>.*
```
En GitHub: añade el secreto `SLACK_WEBHOOK_URL` (opcional); el workflow `daily-citations` corre solo y también a mano.
Edita `configs/citations.json` para cambiar fuentes, cupo por categoría (`per_category`) o ventana de antigüedad.

## Límites conocidos

- Solo titular de feed + página: sitios con paywall o render por JS devuelven pocas oraciones y se descartan.
- Algunos feeds de `configs/citations.json` pueden cambiar de URL; una fuente caída se salta y se registra, no rompe el run.
- Falta (siguiente paso razonable): archivar cada URL en Wayback Machine, y un paso opcional con LLM que *redacte la pregunta*
  del ejemplo (el snippet seguiría siendo literal).
- Probado localmente con servidor de prueba (extracción, filtros, dedupe, enlaces rotos). **No se pudo probar contra los
  feeds reales**: la red del sandbox bloqueó esos dominios. Primer run real: `workflow_dispatch` y revisa el log.
