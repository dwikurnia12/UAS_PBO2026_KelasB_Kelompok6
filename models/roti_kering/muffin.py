# models/roti_kering/muffin.py
"""
Subclass Muffin untuk kategori Kue Kering/Cupcake di Hanari Bakery.

Tanggung Jawab : Diah
Konsep OOP     : Inheritance, Polymorphism (Override Method Abstrak)
"""

from models.produk_roti import ProdukRoti

class Muffin(ProdukRoti):
    """
    Subclass yang merepresentasikan kue Muffin.
    Memerlukan pendiaman adonan singkat (pengembangan) dan taburan topping.
    """

    def aduk(self) -> str:
        """Implementasi proses pengadonan abstrak untuk Muffin."""
        return f"[{self.nama_produk}] Mencampur adonan basah dan adonan kering secara terpisah lalu diaduk perlahan (muffin method) agar tidak bantat."

    def kembangkan(self) -> str:
        """Proses pengembangan adonan singkat (Ayun Interface)."""
        return f"[{self.nama_produk}] Mendiamkan adonan di dalam cup cetakan selama 10 menit agar baking powder aktif bekerja."

    def topping(self) -> str:
        """Proses pemberian topping sebelum oven (Ayun Interface)."""
        return f"[{self.nama_produk}] Menaburkan choco chips premium di atas adonan mentah dalam cup."

    def panggang(self) -> str:
        """Proses pematangan dengan oven (Ayun Interface)."""
        return f"[{self.nama_produk}] Memanggang muffin di oven bersuhu 190°C hingga mengembang merekah cokelat keemasan."

    def kemas(self) -> str:
        """Proses pengemasan kue kering (Ayun Interface)."""
        return f"[{self.nama_produk}] Memasukkan muffin matang ke dalam wadah mika kubus mika satuan."

    def label(self) -> str:
        """Proses pelabelan (Ayun Interface)."""
        return f"[{self.nama_produk}] Menempelkan barcode harga produk {self.kode_produk} di bawah kemasan."