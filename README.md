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

### 🔐 Autenticação com Dois Fatores (2FA) via Telemóvel

---

#### ✅ Fluxo Completo de Login com 2FA

1. **POST /users/login**  
   → Submete email e password  
   → Recebe token JWT de acesso e refresh

2. **POST /users/request-2fa**  
   → Autenticado com JWT  
   → Código 2FA é enviado para o número de telemóvel associado

3. **POST /users/verify-2fa**  
   → Envia código recebido por SMS  
   → Confirma e ativa o 2FA na conta do utilizador

---

#### 🧪 Como testar 2FA em ambiente de desenvolvimento

- Use os scripts disponibilizados no diretório `/scripts` para criar utilizadores com número de telemóvel.  
- O envio do código 2FA é simulado via print no terminal da aplicação para testes locais.  
- Execute os endpoints `/users/request-2fa` e `/users/verify-2fa` conforme o fluxo.

---

#### 📄 Documentação e Relatórios Técnicos

- Relatório técnico detalhado disponível em `/docs/Relatorio_Integracao_2FA.md`.  
- Inclui segurança, migrações, scripts usados, ponto de restauro e recomendações futuras.

---

*Documento atualizado automaticamente em 2025-07-29 pelo sistema de integração VoiceGuard.*

