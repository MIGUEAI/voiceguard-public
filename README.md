## 🔁 CI/CD com GitHub Actions

![Backup VoiceGuard](https://github.com/MIGUEAI/voiceguard/actions/workflows/backup.yml/badge.svg)
![Validação de Ambiente](https://github.com/MIGUEAI/voiceguard/actions/workflows/validate_env.yml/badge.svg)
![Backup Simulado CI](https://github.com/MIGUEAI/voiceguard/actions/workflows/ci_backup.yml/badge.svg)

---

### 📦 Workflows Disponíveis

| Workflow                | Trigger                | Função principal                                  |
|------------------------|------------------------|---------------------------------------------------|
| `backup.yml`           | `cron` + manual        | Executa script de backup do host (local)          |
| `validate_env.yml`     | `push` + manual        | Valida `.env` e ligação à base de dados           |
| `ci_backup.yml`        | `manual` (`dispatch`)  | Executa backup simulado e faz upload de artefacto |

---

### ▶️ Como executar manualmente

1. Aceder ao repositório:  
   [https://github.com/MIGUEAI/voiceguard/actions](https://github.com/MIGUEAI/voiceguard/actions)

2. Escolher o workflow desejado

3. Clicar em **"Run workflow"** (canto superior direito)

---

### 🛡️ Segurança

- Nenhuma variável sensível é exposta diretamente.
- Os scripts de CI não acedem à base de dados real no runner GitHub.
- Recomenda-se usar [GitHub Secrets](https://github.com/MIGUEAI/voiceguard/settings/secrets/actions) para futuras credenciais.

---

### 📁 Artefactos de Backup

- Os ficheiros `.dump` gerados pelo CI são guardados como artefactos:
  - `voiceguard-backups` → via `backup.yml`
  - `voiceguard-backup`  → via `ci_backup.yml`

Podes descarregá-los diretamente no final de cada execução CI.

---
