from sqlalchemy import Boolean
# voiceguard/models/user.py

from extensions import db
from datetime import datetime, UTC

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC))
    login_attempts = db.Column(db.Integer, default=0)
    two_factor_code = db.Column(db.String(6))
    two_factor_expiration = db.Column(db.DateTime)

    two_factor_enabled = db.Column(Boolean, default=False, nullable=False)
# ✅ Campo adicionado para suportar autenticação de dois fatores
from sqlalchemy import Boolean

