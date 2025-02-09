from helpers.date_utils import convert_str_to_date, get_monthly_range

def get_books_read(user_book_library, user_data_library, period):
    id_list = []
    book_list = []

    if period["type"] == "monthly":
        month = period["month"]
        year = period["year"]
        start_monthly, end_monthly = get_monthly_range(month, year)
        for item in user_data_library.library:
            if item["is_read"] == False:
                continue
            parsed_date = convert_str_to_date(item["end_date"])
            if parsed_date >= start_monthly and parsed_date < end_monthly:
                id_list.append(item["id"])

    elif period["type"] == "yearly":
        year = period["year"]
        for item in user_data_library.library:
            if item["is_read"] == False:
                continue
            parsed_date = convert_str_to_date(item["end_date"])
            if parsed_date.year == year:
                id_list.append(item["id"])

    elif period["type"] == "custom":
        start_period = convert_str_to_date(period["start_day"])
        end_period = convert_str_to_date(period["end_day"])
        if start_period > end_period:
            raise ValueError("Period start date cannot be after period end date")
        for item in user_data_library.library:
            if item["is_read"] == False:
                continue
            parsed_date = convert_str_to_date(item["end_date"])
            if parsed_date >= start_period and parsed_date <= end_period:
                id_list.append(item["id"])

    if id_list == []:
        print(f"No book finished in {period["type"]} period given")
        return []
    
    for item in user_book_library.library:
        temp_item = {}
        if item["id"] in id_list:
            temp_item = item
            for data in user_data_library.library:
                if data["id"] == temp_item["id"]:
                    temp_item.update(data)
                    book_list.append(temp_item)

    return book_list



