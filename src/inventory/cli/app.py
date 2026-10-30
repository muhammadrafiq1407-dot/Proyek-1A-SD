import time
from src.inventory.models.product import Product
from src.inventory.interfaces.adt_interface import AbstractInventoryADT
from src.inventory.structures.hash_table import HashTableInventory
from src.inventory.structures.array_list import ArrayListInventory
from src.inventory.structures.linked_list import LinkedListInventory
from src.inventory.services.benchmark_service import PerformanceBenchmarkService


class InventoryCLIApp:
    def __init__(self):
        self.STRUCTURE_REGISTRY = {
            "1": {
                "name": "Hash Table (Python Dict)",
                "class": HashTableInventory,
                "complexity": "O(1) Average"
            },
            "2": {
                "name": "Array List (Dynamic Array)",
                "class": ArrayListInventory,
                "complexity": "O(n)"
            },
            "3": {
                "name": "Singly Linked List",
                "class": LinkedListInventory,
                "complexity": "O(n)"
            }
        }

        self.current_mode = "1"
        self.inventory: AbstractInventoryADT = self.STRUCTURE_REGISTRY[self.current_mode]["class"]()
        
        self._seed_initial_data()

    def _seed_initial_data(self):
        seed = [
            Product("PROD-001", "Laptop Gaming Asus ROG", "Elektronik", 18500000.0, 12),
            Product("PROD-002", "Smartphone Samsung S24 Ultra", "Elektronik", 19999000.0, 25),
            Product("PROD-003", "Mouse Wireless Logitech MX Master 3S", "Aksesori", 1650000.0, 50),
            Product("PROD-004", "Keyboard Mekanikal Keychron K2", "Aksesori", 1250000.0, 30),
            Product("PROD-005", "Monitor Gaming LG UltraGear 27 Inch", "Elektronik", 4500000.0, 15)
        ]
        for p in seed:
            self.inventory.insert(p)

    def display_menu(self):
        active_meta = self.STRUCTURE_REGISTRY[self.current_mode]
        print("\n" + "=" * 80)
        print("     SISTEM MANAJEMEN INVENTARIS PRODUK E-COMMERCE (PROYEK 1)     ")
        print(f"     Struktur Data Aktif: {active_meta['name']} [{active_meta['complexity']}]")
        print("=" * 80)
        print("  1. Tambah Produk Baru (Insert)")
        print("  2. Cari Detail Produk berdasarkan ID (Search)")
        print("  3. Hapus Produk dari Inventaris (Delete)")
        print("  4. Tampilkan Seluruh Inventaris Produk")
        print("  5. Ganti Struktur Data Aktif (Hash Table / Array List / Linked List)")
        print("  6. Jalankan Simulasi Benchmark Komparatif")
        print("  7. Keluar Aplikasi")
        print("-" * 80)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Pilih Menu (1-7): ").strip()

            if choice == "1":
                self._handle_insert()
            elif choice == "2":
                self._handle_search()
            elif choice == "3":
                self._handle_delete()
            elif choice == "4":
                self._handle_list_all()
            elif choice == "5":
                self._handle_switch_structure()
            elif choice == "6":
                self._handle_benchmark()
            elif choice == "7":
                print("\nTerima kasih telah menggunakan Sistem Inventaris Produk!")
                break
            else:
                print("\n❌ Pilihan tidak valid! Silakan masukkan angka 1-7.")

    def _handle_switch_structure(self):
        print("\n" + "=" * 65)
        print("                 PILIH STRUKTUR DATA AKTIF")
        print("=" * 65)
        for key, meta in self.STRUCTURE_REGISTRY.items():
            active_indicator = " ⭐ [AKTIF]" if key == self.current_mode else ""
            print(f"  [{key}] {meta['name']:<28} (Kompleksitas: {meta['complexity']}){active_indicator}")
        print("  [0] Batal / Kembali ke Menu Utama")
        print("-" * 65)

        target = input("Pilih struktur data tujuan (0-3): ").strip()

        if target in ("0", ""):
            print("\n↩️ Penggantian struktur data dibatalkan.")
            return

        if target == self.current_mode:
            print(f"\n⚠️ Struktur data '{self.STRUCTURE_REGISTRY[target]['name']}' sudah aktif saat ini!")
            return

        if target not in self.STRUCTURE_REGISTRY:
            print("\n❌ Pilihan tidak valid! Masukkan angka sesuai opsi.")
            return

        old_products = self.inventory.get_all()
        target_meta = self.STRUCTURE_REGISTRY[target]
        new_inventory: AbstractInventoryADT = target_meta["class"]()

        for p in old_products:
            new_inventory.insert(p)

        self.inventory = new_inventory
        self.current_mode = target

        print(f"\n🔄 SUKSES: Struktur data aktif beralih ke '{target_meta['name']}'!")
        print(f"📦 Sebanyak {len(old_products)} produk berhasil dimigrasikan ke struktur data baru.")

    def _handle_insert(self):
        print("\n--- TAMBAH PRODUK BARU ---")
        p_id = input("ID Produk (contoh: PROD-006) : ").strip()
        name = input("Nama Produk                  : ").strip()
        cat = input("Kategori Produk              : ").strip()

        try:
            price = float(input("Harga Produk (Rp)            : "))
            stock = int(input("Jumlah Stok                  : "))

            product = Product(p_id, name, cat, price, stock)

            t_start = time.perf_counter()
            success = self.inventory.insert(product)
            t_exec = time.perf_counter() - t_start

            active_meta = self.STRUCTURE_REGISTRY[self.current_mode]
            if success:
                print(f"\n✅ SUCCESS: Produk '{name}' berhasil didaftarkan!")
                print(f"⏱️ Waktu Eksekusi ({active_meta['name']} - {active_meta['complexity']}): {t_exec:.8f} detik")
            else:
                print(f"\n❌ ERROR: ID Produk '{p_id}' sudah terdaftar dalam sistem!")

        except ValueError as err:
            print(f"\n❌ ERROR INPUT: {err}")

    def _handle_search(self):
        print("\n--- CARI PRODUK BERDASARKAN ID ---")
        p_id = input("Masukkan ID Produk yang dicari: ").strip()

        t_start = time.perf_counter()
        product = self.inventory.search(p_id)
        t_exec = time.perf_counter() - t_start

        active_meta = self.STRUCTURE_REGISTRY[self.current_mode]
        if product:
            print("\n🔍 HASIL PENCARIAN TERSEDIA:")
            print("-" * 80)
            print(product)
            print("-" * 80)
            print(f"⏱️ Waktu Pencarian ({active_meta['name']} - {active_meta['complexity']}): {t_exec:.8f} detik")
        else:
            print(f"\n❌ ERROR: Produk dengan ID '{p_id}' tidak ditemukan.")

    def _handle_delete(self):
        print("\n--- HAPUS PRODUK DARI INVENTARIS ---")
        p_id = input("Masukkan ID Produk yang dihapus: ").strip()

        t_start = time.perf_counter()
        success = self.inventory.delete(p_id)
        t_exec = time.perf_counter() - t_start

        active_meta = self.STRUCTURE_REGISTRY[self.current_mode]
        if success:
            print(f"\n✅ SUCCESS: Produk ID '{p_id}' berhasil dihapus.")
            print(f"⏱️ Waktu Penghapusan ({active_meta['name']} - {active_meta['complexity']}): {t_exec:.8f} detik")
        else:
            print(f"\n❌ ERROR: Produk ID '{p_id}' tidak ditemukan.")

    def _handle_list_all(self):
        active_meta = self.STRUCTURE_REGISTRY[self.current_mode]
        print(f"\n--- DAFTAR INVENTARIS [{active_meta['name']}] (Total: {self.inventory.count()} Item) ---")
        products = self.inventory.get_all()
        if not products:
            print("Inventaris saat ini kosong.")
            return

        print("-" * 80)
        for p in products:
            print(p)
        print("-" * 80)

    def _handle_benchmark(self):
        print("\n--- UJI KOMPARASI BENCHMARK STRUKTUR DATA ---")
        try:
            n_val = input("Masukkan jumlah sampel data [Default 5000]: ").strip()
            n_items = int(n_val) if n_val else 5000
        except ValueError:
            n_items = 5000

        results = PerformanceBenchmarkService.run_benchmark(n_items)

        print("\n" + "=" * 85)
        print(f" HASIL BENCHMARK EMPIRIS ({n_items:,} DATA PRODUK)")
        print("=" * 85)
        print(f"{'Struktur Data':<26} | {'Insert Total (s)':<18} | {'Search Avg (s)':<18} | {'Delete (s)':<15}")
        print("-" * 85)
        for name, metrics in results.items():
            print(f"{name:<26} | {metrics['insert_total_sec']:<18.6f} | {metrics['search_avg_sec']:<18.8f} | {metrics['delete_sec']:<15.8f}")
        print("=" * 85)
        print("📌 KESIMPULAN: Hash Table (dict) terbukti paling efisien untuk pencarian & penghapusan!")