from helpers.monthly_read import get_books_monthly_read

class MonthlyStatistics:
    def __init__(self, user_book_library, user_data_library, month:int, year:int):
        self.book_library = user_book_library
        self.data_library = user_data_library
        self.month = month
        self.year = year
        self.book_id_read_monthly = get_books_monthly_read(user_data_library, month, year)
        self.book_read_monthly = self._find_books_read()

    def _find_books_read(self):
        book_list = []
        for id in self.book_id_read_monthly:
            for element in self.book_library.library:
                if element["id"] == id:
                    book_list.append(element)
        return book_list

    def read_book_count(self):
        print(f"You've read {len(self.book_id_read_monthly)} books this month !")

    

    