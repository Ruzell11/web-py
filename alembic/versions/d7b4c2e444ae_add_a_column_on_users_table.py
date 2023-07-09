"""Add a column on users table

Revision ID: d7b4c2e444ae
Revises: 294bf156d2c8
Create Date: 2023-07-09 10:29:09.231113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7b4c2e444ae'
down_revision = '294bf156d2c8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users' , sa.Column('first_name' , sa.String(length=255), nullable=False))


def downgrade() -> None:
      op.drop_column('users', 'first_name')
