"""
Subclass Roti Manis untuk produk Hanari Bakery.

Tanggung Jawab : Arofa Karindra Bimantara (K3525051)
Konsep OOP     : Inheritance, Polymorphism
"""
from models.produk_roti import ProdukRoti

from interfaces.pengadonan import Pengadonan
from interfaces.pengembangan import Pengembangan
from interfaces.pemanggangan import Pemanggangan
from interfaces.topping import Topping
from interfaces.pengemasan import Pengemasan
from interfaces.pelabelan import Pelabelan

class RotiManis(ProdukRoti, Pengadonan, Pengembangan, Pemanggangan, Topping, Pengemasan, Pelabelan):
    def __init__(self):
        super().__init__(
            nama_produk ="Roti Manis",
            kode_produk ="RM001",
            bahan_baku  ={
                "Tepung Terigu" : (500, "gram"),
                "Gula Pasir"    : (100, "gram"),
                "Ragi Instan"   : (12, "gram"),
                "Garam"         : (5, "gram"),
                "Kuning Telur"  : (2, "butir"),
                "Susu Cair"     : (250, "ml"),
                "Margarin"      : (60, "gram")
            },
            jumlah_produksi=12,
            biaya_produksi=35000,
            harga_jual_per_pcs=5000
        )

        self.__langkah_simulasi = []
        self.__topping      = "Belum diberi topping"
        self.__pengemasan   = "Belum dikemas"
        self.__pelabelan    = "Belum diberi label"

    def pengadonan(self) -> None:
        self.__langkah_simulasi.append(Pengadonan.roti_manis())

    def pengembangan(self, durasi: int) -> None:
        self.__langkah_simulasi.append(Pengembangan.roti_manis())

    def pemanggangan(self, suhu: int, durasi: int) -> None:
        self.__langkah_simulasi.append(Pemanggangan.roti_manis())

    def topping(self, jenis_topping: str) -> None:
        self.__topping = jenis_topping
        self.__langkah_simulasi.append(Topping.roti_manis())

    def pengemasan(self, jenis_kemasan: str) -> None:
        self.__pengemasan = jenis_kemasan
        self.__langkah_simulasi.append(Pengemasan.roti_manis())

    def pelabelan(self, teks_label: str) -> None:
        self.__pelabelan = teks_label
        self.__langkah_simulasi.append(Pelabelan.roti_manis())

    def simulasi_produksi(self) -> None:
        self.__langkah_simulasi.clear()

        self.pengadonan()
        self.pengembangan(45)
        self.pemanggangan(180, 20)
        self.topping("Cokelat Ceres")
        self.pengemasan("Plastik OPP Premium")
        self.pelabelan("RM001-Kelompok 6B")

    def tampilkan_info(self) -> None:
        print(super().tampilkan_info())

        print("\n--- Langkah Simulasi Produksi ---")

        if not self.__langkah_simulasi:
            print("(Belum ada simulasi)")
        else:
            for langkah in self.__langkah_simulasi:
                print(langkah)

        print(f"Topping      : {self.__topping}")
        print(f"Kemasan      : {self.__pengemasan}")
        print(f"Label Produk : {self.__pelabelan}")