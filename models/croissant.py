"""
Subclass Croissant untuk produk Hanari Bakery.

Tanggung Jawab : Arofa Karindra Bimantara (K3525051)
Konsep OOP     : Inheritance, Polymorphism
"""
from models.produk_roti import ProdukRoti

from interfaces.pengadonan import Pengadonan
from interfaces.pengembangan import Pengembangan
from interfaces.pemanggangan import Pemanggangan
from interfaces.pengemasan import Pengemasan
from interfaces.pelabelan import Pelabelan

class Croissant(ProdukRoti, Pengadonan, Pengembangan, Pemanggangan, Pengemasan, Pelabelan):
    def __init__(self):
        super().__init__(
            nama_produk="Croissant",
            kode_produk="CR001",
            bahan_baku={
                "Tepung Terigu Protein Tinggi": (600, "gram"),
                "Ragi": (10, "gram"),
                "Margarin": (60, "gram"),
                "Garam": (1, "sejumput"),
                "Air Dingin": (300, "ml"),
                "Gula Pasir": (1, "sdm"),
                "Korsvet": (250, "gram")
            },
            jumlah_produksi=10,
            biaya_produksi=75000,
            harga_jual_per_pcs=15000
        )

        self.__langkah_simulasi = []
        self.__pengemasan = "Belum dikemas"
        self.__pelabelan = "Belum diberi label"

    def pengadonan(self) -> None:
        self.__langkah_simulasi.append(Pengadonan.croissant())

    def pengembangan(self, durasi: int) -> None:
        self.__langkah_simulasi.append(Pengembangan.croissant())
    
    def pemanggangan(self, suhu: int, durasi: int) -> None:
        self.__langkah_simulasi.append(Pemanggangan.croissant())
        
    def pengemasan(self, jenis_kemasan: str) -> None:
        self.__langkah_simulasi.append(Pengemasan.croissant())

    def pelabelan(self, teks_label: str) -> None:
        self.__langkah_simulasi.append(Pelabelan.croissant())

    def simulasi_produksi(self) -> None:
        self.__langkah_simulasi.clear()

        self.pengadonan()
        self.pengembangan(45)
        self.pemanggangan(200, 18)
        self.pengemasan("Paper Bag Craft")
        self.pelabelan("CR001-Kelompok6B")

    def tampilkan_info(self) -> None:
        print(super().tampilkan_info())

        print("\n--- Langkah Produksi ---")

        if not self.__langkah_simulasi:
            print("(Belum ada simulasi)")
        else:
            for langkah in self.__langkah_simulasi:
                print(langkah)

        print(f"Kemasan      : {self.__pengemasan}")
        print(f"Label Produk : {self.__pelabelan}")