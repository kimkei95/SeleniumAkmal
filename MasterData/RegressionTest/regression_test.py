import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium.webdriver.common.devtools.v85.fetch import continue_request

from MasterData.Bank.TambahAkunBank import tambah_bank
from MasterData.Bank.EditAkunBank import edit_abank
from MasterData.Kelas.TambahKelas import tambah_kelas
from MasterData.Kelas.EditKelas import edit_kelas
from MasterData.KelolaSiswa.CariSiswa import cari_siswa
from MasterData.KelolaSiswa.EditSiswa import edit_siswa
from MasterData.KelolaSiswa.TambahSiswa import tambah_siswa
from MasterData.KelolaSiswa.FilterSiswa import filter_siswa
from MasterData.KelolaSiswa.LihatSiswa import lihat_siswa
from MasterData.Sumbangan.TambahSumbangan import tambah_sumbangan
from MasterData.Sumbangan.HapusSumbangan import menghapus_sumbangan
from MasterData.Tagihan.TambahTagihan import tambah_tagihan
from MasterData.Tagihan.LihatTagihan import lihat_tagihan
from MasterData.Tagihan.FilterTagihan import filter_tagihan
from MasterTagihan.TagihanPerSiswa.CariTagihanPersiswa import cari_tagihanpersiswa
from MasterTagihan.TagihanPerSiswa.EditTagihanPersiswa import edit_tagihan
from MasterTagihan.TagihanPerSiswa.HapusTagihanPersiswa import hapus_tagihan_persiswa
from MasterTagihan.RiwayatPembayaran.LihatRiwayatPembayaran import lihat_riwayat
from MasterTagihan.RiwayatPembayaran.CariRiwayatPembayaran import cari_riwayat
from MasterTagihan.Pembayaran.BayarTagihan import bayar_tagihan
from MasterPengaturanSistem.PengaturanSekolah.PengaturanSekolahScript import atur_sekolah
from MasterPengaturanSistem.PengaturanInvoice.PengaturanInvoice import atur_invoice
from MasterLaporan.LaporanPembayaran.CariSiswa import cari_pembayaran_siswa
from MasterLaporan.LaporanPembayaran.FilterSiswa import filter_pembayaran_siswa
from MasterLaporan.LaporanPembayaran.UnduhExcel import unduh_pembayaran_excel
from MasterLaporan.LaporanTagihan.CariSiswa import cari_tagihan_siswa
from MasterLaporan.LaporanTagihan.FilterSiswa import filter_laporan_tagihan
from MasterLaporan.LaporanTagihan.UnduhExcel import unduh_laporan_excel
from MasterPengumuman.Pengumuman.CreatePengumuman import create_pengumuman
from MasterPengumuman.Pengumuman.CreateEvent import crete_event
from MasterPengumuman.Pengumuman.EditInformasi import edit_pengumuman_event
from UserManagement.TambahUser.TambahUser import tambah_akun
import logging
import os
from datetime import datetime

# Kelas untuk tes tambah bank
class TestTambahBank(unittest.TestCase):
    def test_tambah_bank(self):
        for i in range(3):
            logging.info(
                f"Menjalankan tes tambah bank ke-{i + 1}...")  # Output untuk mengetahui tes yang sedang dijalankan
            try:
                tambah_bank()  # Memanggil fungsi dari file TambahAkunBank.py
                logging.info(f"Tes tambah bank ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes tambah bank ke-{i + 1} gagal: {e}")
                continue  # Lanjut ke tes berikutnya


# Kelas untuk tes edit bank
class TestEditBank(unittest.TestCase):
    def test_edit_bank(self):
        for i in range(3):  # Menambahkan tes untuk edit bank sebanyak 3 kali
            logging.info(
                f"Menjalankan tes Edit Bank ke-{i + 1}...")  # Output untuk mengetahui tes yang sedang dijalankan
            try:
                edit_abank()  # Memanggil fungsi edit_bank
                logging.info(f"Tes Edit Bank ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Edit Bank ke-{i + 1} gagal: {e}")
                continue  # Lanjut ke tes berikutnya


