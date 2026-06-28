"""
=========================================================
PELABELAN PRODUK BAKERY
=========================================================
Interface proses pelabelan produk Hanari Bakery.

Tanggung jawab : Febriana Putri (K3525007)
Konsep OOP     : Interface, Single Responsibility Principle (SRP)
"""

class Pelabelan:

    @staticmethod
    def roti_manis():
        return (
            "[PELABELAN - Roti Manis]\n"
            "  Label: nama produk, tanggal produksi, "
            "kedaluwarsa, kode RM-001."
        )

    @staticmethod
    def croissant():
        return (
            "[PELABELAN - Croissant]\n"
            "  Label: nama produk, tanggal produksi, "
            "kedaluwarsa, kode CR-001."
        )

    @staticmethod
    def butter_cookies():
        return (
            "[PELABELAN - Butter Cookies]\n"
            "  Label: nama produk, tanggal produksi, "
            "kedaluwarsa, kode BC-001."
        )

    @staticmethod
    def muffin():
        return (
            "[PELABELAN - Muffin]\n"
            "  Label: nama produk, tanggal produksi, "
            "kedaluwarsa, kode MF-001."
        )

    @staticmethod
    def klepon():
        return (
            "[PELABELAN - Klepon]\n"
            "  Label: nama produk, tanggal produksi, "
            "kedaluwarsa 1 hari, kode KB-001."
        )

    @staticmethod
    def kue_soes():
        return (
            "[PELABELAN - kuee Soes]\n"
            "  Label: nama produk, tanggal produksi, "
            "kedaluwarsa 2 hari, kode KB-002."
        )