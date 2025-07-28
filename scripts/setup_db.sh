#!/bin/bash
# Script para criar o banco de dados PostgreSQL (se necessário)

cd "$(dirname "$0")/../infra"
docker-compose exec db psql -U voiceguard_user -c "CREATE DATABASE voiceguard_db;"
