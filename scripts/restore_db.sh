#!/bin/bash

# 📌 [A.2.1] Verificar se o container está ativo
if ! docker ps | grep -q infra-db-1; then
    echo "❌ ERRO: Container 'infra-db-1' não está ativo ou não existe."
    exit 1
fi

# 📌 [A.2.2] Caminho para o diretório de backups
BACKUP_DIR="/Users/zmiguel/Backups/automaticos"

# 📌 [A.2.3] Listar os ficheiros disponíveis
echo "📂 Backups disponíveis em: $BACKUP_DIR"
ls -1 $BACKUP_DIR/*.dump || { echo "❌ ERRO: Nenhum ficheiro .dump encontrado."; exit 1; }

# 📌 [A.2.4] Solicitar nome do ficheiro ao utilizador
read -p "📝 Introduz o nome exato do ficheiro .dump a restaurar (ex: voiceguard_backup_2025-07-23_18-47-13.dump): " FILE

BACKUP_PATH="$BACKUP_DIR/$FILE"

# 📌 [A.2.5] Validar se o ficheiro existe
if [ ! -f "$BACKUP_PATH" ]; then
    echo "❌ ERRO: Ficheiro não encontrado: $BACKUP_PATH"
    exit 1
fi

# 📌 [A.2.6] Copiar o ficheiro para dentro do container
echo "⬆️ A copiar $FILE para o container..."
docker cp "$BACKUP_PATH" infra-db-1:/tmp/restore.dump

# 📌 [A.2.7] Executar o restauro dentro do container
echo "🔁 A restaurar a base de dados 'voiceguard_db'..."
docker exec -e PGPASSWORD=postgres infra-db-1 pg_restore -U voiceguard_user -d voiceguard_db --clean --if-exists /tmp/restore.dump

# 📌 [A.2.8] Limpar ficheiro temporário
docker exec infra-db-1 rm /tmp/restore.dump

# 📌 [A.2.9] Confirmação final
echo "✅ Restauro concluído com sucesso da cópia: $FILE"
