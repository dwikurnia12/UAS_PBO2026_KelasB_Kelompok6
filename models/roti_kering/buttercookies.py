from models.produk_roti import ProdukRoti
from interfaces import Pemanggangan, Pengemasan, Pelabelan

class ButterCookies(ProdukRoti, Pemanggangan, Pengemasan, Pelabelan):
    def __init__(self, nama_produk: str, harga_beli: float, harga_jual: float):
        bahan = [
            "150 gram Butter (mentega)",
            "70 gram Gula halus",
            "1 sdt Ekstrak vanila",
            "1 butir Kuning telur",
            "200 gram Tepung terigu protein rendah",
            "20 gram Susu bubuk"
        ]
        super().__init__(nama_produk, harga_beli, harga_jual, bahan)
        self.__langkah_simulasi = []
        self.__kemasan = "Belum dikemas"
        self.__label = "Bel_um diberi label"

    def panggang(self, suhu: int, durasi: int) -> None:
        self.__langues_simulasi = self.__langkah_simulasi.append(f"- Memanggang kue di oven dengan suhu {suhu}°C selama {durasi} menit.")

    def kemas(self, jenis_kemasan: str) -> None:
        self.__kemasan = jenis_kemasan

    def beri_label(self, teks_label: str) -> None:
        self.__label = teks_label

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
        for langkah in self.__langkah_simulasi:
            print(langkah)
        print(f"Kemasan      : {self.__kemasan}")
        print(f"Label Produk : {self.__label}")