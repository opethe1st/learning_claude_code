"""Pydantic schemas for API requests and responses."""

from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    """Schema for creating an item."""

    name: str = Field(..., min_length=1, max_length=100, description="Item name")
    description: str | None = Field(
        None, max_length=500, description="Item description"
    )
    price: float = Field(..., gt=0, description="Item price (must be positive)")
    quantity: int = Field(..., ge=0, description="Item quantity (must be non-negative)")


class Item(ItemCreate):
    """Schema for an item with ID."""

    id: int = Field(..., description="Unique item identifier")


class ItemResponse(BaseModel):
    """Schema for item creation response."""

    message: str = Field(..., description="Response message")
    item: Item = Field(..., description="Created item")
