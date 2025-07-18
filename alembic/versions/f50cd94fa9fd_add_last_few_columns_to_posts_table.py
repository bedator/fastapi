"""add last few columns to posts table

Revision ID: f50cd94fa9fd
Revises: b51e40aa88d9
Create Date: 2025-07-17 19:14:20.759716

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f50cd94fa9fd'
down_revision: Union[str, Sequence[str], None] = 'b51e40aa88d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default=sa.text('TRUE')))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True) , nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
