# voiceguard/services/user_service.py
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from extensions import db
from models.user import User
import random
from datetime import datetime, timedelta, UTC

class UserService:
    @staticmethod
    def register_user(name, email, password):
        hashed_password = generate_password_hash(password)
        user = User(name=name, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def authenticate_user(email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            return None

        if check_password_hash(user.password, password):
            user.login_attempts = 0
            db.session.commit()
            return user
        else:
            user.login_attempts += 1
            db.session.commit()
            return None

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def verify_password(hashed_password, plain_password):
        return check_password_hash(hashed_password, plain_password)

    @staticmethod
    def generate_2fa_code(user_id):
        user = User.query.get(user_id)
        if not user:
            return None

        code = f"{random.randint(100000, 999999)}"
        user.two_factor_code = code
        user.two_factor_expiration = datetime.now(UTC) + timedelta(minutes=5)
        db.session.commit()

        print(f"[2FA] Código para o utilizador {user.email}: {code}")
        return code

    @staticmethod
    def verify_2fa_code(user_id, code):
        user = User.query.get(user_id)
        if not user:
            return False

        return (
            user.two_factor_code == code and
            datetime.now(UTC) < user.two_factor_expiration
        )
