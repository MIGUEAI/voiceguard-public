import os

required_keys = ["DATABASE_URL", "SECRET_KEY", "FLASK_ENV"]
missing = [key for key in required_keys if not os.getenv(key)]

if missing:
    print(f"❌ Variáveis em falta no .env: {missing}")
else:
    print("✅ Todas as variáveis obrigatórias estão presentes.")
