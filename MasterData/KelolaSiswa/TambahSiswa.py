import random
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from webdriver_manager.chrome import ChromeDriverManager


def tambah_siswa():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--headless")

    # Inisialisasi driver
    print("Inisialisasi driver...")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    print("Akses URL login...")
    # Akses URL
    driver.get("https://sit.siprusedu.com/login")

    # Tunggu hingga elemen email dapat ditemukan
    print("Menunggu elemen email...")
    wait = WebDriverWait(driver, 10)  # Tunggu hingga 10 detik
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))

    print("Menemukan elemen input password...")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main/div[1]/div/form/button")

    print("Masukkan kredensial dan login...")
    # Masukkan kredensial
    email.send_keys("admin.sekolah@gmail.com")
    password.send_keys("Test1234")

    # Klik tombol login
    login_button.click()

    # Tunggu beberapa detik setelah login
    print("Login berhasil, menunggu beberapa detik...")
    time.sleep(9)

    # Klik Menu Master Data
    print("Klik Menu Master Data...")
    master_data = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@data-testid='sidebar-menu-master-data'])[2]")))

    master_data.click()
    time.sleep(5)

    # Klik sub-menu siswa
    print("Klik sub-menu Kelola Siswa...")
    kelola_siswa = driver.find_element(By.XPATH, "(//*[@data-testid='sidebar-menu-kelola-siswa'])[2]")
    kelola_siswa.click()

    time.sleep(4)

    # Button Tambah
    print("Klik tombol Tambah Siswa...")
    btn_tambah_siswa = driver.find_element(By.XPATH, "//div[@class='flex items-center text-center' and text()='Tambah']")
    btn_tambah_siswa.click()

    time.sleep(4)

    # Field Nama Siswa
    print("Masukkan Nama Siswa...")
    nama_siswa1 = driver.find_element(By.XPATH, "//*[@data-testid='full-name-input']")
    nama_siswa1.click()

    nama_murid1 = [
        "Muhammad Akmal",
        "Andrean",
        "Budi Santoso",
        "Dewa Saputra",
        "Joko Prabowo",
        "Andra",
        "Samuel Santoso",
        "Rezaldy",
        "Muhammad Fadel",
        "Asep Darmawan",
        "Agustinus",
        "William",
        "Jackson Wang",
        "Anthony"
    ]

    # Pilih nama secara acak dari array
    nama_siswa1.send_keys(Keys.CONTROL + "a")
    nama_siswa1.send_keys(Keys.BACKSPACE)
    nama_terpilih1 = random.choice(nama_murid1)
    nama_siswa1.send_keys(nama_terpilih1)
    time.sleep(4)

    # NIS
    print("Masukkan NIS Siswa...")
    nis_siswa = driver.find_element(By.NAME, "nis")
    nis_siswa.click()

    nis_random = [random.randint(10000, 99999) for _ in range(5)]
    number_random = random.choice(nis_random)

    nis_siswa.send_keys(number_random)
    time.sleep(5)

    # Status
    print("Pilih Status Siswa...")
    status_siswa = driver.find_element(By.XPATH, "(//*[@data-testid='select-field'])[1]")
    status_siswa.click()

    # Randomize Pilihan Status
    print("Menunggu dropdown menu status...")
    dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='dropdown-menu']")))

    # Tangkap elemen Regular dan Non Regular
    aktif = driver.find_element(By.XPATH, "//div[@data-testid='option-aktif']")
    tamat = driver.find_element(By.XPATH, "//div[@data-testid='option-tamat']")
    pindah_sekolah = driver.find_element(By.XPATH, "//div[@data-testid='option-pindah_sekolah']")
    putus_sekolah = driver.find_element(By.XPATH, "//div[@data-testid='option-dropout']")
    # Pilihan opsi dalam list
    opsi_list = [aktif, tamat, pindah_sekolah, putus_sekolah]

    # Pilih secara acak
    selected_option = random.choice(opsi_list)

    # Klik opsi yang dipilih
    selected_option.click()
    time.sleep(5)

    # Tahun ajaran
    print("Pilih Tahun Ajaran...")
    tahun_ajaran_siswa = driver.find_element(By.XPATH, "(//*[@data-testid='select-field'])[2]")
    tahun_ajaran_siswa.click()

    time.sleep(3)

    cari_tahun_ajaran = driver.find_element(By.XPATH, "//input[@placeholder='Cari tahun ajaran']")
    cari_tahun_ajaran.click()
    cari_tahun_ajaran.send_keys("2025")

    hasilCari = driver.find_element(By.XPATH, "//*[@data-testid='option-71']")
    hasilCari.click()

    time.sleep(3)

    # Tempat Lahir
    print("Masukkan Tempat Lahir...")
    tempatLahir = driver.find_element(By.NAME, "birthPlace")
    tempatLahir.click()

    kota = [
        "Jakarta", "Surabaya", "Bandung", "Medan", "Bekasi", "Semarang",
        "Tangerang", "Depok", "Palembang", "Bogor", "Makassar", "Malang",
        "Padang", "Denpasar", "Yogyakarta", "Pekanbaru", "Banjarmasin", "Pontianak",
        "Manado", "Balikpapan", "Samarinda", "Cirebon", "Tasikmalaya", "Mataram",
        "Kupang", "Jayapura", "Sorong", "Ambon", "Kendari", "Gorontalo"
    ]

    kota_terpilih = random.choice(kota)
    print("Kota terpilih:", kota_terpilih)
    tempatLahir.send_keys(kota_terpilih)

    time.sleep(3)

    # Date picker
    print("Pilih tanggal lahir...")
    date_picker = driver.find_element(By.XPATH, "//*[@data-testid='birth-date-picker']")
    date_picker.click()

    # Pilih Tahun
    yearPicker = driver.find_element(By.XPATH, "(//*[@data-testid='selected-value'])[4]")
    yearPicker.click()

    wait = WebDriverWait(driver, 10)
    dropdown1 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='dropdown-menu']")))

    # Pilih Tahun
    opsi_tahun = []
    for year in range(2000, 2013):  # Range tahun yang diinginkan
        xpath = f"//*[@data-testid='option-{year}']"
        opsi_tahun.append(driver.find_element(By.XPATH, xpath))

    pilihan_tahun = random.choice(opsi_tahun)
    pilihan_tahun.click()
    time.sleep(5)

    # Pilih bulan
    print("Pilih bulan lahir...")
    monthPicker = driver.find_element(By.XPATH, "(//*[@data-testid='selected-value'])[3]")
    monthPicker.click()

    wait = WebDriverWait(driver, 10)
    dropdown2 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='dropdown-menu']")))

    months = []
    for month in range(1, 13):
        xpath = f"//*[@data-testid='option-{month}']"
        months.append(driver.find_element(By.XPATH, xpath))
    random_month = random.choice(months)
    random_month.click()

    time.sleep(5)

    # Pilih tanggal
    print("Pilih tanggal lahir...")
    random_index = random.randint(10, 20)
    xpath = f"(//div[@data-testid='date-cells-picker'])[{random_index}]"
    element = driver.find_element(By.XPATH, xpath)
    element.click()

    time.sleep(5)

    # Pilih Unit
    print("Pilih Unit...")
    unit = driver.find_element(By.XPATH, "(//*[@data-testid='select-field'])[3]")
    unit.click()

    time.sleep(3)

    value_unit = driver.find_element(By.XPATH, "//*[@data-testid='option-3']")
    value_unit.click()

    time.sleep(3)

    # Pilih Kelas
    print("Pilih Kelas...")
    pilih_kelasSiswa = driver.find_element(By.XPATH, "(//*[@data-testid='select-field'])[4]")
    pilih_kelasSiswa.click()

    wait = WebDriverWait(driver, 10)
    dropdown_menu1 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='dropdown-menu']")))

    if dropdown_menu1.is_displayed():
        print("Dropdown menu tersedia dan terlihat.")
    else:
        print("Dropdown menu tidak terlihat.")

    options_kelas = driver.find_elements(By.XPATH, "//div[@data-testid='dropdown-menu']//div[starts-with(@data-testid, 'option-')]")

    if options_kelas:
        # Pilih secara acak
        random_choice1 = random.choice(options_kelas)
        print("Opsi yang dipilih:", random_choice1.text)

        # Klik yang dipilih
        random_choice1.click()
    else:
        print("Tidak ada opsi di dropdown-menu.")
    time.sleep(5)

    # Pilih gender
    print("Pilih gender...")
    gender = driver.find_element(By.XPATH, "//input[@type='radio' and @value='laki-laki']")
    gender.click()
    time.sleep(3)

    # Nohp
    print("Masukkan nomor HP...")
    input_hp = driver.find_element(By.XPATH, "//input[@name='noHandphone']")
    input_hp.click()

    random_number = ''.join(random.choices('0123456789', k=20))
    input_hp.send_keys(random_number)
    print(f"Nomor HP yang dimasukkan: {random_number}")
    time.sleep(5)

    # Agama
    print("Pilih agama...")
    agama = driver.find_element(By.XPATH, "(//*[@data-testid='select-field'])[5]")
    agama.click()
    time.sleep(3)

    dropdown_menuAgama = driver.find_element(By.XPATH, "//div[@data-testid='dropdown-menu']")
    optionsAgama = dropdown_menuAgama.find_elements(By.XPATH, ".//div[contains(@data-testid, 'option-')]")
    random_optionAgama = random.choice(optionsAgama)
    random_optionAgama.click()

    time.sleep(5)

    # Email Ortu
    print("Masukkan email orang tua...")
    email_ortu = driver.find_element(By.NAME, "emailParent")
    email_ortu.click()

    emailortu = ["akmalalhaqi123@gmail.com", "user.ortu@gmail.com"]
    random_email = random.choice(emailortu)
    email_ortu.send_keys(random_email)

    time.sleep(5)

    # Alamat
    print("Masukkan alamat...")
    alamat = driver.find_element(By.NAME, "address")
    alamat.click()

    list_alamat = [
        "Jl. Sudirman No. 23, Jakarta Pusat, DKI Jakarta 10210",
        "Jl. Ahmad Yani No. 45, Surabaya, Jawa Timur 60234",
        "Jl. Braga No. 12, Bandung, Jawa Barat 40111",
        "Jl. Malioboro No. 78, Yogyakarta 55213",
        "Jl. Imam Bonjol No. 56, Medan, Sumatera Utara 20152",
        "Jl. Gajah Mada No. 89, Semarang, Jawa Tengah 50133",
        "Jl. Pattimura No. 10, Makassar, Sulawesi Selatan 90114",
        "Jl. Jendral Sudirman No. 34, Denpasar, Bali 80111",
        "Jl. Diponegoro No. 88, Malang, Jawa Timur 65112",
        "Jl. Panglima Polim No. 5, Balikpapan, Kalimantan Timur 76112"
    ]
    random_alamat = random.choice(list_alamat)
    alamat.send_keys(random_alamat)

    time.sleep(3)

    # Simpan
    print("Simpan data siswa...")
    simpan_addsiswa = driver.find_element(By.XPATH, "//div[text()='Simpan']")
    simpan_addsiswa.click()

    # Pop-up konfirmasi
    print("Klik pop-up konfirmasi Simpan...")
    pop_upAddSiswa = driver.find_element(By.XPATH, "//div[@class='flex items-center text-center' and text()='Ya']")
    pop_upAddSiswa.click()

    time.sleep(7)

if tambah_siswa() == "_main_":
    tambah_siswa()