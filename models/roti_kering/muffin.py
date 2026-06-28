"""
muffin.py
=========
Class Muffin
Tanggung Jawab : Diah
"""

from models.produk_roti import ProdukRoti

from interfaces.pengadonan import Pengadonan
from interfaces.pengembangan import Pengembangan
from interfaces.pemanggangan import Pemanggangan
from interfaces.topping import Topping
from interfaces.pengemasan import Pengemasan
from interfaces.pelabelan import Pelabelan


class Muffin(ProdukRoti):

    def __init__(self):
        bahan = {
            "Tepung Terigu": (250, "gram"),
            "Gula Pasir": (150, "gram"),
            "Telur": (2, "butir"),
            "Susu Cair": (200, "ml"),
            "Mentega": (100, "gram"),
            "Baking Powder": (1, "sdt"),
            "Choco Chips": (100, "gram")
        }

        super().__init__(
            nama_produk="Muffin",
            kode_produk="MF-001",
            bahan_baku=bahan,
            jumlah_produksi=12,
            biaya_produksi=50000,
            harga_jual_per_pcs=10000
        )

    # Method abstrak dari ProdukRoti
    def aduk(self):
        return Pengadonan.muffin()

    # Simulasi produksi
    def simulasi_produksi(self):
        print("=" * 50)
        print("SIMULASI PRODUKSI MUFFIN")
        print("=" * 50)

        print(self.aduk())
        print()

        print(Pengembangan.muffin())
        print()

        print(Topping.muffin())
        print()

        print(Pemanggangan.muffin())
        print()

        print(Pengemasan.muffin())
        print()

        print(Pelabelan.muffin())
        print()

        print("Produksi Muffin selesai.")