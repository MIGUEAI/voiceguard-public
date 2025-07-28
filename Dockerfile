FROM python:3.13-slim

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    libmagic1 \
    file \
    && rm -rf /var/lib/apt/lists/*

# Copia entrypoint e define permissões
COPY infra/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Copia e instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do projeto
COPY . .

# Define o entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Comando padrão: iniciar a aplicação Flask
CMD ["python3", "app.py"]
