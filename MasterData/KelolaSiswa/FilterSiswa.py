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

#Kelas

dropdown_kelas = driver.find_element(By.XPATH,"(//*[@data-testid='selected-value'])[2]")
dropdown_kelas.click()

value_kelas = driver.find_element(By.XPATH,"//input[@placeholder='Cari kelas']")
value_kelas.click()
value_kelas.send_keys("agama")

pilih_value = driver.find_element(By.XPATH,"//*[@data-testid='option-192']")
pilih_value.click()

time.sleep(5)
#terapkan

btn_terapkan_filter = driver.find_element(By.XPATH,"//div[@class='flex items-center text-center' and text()='Terapkan']")
btn_terapkan_filter.click()

time.sleep(7)

driver.quit()

