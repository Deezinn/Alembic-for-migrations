"""add a column

Revision ID: 6fe8b1f53f88
Revises: 0893b3974670
Create Date: 2026-05-03 20:09:12.624887-03:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fe8b1f53f88'
down_revision: Union[str, Sequence[str], None] = '0893b3974670'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))

def downgrade():
    op.drop_column('account', 'last_transaction_date')
