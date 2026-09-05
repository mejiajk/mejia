---
description: Ejecuta un run de rank tracking, escribe al log JSONL e imprime el LOG TAIL
argument-hint: <config> [--solo-serp | --con-llm]
allowed-tools: Bash(./scripts/dfs.sh:*), Bash(./scripts/saldo.sh:*), Bash(jq:*), Bash(tail:*), Bash(wc:*), Bash(sort:*), Bash(mkdir:*), Bash(git:*), Read, Write, Edit, Glob, Grep
---

Ejecuta el run de tracking de **$1**. Flags: `$2` (`--solo-serp` salta la fase de LLM; `--con-llm` la fuerza aunque no toque por calendario).

Config: @configs/$1.yaml

Saldo: !`./scripts/saldo.sh 2>&1 || echo "SIN CREDENCIALES — para aquí"`

Últimas líneas del log: !`tail -n 5 logs/*.jsonl 2>/dev/null | tail -20 || echo "log vacío — este es el primer run"`

## Reglas

- **Presupuesto primero.** Estima el coste antes de lanzar nada: keywords × dispositivos × endpoints. Si supera el `PRESUPUESTO` de la config, para y pregunta con la cifra calculada delante. Si el saldo es cero, para.
- **Parámetros congelados.** `LOCATION_CODE`, `IDIOMA`, `DISPOSITIVO` y `PROFUNDIDAD` salen de la config y no se tocan. Cambiar uno rompe la serie del log.
- **Lotes, no llamadas sueltas.** `task_post` con hasta 100 tareas por envío, luego `tasks_ready`, luego `task_get`. Nada de `live` keyword a keyword.
- **Append-only.** Añades líneas al log. Nunca reescribes ni corriges histórico.
- **`null`, no cero.** Un dato que no se pudo obtener es `null` con nota. Un cero es una medición.

## Pasos

1. **Lanza la SERP.** Construye el payload como array de tareas (`keyword`, `location_code`, `language_code`, `device`, `depth`, `load_async_ai_overview: true`) y envíalo a `/v3/serp/google/organic/task_post`. Espera con `tasks_ready` y recoge con `task_get/advanced/<id>`. Guarda el JSON crudo en `raw/<run_id>/` — si mañana cambia el parser, el dato sigue ahí.

2. **Extrae posición y contexto** con `jq`: `rank_absolute` del primer item orgánico cuyo dominio sea el de la config, la URL, el title y description que Google muestra, los `item_types` presentes en la SERP, y los tres primeros competidores. Marca canibalización si hay dos o más URLs propias en el top 20.

3. **AI Overview.** Del mismo resultado, saca si el bloque existe, si el dominio aparece entre las referencias, en qué orden, el pasaje citado y la lista completa de dominios citados. Calcula el solapamiento con el top 10 orgánico.

4. **Pack local** si `ES_LOCAL` es true: `/v3/serp/google/maps/task_post` y posición en el pack.

5. **LLMs** solo si toca (han pasado 7 días o se pasó `--con-llm`): cada prompt de `PROMPTS_LLM` tres veces por motor. Registra menciones/3 y citas con enlace/3 por separado, y calcula el Share of Model. Si el endpoint no está disponible en el plan, marca `metodo: "manual"` y sigue — no lo omitas en silencio.

6. **Escribe el log.** Una línea JSON por keyword y dispositivo en la ruta `RUTA_LOG`. `delta` sale de comparar con la última entrada de esa misma keyword y dispositivo en runs anteriores. En el primer run `pos_prev` y `delta` van `null`: sin línea base no hay comparación.

7. **Imprime el LOG TAIL**: SUBEN, BAJAN, ENTRAN, SALEN, línea de AI Overview, línea de Share of Model, alertas y una sola acción siguiente. Umbrales: crítica si cae ≥5 posiciones desde el top 10, sale del top 10, pierde una cita en AIO o el Share of Model baja más de un 20%; media si cae 3–4, entra un competidor nuevo al top 3 o hay canibalización.

8. **Commit** del log y del raw.

## Salida

Solo el bloque LOG TAIL, las alertas y la acción prioritaria. Si no hay ningún delta ≥3 ni alertas: `Sin cambios materiales` y la media de posición. Nada de narrar el proceso.
