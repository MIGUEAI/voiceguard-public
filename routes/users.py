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

    access_token = create_access_token(identity=user.email)
    refresh_token = create_refresh_token(identity=user.email)
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
    current_user_email = get_jwt_identity()
    new_token = create_access_token(identity=current_user_email)
    return jsonify(access_token=new_token), 200

@users_bp.route('/me', methods=['GET'])
@jwt_required()
def get_profile():
    identity = get_jwt_identity()
    user = User.query.filter_by(email=identity).first()

    if not user:
        return jsonify({"msg": "Utilizador não encontrado"}), 404

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": user.created_at.isoformat()
    }), 200

@users_bp.route('/update', methods=['PUT'])
@jwt_required()
def update_user():
    identity = get_jwt_identity()
    user = User.query.filter_by(email=identity).first()

    if not user:
        return jsonify({"msg": "Utilizador não encontrado"}), 404

    data = request.get_json()
    new_name = data.get("name")
    current_password = data.get("current_password")
    new_password = data.get("new_password")

    # Validação de password atual (obrigatória para alterações sensíveis)
    if new_password:
        if not current_password or not check_password_hash(user.password, current_password):
            return jsonify({"msg": "Password atual incorreta"}), 403
        user.password = generate_password_hash(new_password)

    if new_name:
        user.name = new_name

    db.session.commit()
    return jsonify({"msg": "Dados atualizados com sucesso"}), 200
