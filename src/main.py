from models.book import Book, ReadingRecord
from book_types.book_type_and_genre import BookTypes
from managers.library import Library, PersonnalLibrary
from datetime import date, datetime
from helpers.reset import reset
from config import LIBRARY_FILE, PERSONAL_LIBRARY_FILE, LOG_FILE

def main():
    pass
    
def initialize_new_libraries():
    reset(LIBRARY_FILE)
    reset(PERSONAL_LIBRARY_FILE)
    user_library = Library()
    user_pers_data_library = PersonnalLibrary()

def new_book(
        user_library, user_pers_data_library,
        title, author, 
        editor=None, page_nbr=None, year_published=None, 
        type=None, genre=None, isbn=None,
        is_read=False, start_date=None, end_date=None
):
    current_book = Book(title, author, editor, page_nbr, year_published, type, genre, isbn)
    user_library.add_book(current_book)
    curr_book_reading_record = ReadingRecord(current_book)
    if start_date != None:
        curr_book_reading_record.begin_reading(start_date)
    if is_read:
        curr_book_reading_record.finish_reading(end_date)
    user_pers_data_library.add_book_reading_record(curr_book_reading_record)

def remove_book(user_library, user_pers_data_library, book_id):
    user_library.del_book(book_id)
    user_pers_data_library.del_book_pers_data(book_id)

def begin_a_book(user_pers_data_library, book_id):
    pass
    
    

main()