from sqlalchemy import create_engine, inspect

DATABASE_URL = "postgresql://voiceguard_user:voiceguard_pass@db:5432/voiceguard_db"

engine = create_engine(DATABASE_URL)
inspector = inspect(engine)

try:
    columns = inspector.get_columns("uploaded_file")
    for col in columns:
        print(f"{col['name']}: {col['type']}")
except Exception as e:
    print(f"❌ Erro: {e}")
