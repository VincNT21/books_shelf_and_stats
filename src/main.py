from models.book import Book, ReadingRecord
from book_types.book_type_and_genre import BookTypes
from managers.library import Library
from datetime import date, datetime
from helpers.reset import reset
from config import LIBRARY_FILE

def main():
    my_library = Library()
    book1 = Book("Silo generations", "Hugh Howey", "Le livre de poche", 540, 2017, "novel", "sf")
    book2 = Book("Millenium 1", "Stieg Larsson", "Babel noir", 750, 2010, "novel", "thriller")
    read = ReadingRecord(book1)
    read.is_read = False
    read.start_date = date(2025, 2, 3)
    my_library.add_book(book1)
    my_library.del_book(book1)
    """
    my_library.add_book(book2)
    """
    

    

main()