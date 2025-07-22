import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
import time

from login import login_to_router
from navigate_system_management import navigate_to_restore_page

options = webdriver.ChromeOptions()
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}

options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-data-dir=/tmp/selenium_profile")
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)

driver.get("http://192.168.99.2")
time.sleep(2)

if login_to_router(driver, "multipro", "Vd@tJg2S"):
    navigate_to_restore_page(driver)
    time.sleep(2)
    driver.save_screenshot("./screenshots/navigate_result.png")
    print("[✓] Navegação concluída. Veja 'navigate_result.png'")
else:
    print("[✗] Falha no login.")

driver.quit()