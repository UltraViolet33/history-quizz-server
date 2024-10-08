"""empty message

Revision ID: 91cd2e5ff0f4
Revises: a40869e105b0
Create Date: 2024-09-05 14:58:40.744630

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '91cd2e5ff0f4'
down_revision = 'a40869e105b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quizzes_categories')
    with op.batch_alter_table('quizzes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'categories', ['category_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quizzes', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('category_id')

    op.create_table('quizzes_categories',
    sa.Column('category_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('quizz_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name='quizzes_categories_ibfk_1'),
    sa.ForeignKeyConstraint(['quizz_id'], ['quizzes.id'], name='quizzes_categories_ibfk_2'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
