import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from check_path_upload_exist import check_path_exist

def upload_restore_user(driver, file_path):
  wait = WebDriverWait(driver, 10)
  
  try:
    # Clicar em Configuração do Usuário
    wait.until(EC.element_to_be_clickable((By.ID, "usrCfgMgr"))).click()
    time.sleep(1)
    
    # Clicar em Configuração da Restauração Padrão
    wait.until(EC.element_to_be_clickable((By.ID, "UserConfUploadBar"))).click()
    time.sleep(1)
    
    abs_path = check_path_exist(file_path)    
    
    upload_input = driver.find_element(By.ID, "ConfigUpload")
    print(f"[Info] Enviando arquivo: {abs_path}")
    upload_input.send_keys(abs_path)
    time.sleep(2)
    
    # Clicar no Botão para fazer Upload
    driver.find_element(By.ID, "Btn_Upload").click()

    time.sleep(1)
    
    driver.find_element(By.ID, "confirmOK").click()
    time.sleep(1)
    
    print("[Sucesso] Restauração iniciada com sucesso.")
    driver.quit()
  except Exception as e:
    print(f"[Erro na restauração] {e}")
