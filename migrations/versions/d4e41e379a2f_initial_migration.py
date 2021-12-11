"""initial migration

Revision ID: d4e41e379a2f
Revises: 
Create Date: 2021-12-10 15:07:31.108189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4e41e379a2f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tickers',
    sa.Column('ticker_id', sa.String(length=45), nullable=False),
    sa.Column('company_name', sa.String(length=45), nullable=False),
    sa.Column('sector', sa.String(length=200), nullable=True),
    sa.Column('marketcap', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('ticker_id'),
    sa.UniqueConstraint('company_name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('portfolios',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('ticker_id', sa.String(length=45), nullable=False),
    sa.ForeignKeyConstraint(['ticker_id'], ['tickers.ticker_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'ticker_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portfolios')
    op.drop_table('users')
    op.drop_table('tickers')
    # ### end Alembic commands ###
