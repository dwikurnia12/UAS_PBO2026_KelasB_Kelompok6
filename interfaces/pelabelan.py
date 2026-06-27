"""
=========================================================
PELABELAN PRODUK BAKERY
=========================================================
Berisi seluruh proses pelabelan setiap produk bakery.
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
    def soes():
        return (
            "[PELABELAN - Soes]\n"
            "  Label: nama produk, tanggal produksi, "
            "kedaluwarsa 2 hari, kode KB-002."
        )