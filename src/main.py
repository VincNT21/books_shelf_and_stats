from models.book import Book, ReadingRecord
from managers.library import PersonalLibrary, BookLibrary
from helpers.reset import reset
from config import BOOK_LIBRARY_FILE, PERSONAL_LIBRARY_FILE, LOG_FILE

def main():
    pass
    
def initialize_new_libraries():
    reset(BOOK_LIBRARY_FILE)
    reset(PERSONAL_LIBRARY_FILE)
    user_library = BookLibrary()
    user_pers_data_library = PersonalLibrary()
    return user_library, user_pers_data_library

def new_book(
        user_library, user_pers_data_library,
        title, author, 
        editor=None, page_nbr=None, year_published=None, 
        main_genre=None, sub_genre=None, isbn=None,
        is_read=False, start_date=None, end_date=None
):
    current_book = Book(title, author, editor, page_nbr, year_published, main_genre, sub_genre, isbn)
    user_library.add_book(current_book)
    user_pers_data_library.add_book_reading_record(current_book, is_read, start_date, end_date)
    return current_book

def remove_book(user_library, user_pers_data_library, book_id):
    user_library.del_book(book_id)
    user_pers_data_library.del_book_pers_data(book_id)

def begin_a_book(user_pers_data_library, book_id, start_date):
    user_pers_data_library.book_started(book_id, start_date)

def finish_a_book(user_pers_data_library, book_id, end_date=None):
    user_pers_data_library.book_finished(book_id, end_date)
    
    

main()