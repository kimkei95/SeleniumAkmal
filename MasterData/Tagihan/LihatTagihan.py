import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def lihat_tagihan():


    try:
        # Inisialisasi driver
        options = Options()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--headless")

        # Inisialisasi driver
        print("Inisialisasi driver...")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.maximize_window()
        print("Driver initialized and window maximized")

        # Akses URL
        driver.get("https://sit.siprusedu.com/login")
        print("Opening the login page")

        # Tunggu hingga elemen email dapat ditemukan
        wait = WebDriverWait(driver, 10)
        email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        print("Email field found")

        password = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main/div[1]/div/form/button")

        # Masukkan kredensial
        email.send_keys("admin.sekolah@gmail.com")
        password.send_keys("Test1234")
        print("Credentials entered")

        # Klik tombol login
        login_button.click()
        print("Login button clicked")

        # Tunggu beberapa detik setelah login
        time.sleep(9)

        # Klik Menu Master Data
        master_data = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[@data-testid='sidebar-menu-master-data'])[2]")))

        master_data.click()
        print("Master Data menu clicked")
        time.sleep(5)

        # Sub-menu tagihan
        sub_tagihan = driver.find_element(By.XPATH, "(//*[@data-testid='sidebar-menu-tagihan'])[4]")
        sub_tagihan.click()
        print("Tagihan sub-menu clicked")
        time.sleep(5)

        # Lihat Tagihan
        lihat = driver.find_element(By.XPATH, "(//*[@data-testid='remove-red-eye-icon'])[1]")
        lihat.click()
        print("Tagihan details viewed")

        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Quit the driver
        driver.quit()
        print("Driver quit, script completed")

if lihat_tagihan() =="_main_":
    lihat_tagihan()