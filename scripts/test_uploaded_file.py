from sqlalchemy import create_engine, MetaData
from datetime import datetime, timezone

DATABASE_URL = "postgresql://voiceguard_user:voiceguard_pass@db:5432/voiceguard_db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)

user_table = metadata.tables.get("user")
uploaded_file = metadata.tables.get("uploaded_file")

if user_table is None or uploaded_file is None:
    print("❌ Tabelas 'user' ou 'uploaded_file' não encontradas.")
else:
    with engine.begin() as conn:
        # ✅ Inserir utilizador de teste
        result_user = conn.execute(user_table.insert().values(
            name="Utilizador Teste",
            email="teste@example.com",
            password="hashed_dummy",
            two_factor_enabled=False,
            created_at=datetime.now(timezone.utc)
        ))
        user_id = result_user.inserted_primary_key[0]
        print(f"👤 Utilizador criado com ID: {user_id}")

        # ✅ Inserir ficheiro associado ao utilizador criado
        result_file = conn.execute(uploaded_file.insert().values(
            filename="teste_audio.wav",
            file_hash="abc1234567890def",
            upload_date=datetime.now(timezone.utc),
            user_id=user_id
        ))
        print(f"✅ Ficheiro inserido com ID: {result_file.inserted_primary_key[0]}")

        # 📦 Mostrar registos da tabela
        rows = conn.execute(uploaded_file.select()).mappings().fetchall()
        print("📂 Registos encontrados em uploaded_file:")
        for row in rows:
            print(dict(row))
