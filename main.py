"""
Program utama aplikasi Hanari Bakery.

Tanggung jawab   : Dwi Kurniawati Hanifah (K3525056)
Konsep OOP       : Composition, Object Interaction,
                   Single Responsibility Principle (SRP)

"""
from managers.system_bakery import SistemBakery

from ui.menu import Menu
from ui.display import Display

from models.roti_manis import RotiManis
from models.croissant import Croissant

from models.roti_kering.buttercookies import ButterCookies
from models.roti_kering.muffin import Muffin

from models.roti_basah.klepon import Klepon
from models.roti_basah.kue_soes import KueSoes


def main():
    bakery = SistemBakery()

    while True:
        Display.judul()

        pilihan = Menu.tampilkan_menu()

        if pilihan == "1":
            print("\nTambah Produk")
            print("1. Roti Manis")
            print("2. Croissant")
            print("3. Butter Cookies")
            print("4. Muffin")
            print("5. Klepon")
            print("6. Kue Soes")

            pilih =  input("Pilih produk:")

            if pilih == "1":
                bakery.tambah_produk(RotiManis())

            elif pilih == "2":
                bakery.tambah_produk(Croissant())

            elif pilih == "3":
                bakery.tambah_produk(ButterCookies())

            elif pilih == "4":
                bakery.tambah_produk(Muffin())

            elif pilih == "5":
                bakery.tambah_produk(Klepon())

            elif pilih == "6":
                bakery.tambah_produk(KueSoes())
            else:
                Display.error("Pilihan tidak tersedia.")
        
        elif pilihan == "2":

            bakery.tampilkan_semua_produk()

        elif pilihan == "3":

            bakery.tampilkan_katalog()

            kode = input("\nMasukkan kode produk : ").upper()

            jumlah = int(input("Jumlah produksi : "))

            bakery.tampilkan_profit(
                kode,
                jumlah
            )

        elif pilihan == "4":

            bakery.tampilkan_katalog()

            kode = input(
                "\nMasukkan kode produk : "
            ).upper()

            bakery.simulasi_produksi(
                kode
            )

        elif pilihan == "5":

            bakery.tampilkan_katalog()

            kode = input(
                "\nMasukkan kode produk yang dihapus : "
            ).upper()

            bakery.hapus_produk(
                kode
            )

        elif pilihan == "0":

            Display.keluar()

            break

        else:
            Display.erroe(
                "Pilihan menu tidak valid."
            )


if __name__ == "__main__":
    main()

