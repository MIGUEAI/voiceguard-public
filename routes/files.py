from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from io import BytesIO
import hashlib
import magic

from extensions import db
from models.file import UploadedFile
from storage import storage_provider

files_bp = Blueprint('files', __name__, url_prefix='/files')

@files_bp.route('/', methods=['POST'])
@jwt_required()
def upload_file():
    if 'file' not in request.files:
        return jsonify({"msg": "Nenhum ficheiro enviado"}), 400

    file = request.files['file']
    file_bytes = file.read()

    mime_type = magic.from_buffer(file_bytes, mime=True)
    file_hash = hashlib.sha256(file_bytes).hexdigest()
    filename = secure_filename(file.filename)

    if storage_provider.exists(file_hash):
        return jsonify({"msg": "Ficheiro já existe"}), 409

    storage_provider.save(file_hash, file_bytes)
    user_id = get_jwt_identity()

    novo_ficheiro = UploadedFile(
        filename=filename,
        file_hash=file_hash,
        user_id=user_id
    )
    db.session.add(novo_ficheiro)
    db.session.commit()

    return jsonify({
        "msg": f"Ficheiro '{filename}' guardado com sucesso.",
        "hash": file_hash,
        "mime": mime_type
    }), 201

@files_bp.route('/', methods=['GET'])
@jwt_required()
def list_files():
    user_id = get_jwt_identity()
    ficheiros = UploadedFile.query.filter_by(user_id=user_id).all()
    return jsonify([{
        "filename": f.filename,
        "hash": f.file_hash,
        "uploaded_at": f.uploaded_at.isoformat()
    } for f in ficheiros])

@files_bp.route('/download/<hash>', methods=['GET'])
@jwt_required()
def download_file(hash):
    ficheiro = UploadedFile.query.filter_by(file_hash=hash).first()
    if not ficheiro:
        return jsonify({"msg": "Ficheiro não encontrado"}), 404

    file_data = storage_provider.read(hash)
    return send_file(BytesIO(file_data), download_name=ficheiro.filename, as_attachment=True)

@files_bp.route('/delete/<hash>', methods=['DELETE'])
@jwt_required()
def delete_file(hash):
    ficheiro = UploadedFile.query.filter_by(file_hash=hash).first()
    if not ficheiro:
        return jsonify({"msg": "Ficheiro não encontrado"}), 404

    storage_provider.delete(hash)
    db.session.delete(ficheiro)
    db.session.commit()

    return jsonify({"msg": f"Ficheiro '{ficheiro.filename}' eliminado com sucesso."}), 200
