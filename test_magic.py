import magic
mime = magic.from_buffer(b'\xFF\xFB\x90\x64', mime=True)
print(f"MIME detectado: {mime}")
