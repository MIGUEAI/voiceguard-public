#!/usr/bin/env python3

import os
import sys

# Caminho absoluto para a raiz do projeto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE_DIR)

from flask import Flask
from flask_migrate import Migrate, upgrade
from config import DevelopmentConfig
from extensions import db

# Criação da aplicação Flask e configuração
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Inicialização da extensão SQLAlchemy
db.init_app(app)

# Inicialização da extensão Flask-Migrate
migrate = Migrate(app, db)

if __name__ == "__main__":
    # Executar migrações com contexto Flask ativo
    with app.app_context():
        upgrade()
        print("✅ Migrações aplicadas com sucesso")
