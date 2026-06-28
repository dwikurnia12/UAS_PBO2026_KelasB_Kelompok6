# models/roti_basah/klepon.py
"""
Subclass Klepon untuk kategori Kue Basah di Hanari Bakery.

Tanggung Jawab : Diah
Konsep OOP     : Inheritance, Polymorphism (Override Method Abstrak)
"""

from models.produk_roti import ProdukRoti

class Klepon(ProdukRoti):
    """
    Subclass yang merepresentasikan kue basah Klepon.
    Menggunakan metode perebusan dan pelumuran kelapa parut.
    """

    def aduk(self) -> str:
        """Implementasi proses pengadonan abstrak untuk Klepon."""
        return f"[{self.nama_produk}] Mengaduk tepung ketan dengan air pandan hangat hingga kalis dan mudah dibentuk bulat dengan isian gula merah."

    def rebus(self) -> str:
        """Proses pematangan dengan direbus (Ayun Interface)."""
        return f"[{self.nama_produk}] Merebus adonan bulat di air mendidih sampai mengapung sebagai tanda matang."

    def topping(self) -> str:
        """Proses pemberian topping kelapa parut (Ayun Interface)."""
        return f"[{self.nama_produk}] Menggulingkan klepon matang di atas parutan kelapa muda yang telah dikukus dengan garam."

    def kemas(self) -> str:
        """Proses pengemasan kue basah (Ayun Interface)."""
        return f"[{self.nama_produk}] Menata beberapa butir klepon di atas mika kecil transparan beralas daun pisang."

    def label(self) -> str:
        """Proses pelabelan (Ayun Interface)."""
        return f"[{self.nama_produk}] Menempelkan sticker logo Hanari Bakery pada segel kemasan mika."