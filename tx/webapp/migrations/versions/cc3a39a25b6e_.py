"""empty message

Revision ID: cc3a39a25b6e
Revises: d85b4a35536f
Create Date: 2021-04-27 17:13:49.183471

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cc3a39a25b6e'
down_revision = 'd85b4a35536f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('moviename', sa.String(length=100), nullable=False))
    op.drop_column('movie', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('username', mysql.VARCHAR(length=100), nullable=False))
    op.drop_column('movie', 'moviename')
    # ### end Alembic commands ###
