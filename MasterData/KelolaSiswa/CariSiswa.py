from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from webdriver_manager.chrome import ChromeDriverManager


def cari_siswa():
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

    # Cari Siswa
    print("Mengisi input pencarian siswa...")
    cariSiswa = driver.find_element(By.XPATH, "//*[@data-testid='input-search']")
    cariSiswa.click()
    cariSiswa.send_keys("Muhammad Akmal")

    print("Menunggu hasil pencarian siswa...")
    value_siswa = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'text-sm') and contains(text(), '890998 - Muhammad Akmal, XI BAHASA Mandiri, SMA')]"))
    )
    value_siswa.click()
    time.sleep(7)

    # Terapkan
    print("Klik tombol Terapkan...")
    try:
        btn_terapkan = driver.find_element(By.XPATH, "//button[contains(@class, 'rounded-[6px]') and contains(@class, 'bg-secondary10') and .//div[text()='Terapkan']]")
        btn_terapkan.click()
        print("Tombol Terapkan berhasil diklik!")
    except Exception as e:
        print(f"Error saat mengklik tombol Terapkan: {e}")

    # Tunggu beberapa detik untuk proses selesai
    time.sleep(5)

    # Menutup browser
    print("Menutup browser...")
    driver.quit()

if cari_siswa() == "_main_":
    cari_siswa()