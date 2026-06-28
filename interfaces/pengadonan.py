"""
=========================================================
PENGADONAN PRODUK BAKERY
=========================================================
Interface proses pengadonan seluruh produk Hanari Bakery.

Tanggung jawab : Febriana Putri (K3525007)
Konsep OOP     : Interface, Single Responsibility Principle (SRP)
"""

class Pengadonan:

    @staticmethod
    def roti_manis():
        return (
            "[PENGADONAN - Roti Manis]\n"
            "  1. Campur tepung, gula, ragi, aduk rata.\n"
            "  2. Tambahkan telur dan susu sedikit demi sedikit.\n"
            "  3. Masukkan mentega dan garam, uleni hingga kalis elastis.\n"
            "  4. Adonan siap untuk proofing."
        )

    @staticmethod
    def croissant():
        return (
            "[PENGADONAN - Croissant]\n"
            "  1. Campur tepung, gula, ragi, dan garam.\n"
            "  2. Tambahkan susu dingin dan butter.\n"
            "  3. Uleni singkat, bentuk persegi panjang.\n"
            "  4. Simpan di kulkas sebelum proses laminasi."
        )

    @staticmethod
    def butter_cookies():
        return (
            "[PENGADONAN - Butter Cookies]\n"
            "  1. Kocok butter dan gula halus hingga creamy.\n"
            "  2. Masukkan kuning telur, vanilla, dan garam.\n"
            "  3. Tambahkan tepung, aduk hingga rata.\n"
            "  4. Masukkan ke piping bag."
        )

    @staticmethod
    def muffin():
        return (
            "[PENGADONAN - Muffin]\n"
            "  1. Campur bahan kering.\n"
            "  2. Campur bahan cair di wadah terpisah.\n"
            "  3. Gabungkan keduanya, aduk sebentar (jangan overmix)."
        )

    @staticmethod
    def klepon():
        return (
            "[PENGADONAN - Klepon]\n"
            "  1. Campur tepung ketan, garam, dan pasta pandan.\n"
            "  2. Tuang air hangat sedikit demi sedikit sambil diuleni.\n"
            "  3. Uleni hingga adonan kalis dan bisa dibentuk.\n"
            "  4. Ambil sedikit adonan, isi gula merah, lalu bulatkan."
        )

    @staticmethod
    def kue_soes():
        return (
            "[PENGADONAN - Kue Soes]\n"
            "  1. Rebus air, margarin, garam, dan gula hingga mendidih.\n"
            "  2. Masukkan tepung sekaligus, aduk cepat hingga kalis.\n"
            "  3. Dinginkan sebentar, lalu masukkan telur satu per satu.\n"
            "  4. Aduk hingga adonan licin dan siap disemprot."
        )