from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

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

#Sub menu Riwayat Pembayaran

riwayat_pembayaran = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-riwayat-pembayaran'])[2]")
riwayat_pembayaran.click()

time.sleep(5)

#lihat
elements_lihat = driver.find_elements(By.XPATH,
                                "(//div[@class='flex size-full justify-center'])//button[contains(text(),'Lihat')]")
if elements_lihat:
    random_element = random.choice(elements_lihat)
    random_element.click()

    time.sleep(7)