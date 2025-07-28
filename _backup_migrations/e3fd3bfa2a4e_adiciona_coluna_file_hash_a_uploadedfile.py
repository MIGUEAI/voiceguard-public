"""Adiciona coluna file_hash a UploadedFile

Revision ID: e3fd3bfa2a4e
Revises: 
Create Date: 2025-07-22 12:53:58.021378
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy import inspect, text

# revision identifiers, used by Alembic.
revision = 'e3fd3bfa2a4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    inspector = inspect(conn)

    columns = [col["name"] for col in inspector.get_columns("uploaded_file")]

    with op.batch_alter_table('uploaded_file', schema=None) as batch_op:
        if 'file_hash' not in columns:
            batch_op.add_column(sa.Column('file_hash', sa.String(length=64), nullable=False))
        if 'mimetype' not in columns:
            batch_op.add_column(sa.Column('mimetype', sa.String(length=128)))
        if 'size' not in columns:
            batch_op.add_column(sa.Column('size', sa.Integer(), nullable=True))
        if 'upload_date' not in columns:
            batch_op.add_column(sa.Column('upload_date', sa.DateTime(), nullable=True))

        # Ajustes existentes
        batch_op.alter_column('filename',
            existing_type=sa.VARCHAR(length=256),
            type_=sa.String(length=255),
            existing_nullable=False)
        batch_op.alter_column('user_id',
            existing_type=sa.INTEGER(),
            nullable=False)
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

        # Só tenta apagar se existir
        if 'uploaded_at' in columns:
            batch_op.drop_column('uploaded_at')


def downgrade():
    with op.batch_alter_table('uploaded_file', schema=None) as batch_op:
        batch_op.drop_column('upload_date')
        batch_op.drop_column('size')
        batch_op.drop_column('mimetype')
        batch_op.drop_column('file_hash')
        batch_op.alter_column('user_id',
            existing_type=sa.INTEGER(),
            nullable=True)
        batch_op.alter_column('filename',
            existing_type=sa.String(length=255),
            type_=sa.VARCHAR(length=256),
            existing_nullable=False)
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.add_column(sa.Column('uploaded_at', sa.TIMESTAMP(), autoincrement=False, nullable=True))

