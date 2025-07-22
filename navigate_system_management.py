import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def navigate_to_restore_page(driver):
    wait = WebDriverWait(driver, 10)
     
    try:    
        try:
            close_button = wait.until(EC.presence_of_element_located((By.ID, "Btn_Close")))
            close_button.click()
            time.sleep(1)
        except Exception:
            print("[Info] Nenhum pop-up encontrado para fechar.")
  
        # Clicar em "Gerenciamento & Diagnostico"
        wait.until(EC.element_to_be_clickable((By.ID, "mgrAndDiag"))).click()
        time.sleep(1)
        
        # Clicar em "Gerenciamento de Sistema"
        wait.until(EC.element_to_be_clickable((By.ID, "devMgr"))).click()
        time.sleep(1)
        return True
    except Exception as e:
        print(f"[Erro na navegação] {e}")
