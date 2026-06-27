# models/roti_basah/klepon.py
"""
Subclass Klepon untuk produk kategori Kue Basah Tradisional di Hanari Bakery.

Tanggung Jawab : Diah
Konsep OOP     : Inheritance, Polymorphism (Override Method Abstrak)
"""

from models.produk_roti import ProdukRoti

class Klepon(ProdukRoti):
    """
    Subclass yang merepresentasikan kue basah Klepon.
    Menggunakan metode perebusan dan pelumuran topping kelapa parut.
    """

    def aduk(self) -> str:
        """Implementasi proses pengadonan khas Klepon."""
        return f"[{self.nama_produk}] Mengaduk tepung ketan dengan air pandan hangat hingga kalis dan elastis, lalu dibentuk bulat dengan isian gula merah."

    def rebus(self) -> str:
        """Proses pematangan dengan cara direbus."""
        return f"[{self.nama_produk}] Memasukkan bulatan adonan ke dalam air mendidih, merebus hingga mengapung sebagai tanda matang."

    def topping(self) -> str:
        """Proses pembungkusan dengan topping kelapa."""
        return f"[{self.nama_produk}] Menggulingkan adonan klepon yang telah matang di atas parutan kelapa muda kukus."

    def kemas(self) -> str:
        """Proses pengemasan produk."""
        return f"[{self.nama_produk}] Menata klepon di atas bodi mika mini transparan beralas daun pisang."

    def label(self) -> str:
        """Proses pelabelan produk."""
        return f"[{self.nama_produk}] Menempelkan sticker logo Hanari Bakery Kelompok 6 pada tutup mika."