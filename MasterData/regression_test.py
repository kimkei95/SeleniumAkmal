import unittest
from HtmlTestRunner import HTMLTestRunner
from MasterData.Bank.TambahAkunBank import tambah_bank
from MasterData.Bank.EditAkunBank import edit_abank
from MasterData.Kelas.TambahKelas import tambah_kelas
from MasterData.Kelas.EditKelas import edit_kelas
import logging
import os
# Menyiapkan logging
logging.basicConfig(level=logging.INFO)  # Set log level ke INFO agar informasi dicetak di console


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
