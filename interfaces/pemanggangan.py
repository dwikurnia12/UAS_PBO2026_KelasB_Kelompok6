"""
=========================================================
PEMANGGANGAN PRODUK BAKERY
=========================================================
Interface proses pemanggangan produk Hanari Bakery.

Tanggung jawab : Febriana Putri (K3525007)
Konsep OOP     : Interface, Single Responsibility Principle (SRP)
"""

class Pemanggangan:

    @staticmethod
    def roti_manis():
        return (
            "[PEMANGGANGAN - Roti Manis]\n"
            "  1. Panaskan oven 180°C.\n"
            "  2. Oles permukaan roti dengan kuning telur.\n"
            "  3. Panggang 20-25 menit hingga keemasan."
        )

    @staticmethod
    def croissant():
        return (
            "[PEMANGGANGAN - Croissant]\n"
            "  1. Panaskan oven 200°C.\n"
            "  2. Oles permukaan dengan egg wash.\n"
            "  3. Panggang 18-22 menit hingga berlapis dan keemasan."
        )

    @staticmethod
    def butter_cookies():
        return (
            "[PEMANGGANGAN - Butter Cookies]\n"
            "  1. Panaskan oven 160°C.\n"
            "  2. Panggang 18-22 menit hingga keemasan."
        )

    @staticmethod
    def muffin():
        return (
            "[PEMANGGANGAN - Muffin]\n"
            "  1. Panaskan oven 190°C.\n"
            "  2. Panggang 20-25 menit hingga matang."
        )

    @staticmethod
    def kue_soes():
        return (
            "[PEMANGGANGAN - Soes]\n"
            "  1. Panaskan oven 200°C.\n"
            "  2. Semprot adonan ke loyang.\n"
            "  3. Panggang 25-30 menit hingga mengembang dan kering.\n"
            "  4. Dinginkan sebelum diisi vla."
        )