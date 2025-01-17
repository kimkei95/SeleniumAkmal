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

#Sub-menu tagihan
sub_tagihan = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-tagihan'])[4]")
sub_tagihan.click()
time.sleep(5)

#Filter
btn_filter = driver.find_element(By.XPATH,"//*[@data-testid='btn-filter-billing']")
btn_filter.click()
time.sleep(5)

#Tipe Tagihan
tipe_tagihan = driver.find_element(By.XPATH,"(//*[@data-testid='selected-value'])[1]")
tipe_tagihan.click()
time.sleep(5)
##=======================================================================================================

#Randomize Pilihan
dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='dropdown-menu']")))

# Tangkap elemen Regular dan Non Regular
regular_option = driver.find_element(By.XPATH, "//div[@data-testid='option-regular']")
non_regular_option = driver.find_element(By.XPATH, "//div[@data-testid='option-non-regular']")

# Pilihan opsi dalam list
options = [regular_option, non_regular_option]

# Pilih secara acak
selected_option = random.choice(options)

# Klik opsi yang dipilih
selected_option.click()
time.sleep(5)

#============================================================================================================

#Pilih Rekening

pilih_rekening = driver.find_element(By.XPATH,"(//*[@data-testid='selected-value'])[2]")
pilih_rekening.click()

time.sleep(5)

#Value Rekening

value_rekening = driver.find_element(By.XPATH,"//*[@data-testid='option-91']")
value_rekening.click()

#Terapkan
btn_submit_filter= driver.find_element(By.XPATH,"//*[@data-testid='btn-submit-filter']")
btn_submit_filter.click()

time.sleep(10)

driver.quit()