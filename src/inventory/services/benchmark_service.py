import time
import random
from typing import Dict, Any
from src.inventory.models.product import Product
from src.inventory.interfaces.adt_interface import AbstractInventoryADT
from src.inventory.structures.hash_table import HashTableInventory
from src.inventory.structures.array_list import ArrayListInventory
from src.inventory.structures.linked_list import LinkedListInventory

class PerformanceBenchmarkService:
    @staticmethod
    def run_benchmark(n_items: int = 5000) -> Dict[str, Dict[str, float]]:
        print(f"\n⚡ Memulai Pengujian Benchmark Empiris ({n_items:,} data produk)...")

        categories = ["Elektronik", "Pakaian", "Aksesori", "Buku", "Rumah Tangga"]
        dataset = [
            Product(
                product_id=f"PRD-{i:07d}",
                name=f"Produk E-Commerce #{i}",
                category=categories[i % len(categories)],
                price=round(random.uniform(10000, 10000000), 2),
                stock=random.randint(1, 500)
            )
            for i in range(1, n_items + 1)
        ]

        target_search_id = dataset[n_items // 2].product_id
        target_delete_id = dataset[n_items // 4].product_id

        structures: Dict[str, AbstractInventoryADT] = {
            "Hash Table (dict)": HashTableInventory(),
            "Array List (python list)": ArrayListInventory(),
            "Linked List (Custom ADT)": LinkedListInventory()
        }

        results = {}

        for name, instance in structures.items():
            t_start = time.perf_counter()
            for p in dataset:
                instance.insert(p)
            t_insert = time.perf_counter() - t_start

            t_start = time.perf_counter()
            for _ in range(1000):
                instance.search(target_search_id)
            t_search = (time.perf_counter() - t_start) / 1000.0

            t_start = time.perf_counter()
            instance.delete(target_delete_id)
            t_delete = time.perf_counter() - t_start

            results[name] = {
                "insert_total_sec": t_insert,
                "search_avg_sec": t_search,
                "delete_sec": t_delete
            }

        return results
