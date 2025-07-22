import time
from browser_utils import create_chrome_driver

from login import login_to_router
from navigate_system_management import navigate_to_restore_page
from upload_restore_user import upload_restore_user
from get_resource_path import get_resource_path

def process_config_user():
    USERNAME = "multipro"
    PASSWORD = "Vd@tJg2S"
    BIN_FILE_PATH = get_resource_path("assets/config.bin")

    driver = create_chrome_driver()
    
    try:
        driver.get("http://192.168.99.1")
        time.sleep(2)

        login_to_router(driver, USERNAME, PASSWORD)
        navigate_to_restore_page(driver)
        upload_restore_user(driver, BIN_FILE_PATH)

        print("[Sucesso] Restauração do usuário concluída.")

    except Exception as e:
        print(f"[Erro na restauração do usuário] {e}")

    finally:
        driver.quit()
        print("[Info] Navegador encerrado.")
