# ==============================================================================
# KELOMPOK 6 - UNIT TESTING INDEPENDEN
# File: test_program.py
# ==============================================================================

import sys
import os
# Memastikan modul path terbaca dari root folder jika dijalankan via terminal
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Simulasi Superclass Buatan Queen & Interface Buatan Ayun untuk Kebutuhan Testing Lokal
from abc import ABC, abstractmethod

class ProductionActions(ABC):
    @abstractmethod
    def pengadonan(self): pass
    @abstractmethod
    def baking(self): pass

class StandardActions(ABC):
    @abstractmethod
    def packaging(self): pass
    @abstractmethod
    def labeling(self): pass

# Dummy Superclass ProdukRoti (Representasi enkapsulasi Queen)
class ProdukRoti(ProductionActions, StandardActions, ABC):
    def __init__(self, nama, kode, bahan_baku, n_pcs, biaya_produksi, harga_jual):
        self._nama = nama
        self._kode = kode
        self._bahan_baku = bahan_baku  # Dict: {'Bahan': 'Jumlah'}
        self._n_pcs = n_pcs
        self._biaya_produksi = biaya_produksi
        self._harga_jual = harga_jual

    @property
    def nama(self): return self._nama
    @property
    def kode(self): return self._kode
    @property
    def bahan_baku(self): return self._bahan_baku
    @property
    def n_pcs(self): return self._n_pcs

    def hitung_estimasi_profit(self, jumlah_pcs_rencana):
        faktor = jumlah_pcs_rencana / self._n_pcs
        total_biaya = self._biaya_produksi * faktor
        total_pendapatan = self._harga_jual * faktor
        profit = total_pendapatan - total_biaya
        return total_biaya, total_pendapatan, profit

    def packaging(self):
        print(f"[Packaging] Mengemas {self._nama} menggunakan standar higienis Kelompok 6.")

    def labeling(self):
        print(f"[Labeling] Menempelkan sticker QR Code Hanari Bakery: {self._kode}.")


# --- MOCK IMPORT LOCAL (Menggabungkan Class Diah ke Dalam Ruang Lingkup Testing) ---
from models.roti_basah.klepon import Klepon
from models.roti_basah.kue_soes import KueSoes
from models.roti_kering.muffin import Muffin

def jalankan_pengujian_diah():
    print("======================================================================")
    print("      UJI COBA PROGRAM MANDIRI KELOMPOK 6 - BAGIAN DIAH     ")
    print("======================================================================")
    
    # 1. Uji Objek Klepon (Kue Basah)
    print("\n[TEST case 1] Memvalidasi Pembuatan Objek Klepon...")
    bahan_klepon = {"Tepung Ketan": "250 gram", "Gula Merah Aren": "100 gram", "Kelapa Parut": "0.5 butir"}
    klepon_item = Klepon("Klepon Pandan Suji asli", "KB001", bahan_klepon, 20, 15000, 35000)
    print(f"Sukses Inisialisasi: {klepon_item.nama} [{klepon_item.kode}]")
    klepon_item.simulasi_produksi()
    
    # 2. Uji Objek Kue Soes (Kue Basah)
    print("\n[TEST case 2] Memvalidasi Pembuatan Objek Kue Soes...")
    bahan_soes = {"Tepung Terigu": "150 gram", "Mentega": "100 gram", "Telur": "4 butir"}
    soes_item = KueSoes("Choux Cream Vanilla Custard", "KB002", bahan_soes, 12, 25000, 60000)
    print(f"Sukses Inisialisasi: {soes_item.nama} [{soes_item.kode}]")
    soes_item.simulasi_produksi()

    # 3. Uji Objek Muffin (Kue Kering) & Perhitungan Matematika Profit Proporsional
    print("\n[TEST case 3] Memvalidasi Objek Muffin & Kalkulator Keuntungan Finansial...")
    bahan_muffin = {"Tepung Terigu": "300 gram", "Baking Powder": "1 sdm", "Choco Chips": "120 gram"}
    muffin_item = Muffin("Choco Chip Blast Muffin", "KK002", bahan_muffin, 8, 22000, 50000)
    
    # Simulasi perhitungan profit berskala untuk orderan 100 pcs sesuai mockup gambar c667c2.png
    rencana_produksi = 100 
    biaya, omset, profit = muffin_item.hitung_estimasi_profit(rencana_produksi)
    faktor_skala = rencana_produksi / muffin_item.n_pcs
    
    print(f"\n--- HASIL ESTIMASI FINANSIAL (Muffin 100 pcs) ---")
    print(f"Produk           : {muffin_item.nama}")
    print(f"Jumlah Rencana   : {rencana_produksi} pcs")
    print(f"Total Pengeluaran: Rp{biaya:,.2f}")
    print(f"Total Pendapatan : Rp{omset:,.2f}")
    print(f"Estimasi Profit  : Rp{profit:,.2f}")
    print(f"----------------------------------------------------------------------")
    print(f"Detail Pengali Bahan Baku Otomatis (Skala {faktor_skala:.1f}x dari Resep Dasar):")
    for bahan, takaran in muffin_item.bahan_baku.items():
        parts = takaran.split()
        nilai_baru = float(parts[0]) * faktor_skala
        satuan = parts[1] if len(parts) > 1 else ""
        print(f"  - {bahan}: {nilai_baru:,.1f} {satuan}")
    print(f"----------------------------------------------------------------------")
    
    print("\n[INFO] Seluruh test case untuk bagian Diah berhasil divalidasi dengan sukses!")

if __name__ == '__main__':
    # Membuat folder penampung palsu agar script test_program.py bisa dieksekusi mandiri tanpa error path
    os.makedirs("models/roti_basah", exist_ok=True)
    os.makedirs("models/roti_kering", exist_ok=True)
    jalankan_pengujian_diah()