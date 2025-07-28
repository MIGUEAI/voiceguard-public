import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv

from config import DevelopmentConfig
from extensions import db
from logger import logger

from routes.users import users_bp
from routes.files import files_bp
from routes.health import health_bp
from routes.auth import auth_bp  # ✅ Importar auth_bp corretamente

# Carregar variáveis de ambiente do .env
load_dotenv()

# Criar instância da aplicação Flask
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
CORS(app, resources={r"/*": {"origins": ["http://localhost:5001"]}})

# Inicializar extensões
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Registar Blueprints
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(files_bp, url_prefix='/files')
app.register_blueprint(health_bp, url_prefix='/')
app.register_blueprint(auth_bp, url_prefix='/auth')  # ✅ Registo do auth_bp

# Criar pasta de uploads se não existir
os.makedirs(app.config.get('UPLOAD_FOLDER', 'uploads'), exist_ok=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    logger.info("🟢 VoiceGuard iniciado com sucesso.")
    app.run(host="0.0.0.0", port=8888, debug=True)
