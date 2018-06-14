"""empty message

Revision ID: 9303b4649eef
Revises: 
Create Date: 2018-06-07 17:07:48.740665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9303b4649eef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grade',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('g_name', sa.VARCHAR(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=16), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('s_grade_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['s_grade_id'], ['grade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('grade')
    # ### end Alembic commands ###