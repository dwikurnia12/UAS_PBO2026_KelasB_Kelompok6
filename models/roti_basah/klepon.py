"""
klepon.py
=========
Class Klepon
Tanggung Jawab : Diah
"""

from models.produk_roti import ProdukRoti

from interfaces.pengadonan import Pengadonan
from interfaces.perebusan import Perebusan
from interfaces.topping import Topping
from interfaces.pengemasan import Pengemasan
from interfaces.pelabelan import Pelabelan


class Klepon(ProdukRoti):

    def __init__(self):
        bahan = {
            "Tepung Ketan": (250, "gram"),
            "Air Hangat": (180, "ml"),
            "Pasta Pandan": (1, "sdt"),
            "Gula Merah": (100, "gram"),
            "Kelapa Parut": (150, "gram")
        }

        super().__init__(
            nama_produk="Klepon",
            kode_produk="KB-001",
            bahan_baku=bahan,
            jumlah_produksi=20,
            biaya_produksi=40000,
            harga_jual_per_pcs=6000
        )

    # Method abstrak dari ProdukRoti
    def aduk(self):
        return Pengadonan.klepon()

    # Simulasi produksi
    def simulasi_produksi(self):
        print("=" * 50)
        print("SIMULASI PRODUKSI KLEPON")
        print("=" * 50)

        print(self.aduk())
        print()

        print(Perebusan.klepon())
        print()

        print(Topping.klepon())
        print()

        print(Pengemasan.klepon())
        print()

        print(Pelabelan.klepon())
        print()

        print("Produksi Klepon selesai.")