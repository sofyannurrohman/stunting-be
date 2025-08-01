"""Add lengths for VARCHAR columns

Revision ID: 5ff508255593
Revises: eca303fd923a
Create Date: 2025-05-04 21:13:21.344827

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '5ff508255593'
down_revision: Union[str, None] = 'eca303fd923a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('information', sa.Column('createdAt', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.add_column('information', sa.Column('updatedAt', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.alter_column('information', 'title',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('information', 'content',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=1000),
               nullable=True)
    op.drop_column('information', 'category')
    op.add_column('toddlers', sa.Column('name', sa.String(length=255), nullable=True))
    op.add_column('toddlers', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('toddlers', sa.Column('createdAt', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.add_column('toddlers', sa.Column('updatedAt', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.alter_column('toddlers', 'age_months',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('toddlers', 'gender',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=50),
               nullable=True)
    op.alter_column('toddlers', 'weight_kg',
               existing_type=mysql.FLOAT(),
               type_=sa.Integer(),
               nullable=True)
    op.alter_column('toddlers', 'height_cm',
               existing_type=mysql.FLOAT(),
               type_=sa.Integer(),
               nullable=True)
    op.create_index(op.f('ix_toddlers_name'), 'toddlers', ['name'], unique=False)
    op.create_foreign_key(None, 'toddlers', 'users', ['user_id'], ['id'])
    op.drop_column('toddlers', 'prediction_result')
    op.add_column('users', sa.Column('password', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('createdAt', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.add_column('users', sa.Column('updatedAt', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.alter_column('users', 'email',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('users', 'name',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', mysql.VARCHAR(length=255), nullable=False))
    op.alter_column('users', 'name',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.drop_column('users', 'updatedAt')
    op.drop_column('users', 'createdAt')
    op.drop_column('users', 'password')
    op.add_column('toddlers', sa.Column('prediction_result', mysql.VARCHAR(length=100), nullable=True))
    op.drop_constraint(None, 'toddlers', type_='foreignkey')
    op.drop_index(op.f('ix_toddlers_name'), table_name='toddlers')
    op.alter_column('toddlers', 'height_cm',
               existing_type=sa.Integer(),
               type_=mysql.FLOAT(),
               nullable=False)
    op.alter_column('toddlers', 'weight_kg',
               existing_type=sa.Integer(),
               type_=mysql.FLOAT(),
               nullable=False)
    op.alter_column('toddlers', 'gender',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(length=20),
               nullable=False)
    op.alter_column('toddlers', 'age_months',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.drop_column('toddlers', 'updatedAt')
    op.drop_column('toddlers', 'createdAt')
    op.drop_column('toddlers', 'user_id')
    op.drop_column('toddlers', 'name')
    op.add_column('information', sa.Column('category', mysql.VARCHAR(length=100), nullable=True))
    op.alter_column('information', 'content',
               existing_type=sa.String(length=1000),
               type_=mysql.TEXT(),
               nullable=False)
    op.alter_column('information', 'title',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.drop_column('information', 'updatedAt')
    op.drop_column('information', 'createdAt')
    # ### end Alembic commands ###
