"""initial migration

Revision ID: a0e3393df77a
Revises: 
Create Date: 2023-12-13 06:17:56.038943

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0e3393df77a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'Departments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('head', sa.String(), nullable=False),

        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
    )

    op.create_table(
        'Positions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('job_group', sa.String(), nullable=False),
        sa.Column('job_description', sa.Text(), nullable=False),
        sa.Column('salary', sa.Integer(), nullable=False),

        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('title'),
    )

    op.create_table(
        'Employees',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('age', sa.Integer(), nullable=False),
        sa.Column('gender', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('phone', sa.Integer(), nullable=False),
        sa.Column('address', sa.String(), nullable=False),
        sa.Column('date_hired', sa.Date(), nullable=False),

        sa.Column('position_id', sa.Integer(), nullable=False),
        sa.Column('department_id', sa.Integer(), nullable=False),

        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['department_id'], ['Departments.id']),
        sa.ForeignKeyConstraint(['position_id'], ['Positions.id']),
    )


def downgrade() -> None:
    pass
