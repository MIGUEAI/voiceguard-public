from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)

@health_bp.route('/')
def root():
    return jsonify({"msg": "🚀 VoiceGuard API ativa e a funcionar!"}), 200

@health_bp.route('/health/')
def health_check():
    return jsonify({"status": "OK"}), 200


