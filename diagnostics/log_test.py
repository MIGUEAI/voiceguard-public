import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("voiceguard")

try:
    logger.info("🔍 Log de teste executado com sucesso.")
    print("✅ Sistema de logs configurado corretamente.")
except Exception as e:
    print(f"❌ Falha no sistema de logs: {e}")
