from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

from webdriver_manager.chrome import ChromeDriverManager

def cari_riwayat():
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

     # Tunggu hingga elemen email dapat ditemukan
    wait = WebDriverWait(driver, 10)  # Tunggu hingga 10 detik
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main/div[1]/div/form/button")

     # Masukkan kredensial
    email.send_keys("admin.sekolah@gmail.com")
    password.send_keys("Test1234")

     # Klik tombol login
    login_button.click()

     # Tunggu beberapa detik setelah login
    time.sleep(9)


     #Master Tagihan Menu
    menu_tagihan = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-tagihan'])[5]")
    menu_tagihan.click()

    time.sleep(4)

    #Sub menu Riwayat Pembayaran

    riwayat_pembayaran = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-riwayat-pembayaran'])[2]")
    riwayat_pembayaran.click()

    time.sleep(5)

    #filter metode pembayaran
    metode_pembayaran = driver.find_element(By.XPATH,"(//*[@data-testid='selected-value'])[1]")
    metode_pembayaran.click()

    dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="dropdown-menu"]'))
    )
    options = dropdown.find_elements(By.CSS_SELECTOR, '[data-testid^="option-"]')
    if options:
        random_option = random.choice(options)
        random_option.click()
    else:
        print("Tidak ada opsi yang ditemukan dalam dropdown.")

    time.sleep(5)

    #status Pembayaran

    status = driver.find_element(By.XPATH,"(//*[@data-testid='selected-value'])[2]")
    status.click()
    time.sleep(3)

    #random pilih status

    dropdown1 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="dropdown-menu"]'))
    )
    options1 = dropdown1.find_elements(By.CSS_SELECTOR, '[data-testid^="option-"]')
    if options1:
        random_option1 = random.choice(options1)
        random_option1.click()
    else:
        print("Tidak ada opsi yang ditemukan dalam dropdown.")

    time.sleep(5)

    #Klik Terapkan

    terapkan_filter = driver.find_element(By.XPATH,"//button[div[text()='Terapkan']]")
    terapkan_filter.click()

    time.sleep(3)
    driver.quit()

if cari_riwayat() == "_main_":
    cari_riwayat()