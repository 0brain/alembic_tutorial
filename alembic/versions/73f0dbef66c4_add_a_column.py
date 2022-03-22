"""Add a column

Revision ID: 73f0dbef66c4
Revises: 6657f52fd5db
Create Date: 2022-03-22 14:17:32.772191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73f0dbef66c4'
down_revision = '6657f52fd5db'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))

def downgrade():
    op.drop_column('account', 'last_transaction_date')
