#!/usr/bin/env python3

import datetime
import os

BASE_DIR = "/Users/zmiguel/Projetos/voiceguard"
DOCS_DIR = os.path.join(BASE_DIR, "docs")
MAIN_DOC_PATH = os.path.join(DOCS_DIR, "Documentacao_Centralizada.md")

hoje = datetime.date.today().isoformat()

relatorio_path = os.path.join(DOCS_DIR, f"Documentacao_Centralizada_{hoje}.md")

conteudo_relatorio = f"""# Documentação Centralizada VoiceGuard - {hoje}

## Sumário

- Resumo do estado atual do projeto
- Scripts utilizados
- Migrações aplicadas
- Configurações do ambiente
- Regras obrigatórias e boas práticas
- Histórico e versionamento dos relatórios

## Observações

Este arquivo foi gerado automaticamente no dia {hoje}.

---

"""

with open(relatorio_path, "w", encoding="utf-8") as f:
    f.write(conteudo_relatorio)

indice_conteudo = ""

if os.path.exists(MAIN_DOC_PATH):
    with open(MAIN_DOC_PATH, "r", encoding="utf-8") as f:
        indice_conteudo = f.read()

link_relatorio = f"- [{hoje}](Documentacao_Centralizada_{hoje}.md)\n"

if link_relatorio not in indice_conteudo:
    indice_conteudo += link_relatorio

with open(MAIN_DOC_PATH, "w", encoding="utf-8") as f:
    f.write("# Documentação Centralizada VoiceGuard\n\n## Histórico de Relatórios\n\n")
    f.write(indice_conteudo)

print(f"✅ Relatório gerado: {relatorio_path}")
print(f"✅ Índice atualizado: {MAIN_DOC_PATH}")

