from models.produk_roti import ProdukRoti
from interfaces import Pengembangan, Pemanggangan, Topping, Pengemasan, Pelabelan

class RotiManis(ProdukRoti, Pengembangan, Pemanggangan, Topping, Pengemasan, Pelabelan):
    def __init__(self, nama_produk: str, harga_beli: float, harga_jual: float):
        bahan = [
            "250 gram Tepung terigu protein tinggi",
            "50 gram Gula pasir",
            "6 gram Ragi instan",
            "1/4 sdt Garam",
            "1 butir Kuning telur",
            "125 ml Susu cair dingin",
            "30 gram Margarin"
        ]
        super().__init__(nama_produk, harga_beli, harga_jual, bahan)
        self.__langkah_simulasi = []
        self.__topping = "Belum diberi topping"
        self.__kemasan = "Belum dikemas"
        self.__label = "Belum diberi label"

    def kembangkan(self, durasi: int) -> None:
        self.__langkah_simulasi.append(f"- Mengembangkan adonan (proofing) selama {durasi} menit.")

    def panggang(self, suhu: int, durasi: int) -> None:
        self.__langkah_simulasi.append(f"- Oven adonan dengan suhu {suhu}°C selama {durasi} menit.")

    def beri_topping(self, jenis_topping: str) -> None:
        self.__topping = jenis_topping
        self.__langkah_simulasi.append(f"- Memberikan topping: {jenis_topping}.")

    def kemas(self, jenis_kemasan: str) -> None:
        self.__kemasan = jenis_kemasan

    def beri_label(self, teks_label: str) -> None:
        self.__label = teks_label

    def simulasi_produksi(self) -> None:
        self.__langkah_simulasi.clear()
        self.__langkah_simulasi.append("1. Mencampur tepung terigu, gula pasir, dan ragi instan dalam wadah.")
        self.__langkah_simulasi.append("2. Memasukkan kuning telur dan susu cair dingin, uleni hingga setengah kalis.")
        self.__langkah_simulasi.append("3. Menambahkan margarin dan garam, uleni kembali hingga kalis elastis.")
        self.kembangkan(45)
        self.__langkah_simulasi.append("4. Membagi adonan menjadi beberapa bagian, diisi sesuai selera, lalu istirahatkan kembali.")
        self.panggang(180, 20)

    def tampilkan_info(self) -> None:
        super().tampilkan_info()
        print("\n--- Langkah/Simulasi Produksi ---")
        for langkah in self.__langkah_simulasi:
            print(langkah)
        print(f"Topping      : {self.__topping}")
        print(f"Kemasan      : {self.__kemasan}")
        print(f"Label Produk : {self.__label}")