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
            biaya_produksi=55000,
            harga_jual_per_pcs=2500
        )
        self.__langkah_simulasi = []
        self.__pengemasan = "Belum dikemas"
        self.__pelabelan = "Belum diberi label"

    def pengadonan(self):
        self.__langkah_simulasi.append(
            Pengadonan.butter_cookies()
        )
    def pemanggangan(self, suhu, durasi):
        self.__langkah_simulasi.append(
            f"- Memanggang butter cookies pada suhu {suhu}°C selama {durasi} menit."
        )
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

    def simulasi_produksi(self) -> None:
        self.__langkah_simulasi.clear()

        self.pengadonan()
        self.pemanggangan(150,25)
        self.pengemasan("Toples Plastik 500 g")
        self.pelabelan("Butter Cookies Hanari Bakery")
    
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