class TestTambahKelas(unittest.TestCase):
    def test_tambah_kelas(self):
        for i in range(3):
            logging.info(
                f"Menjalankan Tes Tambah Kelas ke-{i + 1}..."
            )
            try:
              tambah_kelas()
              logging.info(f"Tes Tambah kelas ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Tambah Kelas ke-{i + 1} gagal: {e}")
                continue
class TestEditKelas(unittest.TestCase):
    def test_edit_kelas(self):
        for i in range(3):
            logging.info(
                f"Menjalankan Tes Edit Kelas ke-{i + 1}..."
            )
            try:
              edit_kelas()
              logging.info(f"Tes Edit Kelas ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Edit Kelas ke-{i + 1} gagal: {e}")
                continue

class TestEditSiswa(unittest.TestCase):
    def test_edit_siswa(self):
        for i in range(3):
            logging.info(
                f"Menjalankan Tes edit Siswa ke-{i + 1}..."
            )
            try:
             edit_siswa()
             logging.info(f"Tes Edit Siswa ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Edit Kelas ke-{i + 1} gagal: {e}")
                continue

class TestTambahSiswa(unittest.TestCase):
    def test_tambah_siswa(self):
        for i in range(3):
            logging.info(
                f"menjalankan Tes Tambah siswa ke-{i + 1}..."
            )
            try:
                tambah_siswa()
                logging.info(f"Tes Tambah Siswa ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Tambah Siswa ke-{i + 1} gagal: {e}")
                continue

class TestCariSiswa(unittest.TestCase):
    def test_cari_siswa(self):
        for i in range(3):
            logging.info(
                f"Menjalankan Tes Cari Siswa ke-{i + 1}..."
            )
            try:
                cari_siswa()
                logging.info(f"Tes Cari Siswa ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Cari Siswa ke-{i + 1} gagal: {e}")
                continue

class TestFilterSiswa(unittest.TestCase):
    def test_filter_siswa(self):
        for i in range(3):
            logging.info(
                f"Menjalankan Tes Filter Siswa ke-{i + 1}..."
            )
            try:
                filter_siswa()
                logging.info(f"Tes Filter Siswa ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Filter Siswa ke-{i + 1} gagal: {e}")
                continue

class TestLihatSiswa(unittest.TestCase):
    def test_lihat_siswa(self):
        for i in range(3):
            logging.info(
                f"Menjalankan Tes Lihat Siswa ke-{i + 1}..."
            )
            try:
                lihat_siswa()
                logging.info(f"Test Lihat Siswa ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Lihat Siswa ke-{i + 1} gagal: {e}")
                continue

class TestTambahSumbangan(unittest.TestCase):
    def test_tambah_sumbangan(self):
        for i in range(3):
            logging.info(
                f"Menjalankan Tes Tambah Sumbangan ke-{i + 1}..."
            )
            try:
                tambah_sumbangan()
                logging.info(f"Tes Tambah Sumbangan ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Tambah Sumbangan ke-{i + 1} gagal: {e}")
                continue

class TestHapusSumbangan(unittest.TestCase):
    def test_hapus_sumbangan(self):
        for i in range(3):
            logging.info(
                f"Menjalankan Tes Hapus Sumbangan ke-{i + 1}..."
            )
            try:
                menghapus_sumbangan()
                logging.info(f"Tes Hapus Sumbangan ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Hapus Sumbangan ke-{i + 1} gagal: {e}")
                continue

class TestTambahTagihan(unittest.TestCase):
    def test_tambah_tagihan(self):
        for i in range(3):
            logging.info(f"Tes Tambah Tagihan ke-{i + 1}...")
            try:
                tambah_tagihan()
                logging.info(f"Tes Tambah Tagihan ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Tambah Tagihan ke-{i + 1} gagal: {e}")
                continue

class TestLihatTagihan(unittest.TestCase):
    def test_lihat_tagihan(self):
        for i in range(3):
            logging.info(f"Tes Lihat Tagihan ke-{i + 1}...")
            try:
                lihat_tagihan()
                logging.info(f"Tes Lihat Tagihan ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Lihat Tagihan ke-{i + 1} gagal: {e}")
                continue

class TestFilterTagihan(unittest.TestCase):
    def test_filter_tagihan(self):
        for i in range(3):
            logging.info(f"Tes Filter Tagihan ke-{i + 1}...")
            try:
                filter_tagihan()
                logging.info(f"Tes Filter Tagihan ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Filter Tagihan ke-{i + 1} gagal: {e}")
                continue

