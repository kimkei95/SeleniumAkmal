import random

import pyautogui
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def tambah_akun():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--headless")

    # Inisialisasi driver
    print("Inisialisasi driver...")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

        # Akses URL
    print("Mengakses URL...")
    driver.get("https://sit.siprusedu.com/login")

        # Tunggu hingga elemen email dapat ditemukan
    print("Menunggu elemen login...")
    wait = WebDriverWait(driver, 10)
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main/div[1]/div/form/button")

        # Masukkan kredensial
    print("Mengisi kredensial login...")
    email.send_keys("admin.sekolah@gmail.com")
    password.send_keys("Test1234")

        # Klik tombol login
    print("Klik tombol login...")
    login_button.click()

        # Tunggu beberapa detik setelah login
    time.sleep(9)


    #Klik Menu User Management

    menu_userManagement = driver.find_element(By.XPATH,"(//*[@data-testid='sidebar-menu-user-management'])[2]")
    menu_userManagement.click()
    time.sleep(4)

    #Klik Tambah User

    btn_tambah_user = driver.find_element(By.XPATH,"//button[div[contains(text(), 'Tambah')]]")
    btn_tambah_user.click()
    time.sleep(3)


    #popup tambah user

    #Pilih role

    try:
        # Buka dropdown
        print("Membuka dropdown role...")
        dropdown = driver.find_element(By.XPATH, "(//*[@data-testid='selected-value'])[3]")
        dropdown.click()
        time.sleep(2)

        # Daftar opsi dalam dropdown
        role_options = {
            "orang tua": "option-2",
            "tatausaha": "option-3",
            "kasir": "option-4",
            "admin": "option-5"
        }

        # Pilih salah satu opsi secara acak
        selected_role_name, selected_role_testid = random.choice(list(role_options.items()))

        # Pilih opsi berdasarkan data-testid
        print(f"Memilih opsi role: {selected_role_name}")
        selected_option = driver.find_element(By.XPATH, f"//*[@data-testid='{selected_role_testid}']")
        selected_option.click()

        # Log hasil
        print(f"Opsi yang dipilih: {selected_role_name}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

        time.sleep(4)
    #Tambah User dan email

    username_list = [
        "test_user1",
        "automation_user",
        "selenium_tester",
        "qa_engineer",
        "dev_user",
        "tester_01",
        "random_user",
        "user123",
        "alpha_tester",
        "beta_user",
        "Anton",
        "Tester_QA_Engineer"
    ]
    email_domains = ["example.com", "testmail.com", "qa.com", "automation.dev", "dummy.com"]


    def get_random_username():
        return random.choice(username_list)

    def get_random_email():
        return f"{random.choice(username_list)}@{random.choice(email_domains)}"

    # Fungsi untuk menambahkan angka jika ada duplikasi
    def add_suffix_if_duplicate(existing, new_value):
        suffix = 1
        original_value = new_value
        while new_value in existing:
            new_value = f"{original_value}{suffix}"
            suffix += 1
        existing.add(new_value)
        return new_value
    #Set Username Dan Email
    used_usernames = set()
    used_emails = set()
    try:
        # Randomize username
        print("Memilih username secara acak...")
        random_username = get_random_username()
        unique_username = add_suffix_if_duplicate(used_usernames, random_username)
        print(f"Username yang dipilih: {unique_username}")

        print("Mengisi field username...")
        username_field = driver.find_element(By.NAME, "username")  # Pastikan atribut NAME sesuai
        username_field.click()
        time.sleep(1)
        username_field.send_keys(unique_username)
        print(f"Username yang dimasukkan: {unique_username}")

        # Randomize email
        print("Memilih email secara acak...")
        random_email = get_random_email()
        unique_email = add_suffix_if_duplicate(used_emails, random_email)
        print(f"Email yang dipilih: {unique_email}")

        print("Mengisi field email...")
        email_field = driver.find_element(By.NAME, "email")  # Pastikan atribut NAME sesuai
        email_field.click()
        time.sleep(5)
        email_field.send_keys(unique_email)
        print(f"Email yang dimasukkan: {unique_email}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

        time.sleep(3)

    #klik terapkan

    tambah_user = driver.find_element(By.XPATH,"//button[div[contains(text(), 'Simpan')]]")
    tambah_user.click()
    time.sleep(4)

if tambah_akun() =="_main_":
    tambah_akun()