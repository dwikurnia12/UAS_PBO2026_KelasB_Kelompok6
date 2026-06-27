from models.produk_roti import ProdukRoti
from interfaces import Pengembangan, Pemanggangan, Pengemasan, Pelabelan

class Croissant(ProdukRoti, Pengembangan, Pemanggangan, Pengemasan, Pelabelan):
    def __init__(self, nama_produk: str, harga_beli: float, harga_jual: float):
        bahan = [
            "600 gram Tepung terigu protein tinggi",
            "10 gram Ragi",
            "60 gram Margarin",
            "Sejumput Garam",
            "-+ 300ml Air dingin",
            "1 sdm Gula pasir",
            "250 gram Korsvet"
        ]
        super().__init__(nama_produk, harga_beli, harga_jual, bahan)
        self.__langkah_simulasi = []
        self.__kemasan = "Belum dikemas"
        self.__label = "Belum diberi label"

    def kembangkan(self, durasi: int) -> None:
        self.__langkah_simulasi.append(f"- Melakukan fermentasi adonan selama {durasi} menit.")

    def panggang(self, suhu: int, durasi: int) -> None:
        self.__langkah_simulasi.append(f"- Baking adonan croissant di oven dengan suhu {suhu}°C selama {durasi} menit.")

    def kemas(self, jenis_kemasan: str) -> None:
        self.__kemasan = jenis_kemasan

    def beri_label(self, teks_label: str) -> None:
        self.__label = teks_label

    def simulasi_produksi(self) -> None:
        self.__langkah_simulasi.clear()
        self.__langkah_simulasi.append("1. Masukkan tepung, margarin, ragi, dan garam, aduk jadi satu di kom adonan.")
        self.__langkah_simulasi.append("2. Campur air es dan gula pasir hingga larut, masukkan ke kom adonan, uleni hingga setengah kalis.")
        self.__langkah_simulasi.append("3. Kempiskan adonan, tipiskan, beri korsvet di tengah, lipat adonan -+ 4 kali hingga bentuk persegi panjang.")
        self.__langkah_simulasi.append("4. Lakukan pemotongan bentuk segitiga lalu gulung membentuk adonan croissant.")
        self.kembangkan(45)
        self.panggang(200, 18)

    def tampilkan_info(self) -> None:
        super().tampilkan_info()
        print("\n--- Langkah/Simulasi Produksi ---")
        for langkah in self.__langkah_simulasi:
            print(langkah)
        print(f"Kemasan      : {self.__kemasan}")
        print(f"Label Produk : {self.__label}")