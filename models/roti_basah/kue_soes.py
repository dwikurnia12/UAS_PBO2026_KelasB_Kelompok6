# models/roti_basah/kue_soes.py
"""
Subclass KueSoes untuk kategori Kue Basah Baked di Hanari Bakery.

Tanggung Jawab : Diah
Konsep OOP     : Inheritance, Polymorphism (Override Method Abstrak)
"""

from models.produk_roti import ProdukRoti

class KueSoes(ProdukRoti):
    """
    Subclass yang merepresentasikan Kue Soes (Choux Pastry).
    Memerlukan pemanggangan suhu tinggi untuk membuat rongga sebelum diisi vla.
    """

    def aduk(self) -> str:
        """Implementasi proses pengadonan abstrak untuk Kue Soes."""
        return f"[{self.nama_produk}] Memasak campuran air, mentega, dan tepung terigu hingga kalis (choux paste), lalu mixer dengan telur setelah dingin."

    def panggang(self) -> str:
        """Proses pematangan kulit soes dengan oven (Ayun Interface)."""
        return f"[{self.nama_produk}] Memanggang adonan kulit soes di dalam oven bersuhu tinggi (200°C) agar mengembang dan berongga."

    def isi_vla(self) -> str:
        """Proses pengisian vla custard pastry."""
        return f"[{self.nama_produk}] Menyuntikkan vla custard vanilla lembut ke dalam rongga kulit soes matang."

    def kemas(self) -> str:
        """Proses pengemasan kue basah (Ayun Interface)."""
        return f"[{self.nama_produk}] Memasukkan kue soes siap saji ke dalam kardus box pastry isi kemasan sedang."

    def label(self) -> str:
        """Proses pelabelan kemasan (Ayun Interface)."""
        return f"[{self.nama_produk}] Menyematkan sticker label identitas kode produk: {self.kode_produk}."