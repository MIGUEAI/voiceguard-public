import os
from dotenv import load_dotenv

env_path = "/Users/zmiguel/Projetos/voiceguard/.env"
load_dotenv(env_path)

print("🔍 Teste de variáveis .env (JWT):\n")

vars_required = [
    "SECRET_KEY",
    "JWT_SECRET_KEY",
    "ALGORITHM",
    "ACCESS_TOKEN_EXPIRE_MINUTES",
    "REFRESH_TOKEN_EXPIRE_DAYS"
]

for var in vars_required:
    value = os.getenv(var)
    if value:
        print(f"✅ {var} = {value}")
    else:
        print(f"❌ ERRO: {var} não está definida no .env")
