import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def tambah_tagihan():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--headless")

    try:
        # Inisialisasi driver


        # Inisialisasi driver
        print("Inisialisasi driver...")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        print("Driver diinisialisasi dan window dimaksimalkan.")

        # Akses URL
        driver.get("https://sit.siprusedu.com/login")
        print("URL login dibuka.")

        # Tunggu hingga elemen email dapat ditemukan
        wait = WebDriverWait(driver, 10)
        email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        password = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main/div[1]/div/form/button")
        print("Elemen login ditemukan.")

        # Masukkan kredensial
        email.send_keys("admin.sekolah@gmail.com")
        password.send_keys("Test1234")
        print("Kredensial dimasukkan.")

        # Klik tombol login
        login_button.click()
        print("Tombol login diklik.")

        # Tunggu beberapa detik setelah login
        time.sleep(9)

        # Klik Menu Master Data
        master_data = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@data-testid='sidebar-menu-master-data'])[2]")))

        master_data.click()
        print("Menu Master Data diklik.")
        time.sleep(5)

        # Sub-menu tagihan
        sub_tagihan = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-tagihan'])[4]")
        sub_tagihan.click()
        print("Sub-menu Tagihan diklik.")
        time.sleep(10)

        # Klik tombol tambah tagihan
        btn_tambah_billing = driver.find_element(By.XPATH,"//*[@data-testid='btn-add-billing']")
        btn_tambah_billing.click()
        print("Tombol 'Tambah Tagihan' diklik.")
        time.sleep(10)

        # Input Nama Tagihan
        nama_tagihan = driver.find_element(By.XPATH,"//input[@type='text' and @name='billingName' and @placeholder='Masukkan nama tagihan']")
        nama_tagihan.click()
        print("Field Nama Tagihan ditemukan dan diklik.")

        namaTagihan = [
            "Tagihan Uang Pangkal",
            "Tagihan Uang Jajan Guru",
            "Tagihan SPP - Januari",
            "Tagihan SPP - Februari",
            "Tagihan Uang Buku",
            "Tagihan Ujian Semester",
            "Tagihan Biaya Kegiatan",
            "Tagihan Iuran Kelas",
            "Tagihan Sumbangan Pengembangan Sekolah",
            "Tagihan Uang Kegiatan Ekstrakurikuler",
            "Tagihan Uang Praktikum",
            "Tagihan Fasilitas Siswa"
        ]
        kumpulanTagihan = random.choice(namaTagihan)
        nama_tagihan.send_keys(kumpulanTagihan)
        print(f"Nama Tagihan yang dimasukkan: {kumpulanTagihan}")
        time.sleep(5)

        # Pilih Tahun Ajaran
        tahun_ajaran = driver.find_element(By.XPATH,"(//*[@data-testid='selected-value'])[1]")
        tahun_ajaran.click()
        print("Field Tahun Ajaran ditemukan dan diklik.")

        textbox = driver.find_element(By.XPATH,"//input[@type='text' and @placeholder='Cari tahun ajaran' and contains(@class, 'rounded-md') and contains(@class, 'cursor-auto')]")
        textbox.click()
        textbox.send_keys("2025")
        print("Tahun ajaran '2025' dimasukkan.")
        time.sleep(3)

        textbox1 = driver.find_element(By.XPATH,"//*[@data-testid='option-71']")
        textbox1.click()
        print("Tahun ajaran '2025' dipilih.")
        time.sleep(3)

        # Pilih Tipe Tagihan
        pilih_tagihan = driver.find_element(By.XPATH,"(//*[@data-testid='select-field'])[3]")
        pilih_tagihan.click()
        print("Field Tipe Tagihan ditemukan dan diklik.")
        time.sleep(3)

        value_tagihan = driver.find_element(By.XPATH,"//*[@data-testid='option-regular']")
        value_tagihan.click()
        print("Tipe Tagihan 'Regular' dipilih.")
        time.sleep(3)

        # Pilih Kelas
        pilih_kelas = driver.find_element(By.XPATH,"//p[@class='text-base w-full text-neutral6' and text()='Pilih kelas']")
        pilih_kelas.click()
        print("Field Pilih Kelas ditemukan dan diklik.")

        checkbox = driver.find_element(By.XPATH,"(//*[@data-testd='checkbox'])[1]")
        checkbox.click()
        print("Kelas pertama dipilih.")
        time.sleep(5)

        # Input Kode Tagihan
        kode_tagihan = driver.find_element(By.NAME,"billingCode")
        kode_tagihan.click()
        print("Field Kode Tagihan ditemukan dan diklik.")

        def generate_random_billing(max_length=5):
            characters = string.ascii_lowercase + string.digits  # Kombinasi huruf kecil dan angka
            return ''.join(random.choices(characters, k=max_length))

        random_billing = generate_random_billing()
        print(f"Kode Tagihan Acak: {random_billing}")

        kode_tagihan.send_keys(random_billing)
        time.sleep(5)

        # Input Jumlah Tagihan perbulan
        tagihan_perbulan = driver.find_element(By.NAME,"billingAmount")
        tagihan_perbulan.click()
        print("Field Jumlah Tagihan per bulan ditemukan dan diklik.")

        def generate_random_nominal(min_value=1000000, max_value=10000000):
            return str(random.randint(min_value, max_value))

        random_nominal = generate_random_nominal()
        tagihan_perbulan.send_keys(random_nominal)
        print(f"Jumlah Tagihan per bulan yang dimasukkan: {random_nominal}")

        time.sleep(5)

        # Pilih Rekening Bank
        field_rekening = driver.find_element(By.XPATH,"(//*[@data-testid='select-field'])[4]")
        field_rekening.click()
        print("Field Rekening Bank ditemukan dan diklik.")
        time.sleep(3)

        # Pilih Rekening Bank
        rek_value = driver.find_element(By.XPATH,"//*[@data-testid='option-28']")
        rek_value.click()
        print("Rekening Bank dipilih.")
        time.sleep(3)

        # Input Keterangan
        keterangan = driver.find_element(By.XPATH,"//textarea[@name='description' and @placeholder='Masukkan keterangan']")
        keterangan.click()
        keterangan.send_keys("SEKOLAH BUTUH DUIT")
        print("Keterangan 'SEKOLAH BUTUH DUIT' dimasukkan.")

        time.sleep(5)

        # Klik Generate Bill
        generate_bill = driver.find_element(By.XPATH,"//button[@type='button' and contains(@class, 'rounded-[6px]') and .//div[text()='Generate']]")
        generate_bill.click()
        print("Tombol 'Generate Bill' diklik.")
        time.sleep(3)

        # Klik Tambahkan
        tambahkan_billing = driver.find_element(By.XPATH,"//button[contains(@class, 'rounded-[6px]') and .//div[text()='Tambahkan']]")
        tambahkan_billing.click()
        print("Tombol 'Tambahkan' diklik.")
        time.sleep(5)

        # Pop-up Ya
        popup_ya = driver.find_element(By.XPATH,"//div[contains(@class, 'flex items-center text-center') and text()='Ya']")
        popup_ya.click()
        print("Pop-up 'Ya' diklik.")

        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Quit the driver
        driver.quit()
        print("Driver dihentikan, script selesai.")
