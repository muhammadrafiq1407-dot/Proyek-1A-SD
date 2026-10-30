from typing import List, Optional
from src.inventory.interfaces.adt_interface import AbstractInventoryADT
from src.inventory.models.product import Product

class Node:
    def __init__(self, data: Product):
        self.data: Product = data
        self.next: Optional['Node'] = None

class LinkedListInventory(AbstractInventoryADT):
    def __init__(self):
        self._head: Optional[Node] = None
        self._size: int = 0

    def insert(self, product: Product) -> bool:
        if self.search(product.product_id) is not None:
            return False
        new_node = Node(product)
        new_node.next = self._head
        self._head = new_node
        self._size += 1
        return True

    def search(self, product_id: str) -> Optional[Product]:
        pid = product_id.strip()
        current = self._head
        while current:
            if current.data.product_id == pid:
                return current.data
            current = current.next
        return None

    def delete(self, product_id: str) -> bool:
        pid = product_id.strip()
        current = self._head
        prev: Optional[Node] = None

        while current:
            if current.data.product_id == pid:
                if prev is None:
                    self._head = current.next
                else:
                    prev.next = current.next
                self._size -= 1
                return True
            prev = current
            current = current.next
        return False

    def get_all(self) -> List[Product]:
        result = []
        current = self._head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def count(self) -> int:
        return self._size

    def clear(self) -> None:
        self._head = None
        self._size = 0
