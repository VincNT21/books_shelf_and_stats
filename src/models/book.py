from datetime import datetime, date
from book_types.book_type_and_genre import BookGenres
from helpers.generate_id import generate_id
from helpers.normalize_text import normalize_text

class Book:
    def __init__(self, title, author, editor=None, page_nbr=None, year_published=None, main_genre=None, sub_genre=None, isbn=None):
        if not title.strip() or not author.strip():
            raise ValueError("Title or Author are required")

        if year_published != None and year_published > date.today().year:
            raise ValueError("Publication year cannot be in the future")
        
        if page_nbr != None and page_nbr <= 0:
            raise ValueError("Page number must be positive")
        
        self.id = generate_id(title, author)

        self.title = normalize_text(title)
        self.author = normalize_text(author)
        self.page_nbr = page_nbr
        self.editor = normalize_text(editor)
        self.year_published = year_published

        self.main_genre = normalize_text(main_genre)
        self.sub_genre = normalize_text(sub_genre)
        self.check_for_genres(self.main_genre, self.sub_genre)

        self.isbn = isbn
        
    def check_for_genres(self, main_genre, sub_genre):
        book_genres = BookGenres()
        if book_genres.is_main_genre_exist(main_genre) is False:
            book_genres.add_main_genre(main_genre)
        if book_genres.is_sub_genre_exist(main_genre, sub_genre) is False:
            book_genres.add_sub_genre(main_genre, sub_genre)

    def __repr__(self):
        return f"Book :\nTitle = {self.title}\nAuthor = {self.author}\nEditor = {self.editor}\nPage number = {self.page_nbr}\nYear published = {self.year_published}\nMain genre = {self.main_genre}\nSub genre = {self.sub_genre}"
    
class ReadingRecord:
    def __init__(self, book:Book, is_read=False):
        self.id = book.id
        self.title = book.title
        self.author = book.author
        self.is_read = is_read
        self.start_date = None
        self.end_date = None
        self.reading_time = None

    def date_validation(self, date_to_val):
        if date_to_val == None:
            return None
        parsed_date = datetime.strptime(date_to_val, "%Y-%m-%d").date()
        if parsed_date <= date.today():
            return parsed_date
        else:
            raise ValueError("The date given is in the future!")

    def calc_duration(self, start_date, end_date):
        if start_date > end_date:
            raise ValueError("End date cannot be before start date")
        else:
            reading_duration = end_date - start_date
            reading_duration = reading_duration.days
            return reading_duration

    def set_start_date(self, start_date):
        self.start_date = self.date_validation(start_date)

    def set_end_date_and_duration(self, end_date):
        end_date = self.date_validation(end_date)
        self.is_read = True
        if end_date != None:
            self.end_date = end_date
            self.reading_time = self.calc_duration(self.start_date, self.end_date)
        else:
            self.end_date = "Unknown"

    def __repr__(self):
        if self.is_read:
            return f"The book '{self.title}' by '{self.author}' has been read in {self.reading_time} days. Beginning: {self.start_date}, end: {self.end_date}."
        elif self.start_date != None:
            return f"This book '{self.title}' by '{self.author}' is currently being read. Beginning: {self.start_date}"
        else:
            return f"This book '{self.title}' by '{self.author}' hasn't been read yet."
        