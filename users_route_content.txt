#!/usr/bin/env python3

from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from extensions import db
from datetime import datetime, timedelta
import random

users_bp = Blueprint('users', __name__)

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"msg": "Email e password são obrigatórios"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Credenciais inválidas"}), 401

    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))
    return jsonify(access_token=access_token, refresh_token=refresh_token), 200

@users_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({"msg": "Todos os campos são obrigatórios"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "Email já registado"}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "Utilizador registado com sucesso"}), 201

@users_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()
    new_token = create_access_token(identity=str(user_id))
    return jsonify(access_token=new_token), 200

@users_bp.route('/me', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))
    if not user:
        return jsonify({"msg": "Utilizador não encontrado"}), 404

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone_number": user.phone_number,
        "created_at": user.created_at.isoformat()
    }), 200

@users_bp.route('/request-2fa', methods=['POST'])
@jwt_required()
def request_two_factor():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))

    if not user or not user.phone_number:
        return jsonify({"msg": "Utilizador não encontrado ou sem número de telemóvel"}), 404

    code = f"{random.randint(100000, 999999)}"
    expiration = datetime.utcnow() + timedelta(minutes=5)

    user.two_factor_code = code
    user.two_factor_expiration = expiration
    db.session.commit()

    print(f"📲 Código 2FA enviado para {user.phone_number}: {code}")

    return jsonify({"msg": "Código 2FA enviado por SMS"}), 200

@users_bp.route('/verify-2fa', methods=['POST'])
@jwt_required()
def verify_two_factor():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))

    if not user:
        return jsonify({"msg": "Utilizador não encontrado"}), 404

    data = request.get_json()
    code = data.get("code")

    if not code:
        return jsonify({"msg": "Código é obrigatório"}), 400

    if user.two_factor_code != code:
        return jsonify({"msg": "Código inválido"}), 401

    if datetime.utcnow() > user.two_factor_expiration:
        return jsonify({"msg": "Código expirado"}), 401

    user.two_factor_code = None
    user.two_factor_expiration = None
    user.two_factor_enabled = True
    db.session.commit()

    return jsonify({"msg": "2FA verificado com sucesso"}), 200
