#!/bin/bash

echo ">> Entrypoint executado!"
export MAGIC_LIBRARY=/usr/lib/aarch64-linux-gnu/libmagic.so.1
echo ">> MAGIC_LIBRARY definido como: $MAGIC_LIBRARY"

if [ "$#" -eq 0 ]; then
    echo ">> Nenhum comando fornecido. A iniciar Flask..."
    exec python3 /app/app.py
else
    echo ">> Comando detectado: $@"
    exec "$@"
fi
