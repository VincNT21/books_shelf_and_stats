from helpers.books_by_period import get_books_read
from helpers.date_utils import convert_str_to_date
from collections import defaultdict
from helpers.logging_utils import log_error
from config import json_path
import json

class YearlyStatistics:
    def __init__(self, user_book_library, user_data_library, year:int):
        self.book_library = user_book_library
        self.user_data_library = user_data_library
        self.year = year
        self.book_read = get_books_read(
            user_book_library,
            user_data_library,
            {"type": "yearly", "year": year}
        )
        self.read_book_count = f"You've read {len(self.book_read)} books in {self.year} !"
        self.books_by_month_data = self.books_by_month()

    def books_by_month(self):
        books_by_month = defaultdict(lambda: {"books": [], "count": 0, "pages": 0, "genres": defaultdict(lambda: {"count": 0, "sub-genres": defaultdict(int)})})
        for book in self.book_read:
            book_date = convert_str_to_date(book["end_date"])
            book_month_name = book_date.strftime("%B")
            books_by_month[book_month_name]["books"].append(book)
            books_by_month[book_month_name]["count"] += 1
            books_by_month[book_month_name]["pages"] += book["page_nbr"]
            books_by_month[book_month_name]["genres"][book["main_genre"]]["count"] += 1
            books_by_month[book_month_name]["genres"][book["main_genre"]]["sub-genres"][book["sub_genre"]] += 1

        return books_by_month
    
    def save_to_json(self):
        filename = f"statistics_{self.year}.json"
        filepath = json_path(filename)
        try:
            with open(filepath, "w") as f:
                json.dump(self.books_by_month_data, f, indent=4, default=list)
            print(f"Data saved to {filename}")
        except OSError as e:
            log_error(f"Error: Failed to write to {filepath}. Reason: {e}")
        


class MonthlyStatistics:
    def __init__(self, user_book_library, user_data_library, month:int, year:int):
        self.book_library = user_book_library
        self.data_library = user_data_library
        self.month = month
        self.year = year
        self.book_read = get_books_read(
            user_book_library,
            user_data_library,
            {"type": "monthly", "month": month, "year": year}
        )
        self.read_book_count = f"You've read {len(self.book_read)} books in {self.year}-{self.month} !"


class ByTimePeriodStatisctics:
    def __init__(self, user_book_library, user_data_library, start_day, end_day):
        self.book_library = user_book_library
        self.user_data_library = user_data_library
        self.start_day = start_day
        self.end_day = end_day
        self.book_read = get_books_read(
            user_book_library,
            user_data_library,
            {"type": "custom", "start_day": start_day, "end_day": end_day}
        )
        self.read_book_count = f"You've read {len(self.book_read)} books between {self.start_day} and {self.end_day} !"



    

    