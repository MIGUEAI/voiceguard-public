#!/usr/bin/env python3

import os
import sys
from flask import Flask
from flask_migrate import Migrate
from alembic.config import main as alembic_main

# 📌 Adiciona o diretório do projeto ao sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BASE_DIR)

from extensions import db, migrate
from config import DevelopmentConfig
from models.user import User

# 🔧 Cria app com contexto Flask
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate.init_app(app, db)

# 🚀 Executa migração
with app.app_context():
    print("🚀 A gerar migração Alembic para adicionar phone_number...")
    alembic_main([
        "revision",
        "--autogenerate",
        "-m",
        "➕ Adiciona campo phone_number ao modelo User"
    ])
