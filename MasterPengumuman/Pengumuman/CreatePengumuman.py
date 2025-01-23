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

tambah_pengumuman = driver.find_element(By.XPATH,"//button[.//div[text()='Tambah']]")
tambah_pengumuman.click()
print("Button Tambah Berhasil Diklik dan Masuk Ke Tambah Pengumuman")
time.sleep(3)

#Add Gambar Pengumuman
tambah_gambar = driver.find_element(By.XPATH,"//*[@data-testid='upload-action-label']")
tambah_gambar.click()

time.sleep(3)

pyautogui.write(r"C:\Users\akmal\Downloads\winter-aespa-hot-mess-4k-wallpaper-uhdpaper.com-362@0@k.jpg")  # Path file gambar
pyautogui.press("enter")  # Tekan Enter untuk memilih file

time.sleep(5)
print("gambar berhasil di upload")

#Tambah Judul Pengumuman
# Daftar judul pengumuman
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
add_title.send_keys(judul_terpilih)

time.sleep(4)

#Deskripsi Pengumuman

desc_pengumuman = driver.find_element(By.XPATH,"//*[@data-gramm='false']")
desc_pengumuman.click()
desc_pengumuman.send_keys("Test")
time.sleep(3)

#Simpan Perubahan

conf_pengumuman = driver.find_element(By.XPATH,"//button[.//div[text()='Simpan']]")
conf_pengumuman.click()
print("tombol Simpan Berhasil Di klik")

#Pop-up

conf_popUp = driver.find_element(By.XPATH,"//button[.//div[text()='Ya']]")
conf_popUp.click()

time.sleep(10)