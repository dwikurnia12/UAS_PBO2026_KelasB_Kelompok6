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

    def aduk(self) -> None:
        pass

    def simulasi_produksi(self) -> None:
        self.aduk()
        self.kembangkan(45)
        self.panggang(200, 18)
        self.kemas("Paper Bag Craft")
        self.beri_label("Premium Pastry Series")

    def tampilkan_info(self) -> None:
        print(super().tampilkan_info())