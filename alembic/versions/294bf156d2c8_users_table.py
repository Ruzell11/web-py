"""users table

Revision ID: 294bf156d2c8
Revises: 
Create Date: 2023-07-09 10:19:18.023997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '294bf156d2c8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users' , 
        sa.Column('id' , sa.Integer() , nullable=False),
        sa.Column('email' , sa.String(length=255) , nullable=False)
    )


def downgrade() -> None:
   op.drop_table('users')
