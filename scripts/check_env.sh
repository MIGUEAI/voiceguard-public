#!/bin/bash

# ✅ check_env.sh — Verifica o ambiente VoiceGuard
set -euo pipefail

echo "🔍 Verificação do ambiente VoiceGuard"

# [1] Verificar se os containers estão a correr
echo "🧱 [1] Containers ativos:"
docker compose -f /Users/zmiguel/Projetos/voiceguard/infra/docker-compose.yml ps

# [2] Verificar se o volume voiceguard_pgdata existe
echo "💾 [2] Verificação do volume 'infra_pgdata':"
docker volume inspect infra_pgdata >/dev/null 2>&1 && echo "✅ Volume existe" || echo "❌ Volume NÃO encontrado"

# [3] Verificar se a base de dados voiceguard_db existe
echo "📦 [3] Verificação da base de dados:"
docker compose -f /Users/zmiguel/Projetos/voiceguard/infra/docker-compose.yml exec -T db psql -U postgres -tAc "SELECT 1 FROM pg_database WHERE datname='voiceguard_db'" | grep -q 1 \
  && echo "✅ voiceguard_db existe" \
  || echo "❌ voiceguard_db NÃO encontrada"

# [4] Verificar se a tabela uploaded_file existe
echo "📄 [4] Verificação da tabela uploaded_file:"
docker compose -f /Users/zmiguel/Projetos/voiceguard/infra/docker-compose.yml exec -T db psql -U postgres -d voiceguard_db -c "\dt" | grep -q uploaded_file \
  && echo "✅ Tabela uploaded_file existe" \
  || echo "❌ Tabela uploaded_file NÃO encontrada"

# [5] Verificar variável STORAGE_BACKEND no .env
echo "🔐 [5] Verificação do .env:"
if grep -q "^STORAGE_BACKEND=" /Users/zmiguel/Projetos/voiceguard/.env; then
  STORAGE=$(grep "^STORAGE_BACKEND=" /Users/zmiguel/Projetos/voiceguard/.env | cut -d '=' -f2)
  echo "✅ STORAGE_BACKEND definido como: $STORAGE"
else
  echo "❌ STORAGE_BACKEND não definido no .env"
fi

echo "✅ Verificação concluída."
