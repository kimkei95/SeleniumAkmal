import random

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

    # Pengturan Sistem
pengaturan_sistem = driver.find_element(By.XPATH, "(//*[@data-testid='sidebar-menu-pengaturan-sistem'])[2]")
pengaturan_sistem.click()
time.sleep(4)
print("berhasil masuk ke menu pengaturan sistem")

# card invoice

invoice = driver.find_element(By.XPATH,"//div[@class='flex h-[148px] w-[160px] cursor-pointer flex-col items-center justify-center gap-3 rounded-md border' and .//p[text()='Invoice']]")
invoice.click()
time.sleep(4)



# Temukan elemen input untuk prefix
field_prefix = driver.find_element(By.NAME, "prefix")
field_prefix.click()  # Klik field untuk memastikan fokus
field_prefix.send_keys(Keys.CONTROL + "a")
field_prefix.send_keys(Keys.BACKSPACE)
time.sleep(3)  # Tunggu sebentar
prefix_options = ["INV-", "INVOICE-", "TAGIHAN-", "NOTA-"]

# Pilih prefix secara acak
random_prefix = random.choice(prefix_options)
field_prefix.send_keys(random_prefix)
time.sleep(4)


#ubah format

# Klik pada elemen yang memunculkan pilihan format
ubah_format = driver.find_element(By.XPATH, "//*[@data-testid='selected-value']")
ubah_format.click()

# Tunggu beberapa detik agar opsi muncul
time.sleep(3)

# Ambil semua elemen yang memiliki atribut data-testid yang dimulai dengan 'option-'
options = driver.find_elements(By.XPATH, "//*[starts-with(@data-testid, 'option-')]")

# Pilih salah satu elemen secara acak
random_option = random.choice(options)

# Klik opsi yang dipilih
random_option.click()

time.sleep(4)

#simpan perubahan

simpan_perubahan = driver.find_element(By.XPATH,"//button[div[text()='Lanjutkan']]")
simpan_perubahan.click()

time.sleep(5)


