import os
import time
import requests
import logging
from datetime import datetime

           # Change this to your laptop path
log_dir = r"C:\Users\Well-King\Documents\DOCUMENT\DISRUPT" 
os.makedirs(log_dir, exist_ok=True)


log_file = os.path.join(log_dir, "shutdown_log.txt")
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")

def shutdown_system():
    logging.info("Shutdown initiated immediately.")
    print("System will shut down in 30 seconds. Save your work now.")
    time.sleep(30)  # Adjust as needed
    if os.name == "nt":
        os.system("shutdown /s /t 5")
    else:
        os.system("sudo shutdown now")

if __name__ == "__main__":
    logging.info("Shutdown script executed manually.")
    shutdown_system()
