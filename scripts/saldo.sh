#!/usr/bin/env bash
# Créditos restantes en DataForSEO. Ejecutar antes de cualquier lote.
# La API no devuelve moneda (currency: null); DataForSEO factura en USD.
set -euo pipefail
cd "$(dirname "$0")/.."
./scripts/dfs.sh GET /v3/appendix/user_data \
  | jq -r '.tasks[0].result[0].money
           | "saldo: \(.balance) USD  ·  gastado hoy: \(.statistics.day.total // 0)  ·  límite diario: \(.limits.day.total)"'
