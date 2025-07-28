#!/usr/bin/env python3
# ✅ Ficheiro: /Users/zmiguel/Projetos/voiceguard/scripts/create_test_user.py

import os
import sys
from werkzeug.security import generate_password_hash
from flask import Flask

# 📌 Inserir explicitamente o diretório raiz do projeto
PROJECT_ROOT = "/Users/zmiguel/Projetos/voiceguard"
sys.path.insert(0, PROJECT_ROOT)

from config import DevelopmentConfig
from extensions import db
from models.user import User

# ✅ Configurar aplicação Flask para usar SQLAlchemy
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)

# ✅ Dados do utilizador de teste
email = "test_user@example.com"
name = "Utilizador Teste"
password = "test123"
hashed_password = generate_password_hash(password)

# ✅ Execução no contexto da app Flask
with app.app_context():
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()
        print(f"⚠️ Utilizador antigo removido: {email}")

    new_user = User(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    print(f"✅ Novo utilizador criado com sucesso: {email}")
