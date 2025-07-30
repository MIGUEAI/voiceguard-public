# /Users/zmiguel/Projetos/voiceguard/models/user.py

from extensions import db
from datetime import datetime, UTC
from sqlalchemy import Boolean


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=True)  # 📞 Suporte para 2FA via SMS
    two_factor_enabled = db.Column(Boolean, default=False, nullable=False)  # ✅ Flag de ativação
    two_factor_code = db.Column(db.String(6))  # ✅ Código enviado
    two_factor_expiration = db.Column(db.DateTime)  # ✅ Expiração do código

    login_attempts = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC))
