#!/usr/bin/env python3

import os
import sys

# ✅ Caminho absoluto da raiz do projeto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE_DIR)

from flask import Flask
from werkzeug.security import check_password_hash
from config import DevelopmentConfig
from extensions import db
from models.user import User

# ✅ Criar contexto da app Flask
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)

with app.app_context():
    email = "test_user@example.com"
    user = User.query.filter_by(email=email).first()

    if user:
        print(f"📧 Email: {user.email}")
        print(f"🔐 Hash da password: {user.password}")
    else:
        print("❌ Utilizador não encontrado.")
