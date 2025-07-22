import time
from browser_utils import create_chrome_driver

from login import login_to_router
from navigate_system_management import navigate_to_restore_page
from upload_restore_default import upload_restore_default
from get_resource_path import get_resource_path

def process_config_default():
    USERNAME = "multipro"
    PASSWORD = "multipro"
    BIN_FILE_PATH = get_resource_path("assets/default_config.bin")

    driver = create_chrome_driver()

    try:
        driver.get("http://192.168.1.1")
        time.sleep(2)

        login_to_router(driver, USERNAME, PASSWORD)
        navigate_to_restore_page(driver)
        upload_restore_default(driver, BIN_FILE_PATH)

        print("[Sucesso] Restauração da configuração default concluída.")

    except Exception as e:
        print(f"[Erro na restauração padrão] {e}")

    finally:
        driver.quit()
        print("[Info] Navegador encerrado.")
