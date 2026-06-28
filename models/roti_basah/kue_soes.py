"""
kue_soes.py
===========
Class Kue Soes
Tanggung Jawab : Diah
"""

from models.produk_roti import ProdukRoti

from interfaces.pengadonan import Pengadonan
from interfaces.pemanggangan import Pemanggangan
from interfaces.topping import Topping
from interfaces.pengemasan import Pengemasan
from interfaces.pelabelan import Pelabelan


class KueSoes(ProdukRoti):

    def __init__(self):
        bahan = {
            "Tepung Terigu": (200, "gram"),
            "Mentega": (100, "gram"),
            "Air": (250, "ml"),
            "Telur": (4, "butir"),
            "Garam": (1, "sdt"),
            "Vla Vanilla": (250, "gram")
        }

        super().__init__(
            nama_produk="Kue Soes",
            kode_produk="KB-002",
            bahan_baku=bahan,
            jumlah_produksi=20,
            biaya_produksi=55000,
            harga_jual_per_pcs=9000
        )

    # Method abstrak dari ProdukRoti
    def aduk(self):
        return Pengadonan.kue_soes()

    # Simulasi proses produksi
    def simulasi_produksi(self):
        print("=" * 50)
        print("SIMULASI PRODUKSI KUE SOES")
        print("=" * 50)

        print(self.aduk())
        print()

        print(Pemanggangan.kue_soes())
        print()

        print(Topping.kue_soes())
        print()

        print(Pengemasan.kue_soes())
        print()

        print(Pelabelan.kue_soes())
        print()

        print("Produksi Kue Soes selesai.")