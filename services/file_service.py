import os
from werkzeug.utils import secure_filename
from models.file import VoiceFile, db

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'm4a'}

class FileService:
    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @staticmethod
    def save_file(file, user_id, description=None):
        if file and FileService.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            voice_file = VoiceFile(filename=filename, user_id=user_id, description=description)
            db.session.add(voice_file)
            db.session.commit()
            return voice_file
        return None

