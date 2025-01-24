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


def edit_kelas():
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

    # Klik Sidebar Menu Kelas
    print("Klik menu Kelas...")
    sidebar_menu_kelas = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@data-testid='sidebar-menu-kelas'])[2]")))
    sidebar_menu_kelas.click()

    time.sleep(15)
    print("Klik tombol Edit Kelas...")
    btn_edit = driver.find_element(By.XPATH, "(//*[@data-testid='btn-edit-class'])[1]")
    btn_edit.click()
    time.sleep(5)

    # Edit Suffix
    print("Mengedit Suffix...")
    suffix = driver.find_element(By.NAME, "suffix")
    suffix.click()
    suffix.send_keys(Keys.CONTROL + "a")
    suffix.send_keys(Keys.BACKSPACE)
    suffixes = ["setengah sesat", "hampir sesat", "super sesat", "dahlah cape gua"]
    random_suffix = random.choice(suffixes)
    suffix.send_keys(random_suffix)
    print(f"Suffix yang dipilih: {random_suffix}")
    time.sleep(5)

    # Klik Simpan
    try:
        print("Menunggu tombol Simpan dapat diklik...")
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']//div[text()='Simpan']"))
        )
        button.click()
        print("Tombol Simpan berhasil diklik!")
    except Exception as e:
        print(f"Error saat mencoba klik tombol Simpan: {e}")
        time.sleep(6)

    # Menutup browser
    print("Menutup browser...")
    driver.quit()
