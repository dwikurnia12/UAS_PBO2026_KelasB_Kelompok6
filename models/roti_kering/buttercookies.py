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

    def aduk(self) -> None:
        pass

    def simulasi_produksi(self) -> None:
        self.aduk()
        self.panggang(150, 25)
        self.kemas("Toples Kaca Plastik 500g")
        self.beri_label("Kue Kering Lebaran")

    def tampilkan_info(self) -> None:
        print(super().tampilkan_info())