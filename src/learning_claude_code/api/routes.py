"""API routes for learning_claude_code."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from learning_claude_code.api.schemas import Item, ItemCreate, ItemResponse
from learning_claude_code.database import get_db
from learning_claude_code.models import ItemModel

router = APIRouter()


@router.get("/items", response_model=list[Item])
def list_items(db: Session = Depends(get_db)) -> list[Item]:
    """List all items."""
    items = db.query(ItemModel).all()
    return [
        Item(
            id=item.id,
            name=item.name,
            description=item.description,
            price=item.price,
            quantity=item.quantity,
        )
        for item in items
    ]


@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int, db: Session = Depends(get_db)) -> Item:
    """Get a specific item by ID."""
    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(
        id=item.id,
        name=item.name,
        description=item.description,
        price=item.price,
        quantity=item.quantity,
    )


@router.post("/items", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate, db: Session = Depends(get_db)) -> ItemResponse:
    """Create a new item."""
    db_item = ItemModel(
        name=item.name,
        description=item.description,
        price=item.price,
        quantity=item.quantity,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    created_item = Item(
        id=db_item.id,
        name=db_item.name,
        description=db_item.description,
        price=db_item.price,
        quantity=db_item.quantity,
    )
    return ItemResponse(message="Item created successfully", item=created_item)


@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)) -> Item:
    """Update an existing item."""
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db_item.name = item.name
    db_item.description = item.description
    db_item.price = item.price
    db_item.quantity = item.quantity

    db.commit()
    db.refresh(db_item)

    return Item(
        id=db_item.id,
        name=db_item.name,
        description=db_item.description,
        price=db_item.price,
        quantity=db_item.quantity,
    )


@router.delete("/items/{item_id}", response_model=dict[str, str])
def delete_item(item_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    """Delete an item."""
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}
