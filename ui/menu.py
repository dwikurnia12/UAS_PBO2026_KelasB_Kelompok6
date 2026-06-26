"""
Menampilkan menu utama aplikasi Hanari Bakery.

Tanggung jawab   : Dwi Kurniawati Hanifah (K3525056)
Konsep OOP       : Single Responsibility Principle (SRP), User Interface (UI)
"""
class Menu:

    @staticmethod
    def tampilkan_menu():

        print("\n" + "=" * 40)
        print("HANARI BAKERY")
        print("=" * 40)

        print("MENU UTAMA")
        print("-" * 40)

        print("1. Tambah Produk Baru")
        print("2. Tampilkan Semua Produk")
        print("3. Kalkulator Estimasi Profit")
        print("4. Simulasi Proses Produksi")
        print("5. Hapus Produk")
        print("0. Keluar")

        print("-" * 40)

        pilihan =  input("Masukkan pilihan : ")
        return pilihan
    