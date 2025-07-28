#!/bin/bash

# 📌 [A.9.2.2.1] Cria timestamp
DATE=$(date +"%Y-%m-%d_%H-%M-%S")

# 📌 [A.9.2.2.2] Diretório de backups relativo ao projeto
BACKUP_DIR="./backups"

# 📌 [A.9.2.2.3] Criação da pasta se não existir
mkdir -p "$BACKUP_DIR"

# 📌 [A.9.2.2.4] Nome do ficheiro de backup
BACKUP_FILE="voiceguard_backup_$DATE.dump"
BACKUP_PATH="$BACKUP_DIR/$BACKUP_FILE"

# 📌 [A.9.2.2.5] Conteúdo simulado (pode ser substituído por pg_dump real)
echo "-- SIMULATED BACKUP for GitHub Actions at $DATE" > "$BACKUP_PATH"

# 📌 [A.9.2.2.6] Verificação final
if [ -f "$BACKUP_PATH" ]; then
    echo "✅ Backup simulado criado com sucesso: $BACKUP_PATH"
else
    echo "❌ ERRO: Backup simulado falhou."
    exit 1
fi
