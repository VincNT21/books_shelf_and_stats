from models.book import Book, ReadingRecord
from book_types.book_type_and_genre import BookTypes
from managers.library import Library, PersonnalLibrary
from datetime import date, datetime
from helpers.reset import reset
from config import LIBRARY_FILE, PERSONAL_LIBRARY_FILE, LOG_FILE

def main():
    pass
    
def initialize_libraries():
    reset(LIBRARY_FILE)
    reset(PERSONAL_LIBRARY_FILE)
    user_library = Library()
    user_pers_data_library = PersonnalLibrary()

def add_book(
        user_library, user_pers_data_library,
        title, author, 
        editor=None, page_nbr=None, year_published=None, 
        type=None, genre=None, isbn=None,
        is_read=False, start_date=None, end_date=None
):
    current_book = Book(title, author, editor, page_nbr, year_published, type, genre, isbn)
    user_library.add_book(current_book)
    user_pers_data_library.add_book_pers_data(current_book)
    book_reading_record = ReadingRecord(current_book)
    if start_date != None:
        book_reading_record.begin_reading(start_date)
    if is_read:
        book_reading_record.finish_reading(end_date)
    

main()