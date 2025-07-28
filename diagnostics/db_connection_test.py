from sqlalchemy import create_engine, text
from os import getenv

DATABASE_URL = getenv("DATABASE_URL")

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("✅ Conexão à base de dados bem sucedida.")
except Exception as e:
    print(f"❌ Erro na conexão à base de dados: {e}")
