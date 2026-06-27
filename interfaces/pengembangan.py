"""
=========================================================
PENGEMBANGAN PRODUK BAKERY
=========================================================
Berisi seluruh proses pengembangan adonan setiap produk bakery.
"""

class Pengembangan:

    @staticmethod
    def roti_manis():
        return (
            "[PENGEMBANGAN - Roti Manis]\n"
            "  1. Diamkan adonan 60 menit hingga mengembang.\n"
            "  2. Kempiskan, bentuk adonan.\n"
            "  3. Diamkan kembali 30 menit sebelum dipanggang."
        )

    @staticmethod
    def croissant():
        return (
            "[PENGEMBANGAN - Croissant]\n"
            "  1. Laminasi butter ke adonan.\n"
            "  2. Lipat dan gilas 3 kali.\n"
            "  3. Bentuk croissant.\n"
            "  4. Proofing akhir 2-3 jam hingga mengembang."
        )

    @staticmethod
    def muffin():
        return (
            "[PENGEMBANGAN - Muffin]\n"
            "  1. Diamkan adonan 5-10 menit.\n"
            "  2. Baking powder akan membantu adonan mengembang."
        )