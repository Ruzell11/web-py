"""modify users column to make auto increment

Revision ID: de5cc16433c6
Revises: d7b4c2e444ae
Create Date: 2023-07-09 12:03:18.372765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de5cc16433c6'
down_revision = 'd7b4c2e444ae'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('users', 'id', existing_type=sa.INTEGER(), nullable=False)
    op.execute('ALTER TABLE users MODIFY id INTEGER AUTO_INCREMENT PRIMARY KEY')

def downgrade() -> None:
    op.alter_column('users', 'id', autoincrement=False)
