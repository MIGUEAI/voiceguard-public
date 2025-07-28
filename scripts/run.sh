#!/bin/bash
# Script para iniciar a aplicação Flask via Docker Compose

cd /Users/zmiguel/Projetos/voiceguard/infra || exit 1

docker compose --env-file /Users/zmiguel/Projetos/voiceguard/infra/.env.example up --build
