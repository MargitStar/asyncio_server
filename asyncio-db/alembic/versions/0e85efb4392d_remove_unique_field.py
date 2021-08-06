"""Remove unique field

Revision ID: 0e85efb4392d
Revises: 1f04f413b8c8
Create Date: 2021-07-29 16:30:49.082814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e85efb4392d'
down_revision = '1f04f413b8c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('packets_packet_key', 'packets', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('packets_packet_key', 'packets', ['packet'])
    # ### end Alembic commands ###