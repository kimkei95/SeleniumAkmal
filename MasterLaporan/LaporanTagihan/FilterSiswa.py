import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def filter_laporan_tagihan():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--headless")

    try:
        # Inisialisasi driver
        print("Inisialisasi driver...")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        # Akses URL
        print("Mengakses URL...")
        driver.get("https://sit.siprusedu.com/login")

        # Tunggu hingga elemen login tersedia
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
        time.sleep(9)  # Tunggu beberapa detik setelah login

        # Menuju halaman laporan
        try:
            print("Navigasi ke menu laporan...")
            menu_laporan = driver.find_element(By.XPATH, "(//*[@data-testid='sidebar-menu-laporan'])[2]")
            menu_laporan.click()
            time.sleep(3)
        except Exception as e:
            print(f"Error saat menuju menu laporan: {e}")

        # Menu tagihan
        try:
            print("Navigasi ke menu tagihan...")
            menu_pembayaran = driver.find_element(By.XPATH, "(//*[@data-testid='sidebar-menu-tagihan'])[6]")
            menu_pembayaran.click()
            time.sleep(3)
        except Exception as e:
            print(f"Error saat menuju menu tagihan: {e}")

        # Pilih kelas
        try:
            print("Memilih kelas...")
            kelas_options = ["option-60", "option-13", "option-14", "option-61"]
            selected_option = random.choice(kelas_options)

            # Klik dropdown kelas
            kelas = driver.find_element(By.XPATH, "(//*[@data-testid='selected-value'])[2]")
            kelas.click()
            time.sleep(3)

            # Klik input untuk mencari kelas
            value_kelas = driver.find_element(By.XPATH, "//input[@placeholder='Cari kelas']")
            value_kelas.click()
            time.sleep(3)

            # Pilih kelas berdasarkan data-testid yang terpilih
            selected_element = driver.find_element(By.XPATH, f"//*[@data-testid='{selected_option}']")
            selected_element.click()

            # Log kelas yang dipilih
            print(f"Kelas yang dipilih: {selected_option}")
            time.sleep(4)
        except Exception as e:
            print(f"Error saat memilih kelas: {e}")

        # Klik tombol "Terapkan"
        try:
            print("Klik tombol Terapkan...")
            btn_terapkan = driver.find_element(By.XPATH, "//button[div[text()='Terapkan']]")
            btn_terapkan.click()
            time.sleep(4)
        except Exception as e:
            print(f"Error saat klik tombol Terapkan: {e}")

    except Exception as e:
        print(f"Error utama: {e}")

    finally:
        # Tutup browser
        print("Menutup browser...")
        driver.quit()

if filter_laporan_tagihan() == "_main_":
    filter_laporan_tagihan()