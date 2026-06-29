"""
test_diah.py
============
Testing Muffin, Klepon, dan Kue Soes
"""

from models.roti_kering.muffin import Muffin
from models.roti_basah.klepon import Klepon
from models.roti_basah.kue_soes import KueSoes
from models.roti_manis import RotiManis
from models.croissant import Croissant
from models.roti_kering.buttercookies import ButterCookies


def main():

    produk_list = [
        Muffin(),
        Klepon(),
        KueSoes(),
        RotiManis(),
        Croissant(),
        ButterCookies(),
    ]

    for produk in produk_list:

        print("\n" + "=" * 60)
        print(produk.tampilkan_info())
        print("=" * 60)

        print("\nEstimasi Profit:")
        hasil = produk.hitung_profit(50)

        print(f"Produk        : {hasil['produk']}")
        print(f"Profit        : Rp {hasil['profit']:,.0f}")
        print(f"Margin        : {hasil['margin_persen']:.2f}%")

        print("\nSimulasi Produksi:")
        produk.simulasi_produksi()

        print("\n")


if __name__ == "__main__":
    main()