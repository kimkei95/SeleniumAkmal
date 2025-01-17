import random

from selenium import webdriver
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


#Master Data Menu
master_data = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@data-testid='sidebar-menu-master-data'])[2]")))
master_data.click()
time.sleep(6)

#Akun Bank
akun_bank = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-akun-bank'])[2]")
akun_bank.click()
time.sleep(6)

#Tambah Akun Bank
btn_tambah = driver.find_element(By.XPATH,"//*[@data-testid='btn-add-bank']")
btn_tambah.click()
time.sleep(6)

#Pilih Nama Bank
dropdown_bank = driver.find_element(By.XPATH,"//*[@data-testid='selected-value']")
dropdown_bank.click()

value_bank = driver.find_element(By.XPATH,"//*[@data-testid='option-PT. BANK CIMB NIAGA UNIT USAHA SYARIAH - (CIMB SYARIAH)']")
value_bank.click()
time.sleep(3)

#Nama Rekening
nasabah = driver.find_element(By.XPATH,"//*[@data-testid='field-bank-name']")
nasabah.click()

nasabah_Array = ["toni", "jono", "Budi Handoko", "Kim jong Un", "Tony Stark", "Tony Hawk", "Dani Aditya", "Oda nobunaga", "Itachi Uchiha"]
random_nasabah= random.choice(nasabah_Array)
nasabah.send_keys(random_nasabah)
time.sleep(7)

#Nomor Rekening

norek = driver.find_element(By.XPATH,"//*[@data-testid='field-bank-number']")
norek.click()

norek_random = [random.randint(10000, 99999) for _ in range(5)]
angka_random = random.choice(norek_random)

norek.send_keys(angka_random)
time.sleep(5)

#Kepemilikan

kepemilikan = driver.find_element(By.XPATH,"(//*[@data-testid='selected-value'])[2]")
kepemilikan.click()

value_kepemilikan = driver.find_element(By.XPATH,"(//*[@data-testid='paragraph'])[1]")
value_kepemilikan.click()

#Tambah Data
button_tambahData = driver.find_element(By.XPATH,"//button[contains(@class, 'rounded-[6px]') and .//div[text()='Tambahkan']]")
button_tambahData.click()

time.sleep(6)

driver.quit()