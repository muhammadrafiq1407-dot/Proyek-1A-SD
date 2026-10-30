# E-Commerce Product Inventory System (Proyek 1 - Struktur Data)

Sistem Manajemen Inventaris Produk E-Commerce berkinerja tinggi yang membandingkan kompleksitas waktu dan efisiensi Hash Table (Python dict), Array-based List (Python list), dan Singly Linked List ADT.

## 📌 Arsitektur Proyek (Clean Architecture & OOP)

Proyek ini disusun berdasarkan standar pemrograman Python profesional (*Separation of Concerns* & *Prinsip SOLID*):

```text
ecommerce-inventory-system/
├── main.py                         # Entry point utama
├── README.md                       # Dokumentasi proyek
├── src/                            # Source code modular
│   └── inventory/
│       ├── models/                 # Domain Model (Product with Encapsulation)
│       ├── interfaces/             # ADT Contract (AbstractInventoryADT)
│       ├── structures/             # Implementasi (Hash Table, List, Linked List)
│       ├── services/               # Benchmark Performance Service
│       └── cli/                    # CLI Presentation Layer
└── tests/                          # Automated Unit Tests
```

## 🚀 Cara Menjalankan Aplikasi

### 1. Eksekusi Program Utama (CLI)
```bash
python main.py
```

### 2. Eksekusi Unit Test Otomatis
```bash
python -m unittest discover -s tests
```

## 👨‍🎓 Informasi Mahasiswa
* **Nama**: Muhammad Rafiq Al-Ghifari
* **NIM**: 12550111036
* **Program Studi**: Teknik Informatika, UIN Sultan Syarif Kasim Riau
