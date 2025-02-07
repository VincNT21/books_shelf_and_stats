from datetime import datetime, date
from config import LOG_FILE

def log_error(error_message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(str(datetime.today()) + " - " + error_message + "\n")