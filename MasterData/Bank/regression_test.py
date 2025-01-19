import unittest
from HtmlTestRunner import HTMLTestRunner
from TambahAkunBank import tambah_bank
from EditAkunBank import edit_abank
import logging

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


def run_regression_tests():
    # Memuat semua tes untuk tambah bank dan edit bank
    test_suite = unittest.TestLoader().loadTestsFromTestCase(
        TestTambahBank) + unittest.TestLoader().loadTestsFromTestCase(TestEditBank)

    report_path = r"C:\Users\akmal\Downloads\Selenium\regression_test_report.html"
    logging.info(f"Menulis laporan di: {report_path}")  # Log untuk mengecek path file
    try:
        with open(report_path, "w") as report_file:
            runner = HTMLTestRunner(stream=report_file, verbosity=2)
            runner.run(test_suite)
        logging.info("Laporan berhasil dibuat")
    except Exception as e:
        logging.error(f"Gagal membuat laporan: {e}")


if __name__ == "__main__":
    run_regression_tests()  # Jalankan regression tests
