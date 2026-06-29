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
            kode_produk="KB001",
            bahan_baku=bahan,
            jumlah_produksi=20,
            biaya_produksi=40000,
            harga_jual_per_pcs=6000
        )

        self.__langkah_simulasi = []
        self.__pengemasan = "Belum dikemas"
        self.__pelabelan = "Belum diberi label"

    # Method abstrak dari ProdukRoti
    def pengadonan(self):
        return Pengadonan.klepon()
    
    def perebusan(self):
        self.__langkah_simulasi.append(Perebusan.klepon())

    def topping(self):
        self.__langkah_simulasi.append(Topping.klepon())

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
        self.perebusan()
        self.topping()
        self.pengemasan("Mika Transparan")
        self.pelabelan("KB001-Kelompok6B")
    
    def tampilkan_info(self) -> None:
    print(super().tampilkan_info())

    print("\n--- Langkah Simulasi Produksi ---")

    if not self.__langkah_simulasi:
        print("(Belum ada simulasi produksi)")
    else:
        for langkah in self.__langkah_simulasi:
            print(langkah)

    print(f"Kemasan      : {self.__pengemasan}")
    print(f"Label Produk : {self.__pelabelan}")