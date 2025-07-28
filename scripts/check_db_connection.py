#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Carregar variáveis de ambiente do .env
load_dotenv(dotenv_path="/Users/zmiguel/Projetos/voiceguard/.env")

db_url = os.getenv("DATABASE_URL")
if not db_url:
    print("❌ ERRO: DATABASE_URL não está definida no .env")
    exit(1)

try:
    engine = create_engine(db_url)
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("✅ Ligação à base de dados estabelecida com sucesso.")
except Exception as e:
    print(f"❌ ERRO: Falha ao ligar à base de dados: {e}")
    exit(1)
