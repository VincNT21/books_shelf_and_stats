from models.book import Book, ReadingRecord
from config import LIBRARY_FILE, PERSONAL_LIBRARY_FILE
from helpers.logging_utils import log_error
import json


class Library:
    def __init__(self):
        self.library_file = LIBRARY_FILE
        self.library = self._load_library()

    def _load_library(self):
        try:
            with self.library_file.open("r") as f:
                return json.load(f)
        except OSError as e:
            log_error(f"Error: Failed to read from {self.library_file}. Reason: {e}")

    def _dump_library(self):
        try:
            with self.library_file.open("w") as f:
                json.dump(self.library, f, indent=4)
        except OSError as e:
            log_error(f"Error: Failed to write to {self.library_file}. Reason: {e}")

    def add_book(self, book):
        book_as_dict = book.__dict__
        for book in self.library:
            if book_as_dict["id"] == book["id"]:
                print(f"'{book["title"]}' by {book["author"]} already in library !")
                return    
        self.library.append(book_as_dict)
        self._dump_library()
        print(f"Added '{book_as_dict["title"]}' by {book_as_dict["author"]} in library !")
    
    def del_book(self, book_id):
        for element in self.library:
            if element["title"] == book_id:
                self.library.remove(element)
                print(f"Succesfully removed '{element["title"]}' by {element["author"]} from library")
        print(f"Book id:{book_id} not found in library")
                
    def edit_book(self, book_id, field_to_edit, new_value):
        for element in self.library:
            if element["id"] == book_id:
                print(f"Succesfully edit book {field_to_edit} from '{element[field_to_edit]}' to '{new_value}'")
                element[field_to_edit] = new_value
                
        self._dump_library()


    def __repr__(self):
        return str(self.library)
    

class PersonnalLibrary:
    def __init__(self):
        self.pers_library_file = PERSONAL_LIBRARY_FILE
        self.pers_library = self._load_library()

    def _load_library(self):
        try:
            with self.pers_library_file.open("r") as f:
                return json.load(f)
        except OSError as e:
            log_error(f"Error: Failed to read from {self.pers_library_file}. Reason: {e}")

    def _dump_library(self):
        try:
            with self.pers_library_file.open("w") as f:
                json.dump(self.pers_library, f, indent=4)
        except OSError as e:
            log_error(f"Error: Failed to write to {self.pers_library_file}. Reason: {e}")

    def add_book_pers_data(self, book):
        reading_record = ReadingRecord(book)
        reading_record_as_dict = reading_record.__dict__
        for element in self.pers_library:
            if reading_record_as_dict["id"] == element["id"]:
                print(f"Personal data for '{book.title}' by {book.author} already in library !")
                return
        self.pers_library.append(reading_record_as_dict)
        self._dump_library()
        print(f"Added personal data for '{book.title}' by {book.author} in library !")

    def del_book_pers_data(self, book_id):
        for element in self.pers_library:
            if element["id"] == book_id:
                self.pers_library.remove(element)
                print(f"Succesfully removed personal data for '{element["title"]}' by {element["author"]} from library")
        print(f"Personal data for book id:{book_id} not found in library")

    def book_started(self, book_id, start_date):
        for element in self.pers_library:
            if element["id"] == book_id:
                element["start_date"] = start_date
        self._dump_library()

    def book_finished(self, book_id, end_date=None):
        for element in self.pers_library:
            if element["id"] == book_id:
                element["is_read"] = True
                if end_date != None:
                    element["end_date"] = end_date
                else:
                    element["end_date"] = "Unknown"

    def __repr__(self):
        return str(self.pers_library)