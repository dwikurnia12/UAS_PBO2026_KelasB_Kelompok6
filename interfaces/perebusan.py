"""
=========================================================
PEREBUSAN PRODUK BAKERY
=========================================================
Interface proses perebusan pada produk Hanari Bakery.

Tanggung jawab : Febriana Putri (K3525007)
Konsep OOP     : Interface, Single Responsibility Principle (SRP)
"""

class Perebusan:

    @staticmethod
    def klepon():
        return (
            "[PEREBUSAN - Klepon]\n"
            "  1. Didihkan air dalam panci.\n"
            "  2. Masukkan klepon ke air mendidih.\n"
            "  3. Rebus hingga klepon mengapung.\n"
            "  4. Angkat dan tiriskan."
        )