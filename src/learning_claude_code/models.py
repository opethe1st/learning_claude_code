"""SQLAlchemy database models."""

from sqlalchemy import Column, Float, Integer, String

from learning_claude_code.database import Base


class ItemModel(Base):
    """SQLAlchemy model for items."""

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
