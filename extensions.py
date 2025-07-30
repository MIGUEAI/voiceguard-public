# /Users/zmiguel/Projetos/voiceguard/extensions.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# ✅ Instâncias globais
db = SQLAlchemy()
migrate = Migrate()
