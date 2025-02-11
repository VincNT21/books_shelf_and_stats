from helpers.logging_utils import log_error

import json

def load_library(file):
    try:
        with file.open("r") as f:
            return json.load(f)
    except OSError as e:
        log_error(f"Error: Failed to read from {file}. Reason: {e}")
        return []

def dump_library(file, library):
    try:
        with file.open("w") as f:
            json.dump(library, f, indent=4)
    except OSError as e:
        log_error(f"Error: Failed to write to {file}. Reason: {e}")