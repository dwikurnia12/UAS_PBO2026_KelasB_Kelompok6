"""
Menampilkan berbagai informasi dan hasil proses
pada sistem Hanari Bakery.



Tanggung jawab   : Dwi Kurniawati Hanifah (K3525056)
Konsep OOP       : Single Responsibility Principle (SRP),
                   User Interface (UI)

"""

class Display:

    @staticmethod
    def judul():
        print("\n" + "=" * 50)
        print("HANARI BAKERY")
        print("=" * 50)

    @staticmethod
    def garis():
        print("-" * 50)

    @staticmethod
    def sukses(pesan):
        print(f"\n[SUKSES] {pesan}")

    @staticmethod
    def error(pesan):
        print(f"\n[ERROR] {pesan}")
    
    @staticmethod
    def info(pesan):
        print(f"\n[INFO] {pesan}")

    @staticmethod
    def keluar():
        print("\n Terima kasih telah menggunakan Hanari Bakery")