class TestCariTagihanPersiswa(unittest.TestCase):
    def test_cari_tagihan_persiswa(self):
        for i in range(3):
            logging.info(f"Tes Cari Tagihan PerSiswa ke-{i + 1}...")
            try:
                cari_tagihanpersiswa()
                logging.info(f"Tes Cari Tagihan PerSiswa ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Cari Tagihan PerSiswa ke-{i + 1} gagal: {e}")
                continue

class TestEditTagihanPersiswa(unittest.TestCase):
    def test_edit_tagihan_persiswa(self):
        for i in range(3):
            logging.info(f"Tes Edit Tagihan Persiswa ke-{i + 1}...")
            try:
                edit_tagihan()
                logging.info(f"Tes Edit Tagihan Persiswa ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Edit Tagihan Persiswa ke-{i + 1} gagal: {e}")
                continue

class TestHapusTagihanPersiswa(unittest.TestCase):
    def test_hapus_tagihan_persiswa(self):
        for i in range(3):
            logging.info(f"Tes Hapus Tagihan Persiswa ke-{i + 1}...")
            try:
                hapus_tagihan_persiswa()
                logging.info(f"Tes Hapus Tagihan Persiswa ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Hapus Tagihan Persoswa ke-{i + 1} gagal: {e}")
                continue

class TestCariRiwayatPembayaran(unittest.TestCase):
    def test_cari_riwayat_tagihan(self):
        for i in range(3):
            logging.info(f"Tes Cari Riwayat Pembayaran ke-{i + 1}...")
            try:
                cari_riwayat()
                logging.info(f"Tes Cari Riwayat Pembayaran ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Test Cari Riwayat Pembayaran ke-{i + 1} gagal: {e}")
                continue

class TestLihatRiwayatPembayaran(unittest.TestCase):
    def test_lihat_riwayat_pembayaran(self):
        for i in range(3):
            logging.info(f"Tes Lihat Riwayat Pembayaran ke-{i + 1}...")
            try:
                lihat_riwayat()
                logging.info(f"Tes Lihat Riwayat Pembayaran ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Test Lihat Riwayat Pembayaran ke-{i + 1} gagal: {e}")
                continue

class TestBayarTagihan(unittest.TestCase):
    def test_bayar_tagihan(self):
        for i in range(3):
            logging.info(f"Test Bayar Tagihan ke-{i + 1}...")
            try:
                bayar_tagihan()
                logging.info(f"Tes Bayar Tagihan ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Bayar Tagihan ke-{i + 1} gagal: {e}")
                continue

class TestPengaturanSekolah(unittest.TestCase):
    def test_atur_sekolah(self):
        for i in range(3):

            logging.info(f"Test Pengaturan Sekolah ke-{i + 1}...")
            try:
                atur_sekolah()
                logging.info(f"Tes Pengaturan Sekolah ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Pengaturan Sekolah ke-{i + 1} gagal: {e}")
                continue

class TestAturInvoice(unittest.TestCase):
    def test_atur_invoice(self):
        for i in range(3):
            logging.info(f"Tes Atur Invoice ke-{i + 1}...")
            try:
                atur_invoice()
                logging.info(f"Tes Atur Invoice ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Atur Invoice ke-{i + 1} gagal: {e}")
                continue

class TestCariPembayaranSiswa(unittest.TestCase):
    def test_cari_pembayaran_siswa(self):
        for i in range(3):
            logging.info(f"Tes Cari Pembayaran Siswa ke-{i + 1}...")
            try:
                cari_pembayaran_siswa()
                logging.info(f"Test cari Pembayaran Siswa ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes cari Pembayaran Siswa ke-{i + 1} gagal: {e}")
                continue

class TestFilterPembayaranSiswa(unittest.TestCase):
    def test_filter_pembayaran_siswa(self):
        for i in range(3):
            logging.info(f"Tes Filter Pembayaran Siswa ke-{i + 1}...")
            try:
                filter_pembayaran_siswa()
                logging.info(f"Tes Filter Pembyaran Siswa ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Filter Pembyaran Siswa ke-{i + 1 } gagal: {e}")
                continue

