from decimal import Decimal
from typing import Dict, Any

class Product:
    def __init__(self, product_id: str, name: str, category: str, price: float, stock: int):
        self._product_id = product_id.strip() if product_id else ""
        if not self._product_id:
            raise ValueError("ID Produk tidak boleh kosong!")
            
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    @property
    def product_id(self) -> str:
        return self._product_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Nama produk tidak boleh kosong!")
        self._name = value.strip()

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, value: str):
        if not value or not value.strip():
            raise ValueError("Kategori produk tidak boleh kosong!")
        self._category = value.strip()

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Harga produk tidak boleh bernilai negatif!")
        self._price = float(value)

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value: int):
        if value < 0:
            raise ValueError("Stok produk tidak boleh bernilai negatif!")
        self._stock = int(value)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "product_id": self._product_id,
            "name": self._name,
            "category": self._category,
            "price": self._price,
            "stock": self._stock
        }

    def __str__(self) -> str:
        return (f"[ID: {self._product_id:<10}] {self._name:<32} | "
                f"Kategori: {self._category:<15} | "
                f"Harga: Rp{self._price:>12,.2f} | Stok: {self._stock:>5}")

    def __repr__(self) -> str:
        return f"Product(id='{self._product_id}', name='{self._name}', price={self._price})"
