from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from webdriver_manager.chrome import ChromeDriverManager


def lihat_siswa():
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
    print("Klik tri-dots untuk membuka opsi...")
    tri_dots = driver.find_element(By.XPATH, "(//*[@data-testid='tridots-icon'])[1]")
    tri_dots.click()
    time.sleep(4)

    # Klik opsi "Lihat"
    print("Klik opsi 'Lihat'...")
    lihat = driver.find_element(By.XPATH, "//p[@class='text-sm font-medium text-blue10 group-hover:text-blue7' and text()='Lihat']")
    lihat.click()
    time.sleep(7)

    # Menutup browser
    print("Menutup browser...")
    driver.quit()

