"""Initial Migration

Revision ID: 3a1fcc4ab349
Revises: 6571629b4382
Create Date: 2019-03-04 10:01:21.038143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a1fcc4ab349'
down_revision = '6571629b4382'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quote', sa.String(), nullable=True),
    sa.Column('Comments_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Comments_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pitches')
    op.add_column('comments', sa.Column('quotes_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_pitches_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'quotes', ['quotes_id'], ['id'])
    op.drop_column('comments', 'pitches_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitches_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_pitches_id_fkey', 'comments', 'pitches', ['pitches_id'], ['id'])
    op.drop_column('comments', 'quotes_id')
    op.create_table('pitches',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='pitches_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='pitches_pkey')
    )
    op.drop_table('quotes')
    # ### end Alembic commands ###