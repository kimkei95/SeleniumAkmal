

import pyautogui
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def atur_sekolah():
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

    # Pengturan Sistem
    pengaturan_sistem = driver.find_element(By.XPATH, "(//*[@data-testid='sidebar-menu-pengaturan-sistem'])[2]")
    pengaturan_sistem.click()
    time.sleep(4)
    print("berhasil masuk ke menu pengaturan sistem")

    # Pilih Card Sekolah

    cardSekolah = driver.find_element(By.XPATH,
                                      "(//div[contains(@class, 'flex') and .//p[text()='Informasi Sekolah']])[5]")
    cardSekolah.click()
    time.sleep(4)
    print("Masuk Ke Menu Informasi Sekolah")

    # ubah logo Sekolah
    ubah_logo = driver.find_element(By.XPATH, "(//*[@data-testid='upload-action-label'])[1]")
    ubah_logo.click()
    print("Membuka File Explorer")
    time.sleep(5)
    pyautogui.write(
        r"C:\Users\akmal\Downloads\winter-aespa-hot-mess-4k-wallpaper-uhdpaper.com-362@0@k.jpg")  # Path file gambar
    pyautogui.press("enter")
    print("Logo Sekolah berhasil ditambahkan")

    time.sleep(5)

    # ubah Kop Surat
    ubah_kop = driver.find_element(By.XPATH, "(//*[@data-testid='upload-action-label'])[2]")
    ubah_kop.click()
    print("Membuka File Explorer")
    time.sleep(5)
    pyautogui.write(r"C:\Users\akmal\Downloads\Logo-OSIS-SMA.png")  # Path file gambar
    pyautogui.press("enter")
    print("Kop Surat berhasil ditambahkan")
    time.sleep(5)

if atur_sekolah() == "_main_":
    atur_sekolah()