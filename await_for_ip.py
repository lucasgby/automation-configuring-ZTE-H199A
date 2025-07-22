import subprocess
import time
import platform

def is_windows():
    return platform.system().lower() == "windows"

def await_for_ip(ip, timeout=60):
    print(f"[INFO] Aguardando {ip} ficar disponível...")
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            cmd = ["ping", "-n", "1", ip] if is_windows() else ["ping", "-c", "1", ip]
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if result.returncode == 0:
                # Verificação extra: checar texto da resposta (ex: no Linux pode retornar 0 mesmo com perda)
                if "ttl" in result.stdout.lower():
                    print(f"[SUCESSO] IP {ip} está acessível.")
                    return True
                else:
                    print(f"[INFO] Ping retornou 0 mas sem resposta válida ainda, tentando novamente...")

        except Exception as e:
            print(f"[Erro interno] {e}")

        time.sleep(2)

    print(f"[ERRO] IP {ip} não respondeu dentro de {timeout} segundos.")
    return False
