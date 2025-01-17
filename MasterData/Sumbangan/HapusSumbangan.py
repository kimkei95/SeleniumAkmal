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

#Hapus Sumbangan

hapus_sumbangan = driver.find_element(By.XPATH,"(//button[contains(@class, 'flex items-center gap-2 text-blue10') and contains(text(), 'Hapus')])[1]")
hapus_sumbangan.click()

time.sleep(5)

#Klik ya

ya = driver.find_element(By.XPATH,"//div[text()='Ya']")
ya.click()

time.sleep(6)

driver.quit()