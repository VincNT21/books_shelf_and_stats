from config import LIBRARY_FILE, LOG_FILE, BOOK_TYPE_FILE
from helpers.logging_utils import log_error
import json

def reset(file):
    if str(file).endswith(".txt"):
        try:
            with open(file, "r+") as f:
                f.truncate(0)
        except OSError as e:
            log_error(f"Error: Failed to reset {file}. Reason: {e}")
    elif str(file).endswith(".json"):
        try:
            with open(file, "w") as f:
                empty_json = []
                json.dump(empty_json, f)
        except OSError as e:
            log_error(f"Error : Failed to reset {file}. Reason: {e}")
    else:
        log_error(f"Failed to reset {file}, wrong file extension.")
