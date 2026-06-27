# models/roti_basah/kue_soes.py
"""
Subclass KueSoes untuk produk kategori Kue Basah Baked di Hanari Bakery.

Tanggung Jawab : Diah
Konsep OOP     : Inheritance, Polymorphism (Override Method Abstrak)
"""

from models.produk_roti import ProdukRoti

class KueSoes(ProdukRoti):
    """
    Subclass yang merepresentasikan kue basah Kue Soes (Choux Pastry).
    Menggunakan teknik pemanggangan suhu tinggi untuk membentuk rongga.
    """

    def aduk(self) -> str:
        """Implementasi proses pengadonan khas Kue Soes."""
        return f"[{self.nama_produk}] Memasak air, mentega, dan terigu hingga kalis (choux paste), lalu diaduk dengan telur ayam setelah adonan mendingin."

    def panggang(self) -> str:
        """Proses pematangan kulit soes dengan oven."""
        return f"[{self.nama_produk}] Memanggang adonan kulit soes di oven bersuhu tinggi (200°C) agar mengembang dan membentuk rongga sempurna."

    def isi_vla(self) -> str:
        """Proses pengisian isi kue soes."""
        return f"[{self.nama_produk}] Menyuntikkan vla custard vanilla cream manis ke dalam rongga kulit soes yang telah matang."

    def kemas(self) -> str:
        """Proses pengemasan produk."""
        return f"[{self.nama_produk}] Menata kue soes ke dalam box kertas kardus pastry higienis."

    def label(self) -> str:
        """Proses pelabelan produk."""
        return f"[{self.nama_produk}] Memberikan kode produk {self.kode_produk} pada kemasan luar box."