#!/usr/bin/env python3
import os
from pathlib import Path
from dotenv import load_dotenv

# Caminho absoluto para o .env
env_path = Path("/Users/zmiguel/Projetos/voiceguard/.env")

if not env_path.exists():
    print("❌ ERRO: Ficheiro .env não encontrado.")
    exit(1)

# Carregar variáveis
load_dotenv(dotenv_path=env_path)

# Chaves obrigatórias
required = ["SECRET_KEY", "JWT_SECRET_KEY", "DATABASE_URL"]

missing = [k for k in required if not os.getenv(k)]

if missing:
    print(f"❌ ERRO: Variáveis em falta: {', '.join(missing)}")
    exit(1)

print("✅ Todas as variáveis .env essenciais estão presentes.")
