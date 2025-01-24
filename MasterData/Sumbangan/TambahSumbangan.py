import logging
import random
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def tambah_sumbangan():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--headless")

    # Inisialisasi driver
    print("Inisialisasi driver...")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # Akses URL
    driver.get("https://sit.siprusedu.com/login")
    print("Membuka halaman login")

    # Tunggu hingga elemen email dapat ditemukan
    wait = WebDriverWait(driver, 10)  # Tunggu hingga 10 detik
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
    print("Field email ditemukan")

    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main/div[1]/div/form/button")

    # Masukkan kredensial
    email.send_keys("admin.sekolah@gmail.com")
    password.send_keys("Test1234")
    print("Kredensial telah dimasukkan")

    # Klik tombol login
    login_button.click()
    print("Tombol login diklik")

    # Tunggu beberapa detik setelah login
    time.sleep(9)

    # Klik Menu Master Data
    master_data = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@data-testid='sidebar-menu-master-data'])[2]")))
    master_data.click()
    print("Menu Master Data diklik")

    # Klik menu Sumbangan
    sumbangan = driver.find_element(By.XPATH, "(//*[@data-testid='sidebar-menu-sumbangan'])[2]")
    driver.execute_script("arguments[0].scrollIntoView(true);", sumbangan)
    time.sleep(1)  # Tunggu sejenak
    sumbangan.click()
    print("Menu Sumbangan diklik")
    time.sleep(5)

    # Klik Button Tambah
    btn_sumbangan = driver.find_element(By.XPATH, "//div[contains(@class, 'flex items-center text-center') and normalize-space(text())='Tambah']")
    btn_sumbangan.click()
    print("Tombol Tambah diklik")
    time.sleep(5)

    # Nama Sumbangan
    nama_sumbangan = wait.until(EC.presence_of_element_located((By.NAME, "donationName")))

    # Pilih Nama Sumbangan Secara Acak
    nama_donasi = [
        "Sumbangan Buku Pelajaran", "Sumbangan Renovasi Sekolah", "Sumbangan Bencana Alam",
        "Sumbangan Perpustakaan", "Sumbangan Teknologi Digital", "Sumbangan Seragam Siswa",
        "Sumbangan Pembangunan Masjid", "Sumbangan Kebun Sekolah", "Sumbangan Kegiatan Pramuka",
        "Sumbangan Kesehatan Anak", "Sumbangan Lab Komputer", "Sumbangan Beasiswa Siswa",
        "Sumbangan Penanaman Pohon", "Sumbangan Festival Seni", "Sumbangan Ekskul Olahraga",
        "Sumbangan Transportasi Siswa", "Sumbangan Infrastruktur Kelas", "Sumbangan Bahan Makanan",
        "Sumbangan Alat Musik", "Sumbangan Fasilitas Kamar Mandi"
    ]
    donasi = random.choice(nama_donasi)
    nama_sumbangan.send_keys(donasi)
    print(f"Nama Sumbangan yang dimasukkan: {donasi}")
    logging.info(f"Donation name entered: {donasi}")

    time.sleep(5)

    # Pilih akun bank
    pilih_akunbank = driver.find_element(By.XPATH, "(//*[@data-testid='selected-value'])[1]")
    pilih_akunbank.click()
    print("Pemilihan akun bank diklik")
    logging.info("Bank account selection clicked")
    time.sleep(5)

    # Pilih value akun bank
    value_akunbank = driver.find_element(By.XPATH, "//*[@data-testid='option-161']")
    value_akunbank.click()
    print("Pilihan akun bank dipilih")
    logging.info("Bank account option selected")

    # Pilih unit
    unit_sekolah = driver.find_element(By.XPATH, "(//*[@data-testid='selected-value'])[2]")
    unit_sekolah.click()
    print("Pemilihan unit sekolah diklik")
    logging.info("Unit selection clicked")

    # Value Sekolah
    value_sekolah = driver.find_element(By.XPATH, "//*[@data-testid='paragraph']")
    value_sekolah.click()
    print("Pilihan unit sekolah dipilih")
    logging.info("School unit option selected")

    # Tombol tambahkan
    btn_tambahkan = driver.find_element(By.XPATH, "//button[contains(@class, 'rounded-[6px] flex whitespace-nowrap justify-center items-center font-bold gap-1 h-[44px] py-2 px-6 text-sm bg-blue8') and @type='submit' and .//div[text()='Tambahkan']]")
    btn_tambahkan.click()
    print("Tombol Tambahkan diklik")
    logging.info("Tambahkan button clicked")

    time.sleep(7)

    driver.quit()
    print("Driver dihentikan, skrip selesai")
    logging.info("Driver quit, script completed")
