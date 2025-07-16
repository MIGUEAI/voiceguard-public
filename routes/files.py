from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
import os

files_bp = Blueprint('files', __name__)
UPLOAD_FOLDER = 'uploads'

@files_bp.route('/', methods=['GET'])
@jwt_required()
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify(files=files)

@files_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    if 'file' not in request.files:
        return jsonify({"msg": "Nenhum ficheiro enviado"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"msg": "Nome de ficheiro vazio"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return jsonify({"msg": f"Ficheiro '{file.filename}' guardado com sucesso!"}), 201


