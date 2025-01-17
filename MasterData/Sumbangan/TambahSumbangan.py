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

#klik menu Sumbangan

sumbangan = driver.find_element(By.XPATH, "(//*[@data-testid='sidebar-menu-sumbangan'])[2]")
driver.execute_script("arguments[0].scrollIntoView(true);", sumbangan)
time.sleep(1)  # Tunggu sejenak
sumbangan.click()

time.sleep(5)

#Klik Button Tambah
btn_sumbangan = driver.find_element(By.XPATH,"//div[contains(@class, 'flex items-center text-center') and normalize-space(text())='Tambah']")
btn_sumbangan.click()
time.sleep(5)

#Nama Sumbangan
nama_sumbangan = wait.until(EC.presence_of_element_located((By.NAME, "donationName")))
nama_sumbangan.click()

# Pilih Nama Sumbangan Secara Acak
nama_donasi = [
    "Sumbangan Buku Pelajaran",
    "Sumbangan Renovasi Sekolah",
    "Sumbangan Bencana Alam",
    "Sumbangan Perpustakaan",
    "Sumbangan Teknologi Digital",
    "Sumbangan Seragam Siswa",
    "Sumbangan Pembangunan Masjid",
    "Sumbangan Kebun Sekolah",
    "Sumbangan Kegiatan Pramuka",
    "Sumbangan Kesehatan Anak",
    "Sumbangan Lab Komputer",
    "Sumbangan Beasiswa Siswa",
    "Sumbangan Penanaman Pohon",
    "Sumbangan Festival Seni",
    "Sumbangan Ekskul Olahraga",
    "Sumbangan Transportasi Siswa",
    "Sumbangan Infrastruktur Kelas",
    "Sumbangan Bahan Makanan",
    "Sumbangan Alat Musik",
    "Sumbangan Fasilitas Kamar Mandi"
]
donasi = random.choice(nama_donasi)
nama_sumbangan.send_keys(donasi)

time.sleep(5)

#pilih akun bank

pilih_akunbank = driver.find_element(By.XPATH,"(//*[@data-testid='selected-value'])[1]")
pilih_akunbank.click()
time.sleep(5)

#pilih value akun bank

value_akunbank = driver.find_element(By.XPATH,"//*[@data-testid='option-161']")
value_akunbank.click()

#pilih unit

unit_sekolah = driver.find_element(By.XPATH,"(//*[@data-testid='selected-value'])[2]")
unit_sekolah.click()

#value Sekolah

value_sekolah = driver.find_element(By.XPATH,"//*[@data-testid='paragraph']")
value_sekolah.click()
#tombol tambahkan

btn_tambahkan = driver.find_element(By.XPATH,"//button[contains(@class, 'rounded-[6px] flex whitespace-nowrap justify-center items-center font-bold gap-1 h-[44px] py-2 px-6 text-sm bg-blue8') and @type='submit' and .//div[text()='Tambahkan']]")
btn_tambahkan.click()

time.sleep(7)

driver.quit()