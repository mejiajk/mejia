#!/usr/bin/env bash
# Créditos restantes en DataForSEO. Ejecutar antes de cualquier lote.
set -euo pipefail
cd "$(dirname "$0")/.."
./scripts/dfs.sh GET /v3/appendix/user_data \
  | jq -r '.tasks[0].result[0] | "saldo: \(.money.balance) \(.money.currency)  ·  límite diario: \(.money.limits.day)"'
