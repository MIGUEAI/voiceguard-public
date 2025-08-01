#!/usr/bin/env python3
import os
import sys
from datetime import datetime

# Caminho absoluto para a raiz do projeto
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, BASE_DIR)

# Arquivos fontes para compilar documentação (exemplo)
DOCS_SRC = [
    'docs/Relatorio_Integracao_2FA.md',
    'docs/Relatorio_Tecnico_Completo.md',
]

# Arquivo de saída com timestamp
timestamp = datetime.now().strftime('%Y-%m-%d')
output_file = f'docs/Documentacao_Centralizada_{timestamp}.md'

def gerar_documentacao_centralizada():
    with open(output_file, 'w', encoding='utf-8') as out_f:
        out_f.write("# Documentação Centralizada VoiceGuard\n\n")
        out_f.write(f"*Atualizado em: {timestamp}*\n\n---\n\n")
        for doc in DOCS_SRC:
            if os.path.exists(doc):
                out_f.write(f"## Conteúdo do arquivo: {doc}\n\n")
                with open(doc, 'r', encoding='utf-8') as f:
                    out_f.write(f.read() + "\n\n---\n\n")
            else:
                out_f.write(f"> ⚠️ Arquivo {doc} não encontrado.\n\n---\n\n")

    print(f"✅ Documentação gerada em: {output_file}")

if __name__ == "__main__":
    gerar_documentacao_centralizada()
