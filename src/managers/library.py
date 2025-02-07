from models.book import Book, ReadingRecord
from config import LIBRARY_FILE
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
        book_reading_record = ReadingRecord(book)
        book_as_dict = book.__dict__
        book_as_dict.update(book_reading_record.as_dict())
        for book in self.library:
            if book_as_dict["title"] == book["title"]:
                print(f"{book["title"]} by {book["author"]} already in library !")
                return    
        self.library.append(book_as_dict)
        self._dump_library()
        print(f"Added {book_as_dict["title"]} by {book_as_dict["author"]} in library !")
    
    def del_book(self, book_title):
        for element in self.library:
            if element["title"] == book_title:
                self.library.remove(element)
                print(f"Succesfully remove {element["title"]} by {element["author"]} from library")

    def __repr__(self):
        return str(self.library)