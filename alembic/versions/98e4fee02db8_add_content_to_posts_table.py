"""add content to posts table

Revision ID: 98e4fee02db8
Revises: 5658a4629d48
Create Date: 2025-07-17 18:58:38.453524

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98e4fee02db8'
down_revision: Union[str, Sequence[str], None] = '5658a4629d48'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
