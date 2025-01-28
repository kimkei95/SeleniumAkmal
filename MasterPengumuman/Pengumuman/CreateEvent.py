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

def crete_event ():
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


    #tambah Event
    tambah_event = driver.find_element(By.XPATH,"//button[.//div[text()='Tambah']]")
    tambah_event.click()
    print("tombol tambah berhasil di klik")
    time.sleep(4)

    #dropdown menu

    dropdown_menu = driver.find_element(By.XPATH,"(//*[@data-testid='selected-value'])[1]")
    dropdown_menu.click()
    print("Dropdown Berhasil Diklik")
    time.sleep(4)

    value_dropdown = driver.find_element(By.XPATH,"//*[@data-testid='option-AT01']")
    value_dropdown.click()
    print("Value Event Terpilih")
    time.sleep(3)

    #pilih gambar
    tambah_gambar = driver.find_element(By.XPATH,"//*[@data-testid='upload-action-label']")
    tambah_gambar.click()
    print("Membuka file explorer")
    time.sleep(6)
    #automate cari pakai gui
    pyautogui.write(r"C:\Users\akmal\Downloads\tarik tambang.jpg")  # Path file gambar
    pyautogui.press("enter")
    print("Gambar berhasil ditambahkan")

    time.sleep(5)

    #title Event
    judul_event = [
        "Pentas Seni Akhir Tahun",
        "Lomba Cerdas Cermat Antar Kelas",
        "Workshop Pengembangan Diri untuk Siswa",
        "Hari Karir: Kenali Dunia Kerja",
        "Peringatan Hari Pendidikan Nasional",
        "Festival Budaya Nusantara",
        "Seminar Motivasi Belajar Efektif",
        "Lomba Kebersihan dan Keindahan Kelas",
        "Workshop Teknologi: Mengenal AI dan Robotika",
        "Bazaar Amal untuk Pendidikan",
        "Pelatihan Menulis Kreatif untuk Siswa",
        "Turnamen Futsal Antar Kelas",
        "Peringatan Hari Kemerdekaan",
        "Pagelaran Musik dan Tari Tradisional",
        "Lomba Debat Bahasa Inggris",
        "Sosialisasi Hidup Sehat untuk Remaja",
        "Kunjungan Edukasi ke Museum",
        "Pentas Drama Bertema Lingkungan",
        "Hari Literasi: Baca Buku, Buka Dunia",
        "Pekan Olahraga dan Seni Sekolah (PORSENI)"
    ]


    # Pilih judul secara acak
    judul_terpilih = random.choice(judul_event)

    print("Judul event terpilih:", judul_terpilih)
    add_title = driver.find_element(By.NAME, "title")
    add_title.click()
    print("field title berhasil di klik")
    add_title.send_keys(judul_terpilih)

    time.sleep(3)

    desc_event = driver.find_element(By.XPATH,"//*[@data-gramm='false']")
    desc_event.click()
    desc_event.send_keys("Test")
    time.sleep(3)

    #Simpan Perubahan

    conf_event = driver.find_element(By.XPATH,"//button[.//div[text()='Simpan']]")
    conf_event.click()
    print("tombol Simpan Berhasil Di klik")

    #Pop-up

    conf_popUp = driver.find_element(By.XPATH,"//button[.//div[text()='Ya']]")
    conf_popUp.click()

    time.sleep(15)

if crete_event() =="_main_":
    crete_event()