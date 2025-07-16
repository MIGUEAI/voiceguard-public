# init_db.py
from app import app
from extensions import db
from models import *  # Garante que os modelos estão corretamente importados em models/__init__.py

with app.app_context():
    db.create_all()
    print("✅ Base de dados criada com sucesso.")
