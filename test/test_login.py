import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from login import login_to_router

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://192.168.1.1")
time.sleep(2)

success = login_to_router(driver, "multipro", "multipro")

driver.save_screenshot("login_result.png")

if success:
    print("[✓] Login feito com sucesso. Veja 'login_result.png'")
else:
    print("[✗] Falha no login. Veja 'login_result.png'")

driver.quit()
