#!/usr/bin/env bash
# dfs.sh — cliente mínimo de DataForSEO para usar desde Claude Code.
#
#   ./scripts/dfs.sh GET  /v3/serp/google/locations/pa
#   ./scripts/dfs.sh POST /v3/serp/google/organic/task_post payload.json
#
# Credenciales por entorno, nunca en el repo:
#   export DATAFORSEO_LOGIN="tu@email"
#   export DATAFORSEO_PASSWORD="tu_password_de_api"
set -euo pipefail

: "${DATAFORSEO_LOGIN:?falta DATAFORSEO_LOGIN en el entorno}"
: "${DATAFORSEO_PASSWORD:?falta DATAFORSEO_PASSWORD en el entorno}"

BASE="https://api.dataforseo.com"
METHOD="${1:?uso: dfs.sh <GET|POST> <endpoint> [payload.json]}"
ENDPOINT="${2:?falta el endpoint}"
PAYLOAD="${3:-}"

case "$METHOD" in
  GET)
    curl -sS --fail-with-body --max-time 120 \
      -u "$DATAFORSEO_LOGIN:$DATAFORSEO_PASSWORD" \
      "$BASE$ENDPOINT"
    ;;
  POST)
    [ -n "$PAYLOAD" ] || { echo "POST requiere un archivo de payload" >&2; exit 2; }
    [ -f "$PAYLOAD" ] || { echo "no existe el payload: $PAYLOAD" >&2; exit 2; }
    curl -sS --fail-with-body --max-time 300 \
      -u "$DATAFORSEO_LOGIN:$DATAFORSEO_PASSWORD" \
      -H "Content-Type: application/json" \
      -X POST "$BASE$ENDPOINT" \
      -d @"$PAYLOAD"
    ;;
  *)
    echo "método no soportado: $METHOD (usa GET o POST)" >&2; exit 2
    ;;
esac
