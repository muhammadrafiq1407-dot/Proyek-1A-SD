import unittest
from src.inventory.models.product import Product

class TestProductModel(unittest.TestCase):
    def test_valid_product_creation(self):
        p = Product("P001", "Laptop ROG", "Elektronik", 15000000.0, 10)
        self.assertEqual(p.product_id, "P001")
        self.assertEqual(p.name, "Laptop ROG")
        self.assertEqual(p.price, 15000000.0)
        self.assertEqual(p.stock, 10)

    def test_invalid_price_raises_error(self):
        with self.assertRaises(ValueError):
            Product("P002", "Mouse", "Aksesori", -50000.0, 5)

    def test_invalid_stock_raises_error(self):
        with self.assertRaises(ValueError):
            Product("P003", "Keyboard", "Aksesori", 500000.0, -2)

    def test_empty_name_raises_error(self):
        with self.assertRaises(ValueError):
            Product("P004", "", "Aksesori", 500000.0, 2)

if __name__ == "__main__":
    unittest.main()
