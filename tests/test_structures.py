import unittest
from src.inventory.models.product import Product
from src.inventory.structures.hash_table import HashTableInventory
from src.inventory.structures.array_list import ArrayListInventory
from src.inventory.structures.linked_list import LinkedListInventory

class TestInventoryStructures(unittest.TestCase):
    def setUp(self):
        self.p1 = Product("P100", "Monitor LG 27", "Elektronik", 4000000.0, 5)
        self.p2 = Product("P200", "Headset HyperX", "Aksesori", 1200000.0, 15)

    def _test_crud_operations(self, inventory):
        self.assertTrue(inventory.insert(self.p1))
        self.assertTrue(inventory.insert(self.p2))
        self.assertFalse(inventory.insert(self.p1))

        self.assertEqual(inventory.count(), 2)
        self.assertEqual(inventory.search("P100").name, "Monitor LG 27")
        self.assertIsNone(inventory.search("P999"))

        self.assertTrue(inventory.delete("P100"))
        self.assertFalse(inventory.delete("P100"))
        self.assertEqual(inventory.count(), 1)
        self.assertIsNone(inventory.search("P100"))

    def test_hash_table_inventory(self):
        self._test_crud_operations(HashTableInventory())

    def test_array_list_inventory(self):
        self._test_crud_operations(ArrayListInventory())

    def test_linked_list_inventory(self):
        self._test_crud_operations(LinkedListInventory())

if __name__ == "__main__":
    unittest.main()
