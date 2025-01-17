import random

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")

# Inisialisasi driver
service = Service(executeable_path="C:\\Users\\akmal\\Selenium-Py\\chrome-headless-shell.exe")
driver = webdriver.Chrome(service=service)
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

# Klik Menu Master Data
master_data = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@data-testid='sidebar-menu-master-data'])[2]")))
master_data.click()
time.sleep(5)

#klik sub-menu siswa
kelola_siswa = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-kelola-siswa'])[2]")
kelola_siswa.click()

time.sleep(4)

#Tri-dots
tri_dots= driver.find_element(By.XPATH,"(//*[@data-testid='tridots-icon'])[1]")
tri_dots.click()

time.sleep(4)

edit = driver.find_element(By.XPATH,"//p[contains(@class, 'text-sm') and contains(@class, 'font-medium') and contains(@class, 'text-blue10') and contains(text(), 'Edit')]")
edit.click()

time.sleep(5)

#Nama Siswa

nama_siswa = driver.find_element(By.XPATH,"//*[@data-testid='full-name-input']")
nama_siswa.click()

nama_murid = [
    "Muhammad Akmal",
    "Rina Sari",
    "Budi Santoso",
    "Dewi Anggraini",
    "Joko Prabowo",
    "Anisa Putri"
]

# Pilih nama secara acak dari array
nama_siswa.send_keys(Keys.CONTROL+"a")
nama_siswa.send_keys(Keys.BACKSPACE)
nama_terpilih = random.choice(nama_murid)
nama_siswa.send_keys(nama_terpilih)
time.sleep(4)

#tombol simpan
simpan = driver.find_element(By.XPATH,"//button[div[contains(text(), 'Simpan')] and contains(@class, 'rounded-[6px]')]")
simpan.click()

time.sleep(3)

#pop-up ya

pop_up = driver.find_element(By.XPATH,"//div[contains(@class, 'flex') and contains(@class, 'items-center') and contains(@class, 'text-center') and text()='Ya']")
pop_up.click()
