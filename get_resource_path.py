import sys
import os

def get_resource_path(relative_path):
  if getattr(sys, 'frozen', False):
    return os.path.join(sys._MEIPASS, relative_path)
  return os.path.join(os.path.abspath("."), relative_path)
