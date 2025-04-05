import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

path = os.path.abspath(os.getcwd())
driver_path = path + "\chromedriver.exe"
service = Service(driver_path)

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

driver = webdriver.Chrome(service=service)

try:
    driver.get("https://www.facebook.com/")
    time.sleep(2)

    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "pass").send_keys(password + Keys.ENTER)

    time.sleep(5)

    if "login" not in driver.current_url:
        print("Статус авторизации: Успешно")
    else:
        print("Статус авторизации: Не успешно")

except Exception as e:
    print("Ошибка:", e)
    print("Статус авторизации: Не успешно")

finally:
    driver.quit()
