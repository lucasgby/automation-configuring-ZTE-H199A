from selenium.webdriver.common.by import By
import time

def login_to_router(driver, username, password):
    try:
        user_input = driver.find_element(By.ID, "Frm_Username")
        pass_input = driver.find_element(By.ID, "Frm_Password")
        login_btn = driver.find_element(By.ID, "LoginId")

        user_input.clear()
        user_input.send_keys(username)
        pass_input.clear()
        pass_input.send_keys(password)
        login_btn.click()
        time.sleep(2)
        return True
    except Exception as e:
        print(f"[Erro no login] {e}")
        return False
