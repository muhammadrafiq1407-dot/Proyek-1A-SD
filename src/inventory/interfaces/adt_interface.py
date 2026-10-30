import abc
from typing import List, Optional
from src.inventory.models.product import Product

class AbstractInventoryADT(abc.ABC):
    @abc.abstractmethod
    def insert(self, product: Product) -> bool:
        pass

    @abc.abstractmethod
    def search(self, product_id: str) -> Optional[Product]:
        pass

    @abc.abstractmethod
    def delete(self, product_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_all(self) -> List[Product]:
        pass

    @abc.abstractmethod
    def count(self) -> int:
        pass

    @abc.abstractmethod
    def clear(self) -> None:
        pass
