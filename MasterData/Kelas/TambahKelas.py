from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from webdriver_manager.chrome import ChromeDriverManager


def tambah_kelas():
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

    # Tambah Kelas
    print("Klik tombol Tambah Kelas...")
    button_tambah = driver.find_element(By.XPATH, "//*[@data-testid='btn-add-class']")
    button_tambah.click()
    time.sleep(3)

    # Dropdown Unit
    print("Memilih unit dari dropdown...")
    dropdown = driver.find_element(By.XPATH, "//*[@data-testid='selected-value']")
    dropdown.click()
    value_dropdown = driver.find_element(By.XPATH, "//*[@data-testid='paragraph']")
    value_dropdown.click()

    # Prefix
    print("Memilih prefix...")
    element1 = driver.find_element(By.XPATH, "(//*[@data-testid='selected-value'])[2]")
    element1.click()
    value_element1 = driver.find_element(By.XPATH, "//*[@data-testid='option-81']")
    value_element1.click()
    time.sleep(5)

    # Pilih Jurusan
    print("Memilih jurusan...")
    jurusan = driver.find_element(By.XPATH, "(//*[@data-testid='selected-value'])[3]")
    jurusan.click()
    value_jurusan = driver.find_element(By.XPATH, "//*[@data-testid='option-53']")
    value_jurusan.click()

    # Suffix
    print("Mengisi suffix...")
    suffix = driver.find_element(By.NAME, "suffix")
    suffix.click()
    suffix.send_keys("sesat")

    # Terapkan
    try:
        print("Menunggu tombol Tambahkan dapat diklik...")
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class, 'flex items-center text-center') and text()='Tambahkan']")
            )
        )
        element.click()
        print("Tombol Tambahkan berhasil diklik!")
    except Exception as e:
        print(f"Error saat mengklik tombol Tambahkan: {e}")
    time.sleep(10)

    # Menutup browser
    print("Menutup browser...")
    driver.quit()
