"""
=========================================================
PENGEMASAN PRODUK BAKERY
=========================================================
Berisi seluruh proses pengemasan setiap produk bakery.
"""

class Pengemasan:

    @staticmethod
    def roti_manis():
        return (
            "[PENGEMASAN - Roti Manis]\n"
            "  1. Dinginkan roti.\n"
            "  2. Masukkan ke plastik kemasan.\n"
            "  3. Tutup rapat dengan sealer."
        )

    @staticmethod
    def croissant():
        return (
            "[PENGEMASAN - Croissant]\n"
            "  1. Dinginkan croissant.\n"
            "  2. Kemas dalam paper bag / box agar tetap renyah."
        )

    @staticmethod
    def butter_cookies():
        return (
            "[PENGEMASAN - Butter Cookies]\n"
            "  1. Dinginkan cookies.\n"
            "  2. Masukkan ke toples kedap udara."
        )

    @staticmethod
    def muffin():
        return (
            "[PENGEMASAN - Muffin]\n"
            "  1. Dinginkan muffin.\n"
            "  2. Kemas dengan paper box / plastik OPP."
        )

    @staticmethod
    def klepon():
        return (
            "[PENGEMASAN - Klepon]\n"
            "  1. Susun klepon dalam mika / kotak makanan.\n"
            "  2. Beri alas daun pisang bila diinginkan.\n"
            "  3. Tutup rapat agar tetap higienis."
        )

    @staticmethod
    def soes():
        return (
            "[PENGEMASAN - Soes]\n"
            "  1. Susun soes dalam box/mika makanan.\n"
            "  2. Simpan rapi agar isian tidak keluar."
        )