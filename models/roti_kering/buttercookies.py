from models.produk_roti import ProdukRoti
from interfaces import Pemanggangan, Pengemasan, Pelabelan

class ButterCookies(ProdukRoti, Pemanggangan, Pengemasan, Pelabelan):
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
        self.__kemasan = "Belum dikemas"
        self.__label = "Belum diberi label"

    def panggang(self, suhu: int, durasi: int) -> None:
        self.__langkah_simulasi.append(f"- Memanggang kue di oven dengan suhu {suhu}°C selama {durasi} menit.")

    def kemas(self, jenis_kemasan: str) -> None:
        self.__kemasan = jenis_kemasan
        self.__langkah_simulasi.append(f"- Mengemas produk menggunakan {jenis_kemasan}.")

    def beri_label(self, teks_label: str) -> None:
        self.__label = teks_label
        self.__langkah_simulasi.append(f"- Melabeli produk dengan teks: '{teks_label}'.")

    def simulasi_produksi(self) -> None:
        self.__langkah_simulasi.clear()
        self.__langkah_simulasi.append("1. Mengocok butter dan gula halus dengan mixer hingga lembut dan pucat.")
        self.__langkah_simulasi.append("2. Memasukkan kuning telur dan ekstrak vanila, lalu diaduk rata.")
        self.__langkah_simulasi.append("3. Memasukkan tepung terigu dan susu bubuk sambil diayak, diaduk menggunakan spatula.")
        self.__langkah_simulasi.append("4. Mencetak atau menyemprotkan adonan kue di atas loyang.")
        self.panggang(150, 25)

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