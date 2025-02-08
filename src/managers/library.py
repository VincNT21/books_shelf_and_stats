from config import BOOK_LIBRARY_FILE, PERSONAL_LIBRARY_FILE
from helpers.logging_utils import log_error
from models.book import ReadingRecord
import json


class Library:
    def __init__(self, library_file):
        self.library_file = library_file
        self.library = self._load_library()

    def _load_library(self):
        try:
            with self.library_file.open("r") as f:
                return json.load(f)
        except OSError as e:
            log_error(f"Error: Failed to read from {self.library_file}. Reason: {e}")
        return []

    def _dump_library(self):
        try:
            with self.library_file.open("w") as f:
                json.dump(self.library, f, indent=4)
        except OSError as e:
            log_error(f"Error: Failed to write to {self.library_file}. Reason: {e}")


    
class BookLibrary(Library):
    def __init__(self):
        super().__init__(BOOK_LIBRARY_FILE) 
        self.name = "Book Library"

    def add_book(self, book):
        LibraryManager.add_item(self, book.__dict__)
    
    def del_book(self, book_id):
        LibraryManager.delete_item(self, book_id)
                
    def edit_book(self, book_id, field_to_edit, new_value):
        LibraryManager.edit_item(self, book_id, field_to_edit, new_value)

    def __repr__(self):
        return str(self.library)
    

class PersonalLibrary(Library):
    def __init__(self):
        super().__init__(PERSONAL_LIBRARY_FILE)
        self.name = "Personal Data Library"

    def add_book_reading_record(self, book, is_read=False, start_date=None, end_date="Unknown"):
        book_reading_record = ReadingRecord(book)
        if start_date != None:
            book_reading_record.set_start_date(start_date)
        if is_read:
            book_reading_record.set_end_date_and_duration(end_date)
        LibraryManager.add_item(self, book_reading_record.to_dict())

    def del_book_pers_data(self, book_id):
        LibraryManager.delete_item(self, book_id)

    def book_started(self, book_id, start_date):
        LibraryManager.edit_item(self, book_id, "start_date", start_date)

    def book_finished(self, book_id, end_date="Unknown"):
        LibraryManager.edit_item(self, book_id, "is_read", True)
        LibraryManager.edit_item(self, book_id, "end_date", end_date)

    def __repr__(self):
        return str(self.library)
    
class LibraryManager:
    @staticmethod
    def add_item(library, item):
        if any(existing["id"] == item["id"] for existing in library.library):
            print(f"Duplicate item for '{item["title"]}' by {["author"]} found in {library.name}.")
            return False
        library.library.append(item)
        library._dump_library()
        print(f"Succesfully added '{item["title"]}' by {item["author"]} in {library.name}.")
        return True

    @staticmethod
    def delete_item(library, book_id):
        counter = 0
        for element in library.library:
            if element["id"] == book_id:
                library.library.remove(element)
                counter += 1
                print(f"Succesfully deleted item for '{element['title']}' by {element['author']} from {library.name}")
        if counter == 0:
            print(f"No item with id:{book_id} found in {library.name}")
        library._dump_library()
        return counter > 0
    
    @staticmethod
    def edit_item(library, book_id, field_to_edit, new_value):
        counter = 0
        for element in library.library:
            if element["id"] == book_id:
                counter += 1
                print(f"Succesfully edit book {field_to_edit} from '{element[field_to_edit]}' to '{new_value}' in {library.name}")
                element[field_to_edit] = new_value
        if counter == 0:
            print(f"No item with id:{book_id} found in {library.name}")
        library._dump_library()
        return counter > 0
