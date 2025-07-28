"""Rollback file_hash de uploaded_file

Revision ID: 9ece89d0e9dd
Revises: e3fd3bfa2a4e
Create Date: 2025-07-22 14:35:21.686263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ece89d0e9dd'
down_revision = 'e3fd3bfa2a4e'
branch_labels = None
depends_on = None


def upgrade():
    # Esta migração é um rollback, por isso não aplica alterações ao subir.
    pass

def downgrade():
    # Esta função reverte a migração anterior, removendo a coluna file_hash.
    with op.batch_alter_table('uploaded_file', schema=None) as batch_op:
        batch_op.drop_column('file_hash')
