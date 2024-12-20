"""add priority field for todo table

Revision ID: e5dd646c0ab0
Revises: b4a792eb6797
Create Date: 2024-12-19 14:49:30.349862

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5dd646c0ab0'
down_revision: Union[str, None] = 'b4a792eb6797'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('priority', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'priority')
    # ### end Alembic commands ###
