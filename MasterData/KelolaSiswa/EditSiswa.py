import random
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from webdriver_manager.chrome import ChromeDriverManager


def edit_siswa():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--headless")

    # Inisialisasi driver
    print("Inisialisasi driver...")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # Akses URL
    print("Mengakses URL...")
    driver.get("https://sit.siprusedu.com/login")

    # Tunggu hingga elemen email dapat ditemukan
    print("Menunggu elemen login...")
    wait = WebDriverWait(driver, 10)
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main/div[1]/div/form/button")

    # Masukkan kredensial
    print("Mengisi kredensial login...")
    email.send_keys("admin.sekolah@gmail.com")
    password.send_keys("Test1234")

    # Klik tombol login
    print("Klik tombol login...")
    login_button.click()

    # Tunggu beberapa detik setelah login
    time.sleep(9)

    # Klik Menu Master Data
    print("Klik menu Master Data...")
    master_data = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@data-testid='sidebar-menu-master-data'])[2]")))
    master_data.click()
    time.sleep(5)

    # Klik sub-menu siswa
    print("Klik sub-menu Kelola Siswa...")
    kelola_siswa = driver.find_element(By.XPATH, "(//*[@data-testid='sidebar-menu-kelola-siswa'])[2]")
    kelola_siswa.click()
    time.sleep(4)

    # Klik tri-dots
    print("Klik tri-dots...")
    tri_dots = driver.find_element(By.XPATH, "(//*[@data-testid='tridots-icon'])[1]")
    tri_dots.click()
    time.sleep(4)

    # Klik edit
    print("Klik opsi Edit...")
    edit = driver.find_element(By.XPATH, "//p[contains(@class, 'text-sm') and contains(@class, 'font-medium') and contains(@class, 'text-blue10') and contains(text(), 'Edit')]")
    edit.click()
    time.sleep(5)

    # Mengedit nama siswa
    print("Mengedit nama siswa...")
    nama_siswa = driver.find_element(By.XPATH, "//*[@data-testid='full-name-input']")
    nama_siswa.click()

    nama_murid = [
        "Muhammad Akmal",
        "Rina Sari",
        "Budi Santoso",
        "Dewi Anggraini",
        "Joko Prabowo",
        "Anisa Putri"
    ]

    # Pilih nama secara acak dari array
    nama_siswa.send_keys(Keys.CONTROL + "a")
    nama_siswa.send_keys(Keys.BACKSPACE)
    nama_terpilih = random.choice(nama_murid)
    print(f"Nama siswa yang dipilih: {nama_terpilih}")
    nama_siswa.send_keys(nama_terpilih)
    time.sleep(4)

    # Klik tombol simpan
    print("Klik tombol Simpan...")
    simpan = driver.find_element(By.XPATH, "//button[div[contains(text(), 'Simpan')] and contains(@class, 'rounded-[6px]')]")
    simpan.click()
    time.sleep(3)

    # Klik pop-up Ya
    print("Klik pop-up konfirmasi Ya...")
    try:
        pop_up = driver.find_element(By.XPATH, "//div[contains(@class, 'flex') and contains(@class, 'items-center') and contains(@class, 'text-center') and text()='Ya']")
        pop_up.click()
        print("Pop-up berhasil diklik!")
    except Exception as e:
        print(f"Error saat mengklik pop-up: {e}")

    # Tunggu beberapa detik untuk menyelesaikan proses
    time.sleep(5)

    # Menutup browser
    print("Menutup browser...")
    driver.quit()

if edit_siswa() == "_main_":
    edit_siswa()