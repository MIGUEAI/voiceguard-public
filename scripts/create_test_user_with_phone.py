#!/usr/bin/env python3

# ✅ Ficheiro: /Users/zmiguel/Projetos/voiceguard/scripts/create_test_user_with_phone.py   
import os
import sys
from flask import Flask
from werkzeug.security import generate_password_hash
from datetime import datetime, UTC

# 📌 Acrescenta raiz ao path
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)

from extensions import db
from config import DevelopmentConfig
from models.user import User

# ✅ Criar app Flask temporária para contexto do SQLAlchemy
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)

with app.app_context():
    email = "test_phone@example.com"
    phone = "+351968054505"
    password = "SenhaConfirmadaUltraSegura999"  # 🔐 Atualização segura
    hashed_password = generate_password_hash(password)

    # 🔄 Remove se já existir
    existing = User.query.filter_by(email=email).first()
    if existing:
        db.session.delete(existing)
        db.session.commit()
        print(f"⚠️ Utilizador antigo removido: {email}")

    # ➕ Criar novo utilizador
    new_user = User(
        name="Utilizador Com Telemóvel",
        email=email,
        password=hashed_password,
        phone_number=phone,
        created_at=datetime.now(UTC)
    )
    db.session.add(new_user)
    db.session.commit()

    # 🔍 Exibir hash para validação
    print(f"✅ Novo utilizador criado com telemóvel: {email} - {phone}")
    print(f"🔐 Hash da password gerada: {hashed_password}")

