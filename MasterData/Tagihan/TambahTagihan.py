import random
import string

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

#Sub-menu tagihan
sub_tagihan = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-tagihan'])[4]")
sub_tagihan.click()
time.sleep(10)

#Tambah Tagihan
btn_tambah_billing = driver.find_element(By.XPATH,"//*[@data-testid='btn-add-billing']")
btn_tambah_billing.click()

time.sleep(10)
#==========================================================================================================
# Input Nama Tagihan
nama_tagihan = driver.find_element(By.XPATH,"//input[@type='text' and @name='billingName' and @placeholder='Masukkan nama tagihan']")
nama_tagihan.click()

namaTagihan = [
    "Tagihan Uang Pangkal",
    "Tagihan Uang Jajan Guru",
    "Tagihan SPP - Januari",
    "Tagihan SPP - Februari",
    "Tagihan Uang Buku",
    "Tagihan Ujian Semester",
    "Tagihan Biaya Kegiatan",
    "Tagihan Iuran Kelas",
    "Tagihan Sumbangan Pengembangan Sekolah",
    "Tagihan Uang Kegiatan Ekstrakurikuler",
    "Tagihan Uang Praktikum",
    "Tagihan Fasilitas Siswa"
]
kumpulanTagihan = random.choice(namaTagihan)
nama_tagihan.send_keys(kumpulanTagihan)

time.sleep(5)

#TahunAjaran

tahun_ajaran = driver.find_element(By.XPATH,"(//*[@data-testid='selected-value'])[1]")
tahun_ajaran.click()

textbox = driver.find_element(By.XPATH,"//input[@type='text' and @placeholder='Cari tahun ajaran' and contains(@class, 'rounded-md') and contains(@class, 'cursor-auto')]")
textbox.click()
textbox.send_keys("2028")
time.sleep(3)

textbox1 = driver.find_element(By.XPATH,"//*[@data-testid='option-72']")
textbox1.click()
time.sleep(3)

#Tipe Tagihan
pilih_tagihan = driver.find_element(By.XPATH,"(//*[@data-testid='select-field'])[3]")
pilih_tagihan.click()
time.sleep(3)

value_tagihan = driver.find_element(By.XPATH,"//*[@data-testid='option-regular']")
value_tagihan.click()

time.sleep(3)

#Kelas

pilih_kelas = driver.find_element(By.XPATH,"//p[@class='text-base w-full text-neutral6' and text()='Pilih kelas']")
pilih_kelas.click()

checkbox = driver.find_element(By.XPATH,"(//*[@data-testd='checkbox'])[2]")
checkbox.click()
time.sleep(5)

#KodeTagihan
kode_tagihan = driver.find_element(By.NAME,"billingCode")
kode_tagihan.click()

def generate_random_billing(max_length=5):
    characters = string.ascii_lowercase + string.digits  # Kombinasi huruf kecil dan angka
    return ''.join(random.choices(characters, k=max_length))


random_billing = generate_random_billing()
print("Random Billing:", random_billing)

kode_tagihan.send_keys(random_billing)

time.sleep(5)

#Jumlah Tagihan perbulan

tagihan_perbulan = driver.find_element(By.NAME,"billingAmount")
tagihan_perbulan.click()

def generate_random_nominal(min_value=1000000, max_value=10000000):
    return str(random.randint(min_value, max_value))

random_nominal = generate_random_nominal()
tagihan_perbulan.send_keys(random_nominal)

time.sleep(5)

#Rekening Bank

field_rekening = driver.find_element(By.XPATH,"(//*[@data-testid='select-field'])[4]")
field_rekening.click()

time.sleep(3)

#Value Rekening
rek_value = driver.find_element(By.XPATH,"//*[@data-testid='option-28']")
rek_value.click()

time.sleep(3)

#Field Keterangan

keterangan = driver.find_element(By.XPATH,"//textarea[@name='description' and @placeholder='Masukkan keterangan']")
keterangan.click()
keterangan.send_keys("SEKOLAH BUTUH DUIT")

time.sleep(5)

#Generate Bill
generate_bill = driver.find_element(By.XPATH,"//button[@type='button' and contains(@class, 'rounded-[6px]') and .//div[text()='Generate']]")
generate_bill.click()
time.sleep(3)

#tambahkan

tambahkan_billing = driver.find_element(By.XPATH,"//button[contains(@class, 'rounded-[6px]') and .//div[text()='Tambahkan']]")
tambahkan_billing.click()
time.sleep(5)
#pop-up ya

popup_ya = driver.find_element(By.XPATH,"//div[contains(@class, 'flex items-center text-center') and text()='Ya']")
popup_ya.click()

time.sleep(7)

driver.quit()