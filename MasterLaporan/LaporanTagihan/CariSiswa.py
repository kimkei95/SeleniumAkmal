import random

import pyautogui
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def cari_tagihan_siswa():
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

    #Menuju halaman Laporan

    menu_laporan = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-laporan'])[2]")
    menu_laporan.click()

    time.sleep(3)


    #Menu Tgihan

    menu_pembayaran = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-tagihan'])[6]")
    menu_pembayaran.click()

    time.sleep(3)

    #cari siswa

    try:
        # Klik dan isi search bar
        search_bar = driver.find_element(By.XPATH, "//*[@data-testid='input-search']")
        search_bar.click()
        search_bar.send_keys("Akmal")
        time.sleep(3)  # Tunggu hingga hasil pencarian muncul

        search_results = driver.find_elements(By.XPATH, "//div[contains(@class, 'absolute left-0 top-12')]//p")


        if not search_results:
            raise NoSuchElementException("Tidak ada hasil pencarian ditemukan.")


        random_result = random.choice(search_results)
        selected_text = random_result.text
        random_result.click()
        print("Hasil pencarian yang dipilih:", selected_text)

    except NoSuchElementException as e:
        print(f"Error: {e}")


    time.sleep(3)

    #Terapkan filter
    button_terapkan = driver.find_element(By.XPATH,"//button[div[text()='Terapkan']]")
    button_terapkan.click()
    time.sleep(5)

    driver.quit()

if cari_tagihan_siswa() == "_main_":
    cari_tagihan_siswa()