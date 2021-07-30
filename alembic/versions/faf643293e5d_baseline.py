"""baseline

Revision ID: faf643293e5d
Revises: 
Create Date: 2021-07-29 16:10:09.628918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'faf643293e5d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'packets',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('packet', sa.String()))


def downgrade():
    op.drop_table('packets')
