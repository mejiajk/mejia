---
description: Analiza el log y devuelve las frases que mejor posicionan, reescritas y listas para publicar
argument-hint: <config>
allowed-tools: Bash(jq:*), Bash(tail:*), Bash(sort:*), Bash(./scripts/dfs.sh:*), Read, Write, Edit, Glob, Grep, WebFetch
---

Analiza el histórico de **$1** y dime qué frases ganan.

Config: @configs/$1.yaml

Volumen de log disponible: !`wc -l logs/*.jsonl 2>/dev/null || echo "sin log — ejecuta /seo-run primero"`

## Reglas

- Esto **no lanza llamadas nuevas** a la API salvo que falte el pasaje citado de algún AI Overview. Trabaja sobre el log y el raw que ya están en disco.
- Cada afirmación se apoya en una línea del log o en un pasaje literal del raw. Si no puedes citar la evidencia, no lo escribas.
- Con menos de dos runs en el log, dilo: sin histórico no hay tendencia, solo una foto.

## Pasos

1. **Ganadoras propias.** Las 20 consultas donde el dominio está en top 5 o citado en AIO/LLM. Extrae el patrón común: longitud, modificadores (`mejor`, `cerca de mí`, `precio`, año), pregunta contra formulación nominal, presencia de ciudad, singular contra plural.

2. **Ganadoras ajenas.** Los dominios citados por la IA donde el nuestro no aparece. Recupera del raw el pasaje exacto que la IA extrajo de ellos y ponlo literal.

3. **Anatomía del pasaje citable.** De cada fragmento extraído: número de palabras, si responde en la primera frase, si es lista o tabla, si lleva cifra o fecha, si va bajo un H2 en forma de pregunta. Saca el promedio de los que sí ganan la cita.

4. **Score por frase**, con la fórmula de `prompts/seo-serp-ai-visibility.md`: 0.30 oportunidad de posición, 0.25 volumen normalizado, 0.20 presencia en AI Overview, 0.15 Share of Model, 0.10 valor comercial.

5. **Quick wins.** Keywords entre las posiciones 4 y 15 con volumen relevante, ordenadas por score.

6. **15 frases reescritas** listas para pegar, cada una con: keyword objetivo, URL destino, ubicación exacta (H2, primer párrafo o FAQ) y en una línea por qué esa formulación gana.

## Salida

Tres tablas — ganadoras propias, ganadoras ajenas, quick wins — y la lista de 15 frases. Guarda el informe en `informes/$1-frases-<fecha>.md` y haz commit.
