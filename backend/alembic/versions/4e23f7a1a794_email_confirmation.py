"""email_confirmation

Revision ID: 4e23f7a1a794
Revises: 8f918a675a0a
Create Date: 2021-09-05 09:58:19.804477

"""
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from alembic import op

# revision identifiers, used by Alembic.
revision = "4e23f7a1a794"
down_revision = "8f918a675a0a"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "email_confirmations",
        sa.Column("id", UUID(as_uuid=True), server_default=sa.text("uuid_generate_v4()"), primary_key=True),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("user.id"), nullable=False),
        sa.Column("token", UUID(as_uuid=True), server_default=sa.text("uuid_generate_v4()"), nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now(), nullable=False),
    )


def downgrade():
    op.drop_table("email_confirmations")
