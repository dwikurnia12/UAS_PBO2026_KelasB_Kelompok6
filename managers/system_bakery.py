"""
Pusat pengelolaan seluruh produk dan proses bisnis
di Hanari Bakery.

Tanggung jawab   : Dwi Kurniawati Hanifah (K3525056)
Konsep OOP       : Encapsulation, Object Management, Composition, Single Responsibility Principle (SRP)

"""

from data.data_product import DATA_PRODUK

class SistemBakery:
    def __init__(self):
        self._daftar_produk = {}
        self.inisialisasi_produk()
    # ==========================================
    # INISIALISASI PRODUK DEFAULT
    # ==========================================

    def inisialisasi_produk(self):

        if not DATA_PRODUK:
            print("Data produk belum tersedia")
            return
        
        for produk in DATA_PRODUK:
            self._daftar_produk[
                produk.kode_produk
            ] = produk

    # ==========================================
    # MENAMBAH PRODUK
    # ==========================================
    def tambah_produk(self, produk):

        if produk.kode_produk in self._daftar_produk:

            print(
                f"Produk dengan kode"
                f"{produk.kode_produk} sudah ada!"
            )
            return False
        
        self._daftar_produk[
            produk.kode_produk
        ] = produk

        print(
            f"{produk.nama_produk} berhasil ditambahkan."
        )

        return True
    # ==========================================
    # MENAMPILKAN KATALOG
    # ==========================================
    def tampilkan_katalog(self):
        print("\n=====KATALOG PRODUK=====")

        for kode, produk in self._daftar_produk.items():

            print(
                f"{kode} - "
                f"{produk.nama_produk}"
            
            )

    # ==========================================
    # MENAMPILKAN SEMUA PRODUK 
    # ==========================================
    def tampilkan_semua_produk(self):
        if not self._daftar_produk:
            print("Belum ada produk.")
            return
        
        print("\n=====DAFTAR PRODUK=====")

        for produk in self._daftar_produk.values():

            print("\n-------------------")
            (produk.tampilkan_info())

            print(
            f"Harga Jual : "
            f"Rp {produk.harga_jual_per_pcs:,}"
            )
        
            print("--------------------")

    # ==========================================
    # CARI PRODUK PRODUK 
    # ==========================================
    def cari_produk(self, kode_produk):
        return self._daftar_produk.get(
            kode_produk
        )

    # ==========================================
    # HITUNG PROFIT
    # ==========================================    
    def hitung_profit(
            self,
            kode_produk,
            jumlah_produksi
    ):
            
            produk = self.cari_produk(
                kode_produk
            )

            if not produk:
                return None
            
            return produk.hitung_profit(
                jumlah_produksi
            )
        
    # ==============================
    # HITUNG KEBUTUHAN BAHAN BAKU
    # ==============================

    def hitung_bahan_baku(
            self,
            kode_produk,
            jumlah_produksi
    ):
        produk = self.cari_produk(
            kode_produk
        )

        if not produk:
            return None
        
        faktor_skala = (
            jumlah_produksi / 
            produk.jumlah_produksi
        )

        kebutuhan_bahan = {}

        for (
            nama_bahan,
            data_bahan
        ) in produk.bahan_baku.items():
            
            jumlah, satuan = data_bahan

            kebutuhan_bahan[
                nama_bahan
            ] = (
                round(
                    jumlah * faktor_skala,
                    2
                ),
                satuan
            )
        return kebutuhan_bahan

    # ==============================
    # TAMPILKAN PROFIT LENGKAP

    def tampilkan_profit(
            self,
            kode_produk,
            jumlah_produksi
    ):
        produk = self.cari_produk(
            kode_produk
        )

        if not produk:
            print(
                "Produk tidak ditemukan."
            )
            return
        
        hasil_profit = self.hitung_profit(
            kode_produk,
            jumlah_produksi
        )
        print(
            f"Margin Profit : "
            f"{hasil_profit['margin_persen']:.2f}%"
        )

        kebutuhan_bahan = (
            self.hitung_bahan_baku(
                kode_produk,
                jumlah_produksi
            )
        )

        print("\n" + "=" * 40)
        print("ESTIMASI PROFIT PRODUK")
        print("=" * 40)

        print(
            f"Produk    : {produk.nama_produk}"
        )

        print(
            f"Jumlah Produksi   : {jumlah_produksi} pcs"
        )

        print(
            f"Biaya Produksi   : Rp {hasil_profit['total_biaya']:,.0f}"
        )

        print(
            f"Pendapatan    : Rp {hasil_profit['total_pendapatan']:,.0f}"
        )

        print(
            f"Profit    : Rp {hasil_profit['profit']:,.0f}"
        )

        print("\n BAHAN BAKU YANG DIPERLUKAN")

        for (
            bahan,
            data
        ) in kebutuhan_bahan.items():
            
            jumlah, satuan = data

            print(
                f"- {bahan:<20}"
                f"{jumlah} {satuan}"
            )

    # ==============================
    # SIMULASI PRODUKSI
    # ==============================
    def simulasi_produksi(
            self,
            kode_produk
    ):
        
        produk = self.cari_produk(
            kode_produk
        )

        if not produk:

            print(
                "Produk tidak ditemukan."
            )

            return
        print("\n" + "=" * 50)

        print(
            f"SIMULASI PRODUKSI {produk.nama_produk.upper()}"
        )
        print("=" * 50)
        produk.simulasi_produksi()
        produk.tampilkan_info()
    # ==============================
    # HAPUS PRODUK
    # ==============================

    def hapus_produk(
            self,
            kode_produk
    ):
        
        if kode_produk in self._daftar_produk:

            del self._daftar_produk[
                kode_produk
            ]

            print(
                "Produk berhasil dihapus."
            )
            return True
        print(
            "Produk tidak ditemukan."
        )
        return False

    # ==============================
    # GETTER
    # ==============================

    @property
    def daftar_produk(self):
        return self._daftar_produk