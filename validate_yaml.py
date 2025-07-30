import yaml
import sys

files = [
    ".github/workflows/ci.yml",
    ".github/workflows/deploy.yml"
]

for file in files:
    try:
        with open(file, 'r') as f:
            yaml.safe_load(f)
        print(f"✅ {file} está válido.")
    except yaml.YAMLError as exc:
        print(f"❌ Erro no {file}:")
        print(exc)
        sys.exit(1)
