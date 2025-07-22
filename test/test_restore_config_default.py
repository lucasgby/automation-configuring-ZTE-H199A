import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from login import login_to_router
from navigate_system_management import navigate_to_restore_page
from upload_restore_default import upload_restore_default
import time

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

#file_path = os.path.join(os.getcwd(), "assets", "default_config.bin")
file_path = "./assets/default_config.bin"
save_screenshots_path = "./screenshots/restore_config_default.png"

if login_to_router(driver, "multipro", "Vd@tJg2S"):
    navigate_to_restore_page(driver)
    time.sleep(1)
    upload_restore_default(driver, file_path)
    time.sleep(2)
    driver.save_screenshot(save_screenshots_path)
    print("[✓] Upload iniciado. Veja 'restore_result.png'")
else:
    print("[✗] Falha no login.")

driver.quit()
