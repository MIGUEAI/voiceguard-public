# services/storage_provider.py

import os
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

# 📦 Provedor base (Local)
class StorageProvider:
    def __init__(self):
        self.base_path = os.path.join(os.getcwd(), 'uploads')
        os.makedirs(self.base_path, exist_ok=True)

    def save(self, name: str, file_storage: FileStorage) -> str:
        filename = secure_filename(name)
        path = os.path.join(self.base_path, filename)
        file_storage.save(path)
        return path

    def exists(self, name: str) -> bool:
        filename = secure_filename(name)
        path = os.path.join(self.base_path, filename)
        return os.path.exists(path)

    def read(self, name: str) -> bytes:
        filename = secure_filename(name)
        path = os.path.join(self.base_path, filename)
        with open(path, 'rb') as f:
            return f.read()

    def delete(self, name: str) -> None:
        filename = secure_filename(name)
        path = os.path.join(self.base_path, filename)
        if os.path.exists(path):
            os.remove(path)

# 🪣 Subclasse para integração com AWS S3 (stub por agora)
class S3StorageProvider(StorageProvider):
    def save(self, name: str, file_storage: FileStorage) -> str:
        raise NotImplementedError("Integração com AWS S3 não implementada ainda.")
        
    def exists(self, name: str) -> bool:
        raise NotImplementedError("Verificação de ficheiro em S3 não implementada.")
    
    def read(self, name: str) -> bytes: 
        raise NotImplementedError("Leitura de ficheiro em S3 não implementada.")
        
    def delete(self, name: str) -> None:
        raise NotImplementedError("Eliminação de ficheiro em S3 não implementada.")

# 🧬 Subclasse para IPFS (stub)
class IPFSStorageProvider(StorageProvider):
    def save(self, name: str, file_storage: FileStorage) -> str:
        raise NotImplementedError("Upload para IPFS não implementado ainda.")
        
    def exists(self, name: str) -> bool:
        raise NotImplementedError("Verificação de ficheiro no IPFS não implementada.")
            
    def read(self, name: str) -> bytes:
        raise NotImplementedError("Leitura de ficheiro no IPFS não implementada.")

    def delete(self, name: str) -> None:
        raise NotImplementedError("Eliminação no IPFS não implementada.")

# 🏭 Factory
def get_storage_provider():
    provider = os.getenv("STORAGE_BACKEND", "local").lower()
    if provider == "s3":
        return S3StorageProvider()
    elif provider == "ipfs":
        return IPFSStorageProvider()
    else:
        return StorageProvider()
