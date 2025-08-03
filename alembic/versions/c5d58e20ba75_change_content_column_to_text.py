"""Change content column to Text

Revision ID: c5d58e20ba75
Revises: 5077fff58f65
Create Date: 2025-07-28 19:09:23.044264

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5d58e20ba75'
down_revision: Union[str, None] = '5077fff58f65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
