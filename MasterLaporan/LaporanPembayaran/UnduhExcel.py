

import pyautogui
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def unduh_pembayaran_excel():

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


    #Menu Pembayaran

    menu_pembayaran = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-pembayaran'])[4]")
    menu_pembayaran.click()

    time.sleep(3)

    #Klik Unduh EXCEL

    unduh_excel = driver.find_element(By.XPATH,"//button[div[text()='Unduh Excel']]")
    unduh_excel.click()

    time.sleep(4)

    driver.quit()

if unduh_pembayaran_excel() == "_main_":
    unduh_pembayaran_excel()