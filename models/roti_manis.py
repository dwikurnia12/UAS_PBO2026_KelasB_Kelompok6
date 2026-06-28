"""
Subclass Roti Manis untuk produk Hanari Bakery.

Tanggung Jawab : Arofa Karindra Bimantara (K3525051)
Konsep OOP     : Inheritance, Polymorphism
"""
from models.produk_roti import ProdukRoti
from interfaces import (Pengadonan, Pengembangan, Pemanggangan, Topping, Pengemasan, Pelabelan)

class RotiManis(ProdukRoti, Pengadonan, Pengembangan, Pemanggangan, Topping, Pengemasan, Pelabelan):
    def __init__(self):
        super().__init__(
            nama_produk="Roti Manis",
            kode_produk="RM001",
            bahan_baku={
                "Tepung Terigu": (500, "gram"),
                "Gula Pasir": (100, "gram"),
                "Ragi Instan": (12, "gram"),
                "Garam": (5, "gram"),
                "Kuning Telur": (2, "butir"),
                "Susu Cair": (250, "ml"),
                "Margarin": (60, "gram")
            },
            jumlah_produksi=20,
            biaya_produksi=85000,
            harga_jual_per_pcs=8000
        )

        self.__langkah_simulasi = []
        self.__topping = "Belum diberi topping"
        self.__pengemasan = "Belum dikemas"
        self.__pelabelan = "Belum diberi label"

    def pengadonan(self):
        self.__langkah_simulasi.append(Pengadonan.roti_manis())

    def pengembangan(self, durasi: int) -> None:
        self.__langkah_simulasi.append(f"- Mengembangkan adonan (proofing) selama {durasi} menit.")

    def pemanggangan(self, suhu: int, durasi: int) -> None:
        self.__langkah_simulasi.append(f"- Oven adonan dengan suhu {suhu}°C selama {durasi} menit.")

    def topping(self, jenis_topping: str) -> None:
        self.__topping = jenis_topping
        self.__langkah_simulasi.append(f"- Memberikan topping: {jenis_topping}.")

    def pengemasan(self, jenis_kemasan: str) -> None:
        self.__pengemasan = jenis_kemasan
        self.__langkah_simulasi.append(f"- Mengemas produk menggunakan {jenis_kemasan}.")

    def pelabelan(self, teks_label: str) -> None:
        self.__pelabelan = teks_label
        self.__langkah_simulasi.append(f"- Melabeli produk dengan teks: '{teks_label}'.")

    def simulasi_produksi(self) -> None:
        self.pengadonan()
        self.pengembangan(45)
        self.pemanggangan(180, 20)
        self.topping("Cokelat Ceres")
        self.pengemasan("Plastik OPP Premium")
        self.pelabelan("RM001-Kelompok 6B")

    def tampilkan_info(self) -> None:
        print(super().tampilkan_info())
        print("\n--- Langkah/Simulasi Produksi ---")
        if not self.__langkah_simulasi:
            print("(Belum ada simulasi produksi yang dijalankan)")
        else:
            for langkah in self.__langkah_simulasi:
                print(langkah)
        print(f"Topping      : {self.__topping}")
        print(f"Kemasan      : {self.__pengemasan}")
        print(f"Label Produk : {self.__pelabelan}")
