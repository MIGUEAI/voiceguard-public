#!/bin/bash

# Caminho base do projeto
cd /Users/zmiguel/Projetos/voiceguard || exit 1

# Ativar ambiente virtual
source venv/bin/activate

# Variáveis de ambiente para testes
export ENV_FILE=".env.test"
export PYTHONPATH=/Users/zmiguel/Projetos/voiceguard:$PYTHONPATH

# Criar base de dados de teste (se necessário)
python init_db.py

# Executar testes
pytest tests

