import random
from selenium.webdriver.common.keys import Keys
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


 #Master Tagihan Menu
menu_tagihan = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-tagihan'])[5]")
menu_tagihan.click()

time.sleep(4)

#sub menu tagihan persiswa

tagihan_perSiswa = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-tagihan-per-siswa'])[2]")
tagihan_perSiswa.click()

time.sleep(3)

#dropdown unit
unit_dropdown = driver.find_element(By.XPATH,"(//*[@data-testid='selected-value'])[1]")
unit_dropdown.click()

value_dropdown = driver.find_element(By.XPATH,"//*[@data-testid='option-3']")
value_dropdown.click()
time.sleep(3)

#dropdown kelas

kelas_dropdown = driver.find_element(By.XPATH,"(//*[@data-testid='selected-value'])[2]")
kelas_dropdown.click()
time.sleep(3)

dropdown_pilihKelas = driver.find_element(By.XPATH,"//input[@placeholder='Cari kelas']")
dropdown_pilihKelas.click()
dropdown_pilihKelas.send_keys("XI IPA 3")

value_kelasIpa3 = driver.find_element(By.XPATH,"//*[@data-testid='option-13']")
value_kelasIpa3.click()

#cari siswa

cari_siswa = driver.find_element(By.XPATH,"//*[@data-testid='input-search']")
cari_siswa.click()
cari_siswa.send_keys("charlotte")
time.sleep(5)

value_siswaDicari = driver.find_element(By.XPATH,"//p[contains(text(), '93034 - charlotte')]")
value_siswaDicari.click()

#terapkan

btn_terapkan_siswa = driver.find_element(By.XPATH,"//div[text()='Terapkan']")
btn_terapkan_siswa.click()

time.sleep(5)

#hapus tagihan
rows = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[id^="table-row-"]')))

filtered_rows = [row for row in rows if int(row.get_attribute("id").split("-")[2]) <= 9]

if filtered_rows:
    random_row = random.choice(filtered_rows)
    random_row.click()
    time.sleep(4)
else:
    print("Tidak ada elemen dengan ID yang dimulai dengan 'table-row-' ditemukan dalam rentang yang diinginkan.")


option_hapus = driver.find_element(By.XPATH,"//*[@data-testid='action-1']")
option_hapus.click()

time.sleep(5)

#opsi Ya

button_ya = driver.find_element(By.XPATH,"//button[div[text()='Ya']]")
button_ya.click()

time.sleep(6)

driver.quit()