from fastapi import APIRouter
from typing import List
from app.models.item import Item

# ルーターのインスタンス化
router = APIRouter()

# ダミーデータ
items = []

# 一覧取得
@router.get("/items/", response_model=List[Item])
def get_all_items():
    return items

# アイテム作成
@router.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

# アイテム取得
@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id < len(items):
        return items[item_id]
    return {"error": "Item not found"}

# アイテム更新
@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    if item_id < len(items):
        items[item_id] = updated_item
        return updated_item
    return {"error": "Item not found"}

# アイテム削除
@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < len(items):
        deleted_item = items.pop(item_id)
        return {"message": f"Item '{deleted_item.name}' deleted successfully"}
    return {"error": "Item not found"}
