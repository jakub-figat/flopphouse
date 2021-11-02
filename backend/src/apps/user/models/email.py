from sqlalchemy import Column, DateTime, ForeignKey, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref, relationship

from src.settings.database import Base


class EmailConfirmation(Base):
    __tablename__ = "email_confirmations"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user = relationship("User", backref=backref("email_confirmation", uselist=False))

    token = Column(UUID(as_uuid=True), server_default=text("uuid_generate_v4()"), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
