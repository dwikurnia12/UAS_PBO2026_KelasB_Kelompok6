# Hanari Bakery — Sistem Informasi Produksi dan Manajemen Produk

> Proyek Akhir Pemrograman Berorientasi Objek (PBO)  
> Program Studi Pendidikan Teknik Informatika dan komputer — FKIP UNS  
> Tahun Akademik 2025/2026

---

## Deskripsi Proyek

**Hanari Bakery** adalah sistem informasi berbasis Python untuk mengelola proses produksi dan manajemen produk pada sebuah toko roti. Sistem ini memungkinkan pengguna untuk:

- Menambahkan dan menampilkan data produk roti
- Menghitung estimasi profit berdasarkan jumlah produksi
- Mensimulasikan proses produksi setiap jenis roti secara lengkap (pengadonan, pengembangan, pemanggangan, topping, pengemasan, pelabelan)

Proyek ini dibangun dengan menerapkan konsep-konsep inti **Pemrograman Berorientasi Objek (OOP)**:

| Konsep | Penerapan |
|--------|-----------|
| **Abstract Class** | `ProdukRoti` sebagai superclass abstrak |
| **Inheritance** | `RotiManis`, `Croissant`, `RotiKering`,  `RotiBasah` → `ProdukRoti` |
| **Interface** | `pelabelan, pemanggangan, pengemasan, pengembangan, perebusan, topping` |
| **Encapsulation** | Atribut private pada `ProdukRoti` dengan property getter |
| **Polymorphism** | Setiap subclass mengimplementasikan `pengadukan()` dan proses produksi secara berbeda |

---

## Anggota Kelompok & Pembagian Tugas

| No | Nama | NIM | Tugas |
|----|------|-----|-------|
| 1 | Febriana Putri Qurrota'ayun | K3525007 | Interface (pelabelan, pemanggangan, pengemasan, pengembangan, perebusan, topping) + Diagram Kelas UML |
| 2 | Queennera Martha Kusuma Wardhani | K3525012 | `ProdukRoti` (Abstract Superclass) + Encapsulation + Method umum (`hitung_profit()`, `tampilkan_info()`) + README |
| 3 | Arofa Karindra Bimantara | K3525051 | `RotiManis`, `Croissant`, `ButterCookies` + Testing ketiga class tersebut |
| 4 | Diah Anggraeni | K3525055 | `Muffin`, `Klepon`, `KueSoes` + Testing ketiga class tersebut |
| 5 | Dwi Kurniawati Hanifah | K3525056 | `BakerySystem`, `DataProduct`, `main.py`, UI (`menu.py`, `display.py`) |

---

## Struktur Direktori

```
UAS_PBO2026_KelasB_Kelompok6/
│
├── main.py                  # Entry point program
├── data_product.py          # Data produk default
├── test_program.py          # File uji coba program
├── README.md
│
├── models/
│   ├── produk_roti.py       # Abstract superclass (Queen)
│   ├── roti_manis.py        # Subclass Roti Manis (Bima)
│   ├── croissant.py         # Subclass Croissant (Bima)
│   ├── roti_basah/
│   │   ├── klepon.py        # Subclass Klepon (Diah)
│   │   └── kue_soes.py      # Subclass Kue Soes (Diah)
│   └── roti_kering/
│       ├── butter_cookies.py # Subclass Butter Cookies (Bima)
│       └── muffin.py        # Subclass Muffin (Diah)
│
├── interfaces/
│   └── interfaces.py        # Semua interface (Ayun)
│
├── ui/
│   ├── menu.py              # Tampilan menu (Nia)
│   └── display.py           # Fungsi tampilan output (Nia)
│
└── system/
    └── bakery_system.py     # Controller sistem (Nia)
```

---

## Tampilan Menu Program

```
==========================================================
       HANARI BAKERY — SISTEM INFORMASI PRODUKSI
==========================================================

  MENU UTAMA
  ----------------------------------------
  1. Tambah Produk Baru
  2. Tampilkan Semua Produk
  3. Kalkulator Estimasi Profit
  4. Simulasi Proses Produksi
  5. Hapus Produk
  0. Keluar
  ----------------------------------------
```

---

## Arsitektur Class

### Abstract Superclass
```
ProdukRoti  (abstract)
├── Atribut private (enkapsulasi)
│   ├── __nama_produk
│   ├── __kode_produk
│   ├── __bahan_baku
│   ├── __jumlah_produksi
│   ├── __biaya_produksi
│   └── __harga_jual_per_pcs
├── Method umum (konkret)
│   ├── hitung_profit(jumlah_pcs) → dict
│   └── tampilkan_info() → str
└── Method abstrak
    └── pengadonan() → str
    └──simulasi_produksi()
```

### Hierarki Inheritance
```
ProdukRoti (abstract)
├── RotiManis        + Pengembangan
├── croissant         + Pengembangan
├── RotiBasah
│   ├── Klepon        
│   └── Kue soes      + Pengembangan
└── RotiKering        + Topping
    ├── Butter cookies
    └── Muffin        + Pengembangan
```

### Interfaces
```
Pemanggangan   → pemanggangan()
Perebusan      → perebusan()
Pengadonan     → pengadonan()
Pengemasan     → pengemasan()
Pelabelan      → pelabelan()
Pengembangan   → pengembangan()
Topping        → topping()

```

> Diagram UML lengkap tersedia di folder `docs/` (dibuat menggunakan Diagrams.io)

---

## Daftar Produk

| Kode | Nama Produk | Per Resep | Biaya Produksi | Harga Jual/pcs |
|------|-------------|-----------|---------------|----------------|
| RM001 | Roti Manis | 12 pcs | Rp 35.000 | Rp 5.000 |
| CR001 | Croissant | 10 pcs | Rp 75.000 | Rp 15.000 |
| BC001 | Butter Cookies | 30 pcs | Rp 45.000 | Rp 3.000 |
| MF001 | Muffin | 12 pcs | Rp 38.000 | Rp 8.000 |
| KB001 | Klepon | 20 pcs | Rp 25.000 | Rp 2.000 |
| KB002 | Kue Soes | 15 pcs | Rp 40.000 | Rp 6.000 |

---

## Penerapan Prinsip SOLID

| Prinsip | Penerapan dalam Proyek |
|---------|----------------------|
| **S** — Single Responsibility | `ProdukRoti` hanya mengelola data produk; `BakerySystem` mengelola katalog; `ui/` mengelola tampilan |
| **O** — Open/Closed | Produk baru cukup ditambahkan sebagai subclass baru tanpa mengubah kode yang sudah ada |
| **L** — Liskov Substitution | Semua subclass dapat digunakan di tempat `ProdukRoti` (misal: di katalog `BakerySystem`) |
| **I** — Interface Segregation | Interface dipecah kecil-kecil sehingga class hanya implement apa yang dibutuhkan |
| **D** — Dependency Inversion | `BakerySystem` bergantung pada abstraksi `ProdukRoti`, bukan pada kelas konkret |
