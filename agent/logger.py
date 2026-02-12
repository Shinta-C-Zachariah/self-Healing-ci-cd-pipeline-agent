import logging
from datetime import datetime

logging.basicConfig(filename="self_heal.log", level=logging.INFO)

def log_action(action):
    logging.info(f"{datetime.now()} - {action}")
    print(f"[LOG] {datetime.now()} - {action}")
