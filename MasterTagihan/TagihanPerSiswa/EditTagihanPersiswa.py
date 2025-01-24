import random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager


def edit_tagihan():
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


    #edit
    rows = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[id^="table-row-"]')))

    filtered_rows = [row for row in rows if int(row.get_attribute("id").split("-")[2]) <= 9]

    if filtered_rows:
        random_row = random.choice(filtered_rows)
        random_row.click()
        time.sleep(4)
    else:
        print("Tidak ada elemen dengan ID yang dimulai dengan 'table-row-' ditemukan dalam rentang yang diinginkan.")


    option_edit = driver.find_element(By.XPATH,"//*[@data-testid='action-0']")
    option_edit.click()

    time.sleep(3)

    field_nominal = driver.find_element(By.NAME,"amount")
    field_nominal.click()

    field_nominal.send_keys(Keys.CONTROL +"a")
    field_nominal.send_keys(Keys.BACKSPACE)

    def generate_random_nominal(min_value=1000000, max_value=10000000):
        return str(random.randint(min_value, max_value))

    random_nominal1 = generate_random_nominal()

    field_nominal.send_keys(random_nominal1)

    time.sleep(4)

    #Terapkan

    button_terapkan = driver.find_element(By.XPATH,"//button[.//div[text()='Simpan']]")
    button_terapkan.click()

    time.sleep(5)