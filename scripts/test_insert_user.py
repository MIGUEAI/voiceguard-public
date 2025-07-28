from sqlalchemy import create_engine, Table, MetaData
from datetime import datetime, timezone

DATABASE_URL = "postgresql://voiceguard_user:voiceguard_pass@db:5432/voiceguard_db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)

user_table = metadata.tables.get("user")

if user_table is None:
    print("❌ Tabela 'user' não encontrada.")
else:
    with engine.begin() as conn:
        result = conn.execute(user_table.insert().values(
            name="Miguel Backup",
            email="miguel.backup@example.com",
            password="hash_super_secreto",
            created_at=datetime.now(timezone.utc),
            login_attempts=0,
            two_factor_code="789123",
            two_factor_expiration=datetime.now(timezone.utc),
            two_factor_enabled=True
        ))
        print(f"✅ Utilizador inserido com ID: {result.inserted_primary_key[0]}")
