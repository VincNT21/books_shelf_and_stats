from config import BOOK_TYPE_FILE
from helpers.logging_utils import log_error
import json

class BookTypes:
    def __init__(self):
        self.type_file = BOOK_TYPE_FILE
        self._valid_types = self._load_types()

    def _load_types(self):
        try:
            with self.type_file.open("r") as f:
                return set(json.load(f))
        except OSError as e:
            log_error(f"Error: Failed to read from {self.type_file}. Reason: {e}")
            return {"novel", "comic book", "essay"}
        
    def _dump_types(self):
        try:
            with self.type_file.open("w") as f:
                json.dump(self._valid_types, f)
        except OSError as e:
            log_error(f"Error: Failed to write to {self.type_file}. Reason: {e}")

    def add_type(self, new_type):
        normalized = new_type.lower().strip()
        self._valid_types.add(normalized)
        self._dump_types()
        return normalized

    def is_valid(self, book_type):
        return book_type.lower().strip() in self._valid_types
    
    def get_all_types(self):
        return sorted(list(self._valid_types))