import os

def check_path_exist(file_path):
  abs_path = os.path.abspath(file_path)
  if not os.path.exists(abs_path):
    print(f"[Erro] Arquivo '{abs_path}' não encontrado.")
    return 
  return abs_path