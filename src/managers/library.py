from config import BOOK_LIBRARY_FILE, PERSONAL_LIBRARY_FILE
from helpers.logging_utils import log_error
from helpers.loading_dumping_utils import load_library, dump_library
from models.book import ReadingRecord
from helpers.date_utils import date_validation_and_format, calc_duration
from helpers.reset import reset
from models.book import Book
from book_types.book_type_and_genre import BookGenres

    
class BookLibrary:
    def __init__(self):
        self.library_file = BOOK_LIBRARY_FILE
        self.library = load_library(self.library_file)
        self.name = "Book Library"

    def add_book(self, book) -> bool:
        return LibraryManager.add_item(self, book.__dict__)
    
    def del_book(self, book_id) -> bool:
        return LibraryManager.delete_item(self, book_id)
                
    def edit_book(self, book_id, field_to_edit, new_value) -> bool:
        return LibraryManager.edit_item(self, book_id, field_to_edit, new_value)

    def __repr__(self):
        return str(self.library)
    

class PersonalLibrary:
    def __init__(self):
        self.library_file = PERSONAL_LIBRARY_FILE
        self.library = load_library(self.library_file)
        self.name = "Personal Data Library"

    def add_book_reading_record(self, book, is_read=False, start_date=None, end_date=None) -> bool:
        book_reading_record = ReadingRecord(book)
        if start_date != None:
            book_reading_record.set_start_date(start_date)
        if is_read:
            book_reading_record.set_end_date_and_duration(end_date)
        return LibraryManager.add_item(self, book_reading_record.to_dict())

    def del_book_pers_data(self, book_id) -> bool:
        return LibraryManager.delete_item(self, book_id)

    def edit_book_info(self, book_id, field_to_edit, new_value) -> bool:
        return LibraryManager.edit_item(self, book_id, field_to_edit, new_value)

    def book_started(self, book_id, start_date) -> bool:
        start_date = date_validation_and_format(start_date)
        return LibraryManager.edit_item(self, book_id, "start_date", start_date)

    def book_finished(self, book_id, end_date) -> bool:
        end_date = date_validation_and_format(end_date)
        start_date = LibraryManager.find_item(self, book_id, "start_date")
        sucess_1 = LibraryManager.edit_item(self, book_id, "is_read", True)
        sucess_2 = LibraryManager.edit_item(self, book_id, "end_date", end_date)
        reading_duration = calc_duration(start_date, end_date)
        sucess_3 = LibraryManager.edit_item(self, book_id, "reading_time", reading_duration)
        return sucess_1 and sucess_2 and sucess_3
    
        

    def __repr__(self):
        return str(self.library)
    
class LibraryManager:
    def __init__(self, book_library, personal_library):
        self.book_library = book_library
        self.pers_data_library = personal_library
        self.book_genres = BookGenres()

    def initialize_new_libraries(self):
        reset(BOOK_LIBRARY_FILE)
        reset(PERSONAL_LIBRARY_FILE)
        self.book_library = BookLibrary()
        self.pers_data_library = PersonalLibrary()

    def get_genres_dict(self):
        return self.book_genres.get_all_types()

    def new_book(
            self,
            title, author, 
            editor=None, page_nbr=None, year_published=None, 
            main_genre=None, sub_genre=None, isbn=None, 
            is_read=False, start_date=None, end_date=None
    ) -> bool:
        current_book = Book(title, author, editor, page_nbr, year_published, main_genre, sub_genre, isbn)
        if not self.book_library.add_book(current_book):
            print("Failed to add '{title}' by {author} in the BookLibrary")
            return False
        if not self.pers_data_library.add_book_reading_record(current_book, is_read, start_date, end_date):
            print("Failed to add '{title}' by {author} in the PersonalDataLibrary")
            return False
        return True
    
    def begin_a_book(self, book_id, start_date) -> bool:
        return self.pers_data_library.book_started(book_id, start_date)
    
    def finish_a_book(self, book_id, end_date) -> bool:
        return self.pers_data_library.book_finished(book_id, end_date)

    def remove_book(self, book_id) -> bool:
        self.book_library.del_book(book_id)
        return self.pers_data_library.del_book_pers_data(book_id)
        
    
    def edit_a_book(self, book_id, field_to_edit, new_value) -> bool: 
        if field_to_edit == "id":
            print("Cannot change a book ID !")
            return False
        if field_to_edit == "title" or field_to_edit == "author":
            book_library_sucess = self.book_library.edit_book(book_id, field_to_edit, new_value)
            data_library_sucess = self.pers_data_library.edit_book_info(book_id, field_to_edit, new_value)
            return book_library_sucess and data_library_sucess
        if field_to_edit == "main_genre":
            if not self.book_genres.is_main_genre_exist(new_value):
                self.book_genres.add_main_genre(new_value)
            return self.book_library.edit_book(book_id, field_to_edit, new_value)
        if field_to_edit == "sub_genre":
            associated_main_genre = self.find_book_and_record(book_id)["main_genre"]
            if not self.book_genres.is_sub_genre_exist(associated_main_genre, new_value):
                self.book_genres.add_sub_genre(associated_main_genre, new_value)
            return self.book_library.edit_book(book_id, field_to_edit, new_value)
        if field_to_edit == "start_date":
            return self.pers_data_library.book_started(book_id, new_value)
        if field_to_edit == "end_date":
            return self.pers_data_library.book_finished(book_id, new_value)
        else:
            return self.book_library.edit_book(book_id, field_to_edit, new_value)

    
    def find_book_and_record(self, book_id):
        if book_id == None:
            return {}
        book_data = next((item for item in self.book_library.library if item["id"] == book_id), None)
        if not book_data:
            print(f"Book with ID {book_id} not found in BookLibrary")
        personal_data = next((item for item in self.pers_data_library.library if item["id"] == book_id), None)
        if not personal_data:
            print(f"Book with ID {book_id} not found in PersonalDataLibrary")
        whole_data = book_data | personal_data
        return whole_data



    @staticmethod
    def add_item(library, item) -> bool:
        if any(existing["id"] == item["id"] for existing in library.library):
            print(f"Duplicate item for '{item["title"]}' by {["author"]} found in {library.name}.")
            return False
        library.library.append(item)
        dump_library(library.library_file, library.library)
        print(f"Succesfully added '{item["title"]}' by {item["author"]} in {library.name}.")
        return True

    @staticmethod
    def delete_item(library, book_id) -> bool:
        counter = 0
        for element in library.library:
            if element["id"] == book_id:
                library.library.remove(element)
                counter += 1
                print(f"Succesfully deleted item for '{element['title']}' by {element['author']} from {library.name}")
        if counter == 0:
            print(f"No item with id:{book_id} found in {library.name}")
        dump_library(library.library_file, library.library)
        return counter > 0
    
    @staticmethod
    def edit_item(library, book_id, field_to_edit, new_value) -> bool:
        counter = 0
        for element in library.library:
            if element["id"] == book_id:
                counter += 1
                print(f"Succesfully edit book {field_to_edit} from '{element[field_to_edit]}' to '{new_value}' in {library.name}")
                element[field_to_edit] = new_value
        if counter == 0:
            print(f"No item with id:{book_id} found in {library.name}")
        dump_library(library.library_file, library.library)
        return counter > 0
    
    @staticmethod
    def find_item(library, book_id, field_value_to_find):
        for element in library.library:
            if element["id"] == book_id:
                return element[field_value_to_find]
