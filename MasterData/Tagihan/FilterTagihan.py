import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def filter_tagihan():
    # Setup options
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
    print("Opening The Site")

    # Tunggu hingga elemen email dapat ditemukan
    wait = WebDriverWait(driver, 10)  # Tunggu hingga 10 detik
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
    print("Field email ditemukan")

    password = driver.find_element(By.NAME, "password")
    print("Field password tersedia")

    login_button = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main/div[1]/div/form/button")
    print("Field Login Tersedia")

    # Masukkan kredensial
    email.send_keys("admin.sekolah@gmail.com")
    password.send_keys("Test1234")
    print("Seluruh credential sudah terisi")

    # Klik tombol login
    login_button.click()
    print("Login button clicked")

    # Tunggu beberapa detik setelah login
    time.sleep(9)

    # Klik Menu Master Data
    master_data = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//*[@data-testid='sidebar-menu-master-data'])[2]")))
    master_data.click()
    print("Menu master data terklik")
    time.sleep(5)

    # Sub-menu tagihan
    sub_tagihan = driver.find_element(By.XPATH, "(//*[@data-testid='sidebar-menu-tagihan'])[4]")
    sub_tagihan.click()
    print("Sub-menu tagihan terklik")
    time.sleep(5)

    # Klik Filter
    btn_filter = driver.find_element(By.XPATH, "//*[@data-testid='btn-filter-billing']")
    btn_filter.click()
    print("Filter button clicked")
    time.sleep(5)

    # # Tipe Tagihan
    # tipe_tagihan = driver.find_element(By.XPATH, "(//*[@data-testid='selected-value'])[1]")
    # tipe_tagihan.click()
    #
    # print("Tipe Tagihan dropdown clicked")
    # time.sleep(5)

    # Pilih Rekening
    pilih_rekening = driver.find_element(By.XPATH, "(//*[@data-testid='selected-value'])[2]")
    pilih_rekening.click()
    print("Rekening dropdown clicked")
    time.sleep(5)

    # Value Rekening
    value_rekening = driver.find_element(By.XPATH, "//*[@data-testid='option-91']")
    value_rekening.click()
    print("Rekening value selected")

    # Terapkan filter
    btn_submit_filter = driver.find_element(By.XPATH, "//*[@data-testid='btn-submit-filter']")
    btn_submit_filter.click()
    print("Filter applied")

    time.sleep(10)

    driver.quit()
    print("Driver quit, script completed")

if filter_tagihan() == "_main_":
    filter_tagihan()