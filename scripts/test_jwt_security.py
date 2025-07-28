import sys
import os

# 📌 Força inclusão do diretório base do projeto
BASE_DIR = "/Users/zmiguel/Projetos/voiceguard"
sys.path.append(BASE_DIR)

from services.security import create_access_token, create_refresh_token, decode_token

print("🔐 Teste de segurança JWT\n")

# 📌 [B.1.3.T1] Payload base
data = {"sub": "test_user@example.com"}

# 📌 [B.1.3.T2] Gerar tokens
access = create_access_token(data)
refresh = create_refresh_token(data)

print("✅ Access Token criado:")
print(access)
print("\n✅ Refresh Token criado:")
print(refresh)

# 📌 [B.1.3.T3] Verificar decodificação
decoded = decode_token(access)
if decoded and decoded.get("sub") == data["sub"]:
    print("\n✅ Token decodificado com sucesso:")
    print(decoded)
else:
    print("\n❌ ERRO: Falha ao decodificar token!")
