from process_config_default import process_config_default
from process_config_user import process_config_user
from await_for_ip import await_for_ip

try:
    while True:
        if await_for_ip("192.168.1.1", timeout=10):  
            process_config_default("http://192.168.1.1")

        if await_for_ip("192.168.99.1", timeout=10):  
            process_config_user("http://192.168.99.1") 
        
except Exception as e:
    print(f"[Erro] {e}")
finally:
    print("Processo finalizado.")