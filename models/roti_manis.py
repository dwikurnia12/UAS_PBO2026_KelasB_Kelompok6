<<<<<<< Updated upstream
from models.produk_roti import ProdukRoti
from interfaces import Pengembangan, Pemanggangan, Topping, Pengemasan, Pelabelan

class RotiManis(ProdukRoti, Pengembangan, Pemanggangan, Topping, Pengemasan, Pelabelan):
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
        self.__langkah_simulasi.append(f"- Mengemas produk menggunakan {jenis_kemasan}.")

    def beri_label(self, teks_label: str) -> None:
        self.__label = teks_label
        self.__langkah_simulasi.append(f"- Melabeli produk dengan teks: '{teks_label}'.")

    def simulasi_produksi(self) -> None:
        self.__langkah_simulasi.clear()
        self.__langkah_simulasi.append("1. Mencampur tepung terigu, gula pasir, and ragi instan dalam wadah sesuai takaran resep.")
        self.__langkah_simulasi.append("2. Memasukkan kuning telur dan susu cair dingin, uleni hingga setengah kalis.")
        self.__langkah_simulasi.append("3. Menambahkan margarin dan garam, uleni kembali hingga kalis elastis.")
        self.kembangkan(45)
        self.__langkah_simulasi.append(f"4. Membagi adonan menjadi {self.jumlah_produksi} bagian, dibentuk bulat, lalu istirahatkan kembali.")
        self.panggang(180, 20)

    def tampilkan_info(self) -> None:
        super().tampilkan_info()
        print("\n--- Langkah/Simulasi Produksi ---")
        if not self.__langkah_simulasi:
            print("(Belum ada simulasi produksi yang dijalankan)")
        else:
            for langkah in self.__langkah_simulasi:
                print(langkah)
        print(f"Topping      : {self.__topping}")
        print(f"Kemasan      : {self.__kemasan}")
        print(f"Label Produk : {self.__label}")
=======