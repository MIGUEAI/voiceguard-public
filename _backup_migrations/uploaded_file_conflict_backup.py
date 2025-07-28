# voiceguard/models/uploaded_file.py

from extensions import db
from datetime import datetime, UTC

class UploadedFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(256), nullable=False)
    file_hash = db.Column(db.String(64), unique=True, nullable=False)
    uploaded_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC))
    user_id = db.Column(db.Integer, nullable=True)
