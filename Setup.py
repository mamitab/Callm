pip install selenium    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# WebDriver'ı başlatın (Chrome tarayıcıyı kullanıyoruz)
driver = webdriver.Chrome()

# Kullanıcıdan telefon numarasını al
phone_number = input("Lütfen telefon numaranızı girin: ")

# Form doldurmak için fonksiyon
def fill_form(url):
    driver.get(url)
    time.sleep(3)
    
    try:
        name = driver.find_element(By.NAME, "name")
        name.send_keys("Adınız")
    except:
        pass
    
    try:
        email = driver.find_element(By.NAME, "email")
        email.send_keys("email@example.com")
    except:
        pass
    
    try:
        phone = driver.find_element(By.NAME, "phone")
        phone.send_keys(phone_number)
    except:
        pass
    
    try:
        message = driver.find_element(By.NAME, "message")
        message.send_keys("Mesajınız")
    except:
        pass
    
    try:
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
    except:
        pass
    
    time.sleep(5)

# Siteler
urls = [
    "https://campusedu.com.tr/biz-sizi-arayalim",
    "https://www.ozelsaglikhastanesi.com/tesekkur/siziarayalim",
    "https://www.ugur.com.tr/biz-sizi-arayalim?status=1",
    "https://www.kerembikmaz.com/iletildi-arama-talebi",
    "https://www.artemisprincess.net/artemis-princess/tr/Biz-Sizi-Arayalim",
    "https://subaru.com.tr/sizi-arayalim",
    "https://www.delfinvinc.com/biz-sizi-arayalim"
]

# Her site için formu doldur
for url in urls:
    fill_form(url)

# Tarayıcıyı kapatın
driver.quit()         
