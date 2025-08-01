from sqlalchemy.orm import declarative_base
Base = declarative_base()

import os
from datetime import timedelta
from dotenv import load_dotenv

# ✅ Carregar variáveis do ambiente
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default-jwt")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 🔐 Parâmetros de segurança JWT
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_TOKEN_LOCATION = ["headers"]
    JWT_HEADER_TYPE = "Bearer"

    # ⚠️ Em produção, ativar CSRF se usares cookies com JWT
    JWT_COOKIE_CSRF_PROTECT = False  # Revisar antes de deploy final

class DevelopmentConfig(Config):
    DEBUG = True

    # ✅ Obrigatório: garantir URL para PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("❌ DATABASE_URL não está definido no ambiente (.env)")

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
