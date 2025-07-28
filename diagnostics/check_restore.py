from sqlalchemy import create_engine, MetaData
from os import getenv

DATABASE_URL = getenv("DATABASE_URL").replace("voiceguard", "voiceguard_restore_test")

engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)

user_table = metadata.tables.get("user")

if user_table is None:
    print("❌ Tabela 'user' não encontrada na base restaurada.")
else:
    with engine.connect() as conn:
        result = conn.execute(user_table.select()).mappings().fetchall()
        print("📄 Utilizadores encontrados na base restaurada:")
        for row in result:
            print(dict(row))
