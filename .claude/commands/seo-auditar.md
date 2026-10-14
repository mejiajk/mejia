---
description: Audita una web inmobiliaria de Panamá y genera el plan de contenido SEO · E-E-A-T · AEO · GEO basado en tendencia y volumen
argument-hint: <dominio> [zonas separadas por coma]
allowed-tools: Bash(./scripts/dfs.sh:*), Bash(./scripts/saldo.sh:*), Bash(jq:*), Bash(mkdir:*), Bash(git:*), Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

Audita **$1** (zonas foco: `$2`, si vacío dedúcelas del sitio) siguiendo al pie de la letra `prompts/seo-auditoria-inmobiliaria-panama.md`.

Saldo actual de la cuenta:
!`./scripts/saldo.sh 2>&1 || echo "sin credenciales de DataForSEO en el entorno"`

Config del proyecto, si existe: !`cat configs/$1.yaml 2>/dev/null || echo "sin config — rellena las VARIABLES desde el sitio y dilo en CONTEXTO"`

## Reglas

- Lee primero el prompt completo y úsalo como especificación; no resumas fases.
- Cero invención: cada cifra sale de `./scripts/dfs.sh`; lo no obtenido va como `N/D` con causa.
- Resuelve `location_code` de Panamá con `/v3/serp/google/locations`; nunca de memoria.
- Afirmaciones legales/fiscales solo con fuente oficial y marcadas `verificar con abogado`. No inventes experiencia, reseñas, licencias ni autores.
- Si el saldo es cero o falla, para y dilo. Estima créditos antes de cada lote y respeta el `PRESUPUESTO` del prompt.

## Salida

Escribe el informe en `informes/$1-<fecha>.md` (crea la carpeta) con los entregables del prompt, y responde con un resumen de 6 líneas, los créditos gastados y la lista de insumos que el cliente debe aportar.
