"""Add additional fields

Revision ID: 9e7c6bede288
Revises: 9ab4932695bc
Create Date: 2024-11-15 20:01:55.396751

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e7c6bede288'
down_revision: Union[str, None] = '9ab4932695bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('title', sa.String(length=500), nullable=False))
    op.add_column('question', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('question', sa.Column('updated_at', sa.DateTime(), nullable=False))
    op.create_index(op.f('ix_question_title'), 'question', ['title'], unique=False)
    op.drop_column('question', 'question')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('question', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_question_title'), table_name='question')
    op.drop_column('question', 'updated_at')
    op.drop_column('question', 'created_at')
    op.drop_column('question', 'title')
    # ### end Alembic commands ###