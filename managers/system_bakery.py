from model.roti_manis import RotiManis
from model.croissant import Croissant

from models.roti_kering.buttercookies import ButterCookies
from models.roti_kering.muffin import Muffin

from models.roti_basah.klepon import Klepon
from models.roti_basah.kue_soes import KueSoes

class SistemBakery:
    def __init__(self):
        self.daftar_produk = {}
        self.inisialisasi_produk()


def inisialisasi_produk(self):

    if not DATA_PRODUK:
        print("Data produk belum tersedia")
        return
    
    for produk in DATA_PRODUK:
        self.data_produk[
            produk.kode_produk
        ] = produk


def tambah_produk(self, produk):

    if produk.kode_produk in self.daftar_produk:

        print(
            f"Prodik dengan kode"
            f"{produk.kode_produk} sudah ada!"
        )



        
