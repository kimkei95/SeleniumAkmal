import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def filter_siswa():
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
        print("Browser dibuka dan dimaksimalkan.")

            # Akses URL
        driver.get("https://sit.siprusedu.com/login")
        print("URL login dibuka.")

        # Tunggu hingga elemen email dapat ditemukan
        wait = WebDriverWait(driver, 10)
        email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        password = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main/div[1]/div/form/button")
        print("Elemen login ditemukan.")

            # Masukkan kredensial
        email.send_keys("admin.sekolah@gmail.com")
        password.send_keys("Test1234")
        print("Kredensial dimasukkan.")

            # Klik tombol login
        login_button.click()
        print("Tombol login diklik.")

            # Tunggu hingga login berhasil
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@data-testid='sidebar-menu-master-data'])[2]")))
        print("Login berhasil.")

            # Klik Menu Master Data
        master_data = driver.find_element(By.XPATH, "(//*[@data-testid='sidebar-menu-master-data'])[2]")
        master_data.click()
        print("Menu Master Data diklik.")

            # Klik sub-menu siswa
        kelola_siswa = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@data-testid='sidebar-menu-kelola-siswa'])[2]")))
        kelola_siswa.click()
        print("Sub-menu Kelola Siswa diklik.")

            # Klik dropdown Kelas
        dropdown_kelas = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@data-testid='selected-value'])[2]")))
        dropdown_kelas.click()
        print("Dropdown Kelas dibuka.")

            # Masukkan nilai kelas
        value_kelas = driver.find_element(By.XPATH, "//input[@placeholder='Cari kelas']")
        value_kelas.send_keys("agama")
        print("Nilai 'agama' dimasukkan ke filter kelas.")

            # Pilih kelas yang sesuai
        pilih_value = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@data-testid='option-192']")))
        pilih_value.click()
        print("Kelas 'agama' dipilih.")

            # Klik tombol Terapkan Filter
        btn_terapkan_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='flex items-center text-center'])[5]")))
        btn_terapkan_filter.click()
        print("Tombol Terapkan Filter diklik.")
        time.sleep(4)

    finally:
            # Menutup browser
            driver.quit()
            print("Browser ditutup.")

