#!/bin/bash

# 📌 [A.1.0] Verifica se o container está ativo
if ! docker ps | grep -q infra-db-1; then
    echo "❌ ERRO: Container 'infra-db-1' não está ativo ou não existe."
    exit 1
fi

# 📌 [A.1.1] Timestamp para o nome do ficheiro
DATE=$(date +"%Y-%m-%d_%H-%M-%S")

# 📌 [A.1.2] Diretório de destino dos backups
BACKUP_DIR="/Users/zmiguel/Backups/automaticos"

# 📌 [A.1.3] Verifica e cria o diretório, se necessário
if [ ! -d "$BACKUP_DIR" ]; then
    echo "📁 Diretório de backup não existe. A criar: $BACKUP_DIR"
    mkdir -p "$BACKUP_DIR"
else
    echo "✅ Diretório de backup já existe: $BACKUP_DIR"
fi

# 📌 [A.1.4] Caminho final para guardar o ficheiro
BACKUP_FILE="voiceguard_backup_$DATE.dump"
BACKUP_PATH="$BACKUP_DIR/$BACKUP_FILE"

# 📌 [A.1.5] Executa o dump dentro do container
echo "📦 A executar pg_dump dentro do container..."
docker exec infra-db-1 pg_dump -U voiceguard_user -F c -d voiceguard_db -f /tmp/backup.dump

# 📌 [A.1.6] Valida se o pg_dump foi bem-sucedido
if [ $? -ne 0 ]; then
    echo "❌ ERRO: Falha ao executar pg_dump no container."
    exit 1
fi

# 📌 [A.1.7] Copiar o ficheiro para o host
echo "⬇️ A copiar backup para: $BACKUP_PATH"
docker cp infra-db-1:/tmp/backup.dump "$BACKUP_PATH"

# 📌 [A.1.8] Remover ficheiro temporário do container
docker exec infra-db-1 rm /tmp/backup.dump

# 📌 [A.1.9] Verifica se o backup foi criado com sucesso
if [ -f "$BACKUP_PATH" ]; then
    echo "✅ Backup concluído com sucesso: $BACKUP_PATH"

    # 📌 [A.5.1] Manter apenas os 10 backups mais recentes
    ls -1t /Users/zmiguel/Backups/automaticos/voiceguard_backup_*.dump | tail -n +11 | xargs -I {} rm -- {}

else
    echo "❌ ERRO: Backup não foi criado no destino esperado."
    exit 1
fi
