---
description: Da de alta un proyecto SEO — resuelve location_code, investiga el sitio y escribe su config
argument-hint: <dominio> <localización> [idioma]
allowed-tools: Bash(./scripts/dfs.sh:*), Bash(./scripts/saldo.sh:*), Bash(jq:*), Bash(mkdir:*), Bash(git:*), Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

Da de alta el proyecto **$1** en **$2** (idioma: `$3`, por defecto `es`).

Saldo actual de la cuenta:
!`./scripts/saldo.sh 2>&1 || echo "sin credenciales de DataForSEO en el entorno"`

Configs que ya existen: !`ls configs/ 2>/dev/null || echo "ninguna"`

## Reglas

- **Cero invención.** Cada cifra sale de una llamada real. Lo que no se pudo obtener va como `null` con una nota del motivo, nunca como estimación.
- **Presupuesto.** Si el saldo de arriba es cero o falla, para aquí y dilo — no montes payloads que no se van a poder ejecutar.
- **Sin credenciales en el repo.** Solo `DATAFORSEO_LOGIN` y `DATAFORSEO_PASSWORD` del entorno.

## Pasos

1. **Resuelve el `location_code`.** `./scripts/dfs.sh GET /v3/serp/google/locations` devuelve miles de filas: fíltralo con `jq` por `location_name`. Si el negocio es local usa el código de ciudad; si vende a todo el país, el de país. **Nunca escribas un código de memoria.** Guarda también el `language_code`.

2. **Entiende el negocio.** `WebFetch` sobre `https://$1` para sacar marca, alias, servicios, ciudades y el vocabulario real del sitio. Si el dominio no es alcanzable, dilo y tira de `WebSearch`, marcando en la config qué quedó sin verificar.

3. **Semillas.** 8–12 keywords que cubran intención transaccional, comercial, de marca e informacional. Salen del vocabulario del sitio, no de tu idea del sector.

4. **Competidores.** Déjalos `[]`. Los deriva `/seo-run` de la SERP real. Anota como comentario los candidatos que hayas visto, separando promotoras/competidores directos de agregadores y directorios — en muchos sectores el agregador es quien gana la SERP y la cita en IA.

5. **Escribe `configs/$1.yaml`** siguiendo el esquema de `prompts/seo-serp-ai-visibility.md`: `WEB`, `MARCA`, `MARCA_ALIAS`, `LOCALIZACION`, `LOCATION_CODE`, `IDIOMA`, `DISPOSITIVO`, `NEGOCIO`, `ES_LOCAL`, `COMPETIDORES`, `KEYWORDS_SEED`, `PROFUNDIDAD`, `TOP_N`, `PRESUPUESTO`, `RUTA_LOG`, `PROMPTS_LLM`. Si el sitio tiene otro idioma o mercado, añade una `SERIE_B` con su propio log.

6. **Prompts de LLM.** 10 preguntas que una persona real escribiría en ChatGPT antes de comprar, no keywords. Al menos una de categoría, una local, una de marca, una comparativa y una de precio.

7. **Crea el log vacío** en la ruta de `RUTA_LOG` y haz commit de la config con un mensaje que explique las decisiones, no solo el archivo.

## Salida

Un resumen corto: qué es el negocio, `location_code` resuelto, cuántas semillas, qué quedó sin verificar y qué cuesta aproximadamente el primer `/seo-run`.
