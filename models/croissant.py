from models.produk_roti import ProdukRoti
from interfaces import Pengembangan, Pemanggangan, Pengemasan, Pelabelan

class Croissant(ProdukRoti, Pengembangan, Pemanggangan, Pengemasan, Pelabelan):
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
            jumlah_produksi=15,
            biaya_produksi=95000,
            harga_jual_per_pcs=15000
        )
        self.__langkah_simulasi = []
        self.__kemasan = "Belum dikemas"
        self.__label = "Belum diberi label"

    def kembangkan(self, durasi: int) -> None:
        self.__langkah_simulasi.append(f"- Melakukan fermentasi adonan selama {durasi} menit.")

    def panggang(self, suhu: int, durasi: int) -> None:
        self.__langkah_simulasi.append(f"- Baking adonan croissant di oven dengan suhu {suhu}°C selama {durasi} menit.")

    def kemas(self, jenis_kemasan: str) -> None:
        self.__kemasan = jenis_kemasan
        self.__langkah_simulasi.append(f"- Mengemas produk menggunakan {jenis_kemasan}.")

    def beri_label(self, teks_label: str) -> None:
        self.__label = teks_label
        self.__langkah_simulasi.append(f"- Melabeli produk dengan teks: '{teks_label}'.")

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
        if not self.__langkah_simulasi:
            print("(Belum ada simulasi produksi yang dijalankan)")
        else:
            for langkah in self.__langkah_simulasi:
                print(langkah)
        print(f"Kemasan      : {self.__kemasan}")
        print(f"Label Produk : {self.__label}")