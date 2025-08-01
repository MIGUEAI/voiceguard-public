# Documentação Centralizada do Projeto VoiceGuard

---

## 1. Estado Atual do Projeto [2025-07-31][Ref:1]

O VoiceGuard encontra-se em fase avançada de desenvolvimento com funcionalidades principais implementadas e validadas:

- Autenticação baseada em JWT usando `user.id` como identity;
- Integração de Autenticação de Dois Fatores (2FA) via telemóvel, com simulação de envio de SMS;
- Mecanismos de segurança reforçados conforme melhores práticas;
- Pipelines de CI/CD implementadas com GitHub Actions para backup, validação e deploy automático;
- Uso de PostgreSQL como base de dados principal com gestão de migrações via Alembic.

Para detalhes completos, consultar o relatório técnico atualizado em:
- `/docs/Relatorio_Tecnico_Completo.md`
- `/docs/Relatorio_Integracao_2FA.md`

---

## 2. Scripts Principais [2025-07-31][Ref:2]

| Script                                | Descrição                                                  |
|-------------------------------------|------------------------------------------------------------|
| `/scripts/create_test_user_with_phone.py`  | Criação de utilizador com número de telemóvel e password hashed |
| `/scripts/show_user_password_hash.py`      | Visualização do hash da password de um utilizador         |
| `/scripts/generate_migration_phone.py`     | Geração da migração Alembic para adicionar campo `phone_number` |
| `/scripts/run_migrations.py`                 | Execução das migrações Alembic com contexto Flask ativo  |
| `/scripts/check_env.py`                       | Validação da existência das variáveis de ambiente essenciais |
| `/scripts/check_db_connection.py`            | Verificação da ligação à base de dados                    |

---

## 3. Configurações e Variáveis Ambiente [2025-07-31][Ref:3]

As configurações essenciais encontram-se no ficheiro `.env` e no módulo `config.py`, incluindo:

- `SECRET_KEY`, `JWT_SECRET_KEY` para segurança;
- `DATABASE_URL` configurada para PostgreSQL;
- Configurações específicas para tokens JWT (tempo de expiração, proteção CSRF).

⚠️ Notar que `JWT_COOKIE_CSRF_PROTECT` está definido para `False` atualmente para ambiente de desenvolvimento, recomendando-se revisão para produção.

---

## 4. Regras Obrigatórias e Boas Práticas Incorporadas [2025-07-31][Ref:4]

Este projeto segue rigorosamente as regras obrigatórias:

- Passo a passo com análise e validação após cada comando;
- Código completo, caminhos absolutos, comandos limpos;
- Nenhuma substituição sem análise fundamentada e autorização;
- Backup e tags Git antes de alterações críticas;
- Segurança, robustez arquitetónica, escalabilidade e interoperabilidade como pilares;
- Documentação e relatórios técnicos atualizados e centralizados.

---

## 5. Histórico e Ponto de Restauro [2025-07-31][Ref:5]

- Tags Git como `backup_pre_user_phone_2fa` garantem possibilidade de rollback;
- Histórico de commits detalhado para auditoria e rastreabilidade.

---

## 6. Próximos Passos Sugeridos [2025-07-31][Ref:6]

- Implementação de integração real para envio SMS via gateway (ex: Twilio);
- Melhoria da segurança JWT para ambiente produção;
- Limitação de requisições 2FA para mitigação de abuso;
- Monitorização e logging aprimorados para fluxos críticos;
- Atualização contínua da documentação centralizada e relatórios técnicos.

---

*Documento gerado automaticamente em 2025-07-31 por sistema VoiceGuard.*
