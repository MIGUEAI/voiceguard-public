# /Users/zmiguel/Projetos/voiceguard/models/file.py

from extensions import db
from datetime import datetime, UTC

class UploadedFile(db.Model):
    __tablename__ = 'uploaded_file'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    mimetype = db.Column(db.String(128), nullable=True)
    size = db.Column(db.Integer, nullable=True)
    file_hash = db.Column(db.String(64), nullable=False, unique=True)  # ✅ este campo resolve o erro
    upload_date = db.Column(db.DateTime, default=lambda: datetime.now(UTC))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
