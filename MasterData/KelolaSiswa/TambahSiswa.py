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

#Button Tambah

btn_tambah_siswa = driver.find_element(By.XPATH,"//div[@class='flex items-center text-center' and text()='Tambah']")
btn_tambah_siswa.click()

time.sleep(4)


#Field Nama Siswa

nama_siswa1 = driver.find_element(By.XPATH,"//*[@data-testid='full-name-input']")
nama_siswa1.click()

nama_murid1 = [
    "Muhammad Akmal",
    "Rina Sari",
    "Budi Santoso",
    "Dewi Anggraini",
    "Joko Prabowo",
    "Anisa Putri"
]

# Pilih nama secara acak dari array
nama_siswa1.send_keys(Keys.CONTROL+"a")
nama_siswa1.send_keys(Keys.BACKSPACE)
nama_terpilih1 = random.choice(nama_murid1)
nama_siswa1.send_keys(nama_terpilih1)
time.sleep(4)

#NIS

nis_siswa = driver.find_element(By.NAME,"nis")
nis_siswa.click()

nis_random = [random.randint(10000, 99999) for _ in range(5)]
number_random = random.choice(nis_random)

nis_siswa.send_keys(number_random)

time.sleep(5)

#Status

status_siswa = driver.find_element(By.XPATH,"(//*[@data-testid='select-field'])[1]")
status_siswa.click()
#========================================================================================================

#Randomize Pilihan Status
dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='dropdown-menu']")))

# Tangkap elemen Regular dan Non Regular
aktif = driver.find_element(By.XPATH, "//div[@data-testid='option-aktif']")
tamat = driver.find_element(By.XPATH, "//div[@data-testid='option-tamat']")
pindah_sekolah = driver.find_element(By.XPATH,"//div[@data-testid='option-pindah_sekolah']")
putus_sekolah = driver.find_element(By.XPATH,"//div[@data-testid='option-dropout']")
# Pilihan opsi dalam list
opsi_list = [aktif,tamat,pindah_sekolah,putus_sekolah]

# Pilih secara acak
selected_option = random.choice(opsi_list)

# Klik opsi yang dipilih
selected_option.click()
time.sleep(5)

#=========================================================================================================

#tahun_ajaran

tahun_ajaran_siswa = driver.find_element(By.XPATH,"(//*[@data-testid='select-field'])[2]")
tahun_ajaran_siswa.click()

time.sleep(3)

cari_tahun_ajaran = driver.find_element(By.XPATH,"//input[@placeholder='Cari tahun ajaran']")
cari_tahun_ajaran.click()
cari_tahun_ajaran.send_keys("2025")

hasilCari = driver.find_element(By.XPATH,"//*[@data-testid='option-71']")
hasilCari.click()

time.sleep(3)

#Tempat Lahir

tempatLahir = driver.find_element(By.NAME,"birthPlace")
tempatLahir.click()

kota = [
    "Jakarta",
    "Surabaya",
    "Bandung",
    "Medan",
    "Bekasi",
    "Semarang",
    "Tangerang",
    "Depok",
    "Palembang",
    "Bogor",
    "Makassar",
    "Malang",
    "Padang",
    "Denpasar",
    "Yogyakarta",
    "Pekanbaru",
    "Banjarmasin",
    "Pontianak",
    "Manado",
    "Balikpapan",
    "Samarinda",
    "Cirebon",
    "Tasikmalaya",
    "Mataram",
    "Kupang",
    "Jayapura",
    "Sorong",
    "Ambon",
    "Kendari",
    "Gorontalo"
]

kota_terpilih = random.choice(kota)
print("Kota terpilih:", kota_terpilih)
tempatLahir.send_keys(kota_terpilih)

time.sleep(3)

