from selenium import webdriver

def create_chrome_driver():
    options = webdriver.ChromeOptions()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }

    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-data-dir=/tmp/selenium_profile")
    options.add_argument("--incognito")

    return webdriver.Chrome(options=options)