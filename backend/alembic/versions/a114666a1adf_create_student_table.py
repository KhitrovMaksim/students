"""Create student table

Revision ID: a114666a1adf
Revises:
Create Date: 2022-10-27 20:48:03.548830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a114666a1adf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('students',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('first_name', sa.String(100), nullable=False),
                    sa.Column('last_name', sa.String(100), nullable=False),
                    sa.Column('date_of_birth', sa.String(10), nullable=False),
                    sa.Column('email', sa.String(100), nullable=False),
                    sa.Column('phone', sa.String(14), nullable=False),
                    sa.Column('favorite_sports', sa.String(250), nullable=True)
                    )


def downgrade():
    op.drop_table('students')
