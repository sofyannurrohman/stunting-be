"""add nik, tanggal_lahir, tempat_lahir to toddlers

Revision ID: 1a88434c3fad
Revises: 66ec77843e64
Create Date: 2025-07-08 20:21:56.669044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a88434c3fad'
down_revision: Union[str, None] = '66ec77843e64'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('toddlers', sa.Column('nik', sa.String(length=20), nullable=True))
    op.add_column('toddlers', sa.Column('tanggal_lahir', sa.Date(), nullable=True))
    op.add_column('toddlers', sa.Column('tempat_lahir', sa.String(length=100), nullable=True))
    op.create_unique_constraint(None, 'toddlers', ['nik'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'toddlers', type_='unique')
    op.drop_column('toddlers', 'tempat_lahir')
    op.drop_column('toddlers', 'tanggal_lahir')
    op.drop_column('toddlers', 'nik')
    # ### end Alembic commands ###
