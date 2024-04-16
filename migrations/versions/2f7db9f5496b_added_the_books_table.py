"""added the books table

Revision ID: 2f7db9f5496b
Revises: c0f802c48f8a
Create Date: 2024-04-17 02:28:09.793572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f7db9f5496b'
down_revision = 'c0f802c48f8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Book_name', sa.String(length=128), nullable=True),
    sa.Column('Book_content', sa.String(length=512), nullable=True),
    sa.Column('Book_author', sa.String(length=128), nullable=True),
    sa.Column('Date_issued', sa.Date(), nullable=True),
    sa.Column('Return_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###