#!/usr/bin/env python3
import sys
sys.path.append("/Users/zmiguel/Projetos/voiceguard")

try:
    from logger import logger
except ImportError:
    print("❌ ERRO: Não foi possível importar logger.py.")
    exit(1)

try:
    logger.info("🧪 Teste de log executado com sucesso.")
    print("✅ Logging estruturado está funcional.")
except Exception as e:
    print(f"❌ ERRO: Falha ao escrever log: {e}")
