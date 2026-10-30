from typing import List, Optional
from src.inventory.interfaces.adt_interface import AbstractInventoryADT
from src.inventory.models.product import Product

class ArrayListInventory(AbstractInventoryADT):
    def __init__(self):
        self._storage: List[Product] = []

    def insert(self, product: Product) -> bool:
        if any(p.product_id == product.product_id for p in self._storage):
            return False
        self._storage.append(product)
        return True

    def search(self, product_id: str) -> Optional[Product]:
        pid = product_id.strip()
        for product in self._storage:
            if product.product_id == pid:
                return product
        return None

    def delete(self, product_id: str) -> bool:
        pid = product_id.strip()
        for idx, product in enumerate(self._storage):
            if product.product_id == pid:
                self._storage.pop(idx)
                return True
        return False

    def get_all(self) -> List[Product]:
        return list(self._storage)

    def count(self) -> int:
        return len(self._storage)

    def clear(self) -> None:
        self._storage.clear()
