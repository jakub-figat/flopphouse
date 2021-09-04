"""user_initial

Revision ID: 8f918a675a0a
Revises: 
Create Date: 2021-09-04 12:04:19.579534

"""
from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from alembic import op

# revision identifiers, used by Alembic.
revision = "8f918a675a0a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4),
        sa.Column("first_name", sa.String(length=30), nullable=False),
        sa.Column("last_name", sa.String(length=30), nullable=False),
        sa.Column("username", sa.String(length=30), unique=True, nullable=False),
        sa.Column("is_active", sa.Boolean, default=False, nullable=False),
        sa.Column("email", sa.String, unique=True, nullable=False),
        sa.Column("date_of_birth", sa.Date, nullable=False),
    )


def downgrade():
    op.drop_table("users")
