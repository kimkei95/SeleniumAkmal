import unittest
from HtmlTestRunner import HTMLTestRunner
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
from MasterData.Sumbangan.HapusSumbangan import hapus_sumbangan
from MasterData.Tagihan.TambahTagihan import tambah_tagihan
from MasterData.Tagihan.LihatTagihan import lihat_tagihan
from MasterData.Tagihan.FilterTagihan import filter_tagihan
from MasterTagihan.TagihanPerSiswa.CariTagihanPersiswa import cari_tagihanpersiswa
import logging
import os
from datetime import datetime


# Menyiapkan logging
logging.basicConfig(level=logging.INFO)  # Set log level ke INFO agar informasi dicetak di console
screenshot_path = r"C:\Users\akmal\PycharmProjects\PythonProject\screenshots"
def take_screenshot(driver, test_name, step_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_filename = f"{test_name}_{step_name}_{timestamp}.png"
    screenshot_full_path = os.path.join(screenshot_path, screenshot_filename)
    driver.save_screenshot(screenshot_full_path)
    logging.info(f"Screenshot disimpan di: {screenshot_full_path}")

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
                hapus_sumbangan()
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
