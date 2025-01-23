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

    #Klik Menu Informasi
informasi = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-informasi'])[2]")
informasi.click()
print("Menu informasi berhasil di klik")
time.sleep(3)

    #Klik Sub-menu Pengumuman & Event
sub_pengumuman = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-pengumuman-&-event'])[2]")
sub_pengumuman.click()
print("Sub-Menu Pengumuman berhasil di klik")
time.sleep(3)

#klik tridots

# Temukan semua elemen dengan data-testid='tridots-icon'
tridots_elemen = driver.find_elements(By.XPATH, "//*[@data-testid='tridots-icon']")

# Pilih salah satu elemen secara acak
tridots_terpilih = random.choice(tridots_elemen)

# Klik elemen yang terpilih
tridots_terpilih.click()
print("Tridots Berhasil Terklik")
time.sleep(4)

#Klik Edit
edit = driver.find_element(By.XPATH,"//*[@data-testid='action-0']")
edit.click()
print("Masuk Ke Fungsi Edit Pengumuman/Event")

time.sleep(4)
#title
judul_pengumuman = [
    "Pengumuman Libur Sekolah Akhir Semester",
    "Jadwal Ujian Tengah Semester Ganjil",
    "Hasil Seleksi Lomba Cerdas Cermat",
    "Kegiatan Bakti Sosial Minggu Depan",
    "Pengambilan Raport Semester Ganjil",
    "Pembagian Seragam untuk Siswa Baru",
    "Kegiatan Study Tour ke Museum Nasional",
    "Lomba Kebersihan Antar Kelas",
    "Pemberitahuan Jam Masuk Baru",
    "Pendaftaran Ekstrakurikuler Dibuka!",
    "Workshop Teknologi untuk Guru dan Siswa",
    "Hari Guru Nasional: Acara dan Perayaan",
    "Kegiatan Donor Darah di Sekolah",
    "Perubahan Jadwal Pelajaran",
    "Informasi Penting untuk Orang Tua/Wali Murid",
    "Jadwal Latihan Paduan Suara",
    "Penggalangan Dana untuk Korban Bencana",
    "Sosialisasi Program Sekolah Bebas Sampah",
    "Latihan Tari Tradisional untuk Lomba",
    "Jadwal Vaksinasi untuk Siswa",
]

# Pilih judul secara acak
judul_terpilih = random.choice(judul_pengumuman)

# Input ke elemen title
add_title = driver.find_element(By.NAME, "title")
add_title.click()
print("field title berhasil di klik")
add_title.send_keys(Keys.CONTROL+ "a")
time.sleep(1)
add_title.send_keys(Keys.BACKSPACE)
time.sleep(1)
add_title.send_keys(judul_terpilih)
print("Judul Berhasil Diganti")
time.sleep(4)


#SimpanPerbuahan

perubahan = driver.find_element(By.XPATH,"//button[.//div[text()='Simpan']]")
perubahan.click()
print("tombol simpan berhasil di klik")
time.sleep(3)

#pop up
popUp = driver.find_element(By.XPATH,"//button[.//div[text()='Ya']]")
popUp.click()
print("menyimpan perubahan...")
time.sleep(7)

