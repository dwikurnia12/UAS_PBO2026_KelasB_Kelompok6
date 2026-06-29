"""
Subclass ButterCookies untuk produk Hanari Bakery.

Tanggung Jawab : Arofa Karindra Bimantara (K3525051)
Konsep OOP     : Inheritance, Polymorphism
"""
from models.produk_roti import ProdukRoti

from interfaces.pengadonan import Pengadonan
from interfaces.pemanggangan import Pemanggangan
from interfaces.pengemasan import Pengemasan
from interfaces.pelabelan import Pelabelan

class ButterCookies(ProdukRoti, Pengadonan, Pemanggangan, Pengemasan, Pelabelan):
    def __init__(self):
        super().__init__(
            nama_produk="Butter Cookies",
            kode_produk="BC001",
            bahan_baku={
                "Butter (Mentega)": (150, "gram"),
                "Gula Halus": (70, "gram"),
                "Ekstrak Vanila": (1, "sdt"),
                "Kuning Telur": (1, "butir"),
                "Tepung Terigu Protein Rendah": (200, "gram"),
                "Susu Bubuk": (20, "gram")
            },
            jumlah_produksi=30,
            biaya_produksi=45000,
            harga_jual_per_pcs=3000
        )
        self.__langkah_simulasi = []
        self.__pengemasan = "Belum dikemas"
        self.__pelabelan = "Belum diberi label"

    def pengadonan(self) -> None:
        self.__langkah_simulasi.append(Pengadonan.butter_cookies())

    def pemanggangan(self, suhu: int, durasi: int) -> None:
        self.__langkah_simulasi.append(Pemanggangan.butter_cookies())
        
    def pengemasan(self, jenis_kemasan: str) -> None:
        self.__langkah_simulasi.append(Pengemasan.butter_cookies())

    def pelabelan(self, teks_label: str) -> None:
        self.__langkah_simulasi.append(Pelabelan.butter_cookies())

    def simulasi_produksi(self) -> None:
        self.__langkah_simulasi.clear()

        self.pengadonan()
        self.pemanggangan(150, 25)
        self.pengemasan("Toples Plastik 500 g")
        self.pelabelan("Butter Cookies Hanari Bakery")
    
    def tampilkan_info(self) -> None:
        print(super().tampilkan_info())

        print("\n--- Langkah Simulasi Produksi ---")

        if not self.__langkah_simulasi:
            print("(Belum ada simulasi)")
        else:
            for langkah in self.__langkah_simulasi:
                print(langkah)

        print(f"Kemasan      : {self.__pengemasan}")
        print(f"Label Produk : {self.__pelabelan}")