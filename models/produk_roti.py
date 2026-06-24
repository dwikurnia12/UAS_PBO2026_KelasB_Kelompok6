produk_roti.py
==============
Abstract superclass untuk semua produk roti di Hanari Bakery.

Tanggung jawab   : Queennera Martha Kusuma Wardhani (K3525012)
Konsep OOP       : Abstract Class, Encapsulation, Method Umum
"""

from abc import ABC, abstractmethod

class ProdukRoti(ABC):
    """
    Abstract superclass yang merepresentasikan produk roti secara umum.

    Semua jenis produk roti (RotiManis, Croissant, KueKering, dst.)
    mewarisi kelas ini dan wajib mengimplementasikan method abstraknya.

    Atribut disimpan sebagai private (enkapsulasi) dan hanya dapat
    diakses melalui property getter.
    """

    def __init__(
        self,
        nama_produk: str,
        kode_produk: str,
        bahan_baku: dict,
        jumlah_produksi: int,
        biaya_produksi: float,
        harga_jual_per_pcs: float
    ):
        """
        Inisialisasi atribut produk roti.

        Parameters
        ----------
        nama_produk       : Nama lengkap produk (misal: "Roti Manis")
        kode_produk       : Kode unik produk   (misal: "RM-001")
        bahan_baku        : Dict {nama_bahan: (jumlah, satuan)}
        jumlah_produksi   : Jumlah pcs yang dihasilkan per satu resep
        biaya_produksi    : Total biaya produksi per satu resep (Rp)
        harga_jual_per_pcs: Harga jual kepada konsumen per pcs (Rp)
        """
        self.__nama_produk        = nama_produk
        self.__kode_produk        = kode_produk
        self.__bahan_baku         = bahan_baku
        self.__jumlah_produksi    = jumlah_produksi
        self.__biaya_produksi     = biaya_produksi
        self.__harga_jual_per_pcs = harga_jual_per_pcs

    # ------------------------------------------------------------------
    # PROPERTY GETTER (Encapsulation)
    # Atribut private hanya bisa dibaca dari luar, tidak bisa diubah
    # sembarangan — menjaga konsistensi data produk.
    # ------------------------------------------------------------------

    @property
    def nama_produk(self) -> str:
        """Nama lengkap produk."""
        return self.__nama_produk

    @property
    def kode_produk(self) -> str:
        """Kode unik produk."""
        return self.__kode_produk

    @property
    def bahan_baku(self) -> dict:
        """
        Daftar bahan baku beserta jumlah dan satuannya.
        Format: {nama_bahan: (jumlah, satuan)}
        """
        return self.__bahan_baku

    @property
    def jumlah_produksi(self) -> int:
        """Jumlah pcs yang dihasilkan per satu resep."""
        return self.__jumlah_produksi

    @property
    def biaya_produksi(self) -> float:
        """Total biaya produksi per satu resep (Rp)."""
        return self.__biaya_produksi

    @property
    def harga_jual_per_pcs(self) -> float:
        """Harga jual kepada konsumen per pcs (Rp)."""
        return self.__harga_jual_per_pcs

    # ------------------------------------------------------------------
    # METHOD UMUM (diwarisi semua subclass tanpa perlu di-override)
    # ------------------------------------------------------------------

    def hitung_profit(self, jumlah_pcs: int) -> dict:
        """
        Menghitung estimasi profit untuk sejumlah pcs yang diproduksi.

        Biaya produksi diskalakan secara proporsional dari biaya per resep
        ke biaya per pcs, kemudian dikalikan dengan jumlah yang diminta.

        Parameters
        ----------
        jumlah_pcs : Jumlah pcs yang ingin diproduksi

        Returns
        -------
        dict berisi rincian kalkulasi profit:
            - produk           : nama produk
            - jumlah_pcs       : jumlah pcs yang diproduksi
            - biaya_per_pcs    : biaya produksi per pcs (Rp)
            - total_biaya      : total biaya seluruh produksi (Rp)
            - harga_jual_per_pcs: harga jual per pcs (Rp)
            - total_pendapatan : total pendapatan jika semua terjual (Rp)
            - profit           : estimasi laba bersih (Rp)
            - margin_persen    : persentase margin profit (%)
        """
        biaya_per_pcs     = self.__biaya_produksi / self.__jumlah_produksi
        total_biaya       = biaya_per_pcs * jumlah_pcs
        total_pendapatan  = self.__harga_jual_per_pcs * jumlah_pcs
        profit            = total_pendapatan - total_biaya
        margin_persen     = (profit / total_pendapatan * 100) if total_pendapatan > 0 else 0

        return {
            "produk"            : self.__nama_produk,
            "jumlah_pcs"        : jumlah_pcs,
            "biaya_per_pcs"     : biaya_per_pcs,
            "total_biaya"       : total_biaya,
            "harga_jual_per_pcs": self.__harga_jual_per_pcs,
            "total_pendapatan"  : total_pendapatan,
            "profit"            : profit,
            "margin_persen"     : margin_persen,
        }

    def tampilkan_info(self) -> str:
        """
        Mengembalikan string informasi lengkap produk yang siap ditampilkan.

        Mencakup kode, nama, jumlah produksi per resep, biaya,
        harga jual, dan daftar bahan baku beserta takarannya.

        Returns
        -------
        str : informasi produk yang sudah diformat
        """
        bahan_str = "\n".join(
            f"      - {bahan}: {jumlah} {satuan}"
            for bahan, (jumlah, satuan) in self.__bahan_baku.items()
        )
        return (
            f"  Kode        : {self.__kode_produk}\n"
            f"  Nama        : {self.__nama_produk}\n"
            f"  Per resep   : {self.__jumlah_produksi} pcs\n"
            f"  Biaya prod  : Rp {self.__biaya_produksi:,.0f}\n"
            f"  Harga jual  : Rp {self.__harga_jual_per_pcs:,.0f}/pcs\n"
            f"  Bahan baku  :\n{bahan_str}"
        )

    # ------------------------------------------------------------------
    # METHOD ABSTRAK (wajib diimplementasikan oleh setiap subclass)
    # ------------------------------------------------------------------

    @abstractmethod
    def aduk(self) -> str:
        """
        Proses pengadonan.
        Setiap produk memiliki teknik pengadonan yang berbeda,
        sehingga method ini bersifat abstrak.
        """
        pass
