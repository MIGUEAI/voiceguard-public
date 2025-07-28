# /Users/zmiguel/Projetos/voiceguard/storage.py

import os

STORAGE_DIR = os.path.join(os.getcwd(), "uploads")
os.makedirs(STORAGE_DIR, exist_ok=True)

class LocalStorageProvider:
    def _file_path(self, file_hash):
        return os.path.join(STORAGE_DIR, file_hash)

    def exists(self, file_hash):
        return os.path.exists(self._file_path(file_hash))

    def save(self, file_hash, file_bytes):
        with open(self._file_path(file_hash), 'wb') as f:
            f.write(file_bytes)

    def read(self, file_hash):
        with open(self._file_path(file_hash), 'rb') as f:
            return f.read()

    def delete(self, file_hash):
        os.remove(self._file_path(file_hash))

storage_provider = LocalStorageProvider()