class TestUnduhLaporanPembayaran(unittest.TestCase):
    def test_unduh_excel(self):
        for i in range(3):
            logging.info(f"Tes Undduh Laporan ke-{i + 1}...")
            try:
                unduh_pembayaran_excel()
                logging.info(f"Tes Unduh Laporan ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Unduh Laporan ke-{i + 1} gagal: {e}")
                continue

class TestCariTagihanSiswa(unittest.TestCase):
    def test_cari_tagihan_siswa(self):
        for i in range(3):
            logging.info(f"Tes Cari Tagihan Siswa ke-{i + 1}...")
            try:
                cari_tagihan_siswa()
                logging.info(f"Tes Cari Tagihan Siswa ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Cari Tagihan Siswa ke-{i + 1} gagal: {e}")
                continue

class TestFilterLaporanTagihan(unittest.TestCase):
    def test_filter_laporan_tagihan(self):
        for i in range(3):
            logging.info(f"Tes Filter Laporan Tagihan ke-{i + 1}")
            try:
                filter_laporan_tagihan()
                logging.info(f"Tes Filter Laporan Tagihan ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Filter Laporan Tagihan ke-{i + 1} gagal: {e}")
                continue

class TestUnduhLaporanTagihan(unittest.TestCase):
    def test_Unduh_Laporan_tagihan(self):
        for i in range(3):
            logging.info(f"Tes Unduh Laporan Tagihan ke-{i + 1}...")
            try:
                unduh_laporan_excel()
                logging.info(f"Tes Unduh Laporan Tagihan ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Unduh Laporan Tagihan ke-{i + 1} gagal: {e}")
                continue
class TestCreateEvent(unittest.TestCase):
    def test_create_event(self):
        for i in range(3):
            logging.info(f"Tes Create event ke-{i + 1}...")
            try:
                crete_event()
                logging.info(f"Tes Create event ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Create event ke-{i + 1} gagal : {e}")
                continue

class TestCreatePengumuman(unittest.TestCase):
    def test_create_pengumuman(self):
        for i in range(3):
            logging.info(f"Tes Create Pengumuman ke-{i + 1}...")
            try:
                create_pengumuman()
                logging.info(f"Tes Create Pengumuman ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Create Pengumuman ke-{i + 1} gagal:{e}")
                continue

class TestEditInformasi(unittest.TestCase):
    def test_edit_informasi(self):
        for i in range(3):
            logging.info(f"Tes Edit Informasi ke-{i + 1}...")
            try:
                edit_pengumuman_event()
                logging.info(f"Tes Edit Informasi ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Edit Informasi ke-{i + 1} gagal: {e}")
                continue

class TestTambahUser(unittest.TestCase):
    def test_tambah_user(self):
        for i in range(3):
            logging.info(f"Tes Tambah User ke-{i + 1}...")
            try:
                tambah_akun()
                logging.info(f"Tes Tambah User ke-{i + 1} berhasil")
            except Exception as e:
                logging.error(f"Tes Tambah User ke-{i +1} gagal: {e}")
                continue


# yang ini belum kepake karna masih nyari buat ubah script terbaca jadi testcase (untuk genereate auto report)
def run_regression_tests():
    # Memuat semua tes untuk tambah bank dan edit bank
    suite_tambah_bank = unittest.TestLoader().loadTestsFromTestCase(TestTambahBank)
    suite_edit_bank = unittest.TestLoader().loadTestsFromTestCase(TestEditBank)
    test_suite = unittest.TestSuite([suite_tambah_bank, suite_edit_bank])

    report_path = r"C:\Users\akmal\Downloads\Selenium\regression_test_report.html"
    report_dir = os.path.dirname(report_path)  # Ambil path direktori
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)  # Buat direktori jika belum ada

    logging.info(f"Menulis laporan di: {report_path}")  # Log untuk mengecek path file
    try:
        with open(report_path, "w") as report_file:
            runner = HTMLTestRunner(stream=report_file, verbosity=2)
            runner.run(test_suite)  # Jalankan suite yang digabungkan
        logging.info("Laporan berhasil dibuat")
    except Exception as e:
        logging.error(f"Gagal membuat laporan: {e}")


if __name__ == "__main__":
    run_regression_tests()  # Jalankan regression tests
