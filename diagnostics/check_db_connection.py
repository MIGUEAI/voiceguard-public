from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL") or "postgresql://voiceguard_user:voiceguard_pass@db:5432/voiceguard_db"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
        print("✅ Conexão à base de dados bem sucedida.")
except Exception as e:
    print(f"❌ Erro na conexão à base de dados: {e}")
