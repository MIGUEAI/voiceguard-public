# Relatório Técnico: Integração de Autenticação de Dois Fatores (2FA) - VoiceGuard

## 1. Objetivos

- Implementar autenticação secundária via código enviado por SMS (simulado).
- Associar número de telemóvel ao utilizador.
- Reforçar segurança da autenticação JWT com 2FA.
- Preparar base para futura integração com serviços SMS reais.

## 2. Scripts Utilizados

- `/scripts/create_test_user_with_phone.py` — criação de utilizador com telefone e password hashed.
- `/scripts/show_user_password_hash.py` — visualização de hash para verificação.
- `/scripts/generate_migration_phone.py` — geração de migração Alembic para adicionar campo phone_number.

## 3. Migrações

- Nova migração Alembic gerada para adicionar coluna `phone_number` na tabela `user`.
- Backup do estado do repositório realizado antes da alteração (Git tag: `backup_pre_user_phone_2fa`).

## 4. Segurança JWT

- Migração do identity JWT de email para user.id (string).
- Confirmação dos tokens gerados com `identity=str(user.id)`.
- Atualização do fluxo de autenticação para usar id para melhor desempenho e segurança.

## 5. Observações de Arquitetura

- Separação clara dos endpoints:  
  - `/users/request-2fa` para gerar e enviar código (simulado).  
  - `/users/verify-2fa` para validação do código e ativação do 2FA.

- Simulação do envio de SMS na consola, garantindo segurança e testes eficazes.

- Configurações para .env indicam atenção para uso futuro de cookies com proteção CSRF.

## 6. Ponto de Restauro

- Commit com tag `backup_pre_user_phone_2fa` disponível para rollback.

## 7. Considerações Futuras

- Implementar limitação de requisições 2FA por IP para mitigar abusos.
- Integrar com gateway SMS real (Twilio ou outro).
- Rever segurança de cookies JWT para ambiente produção.

---

*Documento gerado automaticamente pelo sistema de integração VoiceGuard em 2025-07-29*
