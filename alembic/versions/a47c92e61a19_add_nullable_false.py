"""Add nullable=False

Revision ID: a47c92e61a19
Revises: ce535c46bb01
Create Date: 2021-08-03 15:28:57.116284

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a47c92e61a19'
down_revision = 'a709340b1e6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('data_packets', 'packet_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('data_packets', 'data',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('multipart_data', 'mp_packet_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('multipart_data', 'packet_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('multipart_data', 'data',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('multipart_data', 'idx',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('multipart_packets', 'start_packet_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('multipart_packets', 'end_packet_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('packets', 'type',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('packets', 'timestamp',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('packets', 'client_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('packets', 'client_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('packets', 'timestamp',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('packets', 'type',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('multipart_packets', 'end_packet_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('multipart_packets', 'start_packet_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('multipart_data', 'idx',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('multipart_data', 'data',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('multipart_data', 'packet_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('multipart_data', 'mp_packet_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('data_packets', 'data',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('data_packets', 'packet_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
