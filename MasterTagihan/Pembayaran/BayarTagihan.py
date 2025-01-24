from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

from webdriver_manager.chrome import ChromeDriverManager

def bayar_tagihan():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--headless")

        # Inisialisasi driver
    print("Inisialisasi driver...")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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

    #sidebar menu pembayaran
    pembayaran1 = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-pembayaran'])[3]")
    pembayaran1.click()
    time.sleep(4)

    #Klik menu Pembayaran

    menu_bayar = driver.find_element(By.XPATH,"//*[@data-testid='input-search']")
    menu_bayar.click()
    menu_bayar.send_keys("Akmal")
    time.sleep(4)

    value_nama = driver.find_element(By.XPATH,"//p[contains(text(), '890998 - Muhammad Akmal')]")
    value_nama.click()
    time.sleep(4)

    # Checkbox (coba lebih dari 1 yang di klik)
    checkboxes = driver.find_elements(By.XPATH, "//*[@data-testd='checkbox']")

    #Randomize Si checkbox supaya setidaknya 1 max 7 yang di klik
    num_to_select = random.randint(1, min(7, len(checkboxes)))
    selected_indexes = random.sample(range(len(checkboxes)), num_to_select)
    for index in selected_indexes:
        # Ambil ulang elemen supaya menghindari Error element tidak terbaca
        checkboxes = driver.find_elements(By.XPATH, "//*[@data-testd='checkbox']")
        checkbox = checkboxes[index]

        if not checkbox.is_selected():
            checkbox.click()
            print(f"Checkbox {index + 1} diklik")
        time.sleep(3)
    print(f"Total checkbox yang dipilih: {len(selected_indexes)}")

    #Bayar Taggihan
    bayar_tagihan = driver.find_element(By.XPATH,"//button[.//div[text()='Bayar Sekarang']]")
    bayar_tagihan.click()

    time.sleep(4)
    pilih_diskon = driver.find_element(By.XPATH,"(//*[@data-testid='selected-value'])[2]")
    pilih_diskon.click()
    time.sleep(3)

    value_diskon = driver.find_element(By.XPATH,"//*[@data-testid='option-%']")
    value_diskon.click()
    time.sleep(2)

    input_diskon = driver.find_element(By.XPATH, "//input[@max='100']")
    input_diskon.click()
    # Randomize nilai diskon antara 0% hingga 80%
    random_diskon = random.randint(0, 80)

    input_diskon.clear()  # Pastikan input kosong sebelum memasukkan nilai
    input_diskon.send_keys(str(random_diskon))  # Masukkan nilai diskon
    print(f"Diskon yang dimasukkan: {random_diskon}%")

    time.sleep(5)

    #input nominal uang
    min_nominal = 50000000  # 50 juta
    max_nominal = 100000000  # 100 juta

    # Merandomize nominal antara 50 juta hingga 100 juta
    nominal_random = random.randint(min_nominal, max_nominal)

    # Temukan elemen input dan klik
    bayarin_tagihan = driver.find_element(By.XPATH, "//input[@placeholder='Masukkan uang dibayarkan']")
    bayarin_tagihan.click()

    # Hapus nilai yang ada di input (jika ada)
    bayarin_tagihan.clear()

    # Masukkan nominal yang sudah di-randomize
    bayarin_tagihan.send_keys(str(nominal_random))

    # Menampilkan nilai yang dimasukkan
    print(f"Nominal yang dimasukkan: {nominal_random}")

    time.sleep(4)

    #bayar

    button_lanjut = driver.find_element(By.XPATH,"(//button[.//div[text()='Lanjut Bayar']])[1]")
    button_lanjut.click()

    time.sleep(7)
