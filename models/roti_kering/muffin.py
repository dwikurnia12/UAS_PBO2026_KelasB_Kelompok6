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

class Muffin(ProdukRoti, Pengadonan, Pengembangan, Pemanggangan, Pengemasan, Pelabelan, Topping):

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
            kode_produk="MF001",
            bahan_baku=bahan,
            jumlah_produksi=12,
            biaya_produksi=50000,
            harga_jual_per_pcs=10000
        )
        self.__langkah_simulasi = []
        self.__pengemasan = "Belum dikemas"
        self.__pelabelan = "Belum diberi label"

    # Method abstrak dari ProdukRoti
    def pengadonan(self):
        self.__langkah_simulasi.append(Pengadonan.muffin())

    def pengemasan(self, jenis_kemasan):
        self.__pengemasan = jenis_kemasan
        self.__langkah_simulasi.append(
            f"- Mengemas produk menggunakan {jenis_kemasan}."
        )

    def pelabelan(self, teks_label):
        self.__pelabelan = teks_label
        self.__langkah_simulasi.append(
            f"- Melabeli produk dengan teks: '{teks_label}'."
        )

    # Simulasi produksi
    def simulasi_produksi(self):
        self.__langkah_simulasi.clear()

        self.pengadonan()
        self.__langkah_simulasi.append(Pengembangan.muffin())
        self.__langkah_simulasi.append(Topping.muffin())
        self.__langkah_simulasi.append(Pemanggangan.muffin())

        self.pengemasan("Paper Cup + Mika")
        self.pelabelan("MF001-Kelompok6B")

    def tampilkan_info(self):
        print(super().tampilkan_info())

        print("\n--- Langkah Simulasi Produksi ---")

        if not self.__langkah_simulasi:
            print("(Belum ada simulasi produksi)")
        else:
            for langkah in self.__langkah_simulasi:
                print(langkah)

        print(f"Kemasan      : {self.__pengemasan}")
        print(f"Label Produk : {self.__pelabelan}")