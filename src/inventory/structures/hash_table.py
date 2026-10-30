from typing import Dict, List, Optional
from src.inventory.interfaces.adt_interface import AbstractInventoryADT
from src.inventory.models.product import Product

class HashTableInventory(AbstractInventoryADT):
    def __init__(self):
        self._storage: Dict[str, Product] = {}

    def insert(self, product: Product) -> bool:
        if product.product_id in self._storage:
            return False
        self._storage[product.product_id] = product
        return True

    def search(self, product_id: str) -> Optional[Product]:
        return self._storage.get(product_id.strip(), None)

    def delete(self, product_id: str) -> bool:
        pid = product_id.strip()
        if pid in self._storage:
            del self._storage[pid]
            return True
        return False

    def get_all(self) -> List[Product]:
        return list(self._storage.values())

    def count(self) -> int:
        return len(self._storage)

    def clear(self) -> None:
        self._storage.clear()
