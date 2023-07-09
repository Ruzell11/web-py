"""modify users column make email unique

Revision ID: 57754eb9dc08
Revises: de5cc16433c6
Create Date: 2023-07-09 12:07:29.270265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57754eb9dc08'
down_revision = 'de5cc16433c6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('users', 'email', existing_type=sa.String(length=255), nullable=False)
    op.create_unique_constraint('uq_users_email', 'users', ['email'])


def downgrade() -> None:
    op.alter_column('users', 'email', nullable=True)
    op.drop_constraint('uq_users_email', 'users', type_='unique')
