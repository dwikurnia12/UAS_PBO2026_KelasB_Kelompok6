"""
Pusat penyimpanan data produk default yang tersedia
di Hanari Bakery.

Tanggung jawab   : Dwi Kurniawati Hanifah (K3525056)
Konsep OOP       : Object Instantiation, Aggregation, Single Responsibility Principle (SRP)

"""
from models.roti_manis import RotiManis
from models.croissant import Croissant

from models.roti_kering.butter_cookies import ButterCookies
from models.roti_kering.muffin import Muffin

from models.roti_basah.klepon import Klepon
from models.roti_basah.kue_soes import KueSoes

# ==========================================
# MEMBUAT OBJECT PRODUK
# ==========================================

roti_manis = RotiManis()
croissant = Croissant()
butter_cookies = ButterCookies()
muffin = Muffin()
klepon = Klepon()
kue_soes = KueSoes()

# ==========================================
# DAFTAR PRODUK DEFAULT
# ==========================================

DATA_PRODUK = [
    roti_manis,
    croissant,
    butter_cookies,
    muffin,
    klepon,
    kue_soes
]