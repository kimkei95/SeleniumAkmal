import random

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def edit_abank():
    print("Inisialisasi driver...")
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")

    # Inisialisasi driver
    service = Service(executeable_path="C:\\Users\\akmal\\Selenium-Py\\chrome-headless-shell.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    print("Mengakses URL login...")
    driver.get("https://sit.siprusedu.com/login")

    # Tunggu hingga elemen email dapat ditemukan
    wait = WebDriverWait(driver, 10)  # Tunggu hingga 10 detik
    print("Mencari elemen input email...")
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main/div[1]/div/form/button")

    print("Mengisi kredensial login...")
    email.send_keys("admin.sekolah@gmail.com")
    password.send_keys("Test1234")

    print("Klik tombol login...")
    login_button.click()

    # Tunggu beberapa detik setelah login
    time.sleep(9)

    print("Klik menu Master Data...")
    master_data = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@data-testid='sidebar-menu-master-data'])[2]")))
    master_data.click()

    print("Klik sidebar menu Akun Bank...")
    sidebar_menu_kelas = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@data-testid='sidebar-menu-akun-bank'])[2]")))
    sidebar_menu_kelas.click()

    time.sleep(15)

    print("Klik ikon tiga titik (tridots) untuk mengedit...")
    tridots = driver.find_element(By.XPATH, "(//*[@data-testid='tridots-icon'])[1]")
    tridots.click()
    time.sleep(5)

    print("Memilih menu Edit...")
    pilih_menu = driver.find_element(By.XPATH, "//p[contains(@class, 'text-sm') and text()='Edit']")
    pilih_menu.click()

    print("Mengedit nama nasabah...")
    nasabah = driver.find_element(By.XPATH, "//*[@data-testid='field-bank-name']")
    nasabah.click()
    nasabah.send_keys(Keys.CONTROL + "a")
    nasabah.send_keys(Keys.BACKSPACE)
    nasabah_Array = ["toni", "jono", "Budi Handoko", "Kim jong Un", "Tony Stark", "Tony Hawk", "Dani Aditya", "Oda nobunaga", "Itachi Uchiha", "Uchiha Shisui"]
    random_nasabah = random.choice(nasabah_Array)
    print(f"Nama nasabah yang dipilih: {random_nasabah}")
    nasabah.send_keys(random_nasabah)
    time.sleep(7)

    print("Mengedit nomor rekening...")
    norek = driver.find_element(By.XPATH, "//*[@data-testid='field-bank-number']")
    norek.click()
    norek.send_keys(Keys.CONTROL + "a")
    norek.send_keys(Keys.BACKSPACE)
    norek_random = [random.randint(10000, 99999) for _ in range(5)]
    angka_random = random.choice(norek_random)
    print(f"Nomor rekening yang dipilih: {angka_random}")
    norek.send_keys(angka_random)
    time.sleep(5)

    print("Klik tombol Simpan...")
    btn_simpan = driver.find_element(By.XPATH, "//button[@type='submit' and .//div[text()='Simpan']]")
    btn_simpan.click()
    print("Tombol Simpan berhasil diklik dan data berhasil disimpan.")
    time.sleep(5)

    print("Menutup driver...")
    driver.quit()
