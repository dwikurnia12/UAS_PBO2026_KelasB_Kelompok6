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

class KueSoes(ProdukRoti, Pengadonan, Pemanggangan, Topping, Pengemasan, Pelabelan):

    def __init__(self):
        bahan = {
            "Tepung Terigu" : (200, "gram"),
            "Mentega"       : (100, "gram"),
            "Air"           : (250, "ml"),
            "Telur"         : (4, "butir"),
            "Garam"         : (1, "sdt"),
            "Vla Vanilla"   : (250, "gram")
        }
        super().__init__(
            nama_produk         ="Kue Soes",
            kode_produk         ="KB002",
            bahan_baku          = bahan,
            jumlah_produksi     =20,
            biaya_produksi      =55000,
            harga_jual_per_pcs  =9000
        )

        self.__langkah_simulasi = []
        self.__pengemasan   = "Belum dikemas"
        self.__pelabelan    = "Belum diberi label"


    # Method abstrak dari ProdukRoti
    def pengadonan(self):
        return Pengadonan.kue_soes()

    # Simulasi proses produksi
    def simulasi_produksi(self):
    
        self.__langkah_simulasi.clear()

        self.__langkah_simulasi.append(self.pengadonan())
        self.__langkah_simulasi.append(Pemanggangan.kue_soes())
        self.__langkah_simulasi.append(Topping.kue_soes())
        self.__langkah_simulasi.append(Pengemasan.kue_soes())
        self.__langkah_simulasi.append(Pelabelan.kue_soes())
        self.__pengemasan   = "Box Pastry"
        self.__pelabelan    = "KB002-Kelompok 6B"
    
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