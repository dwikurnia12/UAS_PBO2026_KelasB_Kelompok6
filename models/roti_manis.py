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

    def aduk(self) -> None:
        pass

    def simulasi_produksi(self) -> None:
        self.aduk()
        self.kembangkan(45)
        self.panggang(180, 20)
        self.beri_topping("Cokelat Ceres")
        self.kemas("Plastik OPP Premium")
        self.beri_label("Roti Manis Kelompok 6B")

    def tampilkan_info(self) -> None:
        print(super().tampilkan_info())